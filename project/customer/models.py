from django.db import models
from django.shortcuts import reverse
from company.models import Company


class Customer(models.Model):

	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, blank=False)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=100, blank=True)
	tax_no = models.CharField(max_length=30, blank=True)

	def get_edit_url(self):
		return reverse('edit_customer', kwargs={'pk': self.pk})

	def get_customer_url(self):
		return reverse('detail_customer', kwargs={'pk': self.pk})

	def __str__(self):
		return self.name
