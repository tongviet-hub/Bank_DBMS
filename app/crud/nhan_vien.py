from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Nhan_vien
from app.schemas import NhanVienCreate



def create_nhan_vien(db: Session, nhan_vien: NhanVienCreate):
    db_nhan_vien = Nhan_vien(**nhan_vien.dict())
    db.add(db_nhan_vien)
    db.commit()
    db.refresh(db_nhan_vien)
    return db_nhan_vien

def get_nhan_vien(db: Session, nhan_vien_id: int = None, nhan_vien_name: str = None):
    if nhan_vien_id:
        db_nhan_vien = db.query(Nhan_vien).filter(Nhan_vien.id == nhan_vien_id).first()
    elif nhan_vien_name:
        db_nhan_vien = db.query(Nhan_vien).filter(Nhan_vien.Name == nhan_vien_name).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên nhân viên")
    if db_nhan_vien is None:
        raise HTTPException(status_code=404, detail="Nhân viên không tồn tại")
    return db_nhan_vien

def get_all_nhan_vien(db: Session):
    """
    Lấy danh sách tất cả nhân viên.
    """
    return db.query(Nhan_vien).all()

def delete_nhan_vien(db: Session, nhan_vien_id: int = None, nhan_vien_name: str = None):
    """
    Xóa nhân viên theo ID hoặc tên.
    """
    if nhan_vien_id:
        db_nhan_vien = db.query(Nhan_vien).filter(Nhan_vien.id == nhan_vien_id).first()
    elif nhan_vien_name:
        db_nhan_vien = db.query(Nhan_vien).filter(Nhan_vien.Name.ilike(f"%{nhan_vien_name}%")).all()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên nhân viên")
    if db_nhan_vien is None:
        raise HTTPException(status_code=404, detail="Nhân viên không tồn tại")
    db.delete(db_nhan_vien)
    db.commit()
    return {"message": "Nhân viên đã được xóa thành công"}

def update_nhan_vien(db: Session, nhan_vien_id: int, nhan_vien: NhanVienCreate):
    db_nhan_vien = db.query(Nhan_vien).filter(Nhan_vien.id == nhan_vien_id).first()
    if db_nhan_vien is None:
        raise HTTPException(status_code=404, detail="Nhân viên không tồn tại")
    for key, value in nhan_vien.model_dump().items():
        setattr(db_nhan_vien, key, value)
    db.commit()
    db.refresh(db_nhan_vien)
    return db_nhan_vien

