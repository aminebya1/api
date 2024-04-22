from django.urls import path
from .views import LocationDetail, MoveDetail, PokemonDetail

urlpatterns = [
    path('api/locations/<int:id>/', LocationDetail.as_view()),
    path('api/moves/<int:id>/', MoveDetail.as_view()),
    path('api/pokemons/<int:id>/', PokemonDetail.as_view()),
    # Define other URLs for different endpoints
]
