from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Planet, Universe
from .serializers import PlanetSerializer, UniverseSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    @action(detail= False)
    def by_category(self, request):
        universe = self.request.query_params.get('universe', None)
        products = Planet.objects.filter(universe = universe)
        serializer = PlanetSerializer(products, many=True)
        return Response(serializer.data)

class UniverseViewSet(viewsets.ModelViewSet):
    queryset = Universe.objects.all()
    serializer_class = UniverseSerializer
