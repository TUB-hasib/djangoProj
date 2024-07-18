from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# Create your views here.
from .controller import read_document

from django.http import HttpResponse, JsonResponse
 
# @api_view(['GET']) 
def index(request):
  # return HttpResponse("Hello Geeks")
  exel_file_path = './test_app/static/the-office-lines.xlsx'
  # return read_document(exel_file_path)
  val = read_document(exel_file_path)
  return JsonResponse(val)

