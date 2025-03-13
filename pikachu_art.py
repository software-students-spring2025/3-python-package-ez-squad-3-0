def print_pokemons(pokemon_name):
    if pokemon_name == "Bulbasaur":
        print("work in progress")
    elif pokemon_name == "Charmander":
        print("Work in progress, Charmander")
    elif pokemon_name == "Squirtle":
        print("Work in progress, Squirtle")
    else:
        print("404, Pokemon not Found")

def main():
    while True:
        pokemon = ["Bulbasaur", "Charmander", "Squirtle"]
        command = input("please enter a command:")
        if command == "display":
            for pokemons in pokemon:
                print_pokemons(pokemons)
        if command == "quit"
            break

if __name__ == "__main__":
    main()