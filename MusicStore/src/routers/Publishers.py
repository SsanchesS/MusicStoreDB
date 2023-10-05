from fastapi import APIRouter
from sql_base.models import PublishersM
import resolvers.Publishers

Publishers_router = APIRouter()

@Publishers_router.get('/')
def get_Publisher():
    return f'Response: {{text: Страница со списком Publishers}}'

@Publishers_router.get('/{Publisher_id}')
def get_Publisher(Publisher_id: int):
    get_Publisher1 = resolvers.Publishers.get_Publisher(Publisher_id)
    return f'Publisher: {get_Publisher1}'

@Publishers_router.post('/')
def new_Publisher(Publisher: PublishersM):
    new_id = resolvers.Publishers.new_Publisher(Publisher)
    return f'{{code: 201, id: {new_id}}}'

@Publishers_router.put('/{Publisher_id}')
def update_Publisher(Publisher_id:int,Publisher: PublishersM):
    upd_id = resolvers.Publishers.upd_Publisher(Publisher_id,Publisher)
    return f'Update Publisher {upd_id}'

@Publishers_router.delete('/{Publisher_id}')
def delelte_Publisher(Publisher_id: int):
    del_id = resolvers.Publishers.del_Publisher(Publisher_id)
    return f'Delete Publisher {del_id}'