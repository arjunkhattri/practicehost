import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import ListView, FormView, DetailView
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django .views import View
from django.core.mail import send_mail
from django.conf import settings


class BaseView(View):
    view = {}


class home(BaseView):

    def get(self, request):
        carousel = Carousel.objects.all()
        social_info = CompanyInfo.objects.all()
        nle_info = WebsiteInfo.objects.all()

        activities = self.view['activities'] = Session.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(activities, 3)

        try:
            activity = paginator.page(page)

        except PageNotAnInteger:
            activity = paginator.page(1)

        except EmptyPage:
            activity = paginator.page(paginator.num_pages)
    

# here filter news and blog with there id

        news_blog = self.view['news_blog'] = BlogNews.objects.all()
        page = request.GET.get('page2', 1)
        paginator = Paginator(news_blog, 3)

        try:
            newsblog = paginator.page(page)

        except PageNotAnInteger:
            newsblog = paginator.page(1)

        except EmptyPage:
            newsblog = paginator.page(paginator.num_pages)

        catforform = SessionCategory.objects.all()

        context = {'activity': activity, 'newsblog': newsblog, 'carousel': carousel, 'social_info': social_info, 'nle_info': nle_info, 'catforform': catforform}

        return render(self.request, 'index.html', context)

    def post(self, request):
        if request.method == "POST":
            if request.POST.get("form_type") == 'formOne':
                name = request.POST.get('username', '')
                address = request.POST.get('address', '')
                contact_no = request.POST.get('phone', '')
                email = request.POST.get('email', '')
                cv = request.FILES['cv']
                citizenship = request.FILES['citizenship']
                certificates = request.FILES['certificates']
                photo = request.FILES['photo']

                form = FinancialForm(fullname=name, address=address, contact=contact_no, email=email, CV=cv,
                                     citizenship=citizenship, certificates=certificates, photo=photo)
                form.save()

                context = {'name': name, 'address': address, 'contact_no': contact_no, 'email': email, 'cv': cv,
                           'citizenship': citizenship, 'certificates': certificates, 'photo': photo}

                return render(request, 'index.html', context)

            elif request.POST.get("form_type") == 'formTwo':
                # choices = request.POST.get('multiple', '')

                name = request.POST.get('username', '')
                address = request.POST.get('address', '')
                contact_no = request.POST.get('contact', '')
                email = request.POST.get('email', '')

                data = {
                    "name": name,
                    "address": address,
                    "contact_no": contact_no,
                    "email": email

                }

                send_mail(
                    'Training Forms Data',  # subject
                    data,                # message
                    email,                      # from email
                    ['autovitytechgroup@gmail.com'],
                    fail_silently=False)

                form2 = InsuranceForm(fullname=name, address=address, contact=contact_no, email=email)
                form2.save()

                context2 = {'name': name, 'address': address, 'contact_no': contact_no, 'email': email}

                return render(request, 'index.html', context2)


def BlogNewsDetail(request, id):

    items = BlogNews.objects.filter(id=id)
    photos = BlogNewsImages.objects.filter(post_id=id)

    return render(request, 'blognewsdetail.html', {'items': items, 'photos': photos})


def BlogNewsContent(request):
    cat = BlogCategory.objects.all()
    return render(request, 'blognews.html', {'cat': cat})


def CareerFinancialDetail(request, id):
    items = Session.objects.filter(id=id)
    photos = SessionImages.objects.filter(post_id=id)

    return render(request, 'careerfinancialdetail.html', {'items': items, 'photos': photos})


def CareerFinancialContent(request):
    categories = SessionCategory.objects.all()
    # item = Session.objects.filter(category=id)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(categories, 3)
    #
    # try:
    #     items = paginator.page(page)
    #
    # except PageNotAnInteger:
    #     items = paginator.page(1)
    #
    # except EmptyPage:
    #     items = paginator.page(paginator.num_pages)
    return render(request, 'careerfinancial.html', {'categories': categories})


class Base(BaseView):
    def get(self, request):
        # team_card = TeamCard.objects.all()
        social_info = CompanyInfo.objects.all()

        context = {'social_info': social_info}

        return render(request, 'base.html', context)


