from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Phan_quyen
from schemas import PhanQuyenBase, PhanQuyen



def create_phan_quyen(db: Session, phan_quyen: PhanQuyen):
    db_phan_quyen = Phan_quyen(**phan_quyen.dict())
    db.add(db_phan_quyen)
    db.commit()
    db.refresh(db_phan_quyen)
    return db_phan_quyen
def get_phan_quyen(db: Session, phan_quyen_id: str = None, phan_quyen_name: str = None):
    if phan_quyen_id:
        db_phan_quyen = db.query(Phan_quyen).filter(Phan_quyen.id == phan_quyen_id).first()
    elif phan_quyen_name:
        db_phan_quyen = db.query(Phan_quyen).filter(Phan_quyen.Ten_chuc_vu.ilike(f"%{phan_quyen_name}%")).all()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên phân quyền")
    if db_phan_quyen is None:
        raise HTTPException(status_code=404, detail="Phân quyền không tồn tại")
    return db_phan_quyen

def get_all_phan_quyen(db: Session):
    """
    Lấy danh sách tất cả phân quyền.
    """
    return db.query(Phan_quyen).order_by(Phan_quyen.id).all()

def delete_phan_quyen(db: Session, phan_quyen_id: str = None):
    """
    Xóa phân quyền theo ID.
    """
    if phan_quyen_id:
        db_phan_quyen = db.query(Phan_quyen).filter(Phan_quyen.id == phan_quyen_id).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID để xóa phân quyền")
    if db_phan_quyen is None:
        raise HTTPException(status_code=404, detail="Phân quyền không tồn tại")
    db.delete(db_phan_quyen)
    db.commit()
    return {"message": "Phân quyền đã được xóa thành công"}

def update_phan_quyen(db: Session, phan_quyen_id: str, phan_quyen: PhanQuyenBase):
    db_phan_quyen = db.query(Phan_quyen).filter(Phan_quyen.id == phan_quyen_id).first()
    if db_phan_quyen is None:
        raise HTTPException(status_code=404, detail="Phân quyền không tồn tại")
    for key, value in phan_quyen.model_dump().items():
        setattr(db_phan_quyen, key, value)
    db.commit()
    db.refresh(db_phan_quyen)
    return db_phan_quyen