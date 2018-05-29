from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'auction/index.html')

def sort_by_title(request):
    return render(request, 'auction/by_title.html')

def sort_by_categ(request):
    return render(request, 'auction/by_categ.html')

def create(request):
    return render(request, 'auction/add_auction.html')

def process_new_auc(request):
    errors = Auction.objects.auction_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)
        print('-'*30 + '>', 'New auction form did not pass validation.')
        return redirect('/auction/create')
    else:
        new_auction = Auction.objects.create(title=request.POST['title'], description=request.POST['description'], category=request.POST['category'], duration_seconds=request.POST['duration'], starting_bid=request.POST['starting_bid'], current_bid=request.POST['starting_bid'])
        print(request.POST)
        print('hi')
        return redirect('/auction/create')

def process_new_media(request):
    errors = Media.objects.media_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)
        print('-'*30 + '>', 'New auction form did not pass validation.')
        return redirect('/auction/create')
    else:
        new_media = Media.objects.create(media_title=request.POST['media_title'], genre=request.POST['genre'], release_year=request.POST['release_year'], media_type=request.POST['media_type'])
        new_media.save()
        return redirect('/auction/create', {new_media.id: auction_id})
    print('New media form was submitted')
    return redirect('/auction/create')


# def media_form_html(request):
#     if 'title' not in request.session:
#         request.session['title'] = 
#     return render(request, 'auction/media_form.html')