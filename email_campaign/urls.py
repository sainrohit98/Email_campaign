from django.urls import path, include
from rest_framework import routers
from .views import SubscriberViewSet, CampaignViewSet

router = routers.DefaultRouter()
router.register(r'subscribers', SubscriberViewSet)
router.register(r'campaigns', CampaignViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

