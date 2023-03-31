from django.urls import path
from . import views

urlpatterns = [
    path("shipmentstatus/", views.shipment_status),
    path("shipmentregupdate/", views.shipment_reg_update),
]
