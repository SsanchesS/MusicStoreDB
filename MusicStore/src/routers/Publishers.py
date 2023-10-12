from fastapi import APIRouter
from sql_base.models import PublishersM
import resolvers.Publishers

Publishers_router = APIRouter()

@Publishers_router.get('/{publisher_id}')
def get_Publisher(publisher_id: int):
    publisher = resolvers.Publishers.get_Publisher(publisher_id)
    if publisher is None:
        return {"code": 404, 'message': f"Publisher with id {publisher_id} not found"}
    return {"code": 201, "Publisher": publisher}

@Publishers_router.post('/')
def new_Publisher(publisher: PublishersM):
    new_id = resolvers.Publishers.new_Publisher(publisher)
    return {"code": 201, "id": new_id}


@Publishers_router.put('/{publisher_id}')
def update_Publisher(publisher_id: int, publisher: PublishersM):
    upd_id = resolvers.Publishers.upd_Publisher(publisher_id, publisher)
    if upd_id is None:
        return {"code": 404, 'message': f"Publisher with id {publisher_id} not found"}
    return {"code": 201, "Update Publisher": upd_id}

@Publishers_router.delete('/{publisher_id}')
def delete_Publisher(publisher_id: int):
    del_id = resolvers.Publishers.del_Publisher(publisher_id)
    if del_id is None:
        return {"code": 404, 'message': f"Publisher with id {publisher_id} not found"}
    return {"code": 201, "Delete Publisher": del_id}