from fastapi import APIRouter, HTTPException
from sql_base.models import CopyrightsM
import resolvers.Copyrights

Copyrights_router = APIRouter()

@Copyrights_router.get('/{copyright_id}')
def get_Copyright(copyright_id: int):
    copyright = resolvers.Copyrights.get_Copyright(copyright_id)
    if copyright is None:
        raise HTTPException(status_code=404, detail=f"Copyright with id {copyright_id} not found")
    return {"Copyright": copyright}

@Copyrights_router.post('/')
def new_Copyright(copyright: CopyrightsM):
    new_id = resolvers.Copyrights.new_Copyright(copyright)
    return {"code": 201, "id": new_id}

@Copyrights_router.put('/{copyright_id}')
def update_Copyright(copyright_id: int, copyright: CopyrightsM):
    upd_id = resolvers.Copyrights.upd_Copyright(copyright_id, copyright)
    if upd_id is None:
        raise HTTPException(status_code=404, detail=f"Copyright with id {copyright_id} not found")
    return {"Update Copyright": upd_id}

@Copyrights_router.delete('/{copyright_id}')
def delete_Copyright(copyright_id: int):
    del_id = resolvers.Copyrights.del_Copyright(copyright_id)
    if del_id is None:
        raise HTTPException(status_code=404, detail=f"Copyright with id {copyright_id} not found")
    return {"Delete Copyright": del_id}