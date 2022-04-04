from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin


# Dashboard
class DashboardView(LoginRequiredMixin,View):
    def get(self, request):
        print(request.session)
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['pageview'] = "Tpc"
        return render(request, 'menu/index.html',greeting)


# Calender
class CalendarView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Calendar"
        greeting['pageview'] = "Tpc"
        return render(request, 'menu/calendar.html',greeting)

