# Generated by Django 5.1 on 2024-09-06 08:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0009_alter_activatemodel_end_time_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=None, db_index=True, max_length=200, null=True, verbose_name='名称')),
                ('orders', models.IntegerField(default=0, verbose_name='序号')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('discount', models.SmallIntegerField(choices=[(0, '减免'), (1, '折扣')], default=1, verbose_name='优惠方式')),
                ('coupon_type', models.SmallIntegerField(choices=[(1, '指定方向专业'), (3, '指定课程'), (2, '指定课程分类'), (0, '通用类型')], default=0, verbose_name='优惠券类型')),
                ('get_type', models.SmallIntegerField(choices=[(0, '系统赠送'), (1, '用户领取')], default=0, verbose_name='优惠券领取方式')),
                ('total', models.IntegerField(blank=True, default=100, null=True, verbose_name='发放数量')),
                ('has_total', models.IntegerField(blank=True, default=100, null=True, verbose_name='剩余数量')),
                ('start_time', models.DateTimeField(verbose_name='使用时间')),
                ('end_time', models.DateTimeField(verbose_name='过期时间')),
                ('condition', models.IntegerField(blank=True, default=0, verbose_name='满足优惠券使用的价格条件')),
                ('per_limit', models.SmallIntegerField(default=1, verbose_name='每人限制领取的数量')),
                ('sale', models.TextField(help_text='*表示折扣，例如：*0.8表示打8折-表示满减，-100表示总价基础上减少100块人民币', verbose_name='优惠公式')),
            ],
            options={
                'verbose_name_plural': '优惠券',
                'db_table': 'fg_coupon',
            },
        ),
        migrations.CreateModel(
            name='CouponLogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=None, db_index=True, max_length=200, null=True, verbose_name='名称')),
                ('orders', models.IntegerField(default=0, verbose_name='序号')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('use_time', models.DateTimeField(blank=True, null=True, verbose_name='使用时间')),
                ('use_status', models.SmallIntegerField(blank=True, choices=[(2, '已过期'), (1, '已使用'), (0, '未使用')], default=0, null=True, verbose_name='使用状态')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='to_conpon', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('coupon', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='coupon.couponmodels', verbose_name='优惠券')),
            ],
            options={
                'verbose_name_plural': '优惠发放与日志类',
                'db_table': 'fg_coupon_log',
            },
        ),
        migrations.CreateModel(
            name='CouponCourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('course', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='to_coupon', to='course.coursemodel', verbose_name='课程')),
                ('coupon', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='to_course', to='coupon.couponmodels', verbose_name='优惠券')),
            ],
            options={
                'verbose_name_plural': '优惠券与课程信息',
                'db_table': 'fg_coupon_course',
            },
        ),
        migrations.CreateModel(
            name='CouponCourseDirectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('direction', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='to_coupon', to='course.coursedirectionmodel', verbose_name='专业方向')),
                ('coupon', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='to_direction', to='coupon.couponmodels', verbose_name='优惠券')),
            ],
            options={
                'verbose_name_plural': '优惠券与专业方向',
                'db_table': 'fg_coupon_course_direction',
            },
        ),
        migrations.CreateModel(
            name='CouponCourseCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('category', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='to_coupon', to='course.coursecategorymodel', verbose_name='课程分类')),
                ('coupon', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='to_category', to='coupon.couponmodels', verbose_name='优惠券')),
            ],
            options={
                'verbose_name_plural': '优惠券与课程分类',
                'db_table': 'fg_coupon_course_category',
            },
        ),
    ]
