from django.contrib import admin
from django.urls import path
from main_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('ajouter_solutions/', views.ajouter_solutions, name='ajouter_solutions'),
    path('ajouter_problemes/', views.ajouter_problemes, name='ajouter_problemes'),
    path('voir_problemes/', views.voir_problemes, name='voir_problemes'),
    path('detail_probleme/<int:pk>/', views.detail_probleme, name='detail_probleme')

] 