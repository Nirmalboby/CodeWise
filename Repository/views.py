from django.shortcuts import render
from Repository.models import Questions
from Repository.serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class QuestionListCreateView(APIView):

    def get(self,request):
        qs=Questions.objects.all()  #colection of questions
        serializer_instance=QuestionSerializer(qs,many=True)  #many=true means tells the serializer that the input contains multiple objects
        return Response(serializer_instance.data) #return the serializer data as a response
    
    def post(self,request):
        form_data=request.data #form_data dictionary to python native type
        serializer_instance=QuestionSerializer(data=form_data) #create serializer instance with the form data
        if serializer_instance.is_valid(): #check if the data is valid according to the serializers validation rules
            actual_data=serializer_instance.validated_data #get the validated data from the serializer
            Questions.objects.create(**actual_data)
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

class QuestionRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk): #pk is the primary key of the question to retrieve
        qs=Questions.objects.get(id=pk) #get the question object with the given primary key
        serializer_instance=QuestionSerializer(qs) #serialize the question object
        return Response(data=serializer_instance.data) #return the serialized data as a response

    def put(self,request,pk): #pk is the primary key of the question to update
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data) #creates serializer instance with form data
        if serializer_instance.is_valid(): #check if the data is valid according to the serializers validation rules
            actual_data=serializer_instance.validated_data

            # syntax : Modelname.object.filter(id).update()

            Questions.objects.filter(id=pk).update(**actual_data) #update the question object wth the given primary key
            return Response(data=serializer_instance.data) #return the serialized data as a response
        else:
            return Response(data=serializer_instance.errors) #return the validation errors as a response
