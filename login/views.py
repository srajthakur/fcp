from django.shortcuts import render , redirect
from django.http.response import StreamingHttpResponse
from login.cam import FaceDetect
from django.contrib import messages
from django.http import HttpResponse
from .models import*
from PIL import Image
from numpy import asarray

import cv2
import face_recognition
import PIL as pillow

import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

def index(request):
    return render(request, 'signup_collecting_data.html')
def signup(request):
    if request.method == "POST":
        username = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        log = ltrd.objects.filter(name=username)
        if len(log) == 1:
            messages.info(request, 'User already registered')
            return render(request, 'signup.html')

        if password != password2:
            messages.info(request, 'password not match')
            return render(request, 'signup.html')
        image1 = 'D://Django Project//fcp//fcp//login//image//im' + str(len(ltrd.objects.all()) + 1) + '.jpg'

        log = ltrd(lid=str(len(ltrd.objects.all()) + 1),name=username, email=username, password=password, image1=image1)

        log.save()
        messages.success(request, " sucessfully ")
        return redirect('home')
    else:
        return render(request, 'signup.html')



    return render(request,'signup.html')
def home(request):


    return render(request,'home.html')



def gen(camera,request):
    print("gggggggggggggggggggggggggggggassggggggggggggggggggggggggg")
    detector = cv2.CascadeClassifier('E:\python 3.9\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    sampleNum =0
    while True:
        img,frame = camera.get_frame()
        #print(sampleNum)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        file_name_path = 'D://Django Project//fcp//fcp//login//image//im' + str(len(ltrd.objects.all()) + 1) + '.jpg'
        cv2.imwrite(file_name_path, img)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # incrementing sample number
            sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder

            file_name_path = 'D://Django Project//fcp//fcp//login//image//im' + str(len(ltrd.objects.all()) + 1) + '.jpg'
           # cv2.imwrite(file_name_path, gray[y:y + h, x:x + w])

        if sampleNum > 100:
            return render(request, 'home.html')
        #print(sampleNum)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    return render(request, 'home.html')
def use_camera(request):
    print("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
    k=gen(FaceDetect(),request)
    print("asfesgfsdgfdhbfdghjmf")
    if k == 0:
        print("ldkjhgd;fgjedhlrek;jgnrel/gb")
    return StreamingHttpResponse(k,
                                 content_type='multipart/x-mixed-replace; boundary=frame')



def login(request):
    if request.method == "POST":

        phone = request.POST.get('phone', '')


        cam = cv2.VideoCapture(0)
        i=1
        j=1

        detector = cv2.CascadeClassifier('E:\python 3.9\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
        while True :
                if i%5==0:
                    j=j+1

                ret, img1 = cam.read()
                cv2.imwrite('D://Django Project//fcp//fcp//login//image//c.jpg', img1)

                img = cv2.imread('D://Django Project//fcp//fcp//login//image//im' + str(j) + '.jpg')
                img1 = cv2.imread('D://Django Project//fcp//fcp//login//image//c.jpg')

                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

                face = face_recognition.face_encodings(img)[0]
                enc = face_recognition.face_encodings(img1)[0]

                r = face_recognition.compare_faces([face], enc)
                ra = face_recognition.face_distance([face], enc)
                print(r)
                print(ra)
                i=i+1
                print(r)
                if r==[True]:
                    print("sucess")
                    print(j)
                    k=ltrd.objects.filter(lid=j)
                    k="hello " + k[0].name
                    return HttpResponse(k)
                else :
                    print("false")



        cam.release()
        cv2.destroyAllWindows()





    return render(request, 'login.html')





