from fastapi import FastAPI

from . import api


# tags_metadata = [
#     {
#         'name': 'auth',
#         'description': 'Авторизация и регистрация',
#     },
#     {
#         'name': 'user',
#         'description': 'Получение данных пользователей',
#     },
#     {
#         'name': 'wall',
#         'description': 'Получение записей',
#     },
# ]

app = FastAPI(
    title='Stratum',
    description='Сервис профилирования деятельности пользователей ВКонтакте',
    version='1.0.0',
    # openapi_tags=tags_metadata,
)

app.include_router(api.router)
