from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, joinedload

from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    def create_with_author(
        self, db: Session, *, obj_in: ItemCreate, author_id: int
    ) -> Item:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, author_id=author_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_author(
        self, db: Session, *, author_id: int, skip: int = 0, limit: int = 100
    ) -> List[Item]:
        return (
            db.query(self.model)
            .filter(Item.author_id == author_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_multi_public(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Item]:
        return (
            db.query(self.model)
            .options(joinedload(self.model.author))
            .offset(skip)
            .limit(limit)
            .all()
        )


item = CRUDItem(Item)
