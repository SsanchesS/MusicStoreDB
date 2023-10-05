from fastapi import APIRouter

from sql_base.models import ArtistsM
import resolvers.Artists

Artists_router = APIRouter()

@Artists_router.get('/')
def get_Artists():
    return f'Response: {{text: Страница со списком Artist}}'

@Artists_router.get('/{Artist_id}')
def get_Artist(Artist_id: int):
    get_Artist1 = resolvers.Artists.get_Artist(Artist_id)
    return f'Artist: {get_Artist1}'

@Artists_router.post('/')
def new_Artist(Artist: ArtistsM):
    new_id = resolvers.Artists.new_Artist(Artist)
    return f'{{code: 201, id: {new_id}}}'

@Artists_router.put('/{Artist_id}')
def update_Artist(Artist_id:int,Artist: ArtistsM):
    upd_id = resolvers.Artists.upd_Artist(Artist_id,Artist)
    return f'Update Artist {upd_id}'

@Artists_router.delete('/{Artist_id}')
def delete_Artist(Artist_id: int):
    del_id = resolvers.Artists.del_Artist(Artist_id)
    return f'Delete Artist {del_id}'