from rest_framework import serializers
from  .models import Capital

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = ('id','name','state','pin')