from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Info(models.Model):
    training_type_list = [
        ('INTERNAL', 'Internal'),
        ('EXTERNAL', 'External'),
    ]
    skill_list = [
        ('CORE', 'Core'),
        ('NEW', 'New'),
    ]
    certification_list = [
        ('Yes', 'Available'),
        ('No', 'Unavailable'),
    ]
    certified_list = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('NA', 'Not Applicable'),
    ]
    assessment_list = [
        ('Yes', 'Available'),
        ('No', 'Unavailable'),
    ]
    assessment_status_list = [
        ('Yes', 'Completed'),
        ('No', 'Yet to Complete'),
    ]
    employee_id = models.CharField(max_length=25, null=True)
    employee_name = models.CharField(max_length=25, null=True)
    training_name = models.CharField(max_length=50, null=True)
    source = models.CharField(max_length=10, null=True)

    today_date = models.CharField(max_length=15, null=True)
    training_completion_date = models.CharField(max_length=15, null=True)
    total_training_hours = models.CharField(max_length=25, null=True)
    hours_spent_today = models.CharField(max_length=25, null=True)
    training_type = models.CharField(max_length=25, null=True)
    skill_type = models.CharField(max_length=25, null=True)
    certification = models.CharField(max_length=25, null=True)
    certified = models.CharField(max_length=25, null=True)
    lex_link = models.CharField(max_length=100, null=True)
    task = models.CharField(max_length=25, null=True)
    task_description = models.CharField(max_length=100, null=True)
    total_hours = models.CharField(max_length=25, null=True)
    assessment = models.CharField(max_length=25, null=True)
    assessment_status = models.CharField(max_length=25, null=True)

    def __str__(self):
        return 'Employee_id: ' + str(
            self.employee_id) + " Employee_Name: " + self.employee_name + " Training Name: " + self.training_name + "Source: " + str(
            self.source) + "Today's Date: " + str(self.today_date) + "Completion Date:  " + str(
            self.training_completion_date) + \
               "Total Training Hours: " + str(self.total_training_hours) + "Hours Spent Today: " + str(
            self.hours_spent_today) + \
               "Training Type: " + str(self.training_type) + "Skill Type: " + str(
            self.skill_type) + "certification: " + str(self.certification) + \
               "Certified: " + str(self.certified) + "Lex Link: " + str(self.lex_link) + "Task:" + str(
            self.task) + "Task Description: " + \
               str(self.task_description) + "Total Hours:" + str(self.total_hours) + "Assessment: " + str(
            self.assessment) + \
               "Assessment Status: " + str(self.assessment_status)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
