from sqlalchemy.orm import Session
from typing import Any, Dict, List
from shared.models.pengajuan import PengajuanMasjid


def _get_pk(model):
    """Get primary key column name for a model."""
    return list(model.__table__.primary_key.columns.keys())[0]


def create_record(db: Session, model, data: dict):
    """Generic create handler."""
    obj = model()
    for key, value in data.items():
        if hasattr(obj, key) and value is not None:
            setattr(obj, key, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_record(db: Session, model, pk_value, data: dict):
    """Generic update handler."""
    pk = _get_pk(model)
    obj = db.query(model).filter(getattr(model, pk) == pk_value).first()
    if not obj:
        return None
    for key, value in data.items():
        if hasattr(obj, key) and value is not None:
            setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_record(db: Session, model, pk_value):
    """Generic delete handler."""
    pk = _get_pk(model)
    obj = db.query(model).filter(getattr(model, pk) == pk_value).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True


def list_pengajuan(db: Session, page: int = 1, per_page: int = 10) -> tuple:
    q = db.query(PengajuanMasjid).order_by(PengajuanMasjid.id_pengajuan.desc())
    total = q.count()
    data = q.offset((page - 1) * per_page).limit(per_page).all()
    return data, total


def sync_masjid_detail_replace(
    db: Session,
    model,
    id_masjid: str,
    items: List[Dict[str, Any]],
    parent_field: str = "parent_id",
):
    """Replace all detail items for a masjid."""
    pk = _get_pk(model)
    # Delete existing
    db.query(model).filter(getattr(model, parent_field) == id_masjid).delete()
    # Insert new
    created = []
    valid_columns = [c.name for c in model.__table__.columns]
    for item in items:
        item[parent_field] = id_masjid
        filtered = {k: v for k, v in item.items() if k in valid_columns}
        obj = model(**filtered)
        db.add(obj)
        db.flush()
        created.append({pk: getattr(obj, pk)})
    return created
