from django.conf.urls import url
import views as view

urlpatterns = [
    url(r'^index/$', view.index),
]
