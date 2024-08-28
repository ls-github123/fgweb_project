from rest_framework.serializers import ModelSerializer
from home.models import NavModel

class NavSerializer(ModelSerializer):
    class Meta():
        model = NavModel
        # fields = '__all__'
        fields = ['name', 'link', 'is_http']