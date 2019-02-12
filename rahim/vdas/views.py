from django.shortcuts import render,redirect
from .models import Customer
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView
from .models import Employee
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .serializers import CustmerSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
@csrf_exempt
def homeres(request):
    if request.method== "GET":
        customer= Customer.objects.all()
        serializer= CustmerSerializer(customer,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="POST":
        json_parser= JSONParser()
        data=json_parser.parse(request)
        serializer=CustmerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JSONParser(serializer.errors,status=400)

@csrf_exempt
def poll_details(request,id):
    try:
        instance= Customer.objects.get(id=id)
    except Customer.DoesNotExist as e:
        return JsonResponse({"error":"given customer object not forund"},status=404)
    if request.method=="GET":
        serializer=CustmerSerializer(instance)
        return JsonResponse(serializer.data)
    elif request.method=="PUT":
        json_parser=JSONParser()
        data= json_parser.parse(request)
        serializer=CustmerSerializer(instance,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors,status=400)
    elif request.method== "DELETE":
        instance.delete()
        return HttpResponse(status=204)



class PollView(APIView):
    def get(self, request):
        customer= Customer.objects.all()
        serializer=CustmerSerializer(customer,many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
        data=request.data
        serializer=CustmerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


class PollDetailView(APIView):
    def get_object(self, id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist as e:
            return Response({"errors":"given customer object does not found"},status=404)
    def get(self, request,id=None):
        instance=self.get_object(id)
        serializer=CustmerSerializer(instance)
        return Response(serializer.data)
    def put(self,request,id=None):
        data=request.data
        instance=self.get_object(id)
        serializer=CustmerSerializer(instance,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors, status=400)
    def delete(self,request,id=None):
        instance=self.get_object(id)
        instance.delete()
        return HttpResponse(status=204)




























class HomePageView(ListView):
    model= Employee
    template_name= 'vdas/home.html'


class DetailPageView(DetailView):
    model=Employee
    template_name= 'vdas/detail.html'
    context_object_name= "anything"
class CreatePageView(CreateView):
    model=Employee
    template_name= 'vdas/Create.html'

    fields= '__all__'


class UpdatePageView(UpdateView):
    model=Employee
    template_name= 'vdas/edit.html'

    fields= ['name','age']
class DeletePageView(DeleteView):
    model=Employee
    template_name= 'vdas/delete.html'
    success_url= reverse_lazy('home')




from .forms import CustomerForm

def home(request):
    resp= Customer.objects.all()
    return render(request,'vdas1/home.html',{'resp':resp})


def custpost(request):
    form= CustomerForm()
    if request.method=="POST":
        form= CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'vdas1/create.html',{'form':form})

def custupdate(request,id):
    user= Customer.objects.get(id=id)
    form= CustomerForm(instance=user)
    if request.method =="POST":
        form= CustomerForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'vdas1/edit.html',{'form':form})

def custdetails(request,id):
    resp=Customer.objects.get(id=id)
    return render(request,'vdas1/detail.html',{'resp':resp})
def custdelete(request, id):
    obj= Customer.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('home')
    return render(request,'vdas1/delete.html',{'obj':obj})
