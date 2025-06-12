from sqlalchemy.orm import Session
from fastapi import HTTPException
from helper.security import hash_password
from helper.security import verify_password
from models import Dang_nhap
from schemas import DangNhapBase, DangNhap

def create_dang_nhap(db: Session, dang_nhap: DangNhap):
    # Mã hóa mật khẩu trước khi lưu
    dang_nhap.Mat_khau = hash_password(dang_nhap.Mat_khau)
    db_dang_nhap = Dang_nhap(**dang_nhap.dict())
    db.add(db_dang_nhap)
    db.commit()
    db.refresh(db_dang_nhap)
    return db_dang_nhap

def get_dang_nhap(db: Session, dang_nhap_id: str, username: str = None):
    if dang_nhap_id:
        db_dang_nhap = db.query(Dang_nhap).filter(Dang_nhap.id == dang_nhap_id).first()
    elif username:
        db_dang_nhap = db.query(Dang_nhap).filter(Dang_nhap.Ten_dang_nhap == username).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên người dùng")

def get_all_dang_nhap(db: Session):
    """
    Lấy danh sách tất cả đăng nhập.
    """
    return db.query(Dang_nhap).order_by(Dang_nhap.id).all()

def delete_dang_nhap(db: Session, dang_nhap_id: str):
    db_dang_nhap = db.query(Dang_nhap).filter(Dang_nhap.id == dang_nhap_id).first()
    if db_dang_nhap is None:
        raise HTTPException(status_code=404, detail="Đăng nhập không tồn tại")
    db.delete(db_dang_nhap)
    db.commit()
    return {"detail": "Đăng nhập đã được xóa"}

def update_dang_nhap(db: Session, dang_nhap_id: str, dang_nhap: DangNhapBase):
    db_dang_nhap = db.query(Dang_nhap).filter(Dang_nhap.id == dang_nhap_id).first()
    if db_dang_nhap is None:
        raise HTTPException(status_code=404, detail="Đăng nhập không tồn tại")
    
    # Mã hóa mật khẩu trước khi lưu
    if dang_nhap.Mat_khau:
        dang_nhap.Mat_khau = hash_password(dang_nhap.Mat_khau)
    
    for key, value in dang_nhap.dict(exclude_unset=True).items():
        setattr(db_dang_nhap, key, value)
    
    db.commit()
    db.refresh(db_dang_nhap)
    return db_dang_nhap