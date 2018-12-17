from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models 
from . import permissions 

# Create your views here.

class HelloApiView(APIView):
	""" Test  Api View"""
	serializer_class = serializers.HelloSerializer

	def get(self,request,format=None):
		"""Returns a list of ApiView Features"""
		an_apiview = [
		'Uses HTTP methods as function (get,post,put,patch,delete)',
		'It is similar to a traditional django view',
		'Gives you the most control over your logic',
		'its mapped manually to URLs'
		]
		return Response({'Message': 'Hello World!','an_apiview': an_apiview})

	def post(self, request):
		""" Create a hello message with our name. """
		serializer = serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
	 		name = serializer.data.get('name')
	 		message = 'Hello {0}'.format(name)
	 		return Response({'message': message})
		else:
	 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def put(self, request, pk=None):
		""" Handles updating an object """
		return Response({'method': 'put'})

	def patch(self, request,pk=None):
		"""Patch request , only updates fie;ds provided in the requesr """
		return Response({'methods': 'patch'})

	def delete(self,request,pk=None):
		"""Deletes and object """
		return Response({'method': 'delete'}) 



class HelloViewSet(viewsets.ViewSet):
	""" test API viewset"""

	serializer_class =  serializers.HelloSerializer

	def list(self,request):
		"""Return a hello message """

		a_viewset = [
			'uses actions (list,create,retrieve,update,partial_update)',
			'Automatically maps to URLs using Routers',
			'provides more functionality with less code.'		
		]
		
		return Response({'message':'Hello!','a_viewset':a_viewset})	
	
	def create(self,request):
		""" create a new Hello  message """
		serializer = serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message':message})
		else:
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self,request,pk=None):
		"""Handles getting an object by its ID """

		return Response({'hhtp_methos': 'GET'})

	def update(self,request,pk=None):
		""" Handles updating an object"""


		return Response({'http_methos': 'PUT'})

	def partial_update(self,request,pk=None):
		""" Handles updating part of an object """


		return Response({'http_methos': 'PATCH'})

	def destroy(self, request, pk=None):
		""" Handles removing  an object """
		return Response({'hhtp_methos': 'DELETE'}) 		

class UserProfileViewSet(viewsets.ModelViewSet):
	""" Handles creating, creating and updating profiles"""

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)
	