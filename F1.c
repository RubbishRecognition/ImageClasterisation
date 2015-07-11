#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <limits.h>

int copy_file(int in,int out);

int main(int argc,char **argv) {
    int ch1,fifo,f;
    char buf[PIPE_BUF];
    ssize_t s;
//------------------------------------------------------------------------------
    if (argc!=2) {
	printf("usage: f1 filename\n");
	return -1;
    }
    if ((f=open(argv[1],O_RDONLY))<0) {
	perror("1 open file");
	return -1;
    }
//------------------------------------------------------------------------------
    if (mkfifo("check1",S_IFIFO|0666)<0 && errno!=EEXIST) {
	perror("1 mkfifo check1");
	return -1;
    }
    if ((ch1=open("check1",O_RDWR|O_NDELAY))<0) {
	perror("1 open check1");
	return -1;
    }
//------------------------------------------------------------------------------
    if (write(ch1,buf,PIPE_BUF)<0) {
	printf("1 has already run...");
	return -1;
    }
//------------------------------------------------------------------------------
    if (mkfifo("fifo",S_IFIFO|0666)<0 && errno!=EEXIST) {
	perror("1 mkfifo fifo");
	return -1;
    }
    if ((fifo=open("fifo",O_WRONLY))<0) {
	perror("1 open fifo");
	return -1;
    }
    copy_file(f,fifo);
    if (close(fifo)<0) {
	perror("1 close fifo");
	return -1;
    }
//------------------------------------------------------------------------------
    if (close(ch1)<0) {
	perror("1 close check1");
	return -1;
    }
    if (close(f)<0) {
	perror("1 close file");
	return -1;
    }
}
//==============================================================================
int copy_file(int in,int out) {
    int c;
    char buf[1024];
    do {
	c=read(in,buf,sizeof(buf));
	if (c==0) break;
	write(out,buf,c);
    } while(1);
    return 0;
}