import time
from datetime import *
from threading import Timer


#what sites do you want to block
#working hours?
#while loop

def blockstart():
    test_r = open(path, 'r')
    test_add = open(path, 'a')


    for i in range(0,len(blcksarray)):
        if blcksarray[i] != 0:
            test_add.write("\n127.0.0.1 " + blcksarray[i])



    test_r.close()
    test_add.close()
    # if datetime.today().minute == int(hours[1]):
    # break;
def blockover():
    test_r = open(path, "r+")
    text = test_r.readlines()
    test_r.seek(0)
    c = 0

    for i in text:
        clean = i.strip('\n')
        print clean
        print blcksarray
        if (blcksarray[c]!= 0) and (clean != ("127.0.0.1 " + str(blcksarray[c]))):
            test_r.write(i)
        else:
            c = c + 1

    test_r.truncate()
    test_r.close()



print datetime.today().minute
path = r'C:\Users\princ\Desktop\dog.txt'

blockedsite = raw_input("what sites do you want to block?")
workhours = raw_input("What are your working hours?")
blcksarray=blockedsite.split(",")
hours = workhours.split(",")
print blcksarray
print hours

test_r = open(path, 'r')
test_add = open(path, 'a')
filearray = (test_r.read()).split("127.0.0.1 ")

filearray = map(lambda x: x.strip(), filearray)
print list(filearray)

# check if site to be blocked is already in file
for n in range(0, len(blcksarray)):
    for i in range(0, len(filearray)):
        # print blcksarray[n] + '    ' + filearray[i]
        if blcksarray[n] == filearray[i]:
            blcksarray[n] = 0

test_r.close()
test_add.close()

#if current time is between given time range start block funcion and timer the end of it
if datetime.today().minute >= int(hours[0]) and datetime.today().minute <= int(hours[1]):
        blockstart()
        stoped = Timer((int(hours[1])-int(datetime.today().minute))*60, blockover)
        stoped.start()
#if current time is before given time range timer the start and end function
else:
    started = Timer((int(datetime.today().minute)-int(hours[0]))*60, blockstart)
    started.start()

    stoped = Timer((int(hours[1])-int(datetime.today().minute))*60, blockover)
    stoped.start()

test = open(path, 'r')
print test.read()
test.close()


