from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('test_app/show',views.index)
]