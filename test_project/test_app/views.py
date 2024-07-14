from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# Create your views here.
from .controller import document_view

from django.http import HttpResponse
 
# @api_view(['GET']) 
def index(request):
  # return HttpResponse("Hello Geeks")
  exel_file_path = './test_app/static/the-office-lines.xlsx'
  return document_view(exel_file_path)
  # return Response({'message': 'Hello, World!'})

