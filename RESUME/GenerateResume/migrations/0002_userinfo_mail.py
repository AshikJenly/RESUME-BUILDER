# Generated by Django 4.1 on 2023-04-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GenerateResume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='mail',
            field=models.CharField(default='nogmail', max_length=30),
        ),
    ]
