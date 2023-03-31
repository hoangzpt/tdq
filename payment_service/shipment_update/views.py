# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from payment.models import payment_status as paystat
import requests
import json
### This function is for fetching the user data.
def shipment_details_update(uname):
    ship_dict = {}
    ### It is used for getting data from payment info.
    user = paystat.objects.filter(username=uname)
    for data in user.values():
        print("data", data)
        ship_dict['Product Id'] = data['product_id']
        ship_dict['Quantity'] = data['quantity']
        ship_dict['Payment Status'] = data['status']
        ship_dict['Transaction Id'] = data['id']
        ship_dict['Mobile Number'] = data['mobile']
        ###(self.username, self.product_id, self.price, self.quantity, self.mode_of_payment, self.mobile, self.status)
    ### It is used for getting the user info.
        url = 'http://127.0.0.1:8000/userinfo/'
        d1 = {}
        d1["UserName"] = data['username']
        print(d1)
        data = json.dumps(d1)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        val1 = json.loads(response.content.decode('utf-8'))
        print(val1)
        ship_dict['First Name'] = val1['data']['FirstName']
        ship_dict['Last Name'] = val1['data']['LastName']
        ship_dict['Address'] = val1['data']['Address']
        ship_dict['Email Id'] = val1['data']['EmailId']

        print(ship_dict)
        ### Data is ready for calling the shipment_updates API.
        url = 'http://127.0.0.1:8003/shipmentregupdate/'
        data = json.dumps(ship_dict)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        print(response)
        api_resp = json.loads(response.content.decode('utf-8'))
        return api_resp
