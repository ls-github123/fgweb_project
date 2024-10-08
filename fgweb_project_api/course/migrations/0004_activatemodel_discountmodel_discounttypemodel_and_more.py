# Generated by Django 5.1 on 2024-09-04 10:53

import ckeditor_uploader.fields
import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_coursemodel_status_alter_teachermodel_avatar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=None, db_index=True, max_length=200, null=True, verbose_name='名称')),
                ('orders', models.IntegerField(default=0, verbose_name='序号')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('start_time', models.DateTimeField(default=datetime.datetime(2024, 9, 4, 18, 53, 52, 677666), verbose_name='开始时间')),
                ('end_time', models.DateTimeField(default=datetime.datetime(2024, 9, 4, 18, 53, 52, 677666), verbose_name='结束时间')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='活动介绍')),
                ('remark', models.CharField(blank=True, max_length=300, null=True, verbose_name='备注信息')),
            ],
            options={
                'verbose_name_plural': '优惠活动',
                'db_table': 'fg_activate',
            },
        ),
        migrations.CreateModel(
            name='DiscountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=None, db_index=True, max_length=200, null=True, verbose_name='名称')),
                ('orders', models.IntegerField(default=0, verbose_name='序号')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('condition', models.IntegerField(blank=True, default=0, verbose_name='优惠条件')),
                ('sale', models.CharField(max_length=50, verbose_name='优惠公式')),
            ],
            options={
                'verbose_name_plural': '折扣表',
                'db_table': 'fg_discount',
            },
        ),
        migrations.CreateModel(
            name='DiscountTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=None, db_index=True, max_length=200, null=True, verbose_name='名称')),
                ('orders', models.IntegerField(default=0, verbose_name='序号')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=300, null=True, verbose_name='备注信息')),
            ],
            options={
                'verbose_name_plural': '优惠类型',
                'db_table': 'fg_discount_type',
            },
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='course_type',
            field=models.SmallIntegerField(choices=[(0, '付费购买'), (2, '学位课程'), (1, '会员专享')], default=0, verbose_name='付费课程'),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='level',
            field=models.SmallIntegerField(choices=[(0, '初级'), (2, '高级'), (1, '中级')], default=0, verbose_name='难度等级'),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '下线'), (2, '预上线'), (0, '上线')], default=0, verbose_name='课程状态'),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='role',
            field=models.SmallIntegerField(choices=[(1, '导师'), (0, '讲师'), (2, '班主任')], default=0, verbose_name='讲师身份'),
        ),
        migrations.CreateModel(
            name='CourseActivateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=None, db_index=True, max_length=200, null=True, verbose_name='名称')),
                ('orders', models.IntegerField(default=0, verbose_name='序号')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('activate', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='price_list', to='course.activatemodel', verbose_name='活动')),
                ('course', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='price_list', to='course.coursemodel', verbose_name='课程')),
                ('discount', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='price_list', to='course.discountmodel', verbose_name='折扣')),
            ],
            options={
                'verbose_name_plural': '课程活动',
                'db_table': 'fg_course_activate_price',
            },
        ),
        migrations.AddField(
            model_name='discountmodel',
            name='discount_type',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='course.discounttypemodel', verbose_name='优惠类型'),
        ),
    ]
