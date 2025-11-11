import random

from faker import Faker

faker = Faker("ru_RU")


def generate_entity_data() -> dict:
    """Генерирует случайные данные для использования сущностями.

    Функция генерирует:
    случайное название из трех слов, случайная поставленная метка 'verified',
    важные числа в виде списка из трех чисел от 1 до 99, дополнительная информация в виде текста длиной до 50 символов,
    случайное дополнительное число в диапазоне от 1 до 999."""
    return {
        "title": faker.sentence(nb_words=3),
        "verified": random.choice([True, False]),
        "important_numbers": random.sample(range(1, 100), 3),
        "addition": {
            "additional_info": faker.text(max_nb_chars=50),
            "additional_number": random.randint(1, 999)
        }
    }
