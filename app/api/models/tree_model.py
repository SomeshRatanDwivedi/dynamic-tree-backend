from sqlalchemy import Column, Integer, JSON
from app.db.database  import Base

class Tree(Base):
    __tablename__ = "tree"

    id = Column(Integer, primary_key=True, index=True)
    treeStructure = Column(JSON)
