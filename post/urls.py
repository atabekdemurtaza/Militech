from django.urls import path
#from post.views import PostListView, PostDetailView
#from post.views import UserListView, UserDetailView
from post.views import PostViewSet
from post.views import UserViewSet
from rest_framework import routers

#Старая версия так как у нас много путей то есть (path)
"""urlpatterns = [

	path('users/', UserListView.as_view()),
	path('users/<int:pk>/', UserDetailView.as_view()),
	path('', PostListView.as_view()),
	path('<int:pk>/', PostDetailView.as_view()),
	
]"""

#Все путей(path) соберем в одно место с помощью routers 

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls