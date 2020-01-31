from django.db import models
from django.core.validators import MinValueValidator
from company.models import Company
from decimal import Decimal



class Payment(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	date_paid = models.DateField(auto_now_add=True)
	amount = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
