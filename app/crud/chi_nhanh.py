

from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Chi_nhanh
from schemas import ChiNhanhCreate

def create_chi_nhanh(db: Session, chi_nhanh: ChiNhanhCreate):
    """
    Tạo mới một chi nhánh trong cơ sở dữ liệu.
    """
    db_chi_nhanh = Chi_nhanh(**chi_nhanh.dict())
    db.add(db_chi_nhanh)
    db.commit()
    db.refresh(db_chi_nhanh)
    return db_chi_nhanh

def get_chi_nhanh(db: Session, chi_nhanh_id: int):
    """
    Lấy thông tin chi nhánh theo ID.
    """
    db_chi_nhanh = db.query(Chi_nhanh).filter(Chi_nhanh.id == chi_nhanh_id).first()
    if not db_chi_nhanh:
        raise HTTPException(status_code=404, detail="Chi nhánh không tồn tại")
    return db_chi_nhanh

def get_all_chi_nhanh(db: Session):
    """
    Lấy danh sách tất cả các chi nhánh.
    """
    return db.query(Chi_nhanh).all()

def delete_chi_nhanh(db: Session, chi_nhanh_id: int):
    """
    Xóa một chi nhánh theo ID.
    """
    db_chi_nhanh = db.query(Chi_nhanh).filter(Chi_nhanh.id == chi_nhanh_id).first()
    if not db_chi_nhanh:
        raise HTTPException(status_code=404, detail="Chi nhánh không tồn tại")
    db.delete(db_chi_nhanh)
    db.commit()
    return {"message": "Chi nhánh đã được xóa thành công"}

def update_chi_nhanh(db: Session, chi_nhanh_id: int, chi_nhanh: ChiNhanhCreate):
    """
    Cập nhật thông tin chi nhánh theo ID.
    """
    db_chi_nhanh = db.query(Chi_nhanh).filter(Chi_nhanh.id == chi_nhanh_id).first()
    if not db_chi_nhanh:
        raise HTTPException(status_code=404, detail="Chi nhánh không tồn tại")
    for key, value in chi_nhanh.dict().items():
        setattr(db_chi_nhanh, key, value)
    db.commit()
    db.refresh(db_chi_nhanh)
    return db_chi_nhanh