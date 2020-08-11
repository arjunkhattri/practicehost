from django import forms
from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.urls import reverse
from django.views.generic.base import View


class BlogCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    description = RichTextUploadingField(blank=True, null=True)
    slug = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.title

    @property
    def get_blog_news_category(self):
        return BlogNews.objects.filter(category=self.id)

    # def get_absolute_url(self):
    #     return reverse('blognews', kwargs={'pk': self.pk})

    # @staticmethod
    # def get_all_blognews_category():
    #     return BlogCategory.objects.all()


class BlogNews(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)

    description = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogNewsImages(models.Model):
    post = models.ForeignKey(BlogNews, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/blognewsimages/', blank=True)

    def __str__(self):
        return self.post.title

    # def get_absolute_url(self):
    #     return reverse('home:blognews', kwargs={'id': self.id})
    # #
    # def get_absolute_url(self):
    #     return reverse("home:blognewsdetail", kwargs={'id': self.id})

    # @staticmethod
    # def get_all_items():
    #     return BlogNews.objects.all()
    #
    # @staticmethod
    # def get_all_items_by_categoryid(category_id):
    #     if category_id:
    #         return BlogNews.objects.filter(category=category_id)
    #     else:
    #         return BlogNews.get_all_items()


class TeamCard(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    fullname = models.CharField(max_length=400)
    contact = models.CharField(max_length=50)
    Bio = RichTextUploadingField(blank=True, null=True)
    designation = models.CharField(max_length=400)
    email = models.EmailField(max_length=254, unique=True)
    facebook_link = models.URLField(max_length=500, blank=True)
    instagram_link = models.URLField(max_length=500, blank=True)
    twitter_link = models.URLField(max_length=500, blank=True)
    website = models.URLField(max_length=400, blank=True)
    linked = models.URLField(max_length=400, blank=True)
    github = models.URLField(max_length=400, blank=True)

    def __str__(self):
        return self.title


class SessionCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    description = RichTextUploadingField(blank=True, null=True)
    slug = models.CharField(max_length=400, unique=True)
    together = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def get_sessions(self):
        return Session.objects.filter(category=self.id)

    @property
    def get_training_sessions(self):
        return TrainingSessions.objects.filter(category=self.id)


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    description = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='media')
    date_created = models.DateField()
    date_updated = models.DateField()
    category = models.ForeignKey(SessionCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SessionImages(models.Model):
    post = models.ForeignKey(Session, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/sessionimages/', blank=True, null=True)
    # @staticmethod
    # def get_items_by_id(ids):
    #     return Session.objects.filter(id__in=ids)

    # @staticmethod
    # def get_all_items():
    #     return Session.objects.all()
    #
    # @staticmethod
    # def get_all_items_by_categoryid(category_id):
    #     if category_id:
    #         return Session.objects.filter(category=category_id)
    #     else:
    #         return Session.get_all_items()


class TrainingSessions(models.Model):
    image = models.ImageField(upload_to='media/trainingsessionimages/', blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    category = models.ForeignKey(SessionCategory, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('career', kwargs={'pk': self.pk})


class Carousel(models.Model):
    id = models.AutoField(primary_key=True)
    selected = models.BooleanField(blank=True)
    image = models.ImageField(upload_to='media')


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=70, default="")
    contact = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=500, default="")
    message = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.username


#for about page
class FinancialForm(models.Model):
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=70, default="")
    contact = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=100, default="")
    CV = models.FileField()
    citizenship = models.ImageField(upload_to='media/FinancialForm')
    certificates = models.FileField()
    photo = models.ImageField(upload_to='media/FinancialForm')


class InsuranceForm(models.Model):

    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=70, default="")
    contact = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")



class CompanyInfo(models.Model):
    facebook_link = models.URLField(max_length=500, blank=True)
    instagram_link = models.URLField(max_length=500, blank=True)
    twitter_link = models.URLField(max_length=500, blank=True)
    youtube_link = models.URLField(max_length=500, blank=True)
    contact = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")


class WebsiteInfo(models.Model):
    Nle_info = RichTextUploadingField(blank=True, null=True)
    Our_story = RichTextUploadingField(blank=True, null=True)
    Our_mission = RichTextUploadingField(blank=True, null=True)


class ProductPolicies(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media/product')

    def __str__(self):
        return self.title


class ProductPoliciesDetails(models.Model):
    title = models.CharField(max_length=400)
    description = RichTextUploadingField(blank=True, null=True)
    ImageCategory = models.ForeignKey(ProductPolicies, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# class GalleryPosts(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(blank=True)
#
#     def __str__(self):
#         return self.title
#
#
# class GalleryImage(models.Model):
#     post = models.ForeignKey(GalleryPosts, default=None, on_delete=models.CASCADE)
#     image = models.FileField(upload_to='media/gallery_posts/', blank=True, null=True)
#
#     def __str__(self):
#         return self.post.title










