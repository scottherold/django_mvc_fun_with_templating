from django.urls import path
from . import views # . == current folder

# TEMPLATE TAGGING
app_name = 'basic_app'

# interapp routing
urlpatterns = [
    path('', views.index, name='index'),
    path('relative', views.relative, name='relative'),
    path('other', views.other, name='other')
]