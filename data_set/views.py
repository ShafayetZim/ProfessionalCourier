from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from decimal import *
from django.contrib.auth.models import User

from .models import Parcel, District, Sub, Type
from .forms import TypeCreateForm, ParcelForm, TrackingForm
from .utils import render_to_pdf


# type view
class TypeView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'type': Type.objects.all(),
            'title': "Parcel Type Info",
            'pageview': "Parcel Type"
        }
        return render(request, 'parcel/parcel-type.html', context)


# Add type
@login_required
def add_type(request):
    template_name = 'parcel/new-type.html'
    message = ''

    if request.method == 'GET':
        type_form = TypeCreateForm(request.GET or None)

    elif request.method == 'POST':
        type_form = TypeCreateForm(request.POST, request.FILES)
        message = ''
        print(request.POST)

        if type_form.is_valid():
            obj = type_form.save(commit=False)

            obj.save()
            message = "Success"
            return redirect('parcel-type')

    return render(request, template_name,
                  {'type_form': type_form, 'message': message, 'title': "New Type", 'pageview': "Parcel Type"})


# Edit Type
class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Type
    form_class = TypeCreateForm
    success_url = reverse_lazy('parcel-type')
    template_name = 'parcel/edit-type.html'

    success_message = "Type was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Type"
        context["pageview"] = "Parcel Type"
        return context


# Delete Type
@login_required
def delete_type(request, id):
    obj = get_object_or_404(Type, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('parcel-type')
    context = {
        'obj': Type.objects.get(id=id),
        'title': "Delete Type",
        'pageview': "Type"
    }

    return render(request, "parcel/delete-type.html", context)


# parcel add
@login_required
def add_parcel(request):
    template_name = 'parcel/parcel_form.html'
    message = ''

    if request.method == 'GET':
        form = ParcelForm(request.GET or None)

    elif request.method == 'POST':
        form = ParcelForm(request.POST, request.FILES)
        message = ''
        print(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user

            obj.save()
            message = "Success"
            return redirect('parcel-list')

    return render(request, template_name,
                  {'form': form, 'message': message, 'title': "New Parcel", 'pageview': "Parcel"})


def load_district(request):
    division_id = request.GET.get('division')
    district = District.objects.filter(division_id=division_id).order_by('name')
    context = {'district': district}
    return render(request, 'parcel/city_dropdown_list_options.html', context)


def load_sub(request):
    district_id = request.GET.get('district')
    sub = Sub.objects.filter(district_id=district_id).order_by('name')
    context = {'sub': sub}
    return render(request, 'parcel/vanue_ddl.html', context)


# parcel list view
class ParcelListView(LoginRequiredMixin, ListView, ):
    model = Parcel  # Model I want to Covert to List
    template_name = 'parcel/parcel-list.html'  # Template Name
    context_object_name = 'parcel'  # Change default name of objectList
    ordering = ['-date', '-order_no']  # Ordering post LIFO

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Parcel List"
        context["pageview"] = "Parcel"
        return context


# Edit parcel
class ParcelUpdateView(LoginRequiredMixin, UpdateView):
    model = Parcel
    form_class = ParcelForm
    success_url = reverse_lazy('parcel-list')
    template_name = 'parcel/edit-parcel.html'

    success_message = "Parcel was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Parcel"
        context["pageview"] = "Parcel List"
        return context


@login_required
def print_invoice(request, order_no):
    print(order_no)
    parcel = Parcel.objects.get(order_no=order_no)

    # print('%d in words is: %s' % (total_amount, getWords(total_amount)))

    context = {
        'title': "Invoice",
        'pageview': "Invoice",
        'parcel': parcel,
    }
    pdf = render_to_pdf('pdf/receipt.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


# Edit parcel
class TrackingView(LoginRequiredMixin, UpdateView):
    model = Parcel
    form_class = TrackingForm
    success_url = reverse_lazy('parcel-list')
    template_name = 'parcel/tracking-parcel.html'

    success_message = "Parcel Tracking was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Track Parcel"
        context["pageview"] = "Parcel List"
        return context


@login_required
def invoice_delete(request, order_no):
    if request.method == 'GET':
        instance = Parcel.objects.get(order_no=order_no)
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('parcel-list')
