import datetime
from attrs import exceptions
from prettytable import PrettyTable
from moviepy.editor import VideoFileClip
import cv2
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
client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client['demos']
doc = db['values']
currentime =time.time()
currentime2 =time.time()
currentime3 =time.time()
currentime4 =time.time()
currentime5 =time.time()
currentime6 =time.time()
t1 = float()
t2 = float()
t3 = float()
t4 = float()
t5 = float()
t6=float()
i =float()
e =float()
w =float()
s =float()
a=float()
b=float()
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
        img =cv2.resize(img,(400,600))
        #img = cv2.imread("videos/1.png")
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        #print(lmList)
        if len(lmList) != 0:
                 #right Hand
                 wrist = detector.findwrist(img, 16, 20, 22)
                 #hand = detector.Findhand(img, 12, 14, 16)
                 hand = detector.upperarm(img, 12, 14, 24)
                 leg = detector.findleg( img, 24, 28, 32)
                 #neck = detector.findneck(img, 6,8,12)
                 #wrist = detector.findneck(img, 18,20,22)

                # print("wrist",wrist)
                 print("hand",wrist)
                 #print("neck",neck)
                 #print("leg",leg)
                 now =datetime.datetime.now()
                 Currentime = time.time()
                 #print(start_time)
                 #mydoc = {"hand_angle":hand,"leg_angle":leg,"time":now}
                 #insertmy = doc.insert_one(mydoc)
                 #print(insertmy)
                 # left Hand
                 #temp =0
                # recent =
                 start_time = time.time()
                 #if temp 0<20:

                 if wrist <15:
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
                 if wrist>=15:
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
                 if hand <=20:
                  t3= time.time() - currentime3
                  #print(time.time() - currentime)
                  #print(t1)
                 else:
                     if t3 !=0:
                       w +=t3
                       #print(t3)
                     t3=0

                     #print(time.time() - currentime)
                     currentime3 = time.time()
                 if hand>= 20 and hand<=45:
                     t4= time.time() - currentime4
                     #print(time.time() - currentime2)
                 else:
                     if t4!=0:
                          s+= t4
                          #print(e)
                     t4 = 0
                     #print("less",time.time() - currentime)
                     currentime4 = time.time()
                 if hand2 <= 15:
                  t5= time.time() - currentime5
                  #print(time.time() - currentime)
                  #print(t1)
                 else:
                     if t5 !=0:
                       a +=t5
                       #print(t3)
                     t5=0
                     currentime5 = time.time()
                 if hand2>= 16 and hand2<=45:
                     t6= time.time() - currentime6
                     #print(time.time() - currentime2)
                 else:
                     if t6!=0:
                          b+= t6

                     t6 = 0
                     #print("less",time.time() - currentime)
                     currentime6 = time.time()

                 mydoc = {"angle of hand": hand2, "angle of leg": leg, "hand<=20": i, "hand>=20 and <=45": e,
                          "leg<=20": w, "leg>=20 and <=45": s}
                 myinsert = doc.insert_one(mydoc)
                 #print(myinsert)
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

else:
    print(le)

table = PrettyTable()
table.field_names=["fields","<=20",">=20 and 45"]
table.add_row(["hand",i,e])
table.add_row(["leg",w,s])
print(table)
lv=0
le=0
if i < e:
    le=le+2
else:
    lv=lv
if i>e:
    lv=lv+1
else:
    le=le
lo=0
se=0
if w<s:
    se=se+2
else:
    lo=lo
if w>s:
    lo=lo+1
else:
    se=se
totalh =lv+le
totall=lo+se
level = PrettyTable()
level.field_names = ["object","lvl1","lvl2","Total"]
level.add_row(["hand",lv,le,totalh])
level.add_row(["leg",lo,se,totall])
print(level)
print(a)
print(b)
print(w)
print(s)
print(i)
print(e)