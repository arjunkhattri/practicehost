from django.contrib import admin
from .models import BlogCategory, SessionCategory, BlogNews, BlogNewsImages, TeamCard, Session, SessionImages, TrainingSessions, Carousel, Contact, FinancialForm, InsuranceForm, CompanyInfo, WebsiteInfo, ProductPolicies, ProductPoliciesDetails
# Register your models here.

admin.site.register(BlogCategory)
admin.site.register(SessionCategory)
# admin.site.register(BlogNews)
admin.site.register(TeamCard)
admin.site.register(TrainingSessions)
admin.site.register(Carousel)
admin.site.register(Contact)
admin.site.register(FinancialForm)
admin.site.register(InsuranceForm)
admin.site.register(CompanyInfo)
admin.site.register(WebsiteInfo)
admin.site.register(ProductPolicies)
admin.site.register(ProductPoliciesDetails)


class BlogNewsImageAdmin(admin.StackedInline):
    model = BlogNewsImages


@admin.register(BlogNews)
class BlogNewsAdmin(admin.ModelAdmin):
    inlines = [BlogNewsImageAdmin]

    class Meta:
        model = BlogNews


@admin.register(BlogNewsImages)
class BlogNewsImageAdmin(admin.ModelAdmin):
    pass


class SessionImageAdmin(admin.StackedInline):
    model = SessionImages


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    inlines = [SessionImageAdmin]

    class Meta:
        model = Session


@admin.register(SessionImages)
class SessionImageAdmin(admin.ModelAdmin):
    pass
