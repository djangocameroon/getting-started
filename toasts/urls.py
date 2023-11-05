from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toaster/', views.submit_toast_form, name='toster')
]
