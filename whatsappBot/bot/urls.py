from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('f800d673-fc52-41b7-b6c3-e2ac8de091bf', views.whatsAppWebhook, name = 'whatsapp-web'),
]


# Callback URL - 
# Verify token - d0e1a3ec-640e-4cbf-9d90-e644bd74859a