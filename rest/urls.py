from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest import views

router=DefaultRouter()
router.register('post',views.PostViewSet)
router.register('album',views.ImgViewSet)
router.register('files',views.FileViewSet)

urlpatterns=[
    path('',include(router.urls)),
]