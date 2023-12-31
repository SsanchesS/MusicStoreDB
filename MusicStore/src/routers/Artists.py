from fastapi import APIRouter
from sql_base.models import ArtistsM
import resolvers.Artists

Artists_router = APIRouter()

@Artists_router.get('/{artist_id}')
def get_Artist(artist_id: int):
    artist = resolvers.Artists.get_Artist(artist_id)
    if artist is None:
        return {"code": 404, 'message': f"Artist with id {artist_id} not found"}
    return {"code": 201, "Artist": artist}

@Artists_router.post('/')
def new_Artist(artist: ArtistsM):
    new_id = resolvers.Artists.new_Artist(artist)
    return {"code": 201, "id": new_id}

@Artists_router.put('/{artist_id}')
def update_Artist(artist_id: int, artist: ArtistsM):
    upd_id = resolvers.Artists.upd_Artist(artist_id, artist)
    if upd_id is None:
        return {"code": 404, 'message': f"Artist with id {artist_id} not found"}
    return {"code": 201, "Update Artist": upd_id}
    
@Artists_router.delete('/{artist_id}')
def delete_Artist(artist_id: int):
    del_id = resolvers.Artists.del_Artist(artist_id)
    if del_id is None:
        return {"code": 404, 'message': f"Artist with id {artist_id} not found"}
    return {"code": 201, "Delete Artist": del_id}