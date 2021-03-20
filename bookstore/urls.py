from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookstore import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'auther', views.AuthorViewSet)
router.register(r'book', views.BookViewSet)
router.register(r'bookinstance', views.BookInstanceViewSet)
router.register(r'users', views.UserViewSet)

router.register(r'groups', views.GroupViewSet)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]