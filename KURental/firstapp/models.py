from django.db import models

# Create your models here.

class RenterInfo(models.Model):
    username= models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    
    def __str__(self):
       return self.username


class RentDetails(models.Model):
    property_type=models.CharField(max_length=100)
    floor_no=models.CharField(max_length=20)
    distance=models.IntegerField()
    location=models.CharField(max_length=200)
    images=models.ImageField()
    area=models.IntegerField()
    no_of_rooms=models.IntegerField()
    price=models.IntegerField()
    property_choices=[
        ('hostel','HOST'),
        ('house','HOUSE') ,
        ('room','ROOM'),
        ('flat','FLAT') ]
    property_type=models.CharField(
    max_length=10,
    choices=property_choices,
  )
    renterInfo=models.OneToOneField(RenterInfo, on_delete=models.CASCADE,null=True)

class RenteeInfo(models.Model):
   username= models.CharField(max_length=100)
   password=models.CharField(max_length=50)
  
   def __str__(self):
    return self.username
    