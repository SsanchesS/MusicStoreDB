from fastapi import APIRouter, HTTPException
from sql_base.models import GenresM
import resolvers.Genres

Genres_router = APIRouter()

@Genres_router.get('/{genre_id}')
def get_Genre(genre_id: int):
    genre = resolvers.Genres.get_Genre(genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail=f"Genre with id {genre_id} not found")
    return {"Genre": genre}

@Genres_router.post('/')
def new_Genre(genre: GenresM):
    new_id = resolvers.Genres.new_Genre(genre)
    return {"code": 201, "id": new_id}

@Genres_router.put('/{genre_id}')
def update_Genre(genre_id: int, genre: GenresM):
    upd_id = resolvers.Genres.upd_Genre(genre_id, genre)
    if upd_id is None:
        raise HTTPException(status_code=404, detail=f"Genre with id {genre_id} not found")
    return {"Update Genre": upd_id}

@Genres_router.delete('/{genre_id}')
def delete_Genre(genre_id: int):
    del_id = resolvers.Genres.del_Genre(genre_id)
    if del_id is None:
        raise HTTPException(status_code=404, detail=f"Genre with id {genre_id} not found")
    return {"Delete Genre": del_id}