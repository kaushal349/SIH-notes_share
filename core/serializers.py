# from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from . import models



class NoteSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="categories")

    class Meta:
        model = models.Note
        fields = ("__all__")
