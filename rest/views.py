from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
import requests
import json

# Create your views here.
#CBV 
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class =PostSerializer

#kakao api
url = "https://dapi.kakao.com/v2/search/web"
queryString ={"query" :"덕성여자대학교"}
header={"Authorization":"KakaoAK c2c8cdf34f6544fdea14a3c5784c8fe1"}
r=requests.get(url, headers=header, params=queryString)
print(json.loads(r.text))