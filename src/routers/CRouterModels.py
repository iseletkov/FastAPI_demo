from fastapi import APIRouter
from ..services.CServiceModels import my_sum
from ..model.CMushroom import CMushroom
from ..services.CServiceMushroomClassification import CServiceMushroomClassification

# *******************************************************************************************************
# * Роутер для обработки HTTP REST запросов к пути /models.                                             *
# * @author Селетков И.П. 2023 0218.                                                                    *
# *******************************************************************************************************
router = APIRouter(
    prefix="/models",
    tags=["models"],
    responses={404: {"description": "Not found"}}
)

serviceMushrooms = CServiceMushroomClassification()


@router.get("/")
async def about():
    return "Здесь собраны методы для вызова моделей обработки данных"


@router.get("/sum")
def m_sum(x: float = 0, y: float = 0):
    return my_sum(x, y)


# *******************************************************************************************************
# * Классификация гриба.                                                                                *
# *******************************************************************************************************
@router.post("/mushroom-classification")
def mushroom_classification(mushroom: CMushroom):
    return serviceMushrooms.predict(mushroom)
