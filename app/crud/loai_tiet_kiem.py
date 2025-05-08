from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Loai_tiet_kiem
from app.schemas import LoaiTietKiemCreate



def create_loai_tiet_kiem(db: Session, loai_tiet_kiem: LoaiTietKiemCreate):
    db_loai_tiet_kiem = Loai_tiet_kiem(**loai_tiet_kiem.dict())
    db.add(db_loai_tiet_kiem)
    db.commit()
    db.refresh(db_loai_tiet_kiem)
    return db_loai_tiet_kiem
def get_loai_tiet_kiem(db: Session, loai_tiet_kiem_id: int = None, loai_tiet_kiem_name: str = None):
    if loai_tiet_kiem_id:
        db_loai_tiet_kiem = db.query(Loai_tiet_kiem).filter(Loai_tiet_kiem.id == loai_tiet_kiem_id).first()
    elif loai_tiet_kiem_name:
        db_loai_tiet_kiem = db.query(Loai_tiet_kiem).filter(Loai_tiet_kiem.Name == loai_tiet_kiem_name).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên loại tiết kiệm")
    if db_loai_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Loại tiết kiệm không tồn tại")
    return db_loai_tiet_kiem

def get_all_loai_tiet_kiem(db: Session):
    """
    Lấy danh sách tất cả loại tiết kiệm.
    """
    return db.query(Loai_tiet_kiem).all()

def delete_loai_tiet_kiem(db: Session, loai_tiet_kiem_id: int = None, loai_tiet_kiem_name: str = None):
    """
    Xóa loại tiết kiệm theo ID hoặc tên.
    """
    if loai_tiet_kiem_id:
        db_loai_tiet_kiem = db.query(Loai_tiet_kiem).filter(Loai_tiet_kiem.id == loai_tiet_kiem_id).first()
    elif loai_tiet_kiem_name:
        db_loai_tiet_kiem = db.query(Loai_tiet_kiem).filter(Loai_tiet_kiem.Name.ilike).all()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên loại tiết kiệm")
    if db_loai_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Loại tiết kiệm không tồn tại")
    db.delete(db_loai_tiet_kiem)
    db.commit()
    return {"message": "Loại tiết kiệm đã được xóa thành công"}

def update_loai_tiet_kiem(db: Session, loai_tiet_kiem_id: int, loai_tiet_kiem: LoaiTietKiemCreate):
    db_loai_tiet_kiem = db.query(Loai_tiet_kiem).filter(Loai_tiet_kiem.id == loai_tiet_kiem_id).first()
    if db_loai_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Loại tiết kiệm không tồn tại")
    for key, value in loai_tiet_kiem.model_dump().items():
        setattr(db_loai_tiet_kiem, key, value)
    db.commit()
    db.refresh(db_loai_tiet_kiem)
    return db_loai_tiet_kiem
