from django.shortcuts import render,get_object_or_404
from Repository.models import Questions,Submissions
from Repository.serializers import QuestionSerializer,SubmissionSerializer
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

    def delete(self,request,pk):  #pk is the primary key of the question to delete
        Questions.objects.filter(id=pk).delete() #delete the question object wth the given primary key
        return Response(data={"message": "Question Deleted Successfully"}) #returns a success message

class SubmissionListCreateView(APIView):
    def get(self,request):
        qs=Submissions.objects.all()
        serializer_instance=SubmissionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data=request.data
        serializer_instance=SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            Submissions.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors) 


class SubmissionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        # qs=Submissions.objects.get(id=pk)
        qs= get_object_or_404(Submissions,id=pk)
        serializer_instance=SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)
    
    # PUT: Update a submission
    def put(self, request, pk):
        form_data = request.data
        serializer_instance = SubmissionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data

            Submissions.objects.filter(id=pk).update(**actual_data)

            return Response(serializer_instance.data)

        else:
            return Response(serializer_instance.errors)

    # DELETE: Delete a submission
    def delete(self, request, pk):
        Submissions.objects.filter(id=pk).delete()
        return Response({"message": "Submission deleted successfully"})

class EvaluateSubmissionView(APIView):
    def put(self,request,pk):
        form_data=request.data
        Submissions.objects.filter(id=pk).update(**form_data)
        return Response(data={
            "Message":"Updated..!"
        })