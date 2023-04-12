from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    class Meta():
        verbose_name = "Запис"
        verbose_name_plural = "Записи"
        
    title =models.CharField("Заголоавок", max_length=200)
    description=models.TextField("Короткий опис", max_length=400)
    content=RichTextField("Основний текст",blank=True, max_length=10000)
    # date= models.DateField("Дата створення")
    image=models.ImageField(upload_to="image/%Y", null=True)
    
    def __repr__(self):
        return 'Image(%s, %s)' % (self.title, self.image)
    
    def __str__(self) -> str:
        return f'{self.title}, {self.description}'