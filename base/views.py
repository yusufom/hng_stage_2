from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from datetime import datetime

# Create your views here.
from rest_framework import renderers

from base.models import Person
from base.serializers import PersonSerializer

class CustomRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = data
        return super().render(response_data, accepted_media_type, renderer_context)

class PersonView(APIView):
    renderer_classes = [CustomRenderer]
    serializer_class = PersonSerializer

    def get(self, request):
        serializers = PersonSerializer(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get("name")
            try:
                person = Person.objects.get(name=name)
                res = {
                    "id": person.id,
                    "name": person.name,
                    }
                return Response(res, status=status.HTTP_200_OK)
            except Person.DoesNotExist:
                res = {
                    "message": "Not found",
                    }
                return Response(res, status=status.HTTP_404_NOT_FOUND)
        return Response(serializers.errors, status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request):
        serializers = PersonSerializer(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get("name")
            try:
                person = Person.objects.get(name=name)
                if person:
                    return Response({"message": f"{person.name} already exist"}, status=status.HTTP_200_OK)
            except:
                serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, name):
        try:
            person = Person.objects.get(name=name)
            serializers = PersonSerializer(data=request.data, instance=person)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)
        except Person.DoesNotExist:
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, name):
        try:
            person = Person.objects.get(name=name)
            person.delete()
            return Response({"message": f"{person.name} has been deleted"}, status=status.HTTP_200_OK)
            
        except Person.DoesNotExist:
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
# class PersonCreateView(CreateAPIView):
#     renderer_classes = [CustomRenderer]
#     serializer_class = PersonSerializer
    
#     def post(self, request):
#         serializers = PersonSerializer(data=request.data)
#         if serializers.is_valid():
#             name = serializers.validated_data.get("name")
#             try:
#                 person = Person.objects.get(name=name)
#                 if person:
#                     return Response({"message": f"{person.name} already exist"}, status=status.HTTP_200_OK)
#             except:
#                 serializers.save()
            
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)
    
# class PersonUpdateView(UpdateAPIView):
#     renderer_classes = [CustomRenderer]
#     serializer_class = PersonSerializer
    
#     def put(self, request, name):
#         try:
#             person = Person.objects.get(name=name)
#             serializers = PersonSerializer(data=request.data, instance=person)
#             if serializers.is_valid():
#                 serializers.save()
#                 return Response(serializers.data, status=status.HTTP_200_OK)
#             return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)
#         except Person.DoesNotExist:
#             return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
# class PersonDeleteView(DestroyAPIView):
#     renderer_classes = [CustomRenderer]
    
#     def delete(self, request, name):
#         try:
#             person = Person.objects.get(name=name)
#             person.delete()
#             return Response({"message": f"{person.name} has been deleted"}, status=status.HTTP_200_OK)
            
#         except Person.DoesNotExist:
#             return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        