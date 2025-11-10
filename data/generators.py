import random

from faker import Faker

faker = Faker("ru_RU")


def generate_entity_data():
    return {
        "title": faker.sentence(nb_words=3),
        "verified": random.choice([True, False]),
        "important_numbers": random.sample(range(1, 100), 3),
        "addition": {
            "additional_info": faker.text(max_nb_chars=50),
            "additional_number": random.randint(1, 999)
        }
    }
