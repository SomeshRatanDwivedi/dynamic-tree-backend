from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.tree_routes import router as tree_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tree_router, prefix="/api/tree", tags=["Tree"])
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}