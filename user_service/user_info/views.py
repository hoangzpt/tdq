# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import user_registration as userreg


### This function is for fetching the user data.
def user_data(uname):
    user = userreg.objects.filter(email=uname)
    for data in user.values():
        return data


### This function is created for getting the username and password.
@csrf_exempt
def user_info(request):
    # uname = request.POST.get("UserName")
    val1 = json.loads(request.body)
    uname = val1.get('UserName')
    resp = {}
    if uname:
    ## Calling the getting the user info.
        respdata = user_data(uname)
        dict1 = {}
        if respdata:
            dict1['FirstName'] = respdata.get('fname', '')
            dict1['LastName'] = respdata.get('lname', '')
            dict1['MobileNumber'] = respdata.get('mobile', '')
            dict1['EmailId'] = respdata.get('email', '')
            dict1['Address'] = respdata.get('address', '')
            if dict1:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['data'] = dict1
    ### If a user is not found then it give failed as a response.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'User Not Found.'
                ### The field value is missing.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Fields is mandatory.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'
    return HttpResponse(json.dumps(resp), content_type='application/json')

