from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.login_reg.models import *
from apps.auction.models import *


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
            return render(request, "user_dash/index.html")

    # if user_uniq is present but is not found in db, then it should be altered!
    request.session.clear()        
    return redirect("/login_reg")


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
