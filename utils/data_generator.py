from faker import Faker

# Инициализируем Faker (можно указать язык, но для email лучше оставить английский)
fake = Faker()

def generate_random_user():
    """
    Утилита для генерации случайных данных пользователя.
    Возвращает словарь с email и паролем.
    """
    return {
        "email": fake.email(),
        "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True)
    }