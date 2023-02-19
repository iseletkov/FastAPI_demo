from fastapi import FastAPI
from routers import CRouterModels

# *******************************************************************************************************
# * Основной файл приложения.                                                                           *
# * @author Селетков И.П. 2023 0218.                                                                    *
# *******************************************************************************************************
app = FastAPI()

app.include_router(CRouterModels.router)


# *******************************************************************************************************
# * Технический запрос, позволяющий понять внешним службам, что данный сервис работает.                 *
# *******************************************************************************************************
@app.get("/test")
def read_root():
    return 1


