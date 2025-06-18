from django.db import models

# Create your models here.

class ResumeModel(models.Model):
    Full_Name=models.CharField(max_length=50)
    Profile_Picture=models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    Email=models.EmailField()
    Phone=models.CharField(max_length=15)
    Address=models.CharField(max_length=150)
    Summary=models.CharField(max_length=100)
    Degree=models.CharField(max_length=100)
    Institute_Name=models.CharField(max_length=100)
    Year_of_Graduation=models.DateField()
    Company_Name=models.CharField(max_length=100)
    Position=models.CharField(max_length=100)
    Years_of_Experience=models.PositiveIntegerField()
    Skills = models.TextField(help_text="Enter skills separated by commas")
    Hobbies = models.TextField(help_text="Enter hobbies separated by commas")
    Achievements = models.TextField(help_text="Enter achievements separated by commas")


def __str__(self):
        return self.Full_Name