from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Login_table(AbstractUser):
    usertype=models.CharField(max_length=25)

class Farmer_registration(models.Model):
    name=models.CharField(max_length=25,null=True)
    contact=models.IntegerField(null=True)
    address=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    id_proof=models.FileField(null=True)
    admin_approval=models.BooleanField(default=False)
    profile_picture=models.ImageField(null=True)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Supplier_registration(models.Model):
    name=models.CharField(max_length=25,null=True)
    contact=models.IntegerField(null=True)
    address=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    id_proof=models.FileField(null=True)
    licence=models.FileField(null=True)
    profile_picture=models.ImageField(null=True)
    admin_approval=models.BooleanField(default=False)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Specialist_registration(models.Model):
    name=models.CharField(max_length=25,null=True)
    contact=models.IntegerField(null=True)
    address=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    id_proof=models.FileField(null=True)
    licence=models.FileField(null=True)
    profile_picture=models.ImageField(null=True)
    admin_approval=models.BooleanField(default=False)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Add_tutorials(models.Model):

    title=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=500,null=True)
    video_link=models.CharField(max_length=50,null=True)
    posted_on=models.DateTimeField(null=True)

class Add_categories(models.Model):

    category=models.CharField(max_length=50,null=True)
    category_image=models.ImageField(null=True)

class Add_products(models.Model):

    product=models.CharField(max_length=50,null=True) 
    description=models.CharField(max_length=500,null=True) 
    product_image=models.ImageField(null=True) 
    quantity=models.IntegerField(null=True) 
    price=models.IntegerField(null=True) 
    category_id=models.ForeignKey(Add_categories,on_delete=models.CASCADE,null=True)
    supplier_id=models.ForeignKey(Supplier_registration,on_delete=models.CASCADE,null=True)

class Booking(models.Model):

    farmer_id=models.ForeignKey(Farmer_registration,on_delete=models.CASCADE,null=True)
    product_id=models.ForeignKey(Add_products,on_delete=models.CASCADE,null=True)
    shipping_address=models.CharField(max_length=100,null=True)
    quantity=models.IntegerField(null=True)
    payment_status=models.BooleanField(default=False)
    booking_status=models.BooleanField(default=False)
    cancel_status=models.BooleanField(default=False)
    total_price=models.IntegerField(null=True)
    booked_on=models.DateTimeField(null=True)

class Farmer_specialist_chat(models.Model):

    farmer_id=models.ForeignKey(Farmer_registration,on_delete=models.CASCADE,null=True)
    specialist_id=models.ForeignKey(Specialist_registration,on_delete=models.CASCADE,null=True)
    message=models.CharField(max_length=100,null=True)
    message_on=models.DateTimeField(null=True)
    reply=models.CharField(max_length=100,null=True)
    reply_on=models.DateTimeField(null=True)

class Feedback(models.Model):

    feedback=models.CharField(max_length=500,null=True)
    rating=models.IntegerField(null=True)
    feedback_on=models.DateTimeField(null=True)
    user_type=models.CharField(max_length=50,null=True)
    farmer_id=models.ForeignKey(Farmer_registration,on_delete=models.CASCADE,null=True)
    specialist_id=models.ForeignKey(Specialist_registration,on_delete=models.CASCADE,null=True)
    supplier_id=models.ForeignKey(Supplier_registration,on_delete=models.CASCADE,null=True)

    