from django.db import models

# Create your models here.
class Barber(models.Model):
    barberName = models.CharField('Barber Name',max_length=200,blank=True, null=True)
    barberImage = models.ImageField('Barber Prof Pic', upload_to="barberPics")
    barberBio = models.TextField('Bio',blank=True, null=True)
    styleImage = models.ImageField('New Style Picture',upload_to="stylePics")
   
    
    def __str__(self):
        return self.barberName
    

class Ads(models.Model):
        adsTitle = models.CharField('adsTitle',blank=True, null=True)
        adsFlyer = models.ImageField('ads picture', upload_to="ads")
        adsInfo = models.CharField('ads info', blank=True, null=True )
        
        def __str__(self):
            return self.adsTitle
     
