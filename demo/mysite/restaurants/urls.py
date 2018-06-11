from django.conf.urls import url
#from restaurants.views import index,gallery,generic,contact,submit,nightmarket_submit
from .views import *
from django.contrib import admin
urlpatterns = [
    #url(r'^submit/',views.submit,name='submit' ),
    url(r'^gallery/a1',a1),
    url(r'^gallery/a2',a2),
    url(r'^gallery/a3',a3),
    url(r'^gallery/a4',a4),
    url(r'^gallery/a5',a5),
    url(r'^gallery/a6',a6),
    url(r'^gallery/a7',a7),
    url(r'^$',index),
    url(r'^contact/',submit,name='submit'),
    url(r'^gallery/',nightmarket_submit,name='nightmarket_submit'),
    url(r'^gallery/',gallery),
    url(r'^generic/',generic),
    url(r'^contact/',contact),
	
   #url(r'^contact/submit/',submit),	
    #url(r'^/submit/',views.submit,name='submit'),
]
    