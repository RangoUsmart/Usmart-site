# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# # Create your models here.
# class Post(models.Model):
#     class Meta:
#         verbose_name = 'create post'
#         verbose_name_plural = 'create posts'
        
#     title = models.CharField(max_length=200)
#     content = models.TextField(max_length=5000, blank=True, null=True, help_text="привет")
#     date_created = models.DateTimeField(default=timezone.now)
#     date_created = models.DateTimeField(auto_now=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title
    
# class User(models.Model):
#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
        
#     user_id = models.CharField(max_length=200)
#     user_login = models.TextField(max_length=5000, blank=True, null=True, help_text="Логін користувача")
#     user_name = models.TextField(max_length=5000, blank=True, null=True, help_text="Імя користувача")
#     phone_number = models.DateTimeField(auto_now=True)
#     delivery_adress = models.TextField(max_length=5000, blank=True, null=True, help_text="Адреса доставки")
#     reg_date =models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.title
