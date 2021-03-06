# Generated by Django 3.0.3 on 2020-04-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=25)),
                ('training_name', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=15)),
                ('training_completion_date', models.CharField(max_length=15)),
                ('total_training_hours', models.IntegerField()),
                ('hours_spent_today', models.IntegerField()),
                ('training_type', models.CharField(choices=[('INTERNAL', 'Internal'), ('EXTERNAL', 'External')], default='INTERNAL', max_length=8)),
                ('skill_type', models.CharField(choices=[('CORE', 'Core'), ('NEW', 'New')], default='CORE', max_length=4)),
                ('certification', models.CharField(choices=[('Yes', 'Available'), ('No', 'Unavailable')], default='Yes', max_length=15)),
                ('certified', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'Not Applicable')], default='Yes', max_length=15)),
                ('lex_link', models.CharField(max_length=100, null=True)),
                ('task', models.CharField(max_length=25, null=True)),
                ('task_description', models.CharField(max_length=100, null=True)),
                ('total_hours', models.IntegerField()),
                ('assessment', models.CharField(choices=[('Yes', 'Available'), ('No', 'Unavailable')], default='Yes', max_length=15)),
                ('assessment_status', models.CharField(choices=[('Yes', 'Completed'), ('No', 'Yet to Complete')], default='Yes', max_length=15)),
            ],
        ),
    ]
