from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('users', views.show_users),
    path('admins', views.show_admins),
    path('promote/<int:user_id>', views.promote_user),
    path('demote/<int:user_id>', views.demote_admin),
    path('delete_user/<int:user_id>', views.delete_user),
]
