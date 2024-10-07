from .views import ProductViewSets
from django.urls import path

urlpatterns = [
    path('', ProductViewSets.as_view({'get': 'list', 'post': 'create'}, name='product_list')),
    path('<int:pk>/', ProductViewSets.as_view({'get': 'retrieve',
                                               'put': 'update',
                                               'delete': 'destroy'}), name='product_detail')
]

