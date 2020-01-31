from django.db import models
from django.shortcuts import reverse
from company.models import Company


class Tax(models.Model):

	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	value = models.DecimalField(max_digits=5, decimal_places=2)

	def get_absolute_url(self):
		return reverse('edit_tax', kwargs={'pk': self.id})

	def __str__(self):
		return self.name