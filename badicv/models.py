from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name

    
class SkillType(models.Model):
    type = models.CharField(max_length=32, primary_key=True)
    
    def __str__(self):
        return self.type


class SkillToType(models.Model):
    skill_name = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_type = models.ForeignKey(SkillType, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('skill_name', 'skill_type')
        
    def __str__(self):
        return self.skill_type.type + " skill: " + self.skill_name.name 


class Experience(models.Model):
    type_choice = (("Wrk", "Work"), ("Ed", "Education"), ("Hob", "Hobby"), ("Vol", "Volunteer"))
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=64, default="DEFAULT LOCATION PLEASE REMOVE")
    start_date = models.DateField("Start Date", blank=True)
    end_date = models.DateField("End Date", blank=True)
    description = models.TextField()
    type = models.CharField(max_length=4, choices=type_choice)
    
    def __str__(self):
        return self.name
    

class ExperienceWithSkill(models.Model):
    experience_name = models.ForeignKey(Experience, on_delete=models.CASCADE)
    skill_name = models.ForeignKey(Skill, on_delete=models.CASCADE)
    description = models.TextField(default="DEFAULT DESCRIPTION PLEASE REMOVE")
    
    class Meta:
        unique_together = ('experience_name', 'skill_name')
        
    def __str__(self):
        return self.skill_name.name + " experience at " + self.experience_name.name
        

class Referees(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    email = models.EmailField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
    experience = models.ForeignKey(Experience, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
    

    