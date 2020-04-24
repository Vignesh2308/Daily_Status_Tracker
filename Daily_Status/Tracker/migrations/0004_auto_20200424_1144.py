# Generated by Django 3.0.3 on 2020-04-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0003_userprofileinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='date',
        ),
        migrations.AddField(
            model_name='info',
            name='today_date',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='assessment',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='assessment_status',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='certification',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='certified',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='employee_id',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='employee_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='hours_spent_today',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='skill_type',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='source',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='total_hours',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='total_training_hours',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='training_completion_date',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='training_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='training_type',
            field=models.CharField(max_length=25, null=True),
        ),
    ]