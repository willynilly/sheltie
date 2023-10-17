import os
import requests

from models.food import Food


class USDAFoodDataService:

    def list_foods(self) -> list[Food]:
        api_key: str = os.getenv('USDA_FOOD_DATA_CENTRAL_API_KEY')
        response = requests.get(
            'https://api.nal.usda.gov/fdc/v1/foods/list?dataType=Foundation,SR%20Legacy&pageSize=25&pageNumber=2&api_key=' + api_key)
        data = response.json()
        food_list: list[Food] = []
        for food_info in data:
            food = Food()
            food.info = food_info
            food_list.append(food)
        return food_list
