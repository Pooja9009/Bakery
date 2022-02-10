from django.urls import path
from . import views

urlpatterns = [
    path('category_form', views.category_form, name='category_form'),
    path('get_category', views.get_category, name='get_category'),
    path('delete_category/<int:category_id>', views.delete_category, name='delete_category'),
    path('update_category/<int:category_id>', views.update_category, name='update_category'),

    path('cake_form', views.cake_form),
    path('get_cake', views.get_cake),
    path('delete_cake/<int:cake_id>', views.delete_cake),
    path('update_cake/<int:cake_id>', views.update_cake),

    path('seller_form', views.seller_form),
    path('get_seller', views.get_seller),
    path('delete_seller/<int:cake_id>', views.delete_seller),
    path('update_seller/<int:cake_id>', views.update_seller),

    path('show_categories', views.show_categories, name='show_categories'),
    path('show_cakes/<int:category_id>', views.show_cakes),

    path('about_us', views.about_us, name='about_us'),
    # path('contact_us', views.contact_us),
    path('contact_us', views.contact_form, name='contact_us'),
    path('get_message', views.get_message),
    path('delete_message/<int:message_id>', views.delete_message),

    path('add_to_cart/<int:cake_id>', views.add_to_cart),
    # path('addcart/<int:seller_id>', views.addcart),
    path('mycart', views.show_cart_items),
    path('remove_cart/<int:cart_id>', views.remove_cart),

    path('add_to_wishlist/<int:cake_id>', views.add_to_wishlist),
    path('wishlist', views.show_wishlist_items),
    path('remove_wishlist/<int:wishlist_id>', views.remove_wishlist),

    path('order_form/<int:cart_id>/<int:cake_id>', views.order_form),
    path('my_orders', views.my_order),
    path('get_order', views.get_order),
    path('update_order/<int:order_id>', views.update_order),

    path('esewa_verify', views.esewa_verify),
]
