from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class MainUserInfo(models.Model):
    class Meta:
        verbose_name = 'Основна інформація'
        verbose_name_plural = 'Резюме'
        
    user_id = models.CharField(max_length=200)
    user_image = models.ImageField(upload_to="cv/photo", help_text="Фото")
    user_login = models.TextField(max_length=50, blank=True, null=True, help_text="Логін користувача")
    user_name = models.TextField(max_length=30, blank=True, null=True, help_text="Імя")
    user_sur_name = models.TextField(max_length=50, blank=True, null=True, help_text="Прізвище")
    user_birthday =models.DateTimeField(blank=True, null=True, help_text="Дата народження")
    user_email = models.TextField(max_length=100, blank=True, null=True, help_text="Електронна пошта")
    user_phone = models.TextField(max_length=12, blank=True, null=True, help_text="Телефон")
    user_site = models.TextField(max_length=100, blank=True, null=True, help_text="Сайт")
    reg_date = models.DateTimeField(auto_now=True)
    user_subscribe = RichTextField(max_length=5000, blank=True, null=True, help_text="Короткий опис")
    
    def __str__(self):
        return self.user_name

class MainUserExp(models.Model):
    class Meta:
        verbose_name = 'Досвід'
        verbose_name_plural = 'Досвід роботи'
        
    work_id = models.CharField(max_length=4, blank=True,)
    work_company = models.TextField(max_length=100, blank=True, null=True, help_text="Назва компанії")
    work_position = models.TextField(max_length=100, blank=True, null=True, help_text="Імя")
    work_description = models.TextField(max_length=100, blank=True, null=True, help_text="Прізвище")
    work_start = models.DateField(auto_now_add=False, blank=True,)
    work_end = models.DateField(auto_now_add=False, blank=True,)
    
    def diff_date(self):
        return (self.work_end.year-self.work_start.year)
    
    def __str__(self):
        return self.work_company
    
class MainUserSkill(models.Model):
    CHOICES = (
        ('a', 'Вивчаю'),
        ('b', 'На паузі'),
        ('c', 'В планах')
    )
    
    class Meta:
        verbose_name = 'Навички'
        verbose_name_plural = 'Навички'
    skill_id = models.CharField(max_length=4)    
    skill_name = models.TextField(max_length=100, blank=True, null=True, help_text="Назва")
    skill_count = models.CharField(max_length=4, help_text="Рівень навику")
    skill_status = models.CharField(max_length=1, choices=CHOICES, help_text="Статус")
    skill_description = models.TextField(max_length=1000, blank=True, null=True, help_text="Короткий опис")
    
    def __str__(self):
        return self.skill_name
    
class UserSocial(models.Model):
    class Meta:
        verbose_name = 'Соціальні медіа'
        verbose_name_plural = 'Соціальні медіа'
        
    user_id = models.CharField(max_length=200)
    social_id = models.ImageField(upload_to="cv/photo", help_text="Фото")
    social_link = models.TextField(max_length=50, blank=True, null=True, help_text="Логін користувача")
    social_icn = models.TextField(max_length=30, blank=True, null=True, help_text="Імя")
    social_name = models.TextField(max_length=50, blank=True, null=True, help_text="Прізвище")    
    def __str__(self):
        return self.link