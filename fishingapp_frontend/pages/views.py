"""
pages/views.py
"""
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect

# --- HOMEPAGE --- #

def index_page(request):
    return render(request, "pages/homepage/index.html", {})


def contact_page(request):
    return render(request, "pages/homepage/contact.html", {})


# --- GATEWAY --- #


def register_page(request):
    return render(request, "pages/gateway/register.html", {})


def register_success_page(request):
    return render(request, "pages/gateway/register_success.html", {})


def login_page(request):
    return render(request, "pages/gateway/login.html", {})


def logout_page(request):
    return render(request, "pages/gateway/logout.html", {})


# --- DASHBOARD --- #


def dashboard_page(request):
    return render(request, "pages/dashboard/dashboard.html", {})


# --- INSTRUMENTS --- #


def i_list_page(request):
    return render(request, "pages/instrument/list.html", {})


def i_retrieve_page(request, id):
    return render(request, "pages/instrument/retrieve.html", {
        "instrument_id": int(id),
    })


def i_update_page(request, id):
    return render(request, "pages/instrument/update.html", {
        "instrument_id": int(id),
    })


# --- USERPROFILE --- #


def profile_retrieve_page(request):
    return render(request, "pages/userprofile/retrieve.html", {})


def profile_update_page(request):
    return render(request, "pages/userprofile/update.html", {})


# --- REPORT --- #


def report_list_page(request):
    return render(request, "pages/report/list.html", {})


def report_01_page(request):
    return render(request, "pages/report/01.html", {})


# --- SENSOR --- #
