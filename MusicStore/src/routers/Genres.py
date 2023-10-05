from fastapi import APIRouter
from sql_base.models import GenresM
import resolvers.Genres

Genres_router = APIRouter()

@Genres_router.get('/')
def get_Genress():
    return f'Response: {{text: Страница со списком Genres}}'

@Genres_router.get('/{Genres_id}')
def get_Genres(Genres_id: int):
    get_id = resolvers.Genres.get_Genre(Genres_id)
    return f'Genres: {get_id}'

@Genres_router.post('/')
def new_Genres(Genres: GenresM):
    new_id = resolvers.Genres.new_Genre(Genres)
    return f'{{code: 201, id: {new_id}}}'

@Genres_router.put('/{Genres_id}')
def update_Genres(Genres_id: int,Genres: GenresM):
    upd_id = resolvers.Genres.upd_Genre(Genres_id,Genres)
    return f'Update Genres {upd_id}'

@Genres_router.delete('/{Genres_id}')
def delete_Genres(Genres_id: int):
    del_id = resolvers.Genres.del_Genre(Genres_id)
    return f'Delete Genres {del_id}'