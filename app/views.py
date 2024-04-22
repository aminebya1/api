from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Location, Move, Pokemon, PokemonEggGroup, PokemonFormGeneration, PokemonMove, PokemonStat
from .serializers import LocationSerializer, MoveSerializer, PokemonSerializer, PokemonEggGroupSerializer, PokemonFormGenerationSerializer, PokemonMoveSerializer, PokemonStatSerializer

class LocationDetail(APIView):
    def get(self, request, id):
        location = Location.objects.get(id=id)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

class MoveDetail(APIView):
    def get(self, request, id):
        move = Move.objects.get(id=id)
        serializer = MoveSerializer(move)
        return Response(serializer.data)

class PokemonDetail(APIView):
    def get(self, request, id):
        pokemon = Pokemon.objects.get(id=id)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)



