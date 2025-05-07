from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Loai_tai_khoan
from app.schemas import LoaiTaiKhoanCreate

def create_loai_tai_khoan(db: Session, loai_tai_khoan: LoaiTaiKhoanCreate):
    db_loai_tai_khoan = Loai_tai_khoan(**loai_tai_khoan.dict())
    db.add(db_loai_tai_khoan)
    db.commit()
    db.refresh(db_loai_tai_khoan)
    return db_loai_tai_khoan
def get_loai_tai_khoan(db: Session, loai_tai_khoan_id: int= None, loai_tai_khoan_name: str = None):
    if loai_tai_khoan_id:
        db_loai_tai_khoan = db.query(Loai_tai_khoan).filter(Loai_tai_khoan.id == loai_tai_khoan_id).first()
    elif loai_tai_khoan_name:
        db_loai_tai_khoan = db.query(Loai_tai_khoan).filter(Loai_tai_khoan.Name == loai_tai_khoan_name).first()
    if db_loai_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Loại tài khoản không tồn tại")
    return db_loai_tai_khoan

def get_all_loai_tai_khoan(db: Session):
    """
    Lấy danh sách tất cả loại tài khoản.
    """
    return db.query(Loai_tai_khoan).all()

def delete_loai_tai_khoan(db: Session, loai_tai_khoan_id: int = None, loai_tai_khoan_name: str = None):
    """
    Xóa loại tài khoản theo ID.
    """
    if loai_tai_khoan_id:
        db_loai_tai_khoan = db.query(Loai_tai_khoan).filter(Loai_tai_khoan.id == loai_tai_khoan_id).first()
    elif loai_tai_khoan_name:
        db_loai_tai_khoan = db.query(Loai_tai_khoan).filter(Loai_tai_khoan.Name == loai_tai_khoan_name).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên loại tài khoản")
    db.delete(db_loai_tai_khoan)
    db.commit()
    return {"message": "Loại tài khoản đã được xóa thành công"}

def update_loai_tai_khoan(db: Session, loai_tai_khoan_id: int, loai_tai_khoan: LoaiTaiKhoanCreate):
    db_loai_tai_khoan = db.query(Loai_tai_khoan).filter(Loai_tai_khoan.id == loai_tai_khoan_id).first()
    if db_loai_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Loại tài khoản không tồn tại")
    for key, value in loai_tai_khoan.model_dump().items():
        setattr(db_loai_tai_khoan, key, value)
    db.commit()
    db.refresh(db_loai_tai_khoan)
    return db_loai_tai_khoan