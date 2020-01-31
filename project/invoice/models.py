from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.contrib.postgres.fields import JSONField
from datetime import date
from company.models import Company
from customer.models import Customer
from payments.models import Payment


currency_choices = (
		('USD', 'US Dollar'),
		('CHF', 'Swiss Franc'),
		('GBP', 'Pound Sterling'),
		('EUR', 'Euro'),
		('MKD', 'Denar'),
	)

class Invoice(models.Model):

	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	id_number = models.CharField(max_length=15)
	slug = models.CharField(max_length=15, blank=True)
	date_created = models.DateField(default=timezone.now)
	payment_due = models.DateField(default=timezone.now)
	place = models.CharField(max_length=20, blank=True)
	notes = models.CharField(max_length=400, blank=True)	
	items = JSONField(blank=True)
	invoice_sum = models.DecimalField(max_digits=10, decimal_places=2)
	tax_sum = models.DecimalField(max_digits=10, decimal_places=2)
	full_sum = models.DecimalField(max_digits=10, decimal_places=2)
	paid_sum = models.ManyToManyField(Payment, blank=True)
	currency = models.CharField(choices=currency_choices, max_length=20, default='MKD')
	mail_sent = models.BooleanField(default=False)

	def __str__(self):
		return self.slug

	def save(self, *args, **kwargs):
		slug_save(self)
		super(Invoice, self).save(*args, **kwargs)

	def get_invoice_url(self):
		return reverse('detail_invoice', kwargs={'slug': self.slug})

	@property
	def is_paid(self):
		return sum(v.amount for v in self.paid_sum.all()) == self.full_sum

	@property
	def is_past_due(self):
		if self.payment_due < date.today() and not self.is_paid:
			return False
		elif self.payment_due < date.today() and self.is_paid:
			return True
		elif self.payment_due > date.today():
			return True
	
	@property
	def leftover_invoice_sum(self):
		return self.full_sum - sum(v.amount for v in self.paid_sum.all())

	@property
	def paid_invoice_sum(self):
		return sum(v.amount for v in self.paid_sum.all())


def slug_save(obj):
	if not obj.slug:
		obj.slug = get_random_string(8)
		slug_is_wrong = True  
		while slug_is_wrong:
			slug_is_wrong = False
			other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
			if len(other_objs_with_slug) > 0:
				slug_is_wrong = True
			if slug_is_wrong:
				obj.slug = get_random_string(5)