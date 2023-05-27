from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class MainUserInfo(models.Model):
    class Meta:
        verbose_name = 'Основна інформація'
        verbose_name_plural = 'Персона'
        
    user_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user_image = models.ImageField(upload_to="cv/photo", help_text="Фото")
    user_login = models.CharField(max_length=50, blank=True, null=False, help_text="Логін користувача")
    user_name = models.CharField(max_length=30, blank=True, null=True, help_text="Імя")
    user_sur_name = models.CharField(max_length=50, blank=True, null=True, help_text="Прізвище")
    user_birthday =models.DateTimeField(blank=True, null=True, help_text="Дата народження")
    user_email = models.EmailField()
    user_phone = models.PositiveIntegerField( blank=True, null=True, help_text="Телефон")
    user_site = models.TextField(max_length=100, blank=True, null=True, help_text="Сайт")
    reg_date = models.DateTimeField(auto_now=True)
    user_subscribe = RichTextField(max_length=5000, blank=True, null=True, help_text="Короткий опис")
    
    def __str__(self):
        return self.user_name

class MainUserExp(models.Model):
    class Meta:
        verbose_name = 'Досвід'
        verbose_name_plural = 'Досвід роботи'
    person = models.ForeignKey('MainUserInfo', on_delete=models.CASCADE)
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
        
    person = models.ForeignKey('MainUserInfo', on_delete=models.CASCADE) 
    skill_id = models.CharField(max_length=4)    
    skill_name = models.TextField(max_length=100, blank=True, null=True, help_text="Назва")
    skill_count = models.CharField(max_length=4, help_text="Рівень навику")
    skill_status = models.CharField(max_length=1, choices=CHOICES, help_text="Статус")
    skill_description = models.TextField(max_length=1000, blank=True, null=True, help_text="Короткий опис")
    
    def __str__(self):
        return self.skill_name
    
class MainUserSocial(models.Model):
    CHOICES = (
        ('fb', 'Фейсбук'),
        ('linkid', 'Лінкайді'),
        ('utube', 'Ютуб')
    )
    
    class Meta:
        verbose_name = 'Соціальні медіа'
        verbose_name_plural = 'Соціальні медіа'
        
    person = models.ForeignKey('MainUserInfo', on_delete=models.CASCADE) 
    social_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    social_link = models.URLField(max_length=50, blank=True, null=True, help_text="Посилання")
    social_name = models.CharField(max_length=7, choices=CHOICES, help_text="Назва")   
    def __str__(self):
        return self.social_name