from .models import Planet, Universe
from rest_framework import serializers

class PlanetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Planet
		fields = ('id', 'name', 'universe', 'description', 'price')
		#fields = '__all__'

class UniverseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Universe
		fields = '__all__'