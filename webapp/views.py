from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import empoyleeSerializer
from .models import empoylee
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# for class based view for csrf token
# from django.utils.decorators import method_decorator
# from django.views import View

# @method_decorator(csrf_exempt,name='dispatch')
# class studentApi(View):
#     def get(self,request,*args,**kargs):





@csrf_exempt
def emp_api(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            emp=empoylee.objects.get(id=id)
            serializer=empoyleeSerializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        emp=empoylee.objects.all()
        serializer=empoyleeSerializer(emp,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=empoyleeSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data inserted Succesfully'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
        
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        emp=empoylee.objects.get(id=id)
        serializer=empoyleeSerializer(emp,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        emp=empoylee.objects.get(id=id)
        emp.delete()
        res={'msg':'Delted successfully'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)

