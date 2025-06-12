from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Chi_nhanh
from schemas import ChiNhanhCreate, ChiNhanh

def create_chi_nhanh(db: Session, chi_nhanh: ChiNhanh):
    """
    Tạo mới một chi nhánh trong cơ sở dữ liệu.
    """
    db_chi_nhanh = Chi_nhanh(**chi_nhanh.model_dump())
    db.add(db_chi_nhanh)
    db.commit()
    db.refresh(db_chi_nhanh)
    return db_chi_nhanh

def get_chi_nhanh(db: Session, chi_nhanh_id: str = None, chi_nhanh_name: str = None):
    """
    Lấy thông tin chi nhánh theo ID hoặc tên.
    """
    if chi_nhanh_id:
        db_chi_nhanh = db.query(Chi_nhanh).filter(Chi_nhanh.id == chi_nhanh_id).first()
    elif chi_nhanh_name:
        db_chi_nhanh = db.query(Chi_nhanh).filter(Chi_nhanh.Ten_chi_nhanh.ilike(f"%{chi_nhanh_name}%")).all()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên chi nhánh")
    if db_chi_nhanh is None:
        raise HTTPException(status_code=404, detail="Chi nhánh không tồn tại")
    return db_chi_nhanh

def get_all_chi_nhanh(db: Session):
    """
    Lấy danh sách tất cả các chi nhánh, sắp xếp theo ID.
    """
    return db.query(Chi_nhanh).order_by(Chi_nhanh.id).all()

def delete_chi_nhanh(db: Session, chi_nhanh_id: str, chi_nhanh_name: str = None):
    """
    Xóa chi nhánh theo ID hoặc tên.
    """
    if chi_nhanh_id:
        db_chi_nhanh = db.query(Chi_nhanh).filter(Chi_nhanh.id == chi_nhanh_id).first()
    elif chi_nhanh_name:
        db_chi_nhanh = db.query(Chi_nhanh).filter(Chi_nhanh.Ten_chi_nhanh.ilike(f"%{chi_nhanh_name}%")).all()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên chi nhánh")
    if db_chi_nhanh is None:
        raise HTTPException(status_code=404, detail="Chi nhánh không tồn tại")
    db.delete(db_chi_nhanh)
    db.commit()
    return {"message": "Chi nhánh đã được xóa thành công"}

def update_chi_nhanh(db: Session, chi_nhanh_id: str, chi_nhanh: ChiNhanhCreate):
    """Cập nhật thông tin chi nhánh."""
    db_chi_nhanh = db.query(Chi_nhanh).filter(Chi_nhanh.id == chi_nhanh_id).first()
    if not db_chi_nhanh:
        raise HTTPException(status_code=404, detail="Chi nhánh không tồn tại")

    # Cập nhật các trường từ ChiNhanhCreate
    update_data = chi_nhanh.dict(exclude_unset=True)  # Chỉ cập nhật các trường được cung cấp
    for key, value in update_data.items():
        setattr(db_chi_nhanh, key, value)

    db.commit()
    db.refresh(db_chi_nhanh)
    return db_chi_nhanh