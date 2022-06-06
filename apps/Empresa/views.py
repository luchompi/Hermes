from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sede, Dependencia,sedeDependencia
from .serializers import sedeSerializer,dependenciaSerializer,sedeDepSerializer
# Create your views here.

class sedeAPI(APIView):
	def get(self,request,format=None):
		sedes=Sede.objects.all()
		serializer=sedeSerializer(sedes,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)
	
	def post(self,request,format=None):
		serializer=sedeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	
	def put(self,request,pk,format=None):
		try:
			sede=Sede.objects.get(pk=pk)
		except Sede.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer=sedeSerializer(sede,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self,request,pk,format=None):
		try:
			sede=Sede.objects.get(pk=pk)
		except Sede.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		sede.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class SedeDetailAPI(APIView):
	def get(self,request,pk,format=None):
		try:
			sede=Sede.objects.get(pk=pk)
		except Sede.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer=sedeSerializer(sede)
		return Response(serializer.data)