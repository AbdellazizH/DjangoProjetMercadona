from django.urls import path
from backoffice import views

app_name = 'backoffice'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('promotions/', views.PromotionListView.as_view(), name='promotion_list'),
    path('promotions/add/', views.promotion_add, name='promotion_add'),
    path('promotions/edit/<int:pk>/', views.promotion_edit, name='promotion_edit'),
    path('promotions/delete/<int:pk>/', views.promotion_delete, name='promotion_delete'),
]
