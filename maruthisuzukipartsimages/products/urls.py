from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from products import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('product/',views.product, name="product"),
    path('product_view/<int:pk>',views.product_view, name="product_view"),
    path('base/',views.base, name="base"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('search/',views.search, name="search"),
    path('category/<str:foo>',views.category, name="category"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Include the following line to serve media files in development.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)