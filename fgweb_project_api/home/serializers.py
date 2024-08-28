from rest_framework.serializers import ModelSerializer
from home.models import NavModel, BannerModel

class NavSerializer(ModelSerializer):
    class Meta():
        model = NavModel
        # fields = '__all__'
        fields = ['name', 'link', 'is_http']
        
class BannerSerializer(ModelSerializer):
    class Meta():
        model = BannerModel
        fields = ['image', 'name', 'link', 'is_http']