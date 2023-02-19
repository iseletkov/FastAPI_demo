from pydantic import BaseModel

# *******************************************************************************************************
# * Класс для описания информации об одном грибе.                                                       *
# * @link Описание данных https://www.kaggle.com/datasets/uciml/mushroom-classification                 *
# * @author Селетков И.П. 2023 0219.                                                                    *
# *******************************************************************************************************
class CMushroom(BaseModel):
    cap_shape: str | None = None
    cap_surface: str | None = None
    cap_color: str | None = None
    bruises: str | None = None
    odor: str | None = None
    gill_attachment: str | None = None
    gill_spacing: str | None = None
    gill_size: str | None = None
    gill_color: str | None = None
    stalk_shape: str | None = None
    stalk_root: str | None = None
    stalk_surface_above_ring: str | None = None
    stalk_surface_below_ring: str | None = None
    stalk_color_above_ring: str | None = None
    stalk_color_below_ring: str | None = None
    veil_type: str | None = None
    veil_color: str | None = None
    ring_number: str | None = None
    ring_type: str | None = None
    spore_print_color: str | None = None
    population: str | None = None
    habitat: str | None = None