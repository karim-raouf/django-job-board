from django.db import models

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    )

def image_upload(instance , filename ):
    imagename , extension = filename.split('.')
    return "jobs/%s.%s"%(instance.id , extension)

# Create your models here.
class Job(models.Model):    #table
    title = models.CharField(max_length = 100)  #column 1
    #loctaion                                   #column 2
    job_type = models.CharField(max_length = 15 , choices = JOB_TYPE)   #column 3
    description = models.TextField(max_length = 1000)
    time_published = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default = 1)
    salary = models.IntegerField(default = 0)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to = image_upload)
    slug = models.SlugField(blank = True , null = True)
    
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    