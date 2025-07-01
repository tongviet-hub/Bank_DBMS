from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Loai_tien_te
from schemas import LoaiTienTeBase, LoaiTienTe
def create_loai_tien_te(db: Session, loai_tien_te: LoaiTienTe):
    db_loai_tien_te = Loai_tien_te(**loai_tien_te.dict())
    db.add(db_loai_tien_te)
    db.commit()
    db.refresh(db_loai_tien_te)
    return db_loai_tien_te

def get_loai_tien_te(db: Session, loai_tien_te_id: str = None, loai_tien_te_name: str = None):
    if loai_tien_te_id:
        db_loai_tien_te = db.query(Loai_tien_te).filter(Loai_tien_te.id == loai_tien_te_id).first()
    elif loai_tien_te_name:
        db_loai_tien_te = db.query(Loai_tien_te).filter(Loai_tien_te.Ten_loai_tien_te.ilike(f"%{loai_tien_te_name}%")).all()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên loại tiền tệ")
    
    if db_loai_tien_te is None:
        raise HTTPException(status_code=404, detail="Loại tiền tệ không tồn tại")
    
    return db_loai_tien_te

def get_all_loai_tien_te(db: Session):
    """
    Lấy danh sách tất cả loại tiền tệ.
    """
    return db.query(Loai_tien_te).order_by(Loai_tien_te.id).all()
def delete_loai_tien_te(db: Session, loai_tien_te_id: str = None, loai_tien_te_name: str = None):
    """
    Xóa loại tiền tệ theo ID hoặc tên.
    """
    if loai_tien_te_id:
        db_loai_tien_te = db.query(Loai_tien_te).filter(Loai_tien_te.id == loai_tien_te_id).first()
    elif loai_tien_te_name:
        db_loai_tien_te = db.query(Loai_tien_te).filter(Loai_tien_te.Ten_loai_tien_te.ilike(f"%{loai_tien_te_name}%")).all()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên loại tiền tệ")

    if db_loai_tien_te is None:
        raise HTTPException(status_code=404, detail="Loại tiền tệ không tồn tại")

    db.delete(db_loai_tien_te)
    db.commit()
    return {"message": "Loại tiền tệ đã được xóa thành công"}
def update_loai_tien_te(db: Session, loai_tien_te_id: str, loai_tien_te: LoaiTienTeBase):
    db_loai_tien_te = db.query(Loai_tien_te).filter(Loai_tien_te.id == loai_tien_te_id).first()
    if db_loai_tien_te is None:
        raise HTTPException(status_code=404, detail="Loại tiền tệ không tồn tại")

    for key, value in loai_tien_te.model_dump().items():
        setattr(db_loai_tien_te, key, value)

    db.commit()
    db.refresh(db_loai_tien_te)
    return db_loai_tien_te