from operations import add_recipe, get_all_recipes, delete_recipe  

def menu():
    print("\n--- Recipe Book ---")
    print("1. List Recipes")
    print("2. Add a New Recipe")
    print("3. Delete a Recipe")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        recipes = get_all_recipes()
        if recipes:
            for recipe in recipes:
                print(f"ID: {recipe[0]}, Name: {recipe[1]}, Ingredients: {recipe[2]}, Instructions: {recipe[3]}")
        else:
            print("No recipes found.")

    elif choice == "2":
        name = input("Enter the name of recipe:")
        ingredients = input("Enter the ingredients:")
        instructions = input(" Enter the instructions:")
        recipe_id = add_recipe(name,ingredients,instructions)
        print(f"Recipe added! with ID: {recipe_id}") 

    elif choice == "3":
        recipe_id = input("Enter the ID of the recipe you want to delete:")
        delete_recipe(recipe_id)
        print("Recipe deleted!")

    elif choice == "4":
        print("Exiting...")
        return
    
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        menu()

if __name__ == "__main__":
    while True:
        main()

    
    


