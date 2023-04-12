import datetime
from attrs import exceptions
from prettytable import PrettyTable
from moviepy.editor import VideoFileClip
import cv2
import mediapipe as mp
import numpy as np
from decimal import Decimal
import poseModule as pm
import time
import json
import pymongo
file ="videos/2.mp4"
clip = VideoFileClip(file)
duration = clip.duration
start_Time = time.time()
print(duration)
#hands = None
#legs = None
strt= time.time()
elapsed_time=0
start_time=time.time()
video = cv2.VideoCapture("videos/3.mp4")
vid = VideoFileClip("videos/2.mp4")
detector = pm.PoseDetector()
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client['demos']
doc = db['ergonomics']
currentime = time.time()
currentime2 = time.time()
currentime3 = time.time()
currentime4 = time.time()
currentime5 = time.time()
currentime6 = time.time()
currentime7 = time.time()
currentime8 = time.time()
currentime9 = time.time()
currentime10 = time.time()
currentime11 = time.time()
currentime12 = time.time()
currentime13 = time.time()
currentime14 = time.time()
currentime15 = time.time()
currentime16 = time.time()
t1 = float()
t2 = float()
t3 = float()
t4 = float()
t5 = float()
t6 = float()
t7 = float()
t8 = float()
t9 = float()
t10 = float()
t11 = float()
t12 = float()
t13 = float()
t14 = float()
t15 = float()
t16 = float()
i = float()
e = float()
w = float()
s = float()
a = float()
b = float()
up1 = float()
up2 = float()
up3 = float()
up4 = float()
la1 = float()
la2 = float()
wr1 = float()
wr2 = float()
leg1 = float()
leg2 = float()
while True:
    try:
        c = (time.time() - strt)
        #print(c)
        x = Decimal(c)
        y = Decimal(duration)
        if y - x <= 0:
            print("stop")
            break
        success, img = video.read()
        pose = video.read()
        img = cv2.resize(img,(400,600))
        #img = cv2.imread("videos/1.png")
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        #print(lmList)
        if len(lmList) != 0:
                 neck = detector.findneck(img,12,8,6)
                 trunk = detector.findtrunk(img,24,12,24)
                 upperarm = detector.upperarm(img,12,14,24)
                 lowerarm = detector.lowerarm(img,14,18,22)
                 wrist = detector.findwrist(img,16,20,22)
                 leg= detector.findleg(img,24,28,32)
                 start_time = time.time()
                 #if temp 0<20:

                 if neck<=20:
                  t1= time.time() - currentime
                  #print(time.time() - currentime)
                  #print(t1)
                 else:
                     if t1 !=0:
                       i +=t1
                       #print(t1)
                     t1=0
                     #print(time.time() - currentime)
                     currentime = time.time()
                 if neck>=20:
                     t2= time.time() - currentime2
                     #print(time.time() - currentime2)
                 else:
                     if t2!=0:
                          e+= t2
                          #print(e)
                     t2 = 0
                     #print("less",time.time() - currentime)
                     currentime2 = time.time()
                 #print(hands)
                 if trunk == 0:
                     t3 = time.time() - currentime3
                     # print(time.time() - currentime)
                     # print(t1)
                 else:
                     if t3 != 0:
                         w += t3
                         # print(t3)
                     t3 = 0

                     # print(time.time() - currentime)
                     currentime3 = time.time()
                 if trunk >=0 and trunk <=20:
                     t4 = time.time() - currentime4
                     # print(time.time() - currentime2)
                 else:
                     if t4 != 0:
                         s += t4
                         # print(e)
                     t4 = 0
                     # print("less",time.time() - currentime)
                     currentime4 = time.time()
        if trunk >= 20 and  trunk <= 60:
            t5 = time.time() - currentime5
            # print(time.time() - currentime)
            # print(t1)
        else:
            if t5 != 0:
                a += t5
                # print(t3)
            t5 = 0
            # print(time.time() - currentime)
            currentime5 = time.time()
        if trunk >= 60:
            t6 = time.time() - currentime6
            # print(time.time() - currentime2)
        else:
            if t6 != 0:
                b += t6
                # print(e)
            t6 = 0
            # print("less",time.time() - currentime)
            currentime6 = time.time()
        if upperarm <=20:
            t7 = time.time() - currentime7
            # print(time.time() - currentime)
            # print(t1)
        else:
            if t7 != 0:
                up1 += t7
                # print(t3)
            t7 = 0

            # print(time.time() - currentime)
            currentime7 = time.time()
        if upperarm >= 20 and trunk <= 45:
            t8 = time.time() - currentime8
            # print(time.time() - currentime2)
        else:
            if t8 != 0:
                up2 += t8
                # print(e)
            t8 = 0
            # print("less",time.time() - currentime)
            currentime8 = time.time()
        if upperarm >= 45 and upperarm <= 90:
            t9 = time.time() - currentime9
            # print(time.time() - currentime)
            # print(t1)
        else:
            if t9 != 0:
                up3 += t9
                # print(t3)
            t9 = 0
            # print(time.time() - currentime)
            currentime9 = time.time()
        if upperarm >= 90:
            t10 = time.time() - currentime10
            # print(time.time() - currentime2)
        else:
            if t10 != 0:
                up4 += t10
                # print(e)
            t10 = 0
            # print("less",time.time() - currentime)
            currentime10 = time.time()
        if lowerarm >=60 and lowerarm<=100:
            t11 = time.time() - currentime11
            # print(time.time() - currentime)
            # print(t1)
        else:
            if t11 != 0:
                la1 += t11
                # print(t1)
            t11 = 0
            # print(time.time() - currentime)
            currentime11 = time.time()
        if lowerarm <= 60:
            t12 = time.time() - currentime12
            # print(time.time() - currentime2)
        else:
            if t12 != 0:
                la2 += t12
                # print(e)
            t12 = 0
            # print("less",time.time() - currentime)
            currentime12 = time.time()
        if wrist<=15:
            t13 = time.time() - currentime13
            # print(time.time() - currentime)
            # print(t1)
        else:
            if t13 != 0:
                wr1 += t13
                # print(t1)
            t13 = 0
            # print(time.time() - currentime)
            currentime13 = time.time()
        if wrist >= 15:
            t14 = time.time() - currentime14
            # print(time.time() - currentime2)
        else:
            if t14 != 0:
                wr2 += t14
                # print(e)
            t14 = 0
            # print("less",time.time() - currentime)
            currentime14 = time.time()
        if leg<=60:
            t15 = time.time() - currentime15
            # print(time.time() - currentime)
            # print(t1)
        else:
            if t15 != 0:
                leg1 += t15
                # print(t1)
            t15 = 0
            # print(time.time() - currentime)
            currentime15 = time.time()
        if leg >= 60:
            t16 = time.time() - currentime16
            # print(time.time() - currentime2)
        else:
            if t16 != 0:
                leg2 += t16
                # print(e)
            t16 = 0
            # print("less",time.time() - currentime)
            currentime16 = time.time()
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    except:
        #print("err")
        pass
