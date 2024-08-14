from django.urls import path
from . import views
from .views import about_us

urlpatterns = [
    path('about-us/', views.about_us, name='about_us'),
    path('<int:category_id>/', views.post_by_category, name='post_by_category'),
     
]
