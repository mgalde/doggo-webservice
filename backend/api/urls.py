from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from api import controllers
from django.views.decorators.csrf import csrf_exempt


#REST API routes
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
	url(r'^session', csrf_exempt(controllers.Session.as_view())),
	url(r'^register', csrf_exempt(controllers.Register.as_view())),
	url(r'^events', csrf_exempt(controllers.Events.as_view())),
	url(r'^dogs', csrf_exempt(controllers.DogsList.as_view())),
	url(r'^dogs/(?P<pk>[0-9]+)', csrf_exempt(controllers.DogView.as_view())),
	url(r'^breeds', csrf_exempt(controllers.BreedsList.as_view())),
	url(r'^breeds/(?P<pk>[0-9]+)', csrf_exempt(controllers.BreedView.as_view())),
	url(r'^activateifttt', csrf_exempt(controllers.ActivateIFTTT.as_view())),
	url(r'^', include(router.urls)),
]
