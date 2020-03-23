from django.db import models

# Create your models here.
class Barber(models.Model):
    barberImage = models.ImageField('Barber Prof Pic', upload_to="barberPics")
    barberBio = models.TextField('Bio',blank=True, null=True)
    barberRules = models.CharField('Rules',max_length=200, blank=True, null=True)
    styleImage = models.ImageField('New Style Picture',upload_to="stylePics")
    adsImage = models.ImageField('Ads Flyer',upload_to='ads')
    
    def __str__(self):
        return self.barberName