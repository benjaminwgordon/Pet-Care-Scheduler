from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets', views.pets_index, name='pets_index'),
    path('pets/<int:pet_id>/', views.pets_detail, name='pets_detail'),
    path('pets/<int:pet_id>/edit/', views.pets_edit, name='pets_edit'),
    path('pets/<int:pet_id>/delete', views.pets_delete, name='pets_delete')
]
