from django.urls import path
from backoffice import views

app_name = 'backoffice'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('category/list/', views.category_list, name='category_list'),
    path('category/add/', views.category_add, name='category_add'),
    path('category/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),

    path('product/list', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),

    # path('promotions/', views.PromotionListView.as_view(), name='promotion_list'),
    path('promotion/list', views.promotion_list, name='promotion_list'),
    path('promotion/add/', views.promotion_add, name='promotion_add'),
    path('promotion/edit/<int:pk>/', views.promotion_edit, name='promotion_edit'),
    path('promotion/delete/<int:pk>/', views.promotion_delete, name='promotion_delete'),
]
