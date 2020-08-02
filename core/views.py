from django.db.models import Q
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework import viewsets, permissions, authentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from . import models, serializers
# Create your views here.

class SharedURLGenretor(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        title = request.data.get('title', None)
        body = request.data.get('body', None)

        note, created = models.Note.objects.get_or_create(username = username, title=title, body=body)
        return Response({"id":note.id}, status= HTTP_200_OK)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permissions = [AllowAny,]



