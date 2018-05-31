from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return redirect("/auction")