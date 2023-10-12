from fastapi import APIRouter
from sql_base.models import SongsM
import resolvers.Songs

Songs_router = APIRouter()

@Songs_router.get('/{song_id}')
def get_Song(song_id: int):
    song = resolvers.Songs.get_Song(song_id)
    if song is None:
        return {"code": 404, 'message': f"Song with id {song_id} not found"}
    return {"code": 201, "Song": song}

@Songs_router.post('/')
def new_Song(song: SongsM):
    new_id = resolvers.Songs.new_Song(song)
    return {"code": 201, "id": new_id}

@Songs_router.put('/{song_id}')
def update_Song(song_id: int, song: SongsM):
    upd_id = resolvers.Songs.upd_Song(song_id, song)
    if upd_id is None:
        return {"code": 404, 'message': f"Song with id {song_id} not found"}
    return {"code": 201, "Update Song": upd_id}

@Songs_router.delete('/{song_id}')
def delete_Song(song_id: int):
    del_id = resolvers.Songs.del_Song(song_id)
    if del_id is None:
        return {"code": 404, 'message': f"Song with id {song_id} not found"}
    return {"code": 201, "Delete Song": del_id}