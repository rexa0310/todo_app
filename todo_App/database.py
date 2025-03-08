from motor.motor_asyncio import AsyncIOMotorClient

url="mongodb://localhost:27017/"
client=AsyncIOMotorClient(url)
database = client.todoapp
todo_collection = database.todos