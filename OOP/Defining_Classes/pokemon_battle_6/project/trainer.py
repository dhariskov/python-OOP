from Defining_Classes.pokemon_battle_6.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, pokemon=[]):
        self.name = name
        self.pokemon = pokemon

    def add_pokemon(self, new_pokemon: Pokemon):
        for p in self.pokemon:
            if p.name == new_pokemon.name:
                return "This pokemon is already caught"
        self.pokemon.append(new_pokemon)
        return f"Caught {Pokemon.pokemon_details(new_pokemon)}"

    def release_pokemon(self, pokemon_name):
        for p in self.pokemon:
            if pokemon_name == p.name:
                self.pokemon.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        temp = ""
        for p in self.pokemon:
            temp += f"- {Pokemon.pokemon_details(p)}\n"
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n{temp}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
