# Generated by Django 5.1 on 2024-09-06 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_navmodel_postion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navmodel',
            name='postion',
            field=models.ImageField(choices=[(1, '底部导航'), (0, '顶部导航')], default=0, upload_to='', verbose_name='导航位置区分'),
        ),
    ]
