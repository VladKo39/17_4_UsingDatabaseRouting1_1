from fastapi import APIRouter

router=APIRouter(prefix='/task',tags=['task'])

@router.get('/')
async def all_tasks():
    pass

@router.get('/task_id')
async def all_tasks():
    pass

@router.post('/create')
async def creat_tasks():
    pass

@router.put('/update')
async def update_tasks():
    pass

@router.delete('/delete')
async def delete_tasks():
    pass

