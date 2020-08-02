from django.urls import path, re_path
from . import views
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'core'

router = DefaultRouter()
router.register('notes', views.NoteViewSet, basename='note')


urlpatterns = [
	path("shared-url-generator/", views.SharedURLGenretor.as_view()),

]

urlpatterns += router.urls