#print("hello",hands)
#print("hand less than 20 degree",i)
#print("hand greater than 20 degree",e)
#print("leg less than 20 degree",w)
#print("leg greater than 20 degree",s)
#print(a)
print(i)
print(e)
table = PrettyTable()
table.field_names=["fields","10 to 20",">=20 "]
table.add_row(["neck",i,e])
print(table)
find = PrettyTable()
find.field_names =["fields","0","0-20","20-60",">60"]
find.add_row(["trunk",w,s,a,b])
print(find)
create = PrettyTable()
create.field_names =["fields","<20","20-45","45-90",">90"]
create.add_row(["upperarm",up1,up2,up3,up4])
print(create)
adjust = PrettyTable()
adjust.field_names =["fields","60-100","<60"]
adjust.add_row(["lowerarm",la1,la2])
print(adjust)
duck = PrettyTable()
duck.field_names =["fields","<15",">15"]
duck.add_row(["wrist",wr1,wr2])
print(duck)
mode = PrettyTable()
mode.field_names = ["fields", "30-60", ">60"]
mode.add_row(["leg", leg1, leg2])
print(mode)
caption=0
if w > s and w>a and w>b:
    caption=caption+1
elif s>w and s>a and s>b:
    caption = caption+2
elif a>w and a>s and a>b:
    caption=caption+3
