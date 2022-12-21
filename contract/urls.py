from django.urls import path,include
from contract import views
urlpatterns =[
    path('',views.CooksRecipes.as_view()),
    path('search/', views.search.as_view()),
    path('recipes/',views.CooksAllRecipes.as_view()),
     path('client/',views.CustomerEnd)
]