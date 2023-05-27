from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image=models.ImageField(upload_to="image/theme/%Y", null=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тема'
        verbose_name_plural = 'Теми'

    def __str__(self):
        return self.name
    
    
    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_category',
    #                     args=[self.slug])
class Post(models.Model):
    class Meta():
        verbose_name = "Запис"
        verbose_name_plural = "Записи"
        # index_together = (('id', 'slug'),)
        
    
    theme= models.ForeignKey(Theme, related_name='Теми', on_delete=models.CASCADE)
    title =models.CharField("Заголовок", max_length=200, db_index=True)
    # title2 =models.CharField("Заголовок", max_length=200, db_index=True)
    slug = models.SlugField( max_length=200, db_index=True, unique=True, auto_created=True,)
    description=models.TextField("Короткий опис", max_length=400)
    content=RichTextField("Основний текст",blank=True, max_length=10000)
    # date= models.DateField("Дата створення")
    image=models.ImageField(upload_to="image/%Y", null=True)
    
    def __repr__(self):
        return 'Image(%s, %s)' % (self.title, self.image)
    
    def __str__(self) -> str:
        return f'{self.title}, {self.description}'