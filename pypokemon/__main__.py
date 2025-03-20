from . import show_pokemon, select_pokemon, battle, luckypokemon, pokemon_data, effectiveness, pokemon_ascii

# Main Game Loop
def main():
    print("\n Welcome to the Pokemon Battle Game! ")

    while True:
        print("\n Main Menu:")
        print("1. Show Pokemon")
        print("2. Select Pokemon and Battle")
        print("3. Get Your Lucky Pokemon")
        print("4. Quit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            show_pokemon()
        elif choice == "2":
            p1, p2 = select_pokemon()
            battle(p1, p2)
        elif choice == "3":
            print(luckypokemon())
        elif choice == "4":
            print("\nGoodbye! ")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the game
if __name__ == "__main__":
    main()