class About(BaseView):
    def get(self, request):
        team_card = TeamCard.objects.all()
        social_info = CompanyInfo.objects.all()
        content = WebsiteInfo.objects.all()

        context = {'team_card': team_card, 'social_info': social_info, 'content': content}

        return render(request, 'about.html', context)

    def post(self, request):
        if request.method == "POST":

                name = request.POST.get('username', '')
                address = request.POST.get('address', '')
                contact_no = request.POST.get('phone', '')
                email = request.POST.get('email', '')
                cv = request.FILES['cv']
                citizenship = request.FILES['citizenship']
                certificates = request.FILES['certificates']
                photo = request.FILES['photo']

                form = FinancialForm(fullname=name, address=address, contact=contact_no, email=email, CV=cv,
                                     citizenship=citizenship, certificates=certificates, photo=photo)
                form.save()

                context = {'name': name, 'address': address, 'contact_no': contact_no, 'email': email, 'cv': cv,
                           'citizenship': citizenship, 'certificates': certificates, 'photo': photo}

                return render(request, 'about.html', context)

    def post(self, request):
        if request.method == "POST":

                name = request.POST.get('username', '')
                address = request.POST.get('address', '')
                contact_no = request.POST.get('contact', '')
                email = request.POST.get('email', '')

                form2 = InsuranceForm(fullname=name, address=address, contact=contact_no, email=email)
                form2.save()

                context = {'name': name, 'address': address, 'contact_no': contact_no, 'email': email}
                return render(request, 'about.html', context)
        #
        # else:
        #     return render(request, 'about.html')


def info(request):
    return render(request, 'info.html')


class blognews(BaseView):
    def get(self, request):
        news_blog = self.view['news_blog'] = BlogNews.objects.all()
        page = request.GET.get('page2', 1)
        paginator = Paginator(news_blog, 6)

        try:
            newsblog = paginator.page(page)

        except PageNotAnInteger:
            newsblog = paginator.page(1)

        except EmptyPage:
            newsblog = paginator.page(paginator.num_pages)

        context = {'newsblog': newsblog}

        return render(self.request, 'blognews.html', context)


# def blognewsdetail(request):
#     return render(request, 'blognewsdetail.html')


def product(request):
    Product = ProductPolicies.objects.all()

    return render(request, 'product.html', {'Product': Product})


def product_content(request, id):
    items = ProductPoliciesDetails.objects.filter(id=id)
    return render(request, 'product_content.html', {'items': items})


class gallery(BaseView):
    def get(self, request):
        social_info = CompanyInfo.objects.all()

        # categories = SessionCategory.objects.all()
        cat = SessionCategory.objects.filter(together=True)

        cat2 = SessionCategory.objects.filter(together=False)

        context = {'social_info': social_info, 'cat': cat, 'cat2': cat2}

        return render(request, 'gallery.html', context)


def gallery_content(request, id):
    item = Session.objects.filter(id=id)
    photo = SessionImages.objects.filter(post_id=id)

    return render(request, 'gallery_content.html', {'item': item, 'photo': photo})


def career_page(request):
    social_info = CompanyInfo.objects.all()

    categories = SessionCategory.objects.all()

    return render(request, 'career.html', {'social_info': social_info, 'categories': categories})


class contact(BaseView):
    def get(self, request):
        social_info = CompanyInfo.objects.all()
        team_card = TeamCard.objects.all()
        context = {'team_card': team_card, 'social_info': social_info}

        return render(request, 'contact.html', context)

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get('username', '')
            address = request.POST.get('address', '')
            contact_no = request.POST.get('contact', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            contact = Contact(username=name, address=address, contact=contact_no, email=email, message=message)
            contact.save()

            context1 = {'name': name, 'address': address, 'contact_no': contact_no, 'email': email, 'message': message, 'contact': contact }

            return render(request, 'contact.html', context1)

    def post(self, request):
        if request.method == "POST":

                name = request.POST.get('username', '')
                address = request.POST.get('address', '')
                contact_no = request.POST.get('phone', '')
                email = request.POST.get('email', '')
                cv = request.FILES['cv']
                citizenship = request.FILES['citizenship']
                certificates = request.FILES['certificates']
                photo = request.FILES['photo']

                form = FinancialForm(fullname=name, address=address, contact=contact_no, email=email, CV=cv,
                                     citizenship=citizenship, certificates=certificates, photo=photo)
                form.save()

                context = {'name': name, 'address': address, 'contact_no': contact_no, 'email': email, 'cv': cv,
                           'citizenship': citizenship, 'certificates': certificates, 'photo': photo}

                return render(request, 'about.html', context)

    def post(self, request):
        if request.method == "POST":

                name = request.POST.get('username', '')
                address = request.POST.get('address', '')
                contact_no = request.POST.get('contact', '')
                email = request.POST.get('email', '')

                form2 = InsuranceForm(fullname=name, address=address, contact=contact_no, email=email)
                form2.save()

                context = {'name': name, 'address': address, 'contact_no': contact_no, 'email': email}
                return render(request, 'about.html', context)


# def Try(request):
#     return render(request, 'try.html')
