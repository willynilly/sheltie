from models.environment import Environment
from models.food import Food
from models.sheep import Sheep
from models.sheltie import Sheltie
from services.usda_food_data_service import USDAFoodDataService


if __name__ == '__main__':

    environment = Environment()

    linus = Sheltie()
    linus.name = "Linus"
    linus.weight = 23
    environment.agents.append(linus)

    sirius = Sheltie()
    sirius.name = "Sirius"
    sirius.weight = 23
    environment.agents.append(sirius)

    sheep_count = 2
    for i in range(sheep_count):
        sheep = Sheep()
        sheep.name = 'Sheep ' + str(i)
        environment.agents.append(sheep)

    time_steps = 100
    environment.update(time_steps=time_steps)

    # food_service = USDAFoodDataService()
    # food_list: list[Food] = food_service.list_foods()

    # print(food_list)
