# Generated by Django 5.1 on 2024-08-28 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=None, db_index=True, max_length=200, null=True, verbose_name='名称')),
                ('orders', models.IntegerField(default=0, verbose_name='序号')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('image', models.ImageField(upload_to='banner/%Y')),
                ('link', models.CharField(max_length=300, verbose_name='是否为外部链接')),
                ('note', models.CharField(max_length=100, verbose_name='备注信息')),
                ('is_http', models.BooleanField(default=False, help_text='站点外部连接：http://www.baidu.com <br>站点内的连接：/home/detail/', verbose_name='是否为外部链接')),
            ],
            options={
                'verbose_name': '轮播广告',
                'verbose_name_plural': '轮播广告',
                'db_table': 'fg_banner',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='navmodel',
            name='postion',
            field=models.ImageField(choices=[(0, '顶部导航'), (1, '底部导航')], default=0, upload_to='', verbose_name='导航位置区分'),
        ),
    ]
