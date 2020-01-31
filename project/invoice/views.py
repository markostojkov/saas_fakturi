from django.shortcuts import render, reverse, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from company.mixins import InvoiceDifferentCompany
from company.models import Company
from customer.models import Customer
from datetime import datetime
from tax.models import Tax
from payments.forms import CreatePaymentForm
from .models import Invoice
from .forms import CreateInvoiceForm


@login_required
def home(request):
	return render(request, 'invoice/home.html')


class InvoiceListView(LoginRequiredMixin, ListView):

	model = Invoice
	template_name = 'invoice/invoices.html'

	def get_context_data(self, *args, **kwargs):
		context = super(InvoiceListView, self).get_context_data(**kwargs)
		context['invoices'] = Invoice.objects.filter(company=self.request.user.company)
		return context


class InvoiceUpdate(LoginRequiredMixin, InvoiceDifferentCompany, UpdateView):
	
	model = Invoice
	template_name = 'invoice/edit_invoice.html'
	context_object_name = 'invoice'
	fields = ['date_created', 'payment_due', 'place', 'notes', 'items', 'invoice_sum', 'tax_sum', 'full_sum', 'date_created', ]

	def get_context_data(self, *args, **kwargs):
		context = super(InvoiceUpdate, self).get_context_data(**kwargs)
		company = self.request.user.company
		context['customers'] = Customer.objects.filter(company=company)
		context['company'] = company
		context['taxes'] = Tax.objects.filter(company=company)
		return context

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, 'Успешно')
		return self.object.get_invoice_url()


class InvoiceCreate(LoginRequiredMixin, CreateView):

	template_name = 'invoice/create_invoice.html'
	model = Invoice
	fields = []

	def post(self, request, **kwargs):

		form = CreateInvoiceForm(request.POST)
		if form.is_valid():
			invoice = form.save()
			messages.add_message(self.request, messages.SUCCESS, 'Успешно')
			return redirect(invoice.get_invoice_url())
		else:
			messages.add_message(self.request, messages.ERROR, 'Неуспешно')
			return redirect('create_invoice')

	def get_context_data(self, *args, **kwargs):
		context = super(InvoiceCreate, self).get_context_data(**kwargs)
		company = self.request.user.company
		try:
			pk = Invoice.objects.filter(company=company).last().id
		except Exception:
			pk = 1
		context['customers'] = Customer.objects.filter(company=company)
		context['company'] = company
		context['taxes'] = Tax.objects.filter(company=company)
		context['today_date'] = datetime.today().strftime('%Y-%m-%d')
		context['invoice_id'] = f'{datetime.today().year}-{pk}'
		return context


class InvoiceDetailView(LoginRequiredMixin, InvoiceDifferentCompany, DetailView):

	model = Invoice
	template_name = 'invoice/detail_invoice.html'
	context_object_name = 'invoice'

	#SEND EMAIL FOR INVOICE POST VIEW
	def post(self, request, **kwargs):
		sender = settings.DEFAULT_FROM_EMAIL
		to = request.POST.get('email')
		subject = request.POST.get('subject')
		text = request.POST.get('text')
		invoice = self.get_object()

		context = {
			'client': invoice.customer.name, 
			'cena': invoice.full_sum, 
			'due': invoice.payment_due, 
			'text': request.POST.get('text'),
			'company': request.user.company.name,
			'url': f'{request.build_absolute_uri()}/print',
		}

		msg_html = render_to_string('invoice/email.html', context)
		send_mail(text, '', sender, to, html_message=msg_html, fail_silently=False)
		invoice.mail_sent = True
		invoice.save()
		
		return HttpResponse('')


	def get_context_data(self, *args, **kwargs):
		context = super(InvoiceDetailView, self).get_context_data(**kwargs)
		context['company'] = self.request.user.company
		context['payment_form'] = CreatePaymentForm()
		return context		


class InvoicePrintView(DetailView):

	model = Invoice
	template_name = 'invoice/print_invoice.html'
	context_object_name = 'invoice'

	def get_context_data(self, *args, **kwargs):
		context = super(InvoicePrintView, self).get_context_data(**kwargs)
		context['company'] = self.request.user.company
		return context
