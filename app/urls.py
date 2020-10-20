from django.urls import path
from app.views import *

urlpatterns = [
    path('products/', Products.as_view()),
    path('positions/', Positions.as_view()),
    path('positions/<int:pk>', Positions.as_view()),
    path('baskets/', Baskets.as_view())

]
