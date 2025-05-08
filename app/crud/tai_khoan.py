from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Tai_khoan
from schemas import TaiKhoanCreate


def create_tai_khoan(db: Session, tai_khoan: TaiKhoanCreate):
    db_tai_khoan = Tai_khoan(**tai_khoan.dict())
    db.add(db_tai_khoan)
    db.commit()
    db.refresh(db_tai_khoan)
    return db_tai_khoan
def get_tai_khoan(db: Session, tai_khoan_id: int, tai_khoan_name: str = None):
    if tai_khoan_id:
        db_tai_khoan = db.query(Tai_khoan).filter(Tai_khoan.id == tai_khoan_id).first()
    elif tai_khoan_name:
        db_tai_khoan = db.query(Tai_khoan).filter(Tai_khoan.Name == tai_khoan_name).first()
    if db_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Tài khoản không tồn tại")
    return db_tai_khoan

def get_all_tai_khoan(db: Session):
    """
    Lấy danh sách tất cả tài khoản.
    """
    return db.query(Tai_khoan).all()

def delete_tai_khoan(db: Session, tai_khoan_id: int = None, tai_khoan_name: str = None):
    """
    Xóa tài khoản theo ID hoặc tên.
    """
    if tai_khoan_id:
        db_tai_khoan = db.query(Tai_khoan).filter(Tai_khoan.id == tai_khoan_id).first()
    elif tai_khoan_name:
        db_tai_khoan = db.query(Tai_khoan).filter(Tai_khoan.Name == tai_khoan_name).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên tài khoản")
    if db_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Tài khoản không tồn tại")
    db.delete(db_tai_khoan)
    db.commit()
    return {"message": "Tài khoản đã được xóa thành công"}

def update_tai_khoan(db: Session, tai_khoan_id: int, tai_khoan: TaiKhoanCreate):
    db_tai_khoan = db.query(Tai_khoan).filter(Tai_khoan.id == tai_khoan_id).first()
    if db_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Tài khoản không tồn tại")
    for key, value in tai_khoan.model_dump().items():
        setattr(db_tai_khoan, key, value)
    db.commit()
    db.refresh(db_tai_khoan)
    return db_tai_khoan
