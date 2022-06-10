from django.db import models


class ltrd(models.Model):

    lid =models.CharField(max_length=200,default="")
    name = models.CharField(max_length=200,default="")
    email = models.CharField(max_length=200,default="")
    password = models.CharField(max_length=200,default="")
    image1 =   models.CharField(max_length=100000,default="")
   # image2 = models.ImageField(upload_to='images',default="")
    #image3 = models.ImageField(upload_to='images',default="")
    #image4 = models.ImageField(upload_to='images',default="")
    #image5 = models.ImageField(upload_to='images',default="")


    def __str__(self):
        return self.email