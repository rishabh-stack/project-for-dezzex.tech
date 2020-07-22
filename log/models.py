from django.db import models

# Create your models here.
class signUp(models.Model):
    user_id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    passp=models.CharField(max_length=200)
    dob=models.DateField()
    img=models.ImageField(upload_to="log/images",default="")
    password=models.CharField(max_length=50,default="")
    def __str__(self):
         return self.fullname