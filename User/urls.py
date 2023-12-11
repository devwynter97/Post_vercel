from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name = 'user-registration'),
    # path('register2/', views.register2, name = 'user-registration2'),
    path('update/', views.update, name = 'user-update'),
    path('signin/', views.signin, name = 'user-sign-in'),
    path('profile/',views.profile, name='user-profile'),
    path('add-review/',views.addReview, name='user-add-review'),
    path('delete-comment/<int:id>',views.delete_comment, name='user-delete-comment'),
    # path('update-comment/<int:id>/<str:comment>/',views.update_comment, name='user-update-comment')
]