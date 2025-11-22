from sqlalchemy.orm import Session
from app.api.services.tree_services import TreeService

def get_tree(db: Session):
    return TreeService.get_tree_structure(db)

def update_tree(db: Session, tree_data: dict):
    return TreeService.update_tree_structure(db, tree_data)  

def save_tree(db: Session, tree_data: dict):
  return TreeService.save_new_tree_structure(db, tree_data)  


def delete_tree(db: Session, tree_id: int):
   return TreeService.delete_tree_structure(db, tree_id)


