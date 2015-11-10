from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Funds(models.Model):
	
	"""Sets the Fund details"""

	name = models.CharField('Fund Name', max_length=255)
	timetamp = models.DateTimeField(blank=True, auto_now_add=True)
	amount = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.name

	class Meta: 
		verbose_name = 'Fund'
		verbose_name_plural = 'Funds'