from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from lap4.models import *
from lap4.serializers import *

# Create your views here.
 
@csrf_exempt
def billApi(request, id=0):
    if request.method=='GET':
        bills = historybill.objects.all()
        bills_serializer=historybillSerializer(bills,many=True)
        return JsonResponse(bills_serializer.data,safe=False)
    elif request.method=='POST':
        bill_data=JSONParser().parse(request)
        bills_serializer=historybillSerializer(data=bill_data)
        if bills_serializer.is_valid():
            bills_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        bill_data=JSONParser().parse(request)
        bill=historybill.objects.get(bill_id=bill_data['bill_id'])
        bills_serializer=historybillSerializer(bill,data=bill_data)
        if bills_serializer.is_valid():
            bills_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        bill=historybill.objects.get(bill_id=id)
        bill.delete()
        return JsonResponse("Deleted Successfully",safe=False)
 
