import json
import os

from logging_config import setup_logger
from src.classes import Category, Product

path_logger = os.path.join(os.getcwd(), "log")
os.makedirs(path_logger, exist_ok=True)
logger = setup_logger("utils", f"{path_logger}/utils.txt")


def read_json(path: str) -> dict | list:
    """Функция для считывания данных json-файла и преобразования в список словарей"""

    logger.info("Началось считывание json-файла")
    full_path = os.path.abspath(path)
    if os.path.exists(full_path):
        try:
            with open(full_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            logger.info("Считывание успешно завершено!")
            return data
        except json.JSONDecodeError:
            logger.error("Файл содержит некорректные данные")
            return []
    else:
        logger.error("Файл не существует")
        return []


def create_objects_from_json(data: dict | list) -> list:
    """Функция, которая пробегает по списку словарей и создаёт список экземпляров классов и подклассов внутри них"""

    logger.info("Началось преобразование списка словарей в список экземпляров классов")
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    logger.info("Преобразование успешно завершено!")
    return categories
