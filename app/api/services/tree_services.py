from sqlalchemy.orm import Session
from sqlalchemy import func
from app.api.models.tree_model import Tree

class TreeService:
  @staticmethod
  def get_tree_structure(db:Session):
      trees = db.query(Tree).order_by(Tree.id).all()
      transformed_data = [tree.treeStructure for tree in trees]
      return transformed_data
    
  @staticmethod
  def update_tree_structure(db: Session, tree_data: dict):
      # Assuming tree_data contains an 'id' to identify which tree to update
      tree_id = tree_data.get("id")
      tree = db.query(Tree).filter(Tree.id == tree_id).first()
      if tree:
          tree.treeStructure = tree_data
          db.commit()
          db.refresh(tree)
          return tree.treeStructure
      else:
          return None

  @staticmethod
  def save_new_tree_structure(db: Session, tree_data: dict):
      new_tree = Tree(treeStructure=tree_data)
      db.add(new_tree)
      db.flush() 
      
      tree_data_with_id = {"id": str(new_tree.id), **tree_data}
      new_tree.treeStructure = tree_data_with_id
      
      db.commit()
      db.refresh(new_tree)
      return tree_data_with_id


  @staticmethod
  def delete_tree_structure(db: Session, tree_id: int):
      tree = db.query(Tree).filter(Tree.id == tree_id).first()
      if tree:
          db.delete(tree)
          db.commit()
          return {"message": f"Tree with id {tree_id} deleted successfully."}
      else:
          return {"message": f"Tree with id {tree_id} not found."}  
  