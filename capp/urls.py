from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('category',views.category,name='category'),
    path('add_category',views.add_category,name='add_category'),
    
    path('add_product',views.add_product,name='add_product'),
    path('add_productdb',views.add_productdb,name='add_productdb'),
    path('product_view',views.product_view,name='product_view'),
    path('login1',views.login1,name='login1'),
    path('u_a_login',views.u_a_login,name='u_a_login'),
    path('signup',views.signup,name='signup'),
    path('usercreate',views.usercreate,name='usercreate'),
    
    path('mens',views.mens,name='mens'),
    path('category_page/<int:pk>',views.category_page,name='category_page'),

    path('user_details',views.user_details,name='user_details'),
    path('delete_user/<int:user_id>',views.delete_user,name='delete_user'),
    path('delete_product/<int:product_id>',views.delete_product,name='delete_product'),
    path('cart_details/<int:id>',views.cart_details,name='cart_details'),
    path('cart',views.cart,name='cart'),
    path('decrease_quantity/<int:id>',views.decrease_quantity,name='decrease_quantity'),
    path('increase_quantity/<int:id>',views.increase_quantity,name='increase_quantity'),
    path('removecart/<int:id>',views.removecart,name='removecart'),

    

    
]