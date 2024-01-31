from .models import Subscriber,Campaign
from rest_framework import serializers

#Subscriber Serializer
class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


#Campaign Serializer
class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
