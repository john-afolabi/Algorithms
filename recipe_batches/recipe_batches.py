#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    if set(recipe.keys()) != set(ingredients.keys()):
        return 0
    else:
        rec_values = list(recipe.values())
        ing_values = list(ingredients.values())
        div = [
            ing_values // rec_values
            for ing_values, rec_values in zip(ing_values, rec_values)
        ]
        return min(div)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}."
        .format(batches=recipe_batches(recipe, ingredients),
                ingredients=ingredients))
