from django.urls import path
from . import views

urlpatterns = [
    # path('',views.FoodRecipeListdetailsview.as_view()),
    path('',views.FoodRecipeListView.as_view()),
]

