from django.conf.urls import url


from website import views

urlpatterns = [
    url(r'^equipos/(?P<slug>.*)/$', views.category, name='product_category'),
    url(r'^(?P<slug>.*)/$', views.page, name='page'),

]