from rest_framework.serializers import ModelSerializer
from home.models import NavModel

class NavSerializer(ModelSerializer):
    class Meta():
        model = NavModel
        fields = '__all__'