elif b>w and b>s and b>a:
    caption=caption+4
tony=0
if i>e:
    tony=tony+1
if e>i:
    tony=tony+2
hulk=0
if la1>la2:
    hulk=hulk+1
elif la2>la1:
    hulk=hulk+2
wanda=0
if up1>up2 and up1>up3 and up1>up4:
    wanda=wanda+1
elif up2>up1 and up2>up3 and up2>up4:
    wanda=wanda+2
elif up3>up1 and up3>up2 and up3>up4:
    wanda=wanda+3
elif up4>up1 and up4>up2 and up4>up3:
    wanda=wanda+4
panther=0
if wr1>wr2:
    panther=panther+1
elif wr2>wr1:
    panther=panther+2
miller=0
if leg1>leg2:
    miller=miller+1
if leg2>leg1:
    miller=miller+2
m = PrettyTable()
m.field_names =["neck","lowerarm","upperarm","wrist","leg","trunk"]
m.add_row([tony,hulk,wanda,panther,miller,caption])
print(m)
lp=0
lg=0

Source={
    1:{
        1:{
            1:1,
            2:2,
            3:2,
            4:3
        },
        2:{
            1:2,
            2:3,
            3:4,
            4:5
        }
    },
    2:{
        1:{
            1:1,
            2:3,
            3:4,
            4:5
        },
        2:{
            1:2,
            2:4,
            3:5,
            4:6
        }
    }
}

for i in range(1,3):
    for j in range(1,3):
        for x in range(1,5):
            if tony == i and miller == j and caption == x:
                lp = lp+Source[i][j][x]
            if hulk == i and panther == j and wanda == x:
                lg = lg + Source[i][j][x]
#
van = PrettyTable()
van.field_names=["grade A","grade B"]
van.add_row([lp,lg])
print(van)
clr=0
if lp==1 and lg == 1:
    clr=clr+1
elif lp==2 and lg==1:
    clr=clr+1
elif lp==3 and lg==1:
    clr=clr+2
elif lp == 4 and lg == 1:
    clr = clr + 3
elif lp == 5 and lg == 1:
    clr = clr + 4
elif lp == 6 and lg == 1:
    clr = clr + 6
elif lp==1 and lg==2:
    clr=clr+1
elif lp==2 and lg==2:
    clr=clr+2
elif lp == 3 and lg == 2:
    clr = clr + 3
elif lp == 4 and lg == 2:
    clr = clr + 4
elif lp == 5 and lg == 2:
    clr = clr + 4
elif lp==6 and lg==2:
    clr=clr+6
elif lp==1 and lg==3:
    clr=clr+1
elif lp == 2 and lg == 3:
    clr = clr + 2
elif lp == 3 and lg == 3:
    clr = clr + 3
elif lp == 4 and lg == 3:
    clr = clr + 4
elif lp==5 and lg==3:
    clr=clr+4
elif lp==6 and lg==3:
    clr=clr+6
elif lp == 1 and lg == 4:
    clr = clr + 2
elif lp == 2 and lg == 4:
    clr = clr + 3
elif lp == 3 and lg == 4:
    clr = clr + 3
elif lp==4 and lg==4:
    clr=clr+4
elif lp==5 and lg==4:
    clr=clr+5
elif lp == 6 and lg == 4:
    clr = clr + 7
elif lp == 1 and lg == 5:
    clr = clr + 3
elif lp == 2 and lg == 5:
    clr = clr + 4
elif lp == 3 and lg == 5:
    clr = clr+4
elif lp == 4 and lg == 5:
    clr = clr+5
elif lp == 5 and lg == 5:
    clr = clr + 6
elif lp == 6 and lg == 5:
    clr = clr + 8
elif lp == 1 and lg == 6:
    clr = clr + 4
elif lp == 2 and lg == 6:
    clr = clr+5
elif lp == 3 and lg == 6:
    clr = clr+6
elif lp == 4 and lg == 6:
    clr = clr + 7
elif lp == 5 and lg == 6:
    clr = clr + 8
elif lp == 6 and lg == 6:
    clr = clr + 9

dunk = PrettyTable()
dunk.field_names = ["Final score"]
dunk.add_row([clr])
print(dunk)
