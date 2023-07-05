
from django.urls import path
from .views import *

urlpatterns = [
    path('create/',create,name="create"),
    path('<str:id>',detail,name="detail"),
    path('edit/<str:id>',edit,name="edit"),
    path('new/',new,name="new"),
    path('delete/<str:id>',delete,name="delete"),
    path('comment/<str:id>',comment,name="comment"),
]
