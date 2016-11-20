from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from todo_list.models import *
from todo_list.views import *

urlpatterns = [

    url(r'^set_done/(\d+)$', set_done,name='set_done'),
    url(r'^set_open/(\d+)$', set_open,name='set_open'),
    url(r'^drop/(\d+)$', drop,name='drop'),
    url(r'^create_task', create_task,name='create_task'),
    url(r'^create_project', create_project,name='create_project'),
    url(r'^login', login, name='login'),
    url(r'^logout', logout, name='logout'),
    url(r'', main,name='main'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
