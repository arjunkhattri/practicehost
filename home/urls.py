from django.urls import path
from .import views
# app_name = 'home'

urlpatterns = [
    path('', views.home.as_view(), name='index'),
    path('base', views.Base.as_view(), name='base'),
    path('blognewsdetail/<int:id>/', views.BlogNewsDetail, name='blognewsdetail'),
    path('careerfinancialdetail/<int:id>/', views.CareerFinancialDetail, name='careerfinancialdetail'),
    path('blognews/', views.BlogNewsContent, name='blognews'),
    path('careerfinancial/', views.CareerFinancialContent, name='careerfinancial'),
    path('about/', views.About.as_view(), name='about'),
    # path('insurance/', views.insurance, name='insurance'),
    path('gallery/', views.gallery.as_view(), name='gallery'),
    # path('galleryview/', views.gallery_view, name='gallery'),
    path('gallery_content/<int:id>', views.gallery_content, name='gallery_content'),
    path('career>', views.career_page, name='career'),
    path('contact/', views.contact.as_view(), name='contact'),
    path('info/', views.info, name='info'),

    path('product/', views.product, name='product'),
    path('product_content/<int:id>', views.product_content, name='product_content'),
    # path('', views.gallery_view, name='galleryview'),
    # path('<int:id>/', views.detail_gallery, name='detail')
    # path('try', views.Try, name='try')

]
