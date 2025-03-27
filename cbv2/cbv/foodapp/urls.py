from django.urls import path
from . import views

urlpatterns = [
    # path('',views.FoodRecipeListdetailsview.as_view()),
    # path('',views.FoodRecipeListView.as_view()),
    # path('<int:id>',views.FoodRecipeRetriveView.as_view()),
    # path('create',views.FoodRecipeCreateveView.as_view(),),
    # path('Update/<int:id>',views.FoodRecipeUpdateView.as_view()),
    # path('delete/<int:id>',views.FoodRecipeDeleteView.as_view()),
    path('',views.foodRecipeListCreateView.as_view()),
    path('<int:id>',views.foodRecipeUpdateDeleteRetriveView.as_view()),
    
    
]

