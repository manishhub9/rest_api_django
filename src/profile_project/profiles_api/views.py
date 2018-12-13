from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
	""" Test  Api View"""
	def get(self,request,format=None):
		"""Returns a list of ApiView Features"""
		an_apiview = [
		'Uses HTTP methods as function (get,post,put,patch,delete)',
		'It is similar to a traditional django view',
		'Gives you the most control over your logic',
		'its mapped manually to URLs'
		]
		return Response({'Message': 'Hello World!','an_apiview': an_apiview})
