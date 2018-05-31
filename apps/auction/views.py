from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib import messages

def index(request):
    if "user_uniq" in request.session:
        hashed_uniq_id = request.session["user_uniq"]

        rec = User.objects.filter(user_uniq = hashed_uniq_id).first()

        if rec:
            request.session["first_name"] = rec.first_name
            request.session["last_name"] = rec.last_name
    return render(request, 'auction/index.html')

def sort_by_title(request):
    if "user_uniq" in request.session:
        hashed_uniq_id = request.session["user_uniq"]

    rec = User.objects.filter(user_uniq = hashed_uniq_id).first()

    if rec:
        request.session["first_name"] = rec.first_name
        request.session["last_name"] = rec.last_name
    context = {
        'categories' : Category.objects.all(),
        'auctions' : Auction.objects.all().order_by("fk_media"),
        'media' : Media.objects.all(),
        'user' : User.objects.filter(user_uniq=request.session['user_uniq']).first()
    }
    return render(request, 'auction/by_title.html', context)

def sort_by_categ(request):
    if "user_uniq" in request.session:
        hashed_uniq_id = request.session["user_uniq"]

    rec = User.objects.filter(user_uniq = hashed_uniq_id).first()

    if rec:
        request.session["first_name"] = rec.first_name
        request.session["last_name"] = rec.last_name
    context = {
        'categories' : Category.objects.all(),
        'auctions' : Auction.objects.all(),
        'drink_auc' : Auction.objects.all().filter(fk_category=2),
        'food' : Auction.objects.all().filter(fk_category=1),
        'cp' : Auction.objects.all().filter(fk_category=3),
        'laptop' : Auction.objects.all().filter(fk_category=4),
        'clothing' : Auction.objects.all().filter(fk_category=5),
        'elec' : Auction.objects.all().filter(fk_category=6),
        'homeware' : Auction.objects.all().filter(fk_category=7),
        'furn' : Auction.objects.all().filter(fk_category=8),
        'skin' : Auction.objects.all().filter(fk_category=9),
        'car' : Auction.objects.all().filter(fk_category=10),
        'media' : Media.objects.all(),
        'user' : User.objects.filter(user_uniq=request.session['user_uniq']).first()
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
        user = User.objects.filter(user_uniq = request.session['user_uniq']).first()
        media = Media.objects.filter(media_id=request.POST['media_id']).first()
        new_auction = Auction.objects.create(title=request.POST['title'], description=request.POST['description'], fk_category=new_category, duration_seconds=request.POST['duration'], starting_bid=request.POST['starting_bid'], current_bid=request.POST['starting_bid'], deadline=request.POST['deadline'], fk_user=user, fk_media=media)
        if 'auction_id' not in request.session:
            request.session['auction_id'] = new_auction.auction_id
        request.session['auction_id'] = new_auction.auction_id
        return redirect('auction/by_categ.html')

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

def add_bid(request):
    user = User.objects.filter(user_uniq=request.session['user_uniq']).first()
    auction = Auction.objects.filter(auction_id=request.POST['auction_id']).first()
    bid = Bid.objects.create(bid_amount=request.POST['bid_amount'], fk_auction=auction, fk_user=user)
    print(bid)
    context = {
        'genres' : Genre.objects.all()
    }
    return redirect(reverse('place_bid', kwargs={'id': request.POST['auction_id']}))

def view_auc(request, id):
    if not "user_uniq" in request.session:
        return redirect("/login_reg")
    else:
        hashed_uniq_id = request.session["user_uniq"]

        rec = User.objects.filter(user_uniq = hashed_uniq_id).first()

        if rec:
            request.session["first_name"] = rec.first_name
            request.session["last_name"] = rec.last_name
            context = {
                'auction': Auction.objects.get(auction_id=id),
                'bids': Bid.objects.all().order_by('-bid_amount')
            }
            return render(request, 'auction/display_auc.html', context)

# def media_form_html(request):
#     if 'title' not in request.session:
#         request.session['title'] = 
#     return render(request, 'auction/media_form.html')