from django.db import models

# Create your models here.

class person(models.Model):
    person_name = models.CharField('person_name', max_length=120, default='', blank=True, null=True)
    address = models.CharField('address', max_length=120, default='', blank=True, null=True)
    age = models.IntegerField('Age ', default=0, blank=True, null=True)
    date = models.DateField(null=True)
    address = models.EmailField('address', max_length=120, default='', blank=True, null=True)
    img = models.ImageField(null=True, blank=True)
    hotel_Main_Img = models.ImageField(upload_to='images/',blank=True, null=True)

    def __str__(self):
        return self.person_name or ''

    
class Sales_person(models.Model):
    service_name = models.ForeignKey('person',default='', on_delete=models.CASCADE)
    expense = models.IntegerField('Age ', default=0, blank=True, null=True)
    


    




		
	
	
    
	