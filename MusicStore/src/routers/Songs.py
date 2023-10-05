from fastapi import APIRouter
from sql_base.models import SongsM
import resolvers.Songs

Songs_router = APIRouter()

@Songs_router.get('/')
def get_Songs():
    return f'Response: {{text: Страница со списком Song}}'

@Songs_router.get('/{Song_id}')
def get_Song(Song_id: int):
    get_Song1 = resolvers.Songs.get_Song(Song_id)
    return f'Song: {get_Song1}'

@Songs_router.post('/')
def new_Song(Song: SongsM):
    new_id = resolvers.Songs.new_Song(Song)
    return f'{{code: 201, id: {new_id}}}'

@Songs_router.put('/{Song_id}')
def update_Song(Song_id:int,Song: SongsM):
    upd_id = resolvers.Songs.upd_Song(Song_id,Song)
    return f'Update Song {upd_id}'

@Songs_router.delete('/{Song_id}')
def delete_Song(Song_id: int):
    del_id = resolvers.Songs.del_Song(Song_id)
    return f'Delete Song {del_id}'