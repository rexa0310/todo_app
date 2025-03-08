from bson import ObjectId
from database import todo_collection
from models import TodoCreate,TodoUpdate

def todo_helper(todo)->dict:
    return{
    "_id":str(todo["_id"]),
        "title":todo['title'],
        "description":todo.get("description")
    }

async def create_todo(todo_data:TodoCreate):
    todo=await todo_collection.insert_one(todo_data.dict())
    created_todo=await todo_collection.find_one({"_id":todo.inserted_id})
    return todo_helper(created_todo)

async def get_all_todos():
    todos=[]
    async for todo in todo_collection.find():
        todos.append(todo_helper(todo
        ))
        return todos

async def get_todo_by_id(todo_id:str):
    todo=await todo_collection.find_one({"_id":ObjectId(todo_id)})
    if todo:
        return todo_helper(todo)
    return None

async def update_todo(todo_id:str, update_data:TodoUpdate):
    update_data_dict={k:v for k,v in update_data.dict().items() if v is not None}
    if not update_data_dict:
        return None

    updated_todo=await todo_collection.find_one_and_updaye(
        {"_id":ObjectId(todo_id)},
        {"$set":update_data_dict},
        return_document=True
    )

    if updated_todo:
        return todo_helper(updated_todo)
    return None

async def delete_todo(todo_id:str):
    result=await todo_collection.delete_one({"_id":ObjectId(todo_id)})
    return result.deleted_count>0

