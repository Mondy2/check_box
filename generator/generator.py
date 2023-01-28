import random

from data.data import Person
from faker import Faker



faker_ru = Faker('ru_RU')
Faker.seed()










def generator_person():
    yield Person(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age =random.randint(1000000000,9999999999),
    )
