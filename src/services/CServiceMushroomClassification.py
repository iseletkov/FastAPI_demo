from ..model.CMushroom import CMushroom
from tensorflow import keras
import numpy as np
import pandas as pd


# *******************************************************************************************************
# * Сервис для классификации грибов на съедобные и несъедобные.                                         *
# * @author Селетков И.П. 2023 0219.                                                                    *
# *******************************************************************************************************
class CServiceMushroomClassification:
    # ***************************************************************************************************
    # * Конструктор.                                                                                    *
    # ***************************************************************************************************
    def __init__(self):
        # Загрузка нейросетевой модели из файла.
        self.model = keras.models.load_model("model_mushrooms.h5")
        # Список используемых для классификации признаков.
        self.features = [
            "cap_surface",
            "bruises",
            "gill_attachment",
            "gill_spacing",
            'gill_size',
            "gill_color",
            "stalk_root",
            "stalk_surface_above_ring",
            "ring_type",
            "population"
        ]
        # Словарь для преобразования категориальных признаков.
        self.m_dict = {
            "cap_shape":{"x":0, "b":1, "s":2, "f":3, "k":4, "c":5},
            "cap_surface":{"s":0, "y":1, "f":2, "g":3},
            "cap_color":{"n":0,"y":1, "w":2, "g":3, "e":4, "p":5, "b":6, "u":7, "c":8, "r":9},
            "bruises":{"t":0, "f":1},
            "odor":{"p":0, "a":1, "l":2, "n":3, "f":4, "c":5, "y":6, "s":7, "m":8},
            "gill_attachment":{"f":0, "a":1},
            "gill_spacing":{"c":0, "w":1},
            "gill_size":{"n":0, "b":1},
            "gill_color":{"k":0, "n":1, "g":2, "p":3, "w":4, "h":5, "u":6, "e":7, "b":8, "r":9, "y":10, "o":11},
            "stalk_shape":{"e":0, "t":1},
            "stalk_root":{"e":0, "c":1, "b":2, "r":3, "?":4},
            "stalk_surface_above_ring":{"s":0, "f":1, "k":2, "y":3},
            "stalk_surface_below_ring":{"s":0, "f":1, "y":2, "k":3},
            "stalk_color_above_ring":{"w":0, "g":1, "p":2, "n":3, "b":4, "e":5, "o":6, "c":7, "y":8},
            "stalk_color_below_ring":{"w":0, "p":1, "g":2, "b":3, "n":4, "e":5, "y":6, "o":7, "c":8},
            "veil_type":{"p":0},
            "veil_color":{"w":0, "n":1, "o":2, "y":3},
            "ring_number":{"o":0, "t":1, "n":2},
            "ring_type":{"p":0, "e":1, "l":2, "f":3, "n":4},
            "spore_print_color":{"k":0, "n":1, "u":2, "h":3, "w":4, "r":5, "o":6, "y":7, "b":8},
            "population":{"s":0, "n":1, "a":2, "v":3, "y":4, "c":5},
            "habitat":{"u":0, "g":1, "m":2, "d":3, "p":4, "w":5, "l":6},
            "class":{"p":0, "e":1}
        }

    # ***************************************************************************************************
    # * Определение класса гриба mushroom.                                                              *
    # * @param mushroom - информация о грибе для классификации.                                         *
    # ***************************************************************************************************
    def predict(self, mushroom: CMushroom):
        # Создаём набор данных из данных гриба.
        df = pd.DataFrame([mushroom.dict()])
        # Заменяем категориальные признаки.
        df = df.replace(self.m_dict)
        # Оставляем только нужные признаки.
        df = df[self.features]
        # Осуществление классификации с помощью нейросетевой модели.
        test = np.round(self.model.predict(df.iloc[[0]])[:, 0])
        # Интерпретация результата.
        print(test)
        if test[0] == 1:
            return "Съедобный"
        return "Ядовитый"