from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Chuyen_khoan
from schemas import ChuyenKhoanBase, ChuyenKhoan


def create_chuyen_khoan(db: Session, chuyen_khoan: ChuyenKhoan):
    db_chuyen_khoan = Chuyen_khoan(**chuyen_khoan.model_dump())
    db.add(db_chuyen_khoan)
    db.commit()
    db.refresh(db_chuyen_khoan)
    return db_chuyen_khoan

def get_chuyen_khoan(db: Session, chuyen_khoan_id: str = None):
    if chuyen_khoan_id:
        db_chuyen_khoan = db.query(Chuyen_khoan).filter(Chuyen_khoan.id == chuyen_khoan_id).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên chuyển khoản")
    if db_chuyen_khoan is None:
        raise HTTPException(status_code=404, detail="Chuyển khoản không tồn tại")
    return db_chuyen_khoan

def get_all_chuyen_khoan(db: Session):
    """
    Lấy danh sách tất cả chuyển khoản.
    """
    return db.query(Chuyen_khoan).order_by(Chuyen_khoan.id).all()

def delete_chuyen_khoan(db: Session, chuyen_khoan_id: str = None, chuyen_khoan_name: str = None):
    """
    Xóa chuyển khoản theo ID hoặc tên.
    """
    if chuyen_khoan_id:
        db_chuyen_khoan = db.query(Chuyen_khoan).filter(Chuyen_khoan.id == chuyen_khoan_id).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên chuyển khoản")
    if db_chuyen_khoan is None:
        raise HTTPException(status_code=404, detail="Chuyển khoản không tồn tại")
    db.delete(db_chuyen_khoan)
    db.commit()
    return {"message": "Chuyển khoản đã được xóa thành công"}

def update_chuyen_khoan(db: Session, chuyen_khoan_id: str, chuyen_khoan: ChuyenKhoanBase):
    db_chuyen_khoan = db.query(Chuyen_khoan).filter(Chuyen_khoan.id == chuyen_khoan_id).first()
    if db_chuyen_khoan is None:
        raise HTTPException(status_code=404, detail="Chuyển khoản không tồn tại")
    for key, value in chuyen_khoan.model_dump().items():
        setattr(db_chuyen_khoan, key, value)
    db.commit()
    db.refresh(db_chuyen_khoan)
    return db_chuyen_khoan
