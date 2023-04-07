from django.urls import include, path

from cats.views import cat_list, cat_detail

urlpatterns = [
   path('cats/', cat_list),
   path('cats/<int:id>', cat_detail)
]


