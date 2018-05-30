from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'auction/index.html')

def sort_by_title(request):
    context = {
        'categories' : Category.objects.all(),
        'auctions' : Auction.objects.all(),
        'media' : Media.objects.all()
    }
    return render(request, 'auction/by_title.html', context)

def sort_by_categ(request):
    context = {
        'categories' : Category.objects.all(),
        'auctions' : Auction.objects.all()
    }
    return render(request, 'auction/by_categ.html', context)

def create(request):
    context = {
        'categories' : Category.objects.all(),
        'auctions' : Auction.objects.all(),
        'media' : Media.objects.all()
    }
    return render(request, 'auction/add_auction.html', context)

def process_new_auc(request):
    errors = Auction.objects.auction_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)
        print('-'*30 + '>', 'New auction form did not pass validation.')
        return redirect('/auction/create')
    else:
        new_category = Category.objects.get(category_id=request.POST['category'])
        user = User.objects.get(user_id=2)
        # user = User.objects.get(user_id=request.POST['user_id'])
        media = Media.objects.get(media_id=request.POST['media_id'])
        new_auction = Auction.objects.create(title=request.POST['title'], description=request.POST['description'], fk_category=new_category, duration_seconds=request.POST['duration'], starting_bid=request.POST['starting_bid'], current_bid=request.POST['starting_bid'], deadline=request.POST['deadline'], fk_user=user, fk_media=media)
        if 'auction_id' not in request.session:
            request.session['auction_id'] = new_auction.auction_id
        request.session['auction_id'] = new_auction.auction_id
        return redirect('auction/view_auc')

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

def add_media(request):
    context = {
        'genres' : Genre.objects.all()
    }
    return render(request, 'auction/add_media.html', context)

def view_auc(request):
    context = {
         'auction': Auction.objects.get(auction_id=request.session['auction_id'])
    }
    return render(request, 'auction/display_auc.html', context)

# def media_form_html(request):
#     if 'title' not in request.session:
#         request.session['title'] = 
#     return render(request, 'auction/media_form.html')