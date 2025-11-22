from fastapi import APIRouter,Depends
from  app.api.controllers.tree_controllers import get_tree, update_tree,save_tree,delete_tree
from sqlalchemy.orm import Session
from app.db.session import get_db
from typing import Dict

router = APIRouter()


@router.get("/")
def get_tree_structure(db: Session = Depends(get_db)):
    return get_tree(db)


@router.put("/update-tree")
def update_tree_structure(request:Dict, db: Session = Depends(get_db)):
    return update_tree(db, request)


@router.post("/save-new-tree")
def save_tree_structure(request:Dict, db: Session = Depends(get_db)):
    return save_tree(db, request)

@router.delete("/delete-tree/{id}")
def delete_tree_structure(id:int, db: Session = Depends(get_db)):
    return delete_tree(db, id)  