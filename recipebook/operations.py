from database import connect_db

def add_recipe(name, ingredients, instructions):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO recipes (name, ingredients, instructions)
            VALUES (%s, %s, %s)
            RETURNING id;
        """, (name, ingredients, instructions))
        recipe_id = cursor.fetchone()[0]  
        conn.commit() 
        cursor.close()
        conn.close()
        return recipe_id
    else:
        print("Bağlantı sağlanamadı.")
        return None


def get_all_recipes():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recipes")
        recipes = cursor.fetchall()
        cursor.close()
        conn.close()
        return recipes
    
def get_recipe_by_id(recipe_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recipes WHERE id = %s", (recipe_id,))
        recipe = cursor.fetchone()
        cursor.close()
        conn.close()
        return recipe
    
def delete_recipe(recipe_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    cursor.close()
    conn.close()


if __name__== "__main__":
    add_recipe("Pancakes", "flour, eggs, milk", "Mix ingredients and cook on a griddle")
    recipes = get_all_recipes()
    for recipe in recipes:
        print(recipe)
