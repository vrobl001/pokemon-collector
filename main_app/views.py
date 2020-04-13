from django.shortcuts import render

from django.http import HttpResponse


class Pokemon:
    def __init__(self, name, pokemon_type, weakness, lvl, description):
        self.name = name
        self.pokemon_type = pokemon_type
        self.weakness = weakness
        self.lvl = lvl
        self.description = description


pokemon = [
    Pokemon('Bulbasaur', 'Grass', 'Fire', 1,
            "Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger."),
    Pokemon('Squirtle', 'Water', 'Electric', 1, "Squirtle's shell is not merely used for protection. The shell's rounded shape and the grooves on its surface help minimize resistance in water, enabling this Pokémon to swim at high speeds."),
    Pokemon('Charmander', 'Fire', 'Water', 1, "The flame that burns at the tip of its tail is an indication of its emotions. The flame wavers when Charmander is enjoying itself. If the Pokémon becomes enraged, the flame burns fiercely."),
]


def home(request):
    return HttpResponse('<h1>Hello<h1>')


def about(request):
    return render(request, 'about.html')


def pokemon_index(request):
    return render(request, 'pokemon/index.html', {'pokemon': pokemon})
