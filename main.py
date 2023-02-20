with open('recipes.txt') as file:
    cook_book = {}
    for item in file:
        name_of_dish = item.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity,
                                'measure': measure
                                })
        file.readline()
        cook_book[name_of_dish] = ingredients

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    cook = {}
    for key, value in cook_book.items():
        if key in dishes:
            for elem in value:
                cook.setdefault(elem['ingredient_name'],
                                {'measure': elem['measure'], 'quantity': int(elem['quantity']) * person_count})
    return cook


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
