
from PIL import Image, ImageDraw


print("Enter image filename (for example \"test.jpg\")")
picture = input()
#picture = "test4.jpg"
image = Image.open(picture)

pixel = image.load()
res_pixel = []

height = image.size[1]
width = image.size[0]

for i in range(width):
    for j in range(height):
        if ((i == 0) | (j == 0)):
            res_pixel.append([0, 0, 0])
        else:
            diff = 0
            diff = (pixel[i - 1, j][0] - pixel[i, j][0]) ** 2 
            diff = diff + (pixel[i - 1, j][1] - pixel[i, j][1]) ** 2
            diff = diff + (pixel[i - 1, j][2] - pixel[i, j][2]) ** 2
            if (diff > 700):
                res_pixel.append([255, 255, 255]) 
            else:
                res_pixel.append([0, 0, 0])                



objects = Image.open(picture)
draw = ImageDraw.Draw(objects)

rang = 3
# * rang * rang // 2 - 255*3
for i in range(width // rang - rang):
    for j in range(height // rang - rang):
        new_i = i * rang
        new_j = j * rang
        num = 0
        for a in range(rang):
            for b in range(rang):
                true_i = new_i + a
                true_j = new_j + b
                num = num + res_pixel[(true_i - 1) * height + true_j][0]
        if (num >= 255*3): #& (num <= 255 * rang * rang // 2 + 255 * 80):
            for a in range(rang):
                for b in range(rang):
                    true_i = new_i + a
                    true_j = new_j + b  
                    draw.point((true_i, true_j), (255, 255, 255))
objects.save("obj.jpg")
       
        

result = Image.open(picture)
draw = ImageDraw.Draw(result)

for i in range(width):
    for j in range(height):
        draw.point((i, j), (res_pixel[(i - 1) * height + j][0], res_pixel[(i - 1) * height + j][1], res_pixel[(i - 1) * height + j][2]))
result.save("res.jpg")


print("begin")

fuck_the_details = res_pixel
rang = 5
end_flag = 1

for i in range(width):
    #print(i)
    end_flag = 1
    while (end_flag):
        flag = 0
        lengths = [1000]
        num = 0        
        end_flag = 0
        for j in range(height):
            #print(fuck_the_details[(i - 1) * height + j][0])
            if (fuck_the_details[(i - 1) * height + j][0] == flag):
                num = num + 1
            else:
                #flag = fuck_the_details[(i - 1) * height + j][0]
                if (num > 0):
                    lengths.append(num)
                num = 0
        lengths.sort()
	#print(lengths)
	#buff = input()
        if (lengths[0] < rang):
            #print(lengths[0])
            #print(lengths)
            #print(fuck_the_details[0:height])
            #pic = input()
            end_flag = 1
            num = 0
            flag = 0
            bad_trip = 1
            for j in range(height):
                if (fuck_the_details[(i - 1) * height + j][0] == flag):
                    num = num + 1
                else:
                    #flag = fuck_the_details[(i - 1) * height + j][0]
                    if (num > 0):
			# & (bad_trip)
                        if (num == lengths[0]):
                            bad_trip = 0
                            if (flag == 0):
                                flag = 255
                            for k in range(num + 1):
                                if (k > 0):
                                    true_j = j - k
                                    fuck_the_details[(i - 1) * height + true_j][0] = fuck_the_details[(i - 1) * height + true_j][0] + flag
                                    fuck_the_details[(i - 1) * height + true_j][1] = fuck_the_details[(i - 1) * height + true_j][1] + flag
                                    fuck_the_details[(i - 1) * height + true_j][2] = fuck_the_details[(i - 1) * height + true_j][2] + flag
                        else:
                            if (num == lengths[0]) & (bad_trip == 0):
                                bad_trip = 1
                            
                    num = 0
#fufufufufufufufuckckckckckckck
print("first")
#rang = 10
end_flag = 1


for j in range(height):
    #print(i)
    end_flag = 1
    while (end_flag):
        flag = 0
        lengths = [1000]
        num = 0        
        end_flag = 0
        for i in range(width):
            #print(fuck_the_details[(i - 1) * height + j][0])
            if (fuck_the_details[(i - 1) * height + j][0] == flag):
                num = num + 1
            else:
                #flag = fuck_the_details[(i - 1) * height + j][0]
                if (num > 0):
                    lengths.append(num)
                num = 0
        lengths.sort()
        if (lengths[0] < rang):
            #print(lengths[0])
            #print(lengths)
            #print(fuck_the_details[0:height])
            #pic = input()
            end_flag = 1
            num = 0
            flag = 0
            bad_trip = 1
            for i in range(width):
                if (fuck_the_details[(i - 1) * height + j][0] == flag):
                    num = num + 1
                else:
                    #flag = fuck_the_details[(i - 1) * height + j][0]
                    if (num > 0):
			# & (bad_trip)
                        if (num == lengths[0]):
                            bad_trip = 0
                            if (flag == 0):
                                flag = 255
                            for k in range(num + 1):
                                if (k > 0):
                                    #print(1)
                                    true_i = i - k
                                    fuck_the_details[(true_i - 1) * height + j][0] = fuck_the_details[(true_i - 1) * height + j][0] + flag
                                    fuck_the_details[(true_i - 1) * height + j][1] = fuck_the_details[(true_i - 1) * height + j][1] + flag
                                    fuck_the_details[(true_i - 1) * height + j][2] = fuck_the_details[(true_i - 1) * height + j][2] + flag
                        else:
                            if (num == lengths[0]) & (bad_trip == 0):
                                bad_trip = 1
                            
                    num = 0




print("second")

#//////////////////////////////
                    






for i in range(width):
    #print(i)
    end_flag = 1
    while (end_flag):
        flag = 0
        lengths = [1000]
        num = 0        
        end_flag = 0
        for j in range(height):
            #print(fuck_the_details[(i - 1) * height + j][0])
            if (fuck_the_details[(i - 1) * height + j][0] == flag):
                num = num + 1
            else:
                #flag = fuck_the_details[(i - 1) * height + j][0]
                if (num > 0):
                    lengths.append(num)
                num = 0
        lengths.sort()
	#print(lengths)
	#buff = input()
        if (lengths[0] < rang):
            #print(lengths[0])
            #print(lengths)
            #print(fuck_the_details[0:height])
            #pic = input()
            end_flag = 1
            num = 0
            flag = 0
            bad_trip = 1
            for j in range(height):
                if (fuck_the_details[(i - 1) * height + j][0] == flag):
                    num = num + 1
                else:
                    #flag = fuck_the_details[(i - 1) * height + j][0]
                    if (num > 0):
			# & (bad_trip)
                        if (num == lengths[0]):
                            bad_trip = 0
                            if (flag == 0):
                                flag = 255
                            for k in range(num + 1):
                                if (k > 0):
                                    true_j = j - k
                                    fuck_the_details[(i - 1) * height + true_j][0] = fuck_the_details[(i - 1) * height + true_j][0] + flag
                                    fuck_the_details[(i - 1) * height + true_j][1] = fuck_the_details[(i - 1) * height + true_j][1] + flag
                                    fuck_the_details[(i - 1) * height + true_j][2] = fuck_the_details[(i - 1) * height + true_j][2] + flag
                        else:
                            if (num == lengths[0]) & (bad_trip == 0):
                                bad_trip = 1
                            
                    num = 0
#fufufufufufufufuckckckckckckck
print("third")
#rang = 10
end_flag = 1


for j in range(height):
    #print(i)
    end_flag = 1
    while (end_flag):
        flag = 0
        lengths = [1000]
        num = 0        
        end_flag = 0
        for i in range(width):
            #print(fuck_the_details[(i - 1) * height + j][0])
            if (fuck_the_details[(i - 1) * height + j][0] == flag):
                num = num + 1
            else:
                #flag = fuck_the_details[(i - 1) * height + j][0]
                if (num > 0):
                    lengths.append(num)
                num = 0
        lengths.sort()
        if (lengths[0] < rang):
            #print(lengths[0])
            #print(lengths)
            #print(fuck_the_details[0:height])
            #pic = input()
            end_flag = 1
            num = 0
            flag = 0
            bad_trip = 1
            for i in range(width):
                if (fuck_the_details[(i - 1) * height + j][0] == flag):
                    num = num + 1
                else:
                    #flag = fuck_the_details[(i - 1) * height + j][0]
                    if (num > 0):
			# & (bad_trip)
                        if (num == lengths[0]):
                            bad_trip = 0
                            if (flag == 0):
                                flag = 255
                            for k in range(num + 1):
                                if (k > 0):
                                    #print(1)
                                    true_i = i - k
                                    fuck_the_details[(true_i - 1) * height + j][0] = fuck_the_details[(true_i - 1) * height + j][0] + flag
                                    fuck_the_details[(true_i - 1) * height + j][1] = fuck_the_details[(true_i - 1) * height + j][1] + flag
                                    fuck_the_details[(true_i - 1) * height + j][2] = fuck_the_details[(true_i - 1) * height + j][2] + flag
                        else:
                            if (num == lengths[0]) & (bad_trip == 0):
                                bad_trip = 1
                            
                    num = 0


print("fourth")



fuck = Image.open(picture)
draw = ImageDraw.Draw(fuck)
                    
for i in range(width):
    for j in range(height):
        draw.point((i, j), (fuck_the_details[(i - 1) * height + j][0], fuck_the_details[(i - 1) * height + j][1], fuck_the_details[(i - 1) * height + j][2]))
fuck.save("fuck.jpg")



#//////////////////////////////
#WHITES

rang = 30

for i in range(width):
    #print(i)
    end_flag = 1
    while (end_flag):
        flag = 255
        lengths = [1000]
        num = 0        
        end_flag = 0
        for j in range(height):
            #print(fuck_the_details[(i - 1) * height + j][0])
            if (fuck_the_details[(i - 1) * height + j][0] >= flag):
                num = num + 1
            else:
                #flag = fuck_the_details[(i - 1) * height + j][0]
                if (num > 0):
                    lengths.append(num)
                num = 0
        lengths.sort()
	#print(lengths)
	#buff = input()
        if (lengths[0] < rang):
            #print(lengths[0])
            #print(lengths)
            #print(fuck_the_details[0:height])
            #pic = input()
            end_flag = 1
            num = 0
            flag = 255
            bad_trip = 1
            for j in range(height):
                if (fuck_the_details[(i - 1) * height + j][0] >= flag):
                    num = num + 1
                else:
                    #flag = fuck_the_details[(i - 1) * height + j][0]
                    if (num > 0):
			# & (bad_trip)
                        if (num == lengths[0]):
                            bad_trip = 0
                            if (flag == 255):
                                flag = -255
                            for k in range(num + 1):
                                if (k > 0):
                                    true_j = j - k
                                    fuck_the_details[(i - 1) * height + true_j][0] = 0
                                    fuck_the_details[(i - 1) * height + true_j][1] = 0
                                    fuck_the_details[(i - 1) * height + true_j][2] = 0
                        else:
                            if (num == lengths[0]) & (bad_trip == 0):
                                bad_trip = 1
                            
                    num = 0
#fufufufufufufufuckckckckckckck
print("fivth")
#rang = 10
end_flag = 1


for j in range(height):
    #print(i)
    end_flag = 1
    while (end_flag):
        flag = 255
        lengths = [1000]
        num = 0        
        end_flag = 0
        for i in range(width):
            #print(fuck_the_details[(i - 1) * height + j][0])
            if (fuck_the_details[(i - 1) * height + j][0] >= flag):
                num = num + 1
            else:
                #flag = fuck_the_details[(i - 1) * height + j][0]
                if (num > 0):
                    lengths.append(num)
                num = 0
        lengths.sort()
        if (lengths[0] < rang):
            #print(lengths[0])
            #print(lengths)
            #print(fuck_the_details[0:height])
            #pic = input()
            end_flag = 1
            num = 0
            flag = 255
            bad_trip = 1
            for i in range(width):
                if (fuck_the_details[(i - 1) * height + j][0] >= flag):
                    num = num + 1
                else:
                    #flag = fuck_the_details[(i - 1) * height + j][0]
                    if (num > 0):
			# & (bad_trip)
                        if (num == lengths[0]):
                            bad_trip = 0
                            if (flag == 255):
                                flag = -255
                            for k in range(num + 1):
                                if (k > 0):
                                    #print(1)
                                    true_i = i - k
                                    fuck_the_details[(true_i - 1) * height + j][0] = fuck_the_details[(true_i - 1) * height + j][0] + flag
                                    fuck_the_details[(true_i - 1) * height + j][1] = fuck_the_details[(true_i - 1) * height + j][1] + flag
                                    fuck_the_details[(true_i - 1) * height + j][2] = fuck_the_details[(true_i - 1) * height + j][2] + flag
                        else:
                            if (num == lengths[0]) & (bad_trip == 0):
                                bad_trip = 1
                            
                    num = 0

print("end")




#//////////////////////////////
#AND AGAIN BLACS


rang = 15



for i in range(width):
    #print(i)
    end_flag = 1
    while (end_flag):
        flag = 0
        lengths = [1000]
        num = 0        
        end_flag = 0
        for j in range(height):
            #print(fuck_the_details[(i - 1) * height + j][0])
            if (fuck_the_details[(i - 1) * height + j][0] == flag):
                num = num + 1
            else:
                #flag = fuck_the_details[(i - 1) * height + j][0]
                if (num > 0):
                    lengths.append(num)
                num = 0
        lengths.sort()
	#print(lengths)
	#buff = input()
        if (lengths[0] < rang):
            #print(lengths[0])
            #print(lengths)
            #print(fuck_the_details[0:height])
            #pic = input()
            end_flag = 1
            num = 0
            flag = 0
            bad_trip = 1
            for j in range(height):
                if (fuck_the_details[(i - 1) * height + j][0] == flag):
                    num = num + 1
                else:
                    #flag = fuck_the_details[(i - 1) * height + j][0]
                    if (num > 0):
			# & (bad_trip)
                        if (num == lengths[0]):
                            bad_trip = 0
                            if (flag == 0):
                                flag = 255
                            for k in range(num + 1):
                                if (k > 0):
                                    true_j = j - k
                                    fuck_the_details[(i - 1) * height + true_j][0] = fuck_the_details[(i - 1) * height + true_j][0] + flag
                                    fuck_the_details[(i - 1) * height + true_j][1] = fuck_the_details[(i - 1) * height + true_j][1] + flag
                                    fuck_the_details[(i - 1) * height + true_j][2] = fuck_the_details[(i - 1) * height + true_j][2] + flag
                        else:
                            if (num == lengths[0]) & (bad_trip == 0):
                                bad_trip = 1
                            
                    num = 0
#fufufufufufufufuckckckckckckck
print("third")
#rang = 10
end_flag = 1


for j in range(height):
    #print(i)
    end_flag = 1
    while (end_flag):
        flag = 0
        lengths = [1000]
        num = 0        
        end_flag = 0
        for i in range(width):
            #print(fuck_the_details[(i - 1) * height + j][0])
            if (fuck_the_details[(i - 1) * height + j][0] == flag):
                num = num + 1
            else:
                #flag = fuck_the_details[(i - 1) * height + j][0]
                if (num > 0):
                    lengths.append(num)
                num = 0
        lengths.sort()
        if (lengths[0] < rang):
            #print(lengths[0])
            #print(lengths)
            #print(fuck_the_details[0:height])
            #pic = input()
            end_flag = 1
            num = 0
            flag = 0
            bad_trip = 1
            for i in range(width):
                if (fuck_the_details[(i - 1) * height + j][0] == flag):
                    num = num + 1
                else:
                    #flag = fuck_the_details[(i - 1) * height + j][0]
                    if (num > 0):
			# & (bad_trip)
                        if (num == lengths[0]):
                            bad_trip = 0
                            if (flag == 0):
                                flag = 255
                            for k in range(num + 1):
                                if (k > 0):
                                    #print(1)
                                    true_i = i - k
                                    fuck_the_details[(true_i - 1) * height + j][0] = fuck_the_details[(true_i - 1) * height + j][0] + flag
                                    fuck_the_details[(true_i - 1) * height + j][1] = fuck_the_details[(true_i - 1) * height + j][1] + flag
                                    fuck_the_details[(true_i - 1) * height + j][2] = fuck_the_details[(true_i - 1) * height + j][2] + flag
                        else:
                            if (num == lengths[0]) & (bad_trip == 0):
                                bad_trip = 1
                            
                    num = 0



fuck_result = Image.open(picture)
draw = ImageDraw.Draw(fuck_result)
                    
for i in range(width):
    for j in range(height):
        draw.point((i, j), (fuck_the_details[(i - 1) * height + j][0], fuck_the_details[(i - 1) * height + j][1], fuck_the_details[(i - 1) * height + j][2]))
fuck_result.save("fuck_res.jpg")


total = Image.open(picture)
draw = ImageDraw.Draw(total)

for i in range(width):
    for j in range(height):
	if (fuck_the_details[(i - 1) * height + j][0] >= 255):
            draw.point((i, j), (255, 255,255))
total.save("total.jpg")















