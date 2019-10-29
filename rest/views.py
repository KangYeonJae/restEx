from django.shortcuts import render
from .models import Post, Album, Files
from .serializers import PostSerializer, AlbumSerializer, FilesSerializer
from rest_framework import viewsets, serializers
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status 

# import requests
# import json

# Create your views here.
#CBV 
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class =PostSerializer

    filter_backends =[SearchFilter]
    search_fields=('title','body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # 현재 request를 보낸 유저
    # == self.request.user

    def get_queryset(self):
        qs =super().get_queryset()

        if self.request.user.is_authenticated:
            qs=qs.filter(author=self.request.user)
        else:
            qs=qs.none()
        return qs

class ImgViewSet(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class =AlbumSerializer
 
class FileViewSet(viewsets.ModelViewSet):
    queryset= Files.objects.all()
    serializer_class =FilesSerializer

    parser_classes =(MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer=FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)


#kakao api
#url = "https://dapi.kakao.com/v2/search/web"
#queryString ={"query" :"덕성여자대학교"}
#header={"Authorization":"KakaoAK c2c8cdf34f6544fdea14a3c5784c8fe1"}
#r=requests.get(url, headers=header, params=queryString)
#print(json.loads(r.text))