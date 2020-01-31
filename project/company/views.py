from django.shortcuts import render, reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Company
from .mixins import DifferentCompany


class CompanyUpdate(LoginRequiredMixin, DifferentCompany, UpdateView):
	model = Company
	fields = ['name', 'address','number','city','country','email','website','logo','tax_number','bank', 'account_number','default_currency']
	template_name_suffix = 'form'
	template_name = 'company/edit_company.html'

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, 'Успешно')
		return reverse('edit_company', kwargs={'pk': self.object.id})
