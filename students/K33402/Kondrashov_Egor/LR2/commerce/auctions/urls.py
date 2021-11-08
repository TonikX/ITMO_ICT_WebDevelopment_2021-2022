from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.ListingList.as_view(), name="index"),
    path("login/", auth_views.LoginView.as_view(template_name='auctions/login.html'), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("register", views.register, name="register"),
    path('listing/create', views.CreateListing.as_view(), name='create_listing'),
    path('listing/<int:pk>/', views.ListingDetail.as_view(), name='listing_detail'),
    path('add_to_watchlist/<int:pk>',
         views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/<int:pk>',
         views.remove_from_watchlist, name='remove_from_watchlist'),
    path('watchlist', views.WatchListList.as_view(), name='watchlist'),
    path('new_bid/<int:pk>', views.new_bid, name='new_bid'),
    path('close_listing/<int:pk>', views.close_listing, name='close_listing'),
    path('make_comment/<int:pk>', views.make_comment, name='make_comment'),
    path('categories', views.CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>', views.ViewCategory.as_view(), name='view_category'),
]
