from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from apps.login_reg.models import *


# Create your views here.
def index(request):
    if "user_uniq" in request.session:
        return redirect("/login_reg/success")

    return render(request, "login_reg/login.html")


def sign_up(request):
    if "user_uniq" in request.session:
        return redirect("/login_reg/success")

    return render(request, "login_reg/sign_up.html")
    

def logout(request):
    # if request.method == "POST":
    #     request.session.clear()
    #     return redirect("/login_reg/success")

    request.session.clear()
    return redirect("/login_reg/success")


def success(request):
    if not "user_uniq" in request.session:
        return redirect("/auction")
    else:
        hashed_uniq_id = request.session["user_uniq"]
        #print("\n", "%" * 40)

        rec = User.objects.filter(user_uniq = hashed_uniq_id).first()

        if rec:
            request.session["user_full_name"] = rec.first_name + " " + rec.last_name
            return redirect("/auction")

    return redirect("/auction")


def confirm(request):
    if "user_uniq" in request.session:
        return redirect("/login_reg/success")

    if request.method == "POST":
        email = request.POST["email"]

        result = User.objects.filter(email = email).first()
        # print("POST", request.POST)

        if result:
            if bcrypt.checkpw(request.POST["passcode"].encode(), result.passcode.encode()):
                request.session.clear()
                request.session["user_uniq"] = result.user_uniq

                messages.success(request, "Welcome back!")

                return redirect("/login_reg/success")
            else:
                request.session["email_login"] = request.POST["email"]
                messages.error(request, "You can not login to the website!", extra_tags = "general")
                return redirect("/login_reg")
        else:
            messages.error(request, "You can not login to the website!", extra_tags = "general")
            #messages.error(request, "You can not login to the website!")
            return redirect("/login_reg/success")

    return redirect("/login_reg/success")


def register(request):
    if "user_uniq" in request.session:
        return redirect("/login_reg/success")

    first_name = request.POST["first_name"].strip()
    last_name = request.POST["last_name"].strip()
    email = request.POST["email"].strip()
    passcode = request.POST["passcode"].strip()

    if request.method == "POST":
        errors = User.objects.record_validator(request.POST)

        if len(errors):
            # Return errors to template
            for key, value in errors.items():
                messages.add_message(request, level = 40, message = value, extra_tags = key)
                request.session["first_name"] = first_name
                request.session["last_name"] = last_name
                request.session["email"] = email

            return redirect("/login_reg/sign_up")
        else:
            # Create new user
            hashed_pass = bcrypt.hashpw(passcode.encode(), bcrypt.gensalt())

            rec = User.objects.create(first_name = first_name, last_name = last_name, email = email, passcode = hashed_pass)

            if rec.user_id > 0:
                # Create user_uniq field and save it back to the table
                uniq_id = str(rec.user_id) + "_" + rec.created_at.strftime("%Y-%m-%d_%H-%M-%S-%f")

                hashed_uniq_id = bcrypt.hashpw(uniq_id.encode(), bcrypt.gensalt()).decode("utf-8")

                rec.user_uniq = hashed_uniq_id
                rec.save()

                request.session.clear()
                request.session["user_uniq"] = rec.user_uniq
                messages.success(request, "You registration was successfull!")
            else:
                messages.add_message(request, level = 40, message = "Something went wrong! Record didn't save.", extra_tags = 'general')
                return redirect("/login_reg/sign_up")

    return redirect("/login_reg/success")
