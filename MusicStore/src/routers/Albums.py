from fastapi import APIRouter
from sql_base.models import AlbumsM
import resolvers.Albums

Albums_router = APIRouter()

@Albums_router.get('/{album_id}')
def get_Album(album_id: int):
    album = resolvers.Albums.get_Album(album_id)
    if album is None:
        return {"code": 404, 'message': f"Album with id {album_id} not found"}
    return {"code": 201, "Album": album}

@Albums_router.post('/')
def new_Album(album: AlbumsM):
    new_id = resolvers.Albums.new_Album(album)
    return {"code": 201, "id": new_id}

@Albums_router.put('/{album_id}')
def update_Album(album_id: int, album: AlbumsM):
    upd_id = resolvers.Albums.upd_Album(album_id, album)
    if upd_id is None:
        return {"code": 404, 'message': f"Album with id {album_id} not found"}
    return {"code": 201, "Update Album": upd_id}

@Albums_router.delete('/{album_id}')
def delete_Album(album_id: int):
    del_id = resolvers.Albums.del_Album(album_id)
    if del_id is None:
        return {"code": 404, 'message': f"Album with id {album_id} not found"}
    return {"code": 201, "Delete Album": del_id}