# Generated by Django 4.1.7 on 2023-03-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_mainuserskill_delete_mainuserskills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuserskill',
            name='skill_status',
            field=models.CharField(choices=[('a', 'Вивчаю'), ('b', 'На паузі'), ('c', 'В планах')], default=1, help_text='Статус', max_length=1),
            preserve_default=False,
        ),
    ]
