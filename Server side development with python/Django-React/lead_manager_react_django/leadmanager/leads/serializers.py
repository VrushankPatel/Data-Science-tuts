from rest_framework import serializers
from leads.models import Lead

# Lead searializer
class LeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"