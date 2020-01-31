from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Tax
from .forms import CreateTaxForm
from company.mixins import TaxDifferentCompany


class TaxListView(LoginRequiredMixin, ListView):

	model = Tax
	template_name = 'tax/taxes.html'

	def get_context_data(self, *args, **kwargs):
		context = super(TaxListView, self).get_context_data(**kwargs)
		context['taxes'] = Tax.objects.filter(company=self.request.user.company)
		return context


class TaxUpdate(LoginRequiredMixin, TaxDifferentCompany, UpdateView):
	model = Tax
	fields = ['name', 'value']
	template_name_suffix = 'form'
	template_name = 'tax/edit_tax.html'

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, 'Успешно')
		return reverse('edit_tax', kwargs={'pk': self.object.id})


class TaxCreate(LoginRequiredMixin, CreateView):

	template_name = 'tax/create_tax.html'
	form_class = CreateTaxForm

	def post(self, request, **kwargs):
		name = request.POST.get('name')
		value = request.POST.get('value')
		Tax.objects.create(company=request.user.company, name=name, value=value)
		return redirect('taxes')

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, 'Успешно')
		return reverse('taxes')
