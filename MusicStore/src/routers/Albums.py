from fastapi import APIRouter

from sql_base.models import AlbumsM
import resolvers.Albums

Albums_router = APIRouter()

@Albums_router.get('/')
def get_Albums():
    return f'Response: {{text: Страница со списком Albums}}'

@Albums_router.get('/{Album_id}')
def get_Album(Album_id: int):
    get_Album1 = resolvers.Albums.get_Album(Album_id)
    return f'Album: {get_Album1}'

@Albums_router.post('/')
def new_Album(Album: AlbumsM):
    new_id = resolvers.Albums.new_Album(Album)
    return f'{{code: 201, id: {new_id}}}'

@Albums_router.put('/{Album_id}')
def update_Album(Album_id:int,Album: AlbumsM):
    upd_id = resolvers.Albums.upd_Album(Album_id,Album)
    return f'Update Album {upd_id}'

@Albums_router.delete('/{Album_id}')
def delete_Album(Album_id: int):
    del_id = resolvers.Albums.del_Album(Album_id)
    return f'Delete Album {del_id}'