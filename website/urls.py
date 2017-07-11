from django.conf.urls import url


from website import views

urlpatterns = [
    url(r'^(?P<slug>.*)/$', views.page, name='page')
]