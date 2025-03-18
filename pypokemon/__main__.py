from pypokemon import show_pokemon, select_pokemon, battle, luckypokemon

# Main Game Loop
def main():
    print("\n🌟 Welcome to the Pokémon Battle Game! 🌟")

    while True:
        print("\n🎮 Main Menu:")
        print("1️⃣ Show Pokémon")
        print("2️⃣ Select Pokémon and Battle")
        print("3️⃣ Get Your Lucky Pokémon")
        print("4️⃣ Quit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            show_pokemon()
        elif choice == "2":
            p1, p2 = select_pokemon()
            battle(p1, p2)
        elif choice == "3":
            print(luckypokemon())
        elif choice == "4":
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the game
if __name__ == "__main__":
    main()
