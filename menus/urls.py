from django.conf.urls import url


from menus import views

urlpatterns = [
    url(r'^get_objects/(?P<id>[0-9]*)/$', views.get_objects, name='get_objects')
]