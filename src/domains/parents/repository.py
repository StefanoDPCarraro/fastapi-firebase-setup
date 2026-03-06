from typing import Any

from firebase_admin import firestore

from .irepository import IParentRepository


class FirebaseParentRepository(IParentRepository):
    def __init__(self) -> None:
        self.db = firestore.client()
        self.collection = "parents"

    def save(self, data: dict[str, Any]) -> dict[str, Any]:
        doc_id = data["id"]
        self.db.collection(self.collection).document(doc_id).set(data)
        return data

    def get_by_id(self, parent_id: str) -> dict[str, Any] | None:
        doc = self.db.collection(self.collection).document(parent_id).get()
        return doc.to_dict() if doc.exists else None
