from fastapi import FastAPI, Depends
import models
from database import engine
from routers import auth, todos, address, users
from starlette.staticfiles import StaticFiles, RedirectResponse
from starlette import status


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return RedirectResponse("/todos", status_code=status.HTTP_302_FOUND)

app.include_router(auth.router)  # included this so that auth is also in the same application
app.include_router(todos.router)  # included as all our todos functionality is moved to another file and set as router
# app.include_router(address.router)
app.include_router(users.router)

# Moving below commented code to routers.todos.py
# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()
#
#
# class Todo(BaseModel):
#     title: str
#     description: Optional[str]
#     priority: int = Field(gt=0, lt=6, description="Priority must be between 1 and 5")
#     complete: bool
#
#
# @app.get("/")
# async def read_database(db: Session = Depends(get_db)):
#     return db.query(models.Todos).all()
#
#
# @app.get("/todos/user")
# async def read_all_by_user(user: dict = Depends(get_current_user),
#                            db: Session = Depends(get_db)):
#     # print(user.get("id"))
#     if not user:
#         raise get_user_exception()
#     return db.query(models.Todos)\
#         .filter(models.Todos.owner_id == user.get("Id")).all()
#
#
# @app.get("/todo/{todo_id}")
# async def read_todo(todo_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
#     if not user:
#         raise get_user_exception()
#     todo_model = db.query(models.Todos)\
#         .filter(models.Todos.id == todo_id)\
#         .filter(models.Todos.owner_id == user.get("Id"))\
#         .first()
#     if todo_model:
#         return todo_model
#     raise http_exception()
#
#
# @app.post("/")
# async def create_todo(todo: Todo,
#                       user: dict = Depends(get_current_user),
#                       db: Session = Depends(get_db)):
#     if not user:
#         raise get_user_exception()
#     todo_model = models.Todos()
#     todo_model.title = todo.title
#     todo_model.description = todo.description
#     todo_model.priority = todo.priority
#     todo_model.complete = todo.complete
#     todo_model.owner_id = user.get("Id")
#     db.add(todo_model)
#     db.commit()
#     return successful_response(201)
#
#
# @app.put("/{todo_id}")
# async def update_todo(todo_id: int,
#                       todo: Todo,
#                       user: dict = Depends(get_current_user),
#                       db: Session = Depends(get_db)):
#     if not user:
#         raise get_user_exception()
#
#     todo_model = db.query(models.Todos)\
#         .filter(models.Todos.id == todo_id)\
#         .filter(models.Todos.owner_id == user.get("Id"))\
#         .first()
#     if todo_model:
#         todo_model.title = todo.title
#         todo_model.description = todo.description
#         todo_model.priority = todo.priority
#         todo_model.complete = todo.complete
#         db.add(todo_model)
#         db.commit()
#         return successful_response(200)
#     raise http_exception()
#
#
# @app.delete("/todo/{todo_id}")
# async def delete_todo(todo_id: int,
#                       user: dict = Depends(get_current_user),
#                       db: Session = Depends(get_db)):
#     if not user:
#         raise get_user_exception()
#     todo_model = db.query(models.Todos)\
#         .filter(models.Todos.owner_id == user.get("Id"))\
#         .filter(models.Todos.id == todo_id)\
#         .first()
#     if not todo_model:
#         raise http_exception()
#     db.query(models.Todos).filter(models.Todos.id == todo_id).delete()
#     db.commit()
#     return successful_response(200)
#
#
# def successful_response(status_code: int):
#     return {"Status Code": status_code, "Transaction": "Successful"}
#
#
# def http_exception():
#     return HTTPException(status_code=404, detail="Todo not found")
