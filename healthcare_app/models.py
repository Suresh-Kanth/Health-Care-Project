from django.db import models
from django.utils import timezone
import uuid

# class Doctor(models.Model):
#     first_name = models.CharField("First Name", max_length=122, null=False, blank=False)
#     last_name = models.CharField("Last Name", max_length=122, null=False, blank=False)
#     username = models.CharField("Username", max_length=50, null=False, blank=False)
#     email = models.EmailField("Email ID", unique=True, null=False, blank=False)
#     address_line1 = models.CharField("Address Line 1", max_length=255, null=False, blank=False)
#     city = models.CharField("City", max_length=50, null=False, blank=False)
#     state = models.CharField("State", max_length=50, null=False, blank=False)
#     pincode = models.CharField("Pincode", max_length=10, null=False, blank=False)
#     image = models.ImageField(upload_to='pics',default='default.svg')

#     def natural_key(self):
#         return self.email

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


# class Patient(models.Model):
#     first_name = models.CharField("First Name", max_length=122, null=False, blank=False)
#     last_name = models.CharField("Last Name", max_length=122, null=False, blank=False)
#     username = models.CharField("Username", max_length=50, null=False, blank=False)
#     email = models.EmailField("Email ID", unique=True, null=False, blank=False)
#     address_line1 = models.CharField("Address Line 1", max_length=255, null=False, blank=False)
#     city = models.CharField("City", max_length=50, null=False, blank=False)
#     state = models.CharField("State", max_length=50, null=False, blank=False)
#     pincode = models.CharField("Pincode", max_length=10, null=False, blank=False)
#     image = models.ImageField(upload_to='pics',default='default.svg')
    
#     def natural_key(self):
#         return self.email

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


class Users(models.Model):
    first_name = models.CharField("First Name", max_length=122, null=False, blank=False)
    last_name = models.CharField("Last Name", max_length=122, null=False, blank=False)
    username = models.CharField("Username", max_length=50, null=False, blank=False)
    email = models.EmailField("Email ID", unique=True, null=False, blank=False)
    address_line1 = models.CharField("Address Line 1", max_length=255, null=False, blank=False)
    city = models.CharField("City", max_length=50, null=False, blank=False)
    state = models.CharField("State", max_length=50, null=False, blank=False)
    pincode = models.CharField("Pincode", max_length=10, null=False, blank=False)
    image = models.ImageField(upload_to='pics',default='default.svg')
    is_doctor = models.BooleanField(default=True)

    def natural_key(self):
        return self.email

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Blog(models.Model):
    no = models.CharField("Blog Number",max_length=50, default=uuid.uuid4, null=False, blank=False, editable=False,unique=True)
    title = models.CharField("Title", max_length=255, null=False, blank=False)
    image = models.ImageField("Image", upload_to='pics', null=True, blank=True)
    category = models.CharField("Category", max_length=50, null=False, blank=False)
    summary = models.TextField("Summary", null=False, blank=False)
    content = models.TextField("Content", null=False, blank=False)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='blogs')
    draft = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def natural_key(self):
        return self.no
    
