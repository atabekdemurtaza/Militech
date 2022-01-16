from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from rest_framework import schemas
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


API_TITLE = 'Militech API'
API_DESCRIPTION = 'A web API for creating and editing blog posts.'
#schema_view = schemas.get_schema_view(title=API_TITLE) #Это для машины то есть для компьютера
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('post/api/', include('post.urls')),
    path('post/api-auth/', include('rest_framework.urls')),
    path('post/api/rest-auth/', include('rest_auth.urls')),
    path('post/api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)), #это для людей
    #path('schema/', schema_view) #это для машины
    path('swagger-docs/', schema_view),

]


