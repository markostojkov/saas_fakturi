from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from company.mixins import CustomerDifferentCompany
from .models import Customer
from .forms import CreateCustomerForm


class CustomerListView(LoginRequiredMixin, ListView):

	model = Customer
	template_name = 'customer/customers.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CustomerListView, self).get_context_data(**kwargs)
		context['customers'] = Customer.objects.filter(company=self.request.user.company)
		return context


class CustomerUpdate(LoginRequiredMixin, CustomerDifferentCompany, UpdateView):
	model = Customer
	fields = ['name', 'email', 'phone', 'address', 'tax_no']
	template_name_suffix = 'form'
	template_name = 'customer/edit_customer.html'

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, 'Успешно')
		return reverse('edit_customer', kwargs={'pk': self.object.id})


class CustomerCreate(LoginRequiredMixin, CreateView):

	template_name = 'customer/create_customer.html'
	form_class = CreateCustomerForm

	def post(self, request, **kwargs):
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		address = request.POST.get('address')
		tax_no = request.POST.get('tax_no')

		Customer.objects.create(company=request.user.company, 
			name=name, 
			email=email, 
			phone=phone, 
			address=address, 
			tax_no=tax_no)
		return redirect('customers')

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, 'Успешно')
		return reverse('customers')


class CustomerDetailView(LoginRequiredMixin, CustomerDifferentCompany, DetailView):

	model = Customer
	template_name = 'customer/detail_customer.html'
	context_object_name = 'customer'