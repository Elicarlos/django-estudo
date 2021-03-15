from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    # Views feitas no braço
#     path('cursos/', views.index, name="index"),
#     path('cursos/<int:curso_id>/', views.detalhes, name="detalhes"),
#     path('cursos/<int:curso_id/cursos/', views.resultados, name="cursos"),
    path('cursos/', views.IndexView.as_view(), name="index"),
    path('cursos/<int:pk>/', views.DetalhesView.as_view(), name="detalhes")
]