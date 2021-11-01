from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create-listing", views.create_listing, name="create-listing"),
    path("listing/<int:listing_id>", views.listing_page, name="listing"),
    path("listing-normal", views.listing_normal, name="listing-normal"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories-list", views.categories, name="categories-list"),
    path("category/<str:name>", views.category, name="category")
]

app_name = 'commerce'