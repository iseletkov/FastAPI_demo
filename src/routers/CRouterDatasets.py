from fastapi import APIRouter
from fastapi import UploadFile
import pandas as pd

# *******************************************************************************************************
# * Роутер для обработки HTTP REST запросов к пути /models.                                             *
# * @author Селетков И.П. 2023 0218.                                                                    *
# *******************************************************************************************************
router = APIRouter(
    prefix="/datasets",
    tags=["datasets"],
    responses={404: {"description": "Not found"}}
)

#serviceMushrooms = CServiceMushroomClassification()


@router.post("/upload/")
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    df = pd.read_excel(contents)
    print(df)
    return {"filename": file.filename}
