#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <limits.h>

int copy_file(int in,int out);

int main() {
    int ch2,fifo;
    char buf[PIPE_BUF];
    ssize_t s;
//------------------------------------------------------------------------------
    if (mkfifo("check2",S_IFIFO|0666)<0 && errno!=EEXIST) {
	perror("2 mkfifo check2");
	return -1;
    }
    printf("2 opening ch2");
    if ((ch2=open("check2",O_RDWR))<0) {
	perror("2 open check2");
	return -1;
    }
//------------------------------------------------------------------------------
    printf("2 preparing to write to ch2");
    if (write(ch2,buf,PIPE_BUF)<0) {
	printf("2 has already run...");
	return -1;
    }
    printf("2 has writen to ch2");
//------------------------------------------------------------------------------
    if (mkfifo("fifo",S_IFIFO|0666)<0 && errno!=EEXIST) {
	perror("2 mkfifo fifo");
	return -1;
    }
    if ((fifo=open("fifo",O_RDONLY))<0) {
	perror("2 open fifo");
	return -1;
    }
    copy_file(fifo,0);
    if (close(fifo)<0) {
	perror("2 close fifo");
	return -1;
    }
//------------------------------------------------------------------------------
    if (close(ch2)<0) {
	perror("2 close check2");
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