from fastapi import APIRouter
from sql_base.models import CopyrightsM
import resolvers.Copyrights

Copyrights_router = APIRouter()

@Copyrights_router.get('/')
def get_Copyrights():
    return f'Response: {{text: Страница со списком Copyright}}'

@Copyrights_router.get('/{transaction_code}')
def get_Copyright(transaction_code: int):
    get_Copyright1 = resolvers.Copyrights.get_Copyright(transaction_code)
    return f'Copyright: {get_Copyright1}'

@Copyrights_router.post('/')
def new_Copyright(Copyright: CopyrightsM):
    new_transaction_code = resolvers.Copyrights.new_Copyright(Copyright)
    return f'{{code: 201, id: {new_transaction_code}}}'

@Copyrights_router.put('/{transaction_code}')
def update_Copyright(transaction_code:int,Copyright: CopyrightsM):
    upd_transaction_code = resolvers.Copyrights.upd_Copyright(transaction_code,Copyright)
    return f'Update Copyright {upd_transaction_code}'

@Copyrights_router.delete('/{transaction_code}')
def delete_Copyright(transaction_code: int):
    del_transaction_code = resolvers.Copyrights.del_Copyright(transaction_code)
    return f'Delete Copyright {del_transaction_code}'