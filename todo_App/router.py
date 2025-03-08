from fastapi import APIRouter, HTTPException, status
from models import TodoCreate, TodoUpdate, TodoResponse
from utility import create_todo, get_all_todos, get_todo_by_id, update_todo, delete_todo


router=APIRouter()

@router.post("/", response_model=TodoResponse)
async def create_todo_route(todo:TodoCreate):
    return await create_todo(todo)

@router.get("/", response_model=list[TodoResponse])
async def get_todos_route():
    return await get_all_todos()

@router.get("/{todo_id}",response_model=TodoResponse)
async def get_todo_route(todo_id: str):
    todo = await get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo Not found")
    return todo

@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo_route(todo_id: str, todo: TodoUpdate):
    updated_todo = await update_todo(todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return updated_todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo_route(todo_id: str):
    deleted = await delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")