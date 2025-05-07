from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.helper.security import hash_password
from app.helper.security import verify_password
from app.models import Dang_nhap
from app.schemas import DangNhapCreate

def create_dang_nhap(db: Session, dang_nhap: DangNhapCreate):
    # Mã hóa mật khẩu trước khi lưu
    dang_nhap.password = hash_password(dang_nhap.password)
    db_dang_nhap = Dang_nhap(**dang_nhap.dict())
    db.add(db_dang_nhap)
    db.commit()
    db.refresh(db_dang_nhap)
    return db_dang_nhap

def get_dang_nhap(db: Session, dang_nhap_id: int):
    db_dang_nhap = db.query(Dang_nhap).filter(Dang_nhap.id == dang_nhap_id).first()
    if db_dang_nhap is None:
        raise HTTPException(status_code=404, detail="Đăng nhập không tồn tại")
    return db_dang_nhap

def get_all_dang_nhap(db: Session):
    """
    Lấy danh sách tất cả đăng nhập.
    """
    return db.query(Dang_nhap).all()

