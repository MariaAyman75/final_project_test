from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urls.py
# from django.urls import path
# from .views import menu_items

# urlpatterns = [
#     path('api/menu-items/', menu_items, name='menu_items'),
# ]
