from django.db import models


currency_choices = (
		('USD', 'US Dollar'),
		('CHF', 'Swiss Franc'),
		('GBP', 'Pound Sterling'),
		('EUR', 'Euro'),
		('MKD', 'Denar'),
	)

subscription_choices = (
		('Бесплатен', 'Бесплатен'),
		('Класик', 'Класик'),
		('Премиум', 'Премиум'),
	)

class Company(models.Model):

	name = models.CharField(max_length=50, blank=False, unique=True)
	address = models.CharField(max_length=50, blank=True)
	number = models.CharField(max_length=20, blank=True)
	city = models.CharField(max_length=20, blank=True)
	country = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)
	website = models.CharField(max_length=20, blank=True)
	logo = models.ImageField(upload_to='', blank=True)
	tax_number = models.CharField(max_length=30, blank=True)
	bank = models.CharField(max_length=50, blank=True)
	account_number = models.CharField(max_length=15, blank=True)	
	default_currency = models.CharField(choices=currency_choices, max_length=20, default='MKD')
	subscription_package = models.CharField(choices=subscription_choices, max_length=20, default='Бесплатен')

	def __str__(self):
		return self.name