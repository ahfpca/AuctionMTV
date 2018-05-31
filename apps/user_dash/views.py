from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.login_reg.models import *
from apps.auction.models import *
from datetime import datetime
from datetime import timedelta
from django.utils import timezone



# Create your views here.
def index(request):
    if not "user_uniq" in request.session:
        return redirect("/login_reg")
    else:
        hashed_uniq_id = request.session["user_uniq"]

        rec = User.objects.filter(user_uniq = hashed_uniq_id).first()

        if rec:
            request.session["first_name"] = rec.first_name
            request.session["last_name"] = rec.last_name

            aucRecords = getAuctionRecords(rec)
            bidRecords = getBidRecords(rec)

            context = {
                "aucRecords": aucRecords,
                "bidRecords": bidRecords
            }

            return render(request, "user_dash/index.html", context)

    # if user_uniq is present but is not found in db, then it should be altered!
    request.session.clear()        
    return redirect("/login_reg")


def getAuctionRecords(user):
    records = []

    rows = Auction.objects.filter(fk_user = user.user_id).all().order_by("-created_at")

    row_num = 0
    for row in rows:
        row_num += 1

        created_date = row.created_at
        deadline_date = row.deadline

        # calculate remaining days to deadline  
        today = timezone.now()
        if today < row.deadline:
            delta = row.deadline - datetime.now()
            remain_days = delta.day
        else:
            remain_days = 0
        
        # define state of auction
        if remain_days == 0:
            state = "Closed"
        else:
            if remain_days == 1:
                state = "Open (" + remain_days + " day left)"
            else:
                state = "Open (" + remain_days + " days left)"

        
        # get bid info
        bids_count = Bid.objects.filter(fk_auction = row.auction_id).count()
        last_bid = Bid.objects.filter(fk_auction = row.auction_id).order_by("-bid_amount").first()
        if not last_bid:
            max_bid = 0
        else:
            max_bid = last_bid.bid_amount

        # define buttons states
        btn_delete = False
        btn_edit = False
        btn_connect = False

        if remain_days == 0:
            btn_connect = True
        else:
            btn_delete = True
            if bids_count == 0:
                btn_edit = True

        # create record object
        rec = {
            "auction_id": row.auction_id,
            "row": row_num,
            "date": created_date,
            "title": row.title,
            "category": row.fk_category.category_name,
            "companies": "Level 2",
            "deadline": deadline_date,
            "bids": bids_count,
            "max_bid": max_bid,
            "state": state,
            "btn_delete": btn_delete,
            "btn_edit": btn_edit,
            "btn_connect": btn_connect
        }

        # add it to records list
        records.append(rec)

    return records


def getBidRecords(user):
    records = []



    return records


def edit(request):
    if not "user_uniq" in request.session:
        return redirect("/login_reg")
    else:
        hashed_uniq_id = request.session["user_uniq"]

        rec = User.objects.filter(user_uniq = hashed_uniq_id).first()

        if rec:
            request.session["first_name"] = rec.first_name
            request.session["last_name"] = rec.last_name
            request.session["email"] = rec.email
            return render(request, "user_dash/edit.html")

    # if user_uniq is present but is not found in db, then it should be altered!
    request.session.clear()        
    return redirect("/login_reg")


def update(request):
    if not "user_uniq" in request.session:
        return redirect("/login_reg/success")

    first_name = request.POST["first_name"].strip()
    last_name = request.POST["last_name"].strip()
    email = request.POST["email"].strip()

    hashed_uniq_id = request.session["user_uniq"]

    if request.method == "POST":
        errors = User.objects.record_validator(request.POST, hashed_uniq_id, True)

        if len(errors):
            # Return errors to template
            for key, value in errors.items():
                messages.add_message(request, level = 40, message = value, extra_tags = key)
                request.session["first_name"] = first_name
                request.session["last_name"] = last_name
                request.session["email"] = email

            return render(request, "user_dash/edit.html")
        else:
            # Update current user
            rec = User.objects.filter(user_uniq = hashed_uniq_id).first()

            if rec:
                rec.first_name = first_name
                rec.last_name = last_name
                rec.email = email
                rec.save()
            else:
                messages.add_message(request, level = 40, message = "Something went wrong! Record didn't save.", extra_tags = 'general')
                return redirect("/user_dash/edit")

    return redirect("/user_dash/index")
