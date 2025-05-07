from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException
from models import Khach_hang
from schemas import KhachHangCreate

def create_khach_hang(db: Session, khach_hang: KhachHangCreate):
    db_khach_hang = Khach_hang(**khach_hang.dict())
    db.add(db_khach_hang)
    db.commit()
    db.refresh(db_khach_hang)
    return db_khach_hang

def get_khach_hang(db: Session, khach_hang_id: int = None, khach_hang_name: str = None):
    """
    Lấy thông tin khách hàng theo ID hoặc tìm kiếm theo một phần tên.
    """
    if khach_hang_id:
        db_khach_hang = db.query(Khach_hang).filter(Khach_hang.id == khach_hang_id).first()
    elif khach_hang_name:
        db_khach_hang = db.query(Khach_hang).filter(Khach_hang.Name.ilike(f"%{khach_hang_name}%")).all()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên khách hàng")

    if not db_khach_hang:
        raise HTTPException(status_code=404, detail="Không tìm thấy khách hàng")
    return db_khach_hang

def get_all_khach_hang(db: Session):
    """
    Lấy danh sách tất cả khách hàng.
    """
    return db.query(Khach_hang).all()

def delete_khach_hang(db: Session, khach_hang_id: int = None, khach_hang_name: str = None):
    """
    Xóa khách hàng theo ID hoặc tìm kiếm theo một phần tên.
    """
    if khach_hang_id:
        db_khach_hang = db.query(Khach_hang).filter(Khach_hang.id == khach_hang_id).first()
    elif khach_hang_name:
        db_khach_hang = db.query(Khach_hang).filter(Khach_hang.Name.ilike(f"%{khach_hang_name}%")).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên khách hàng")

    if not db_khach_hang:
        raise HTTPException(status_code=404, detail="Không tìm thấy khách hàng")

    db.delete(db_khach_hang)
    db.commit()
    return {"message": "Khách hàng đã được xóa thành công"}


def update_khach_hang(db: Session, khach_hang_id: int, khach_hang: KhachHangCreate):
    db_khach_hang = db.query(Khach_hang).filter(Khach_hang.id == khach_hang_id).first()
    if db_khach_hang is None:
        raise HTTPException(status_code=404, detail="Khách hàng không tồn tại")
    for key, value in khach_hang.model_dump().items():
        setattr(db_khach_hang, key, value)
    db.commit()
    db.refresh(db_khach_hang)
    return db_khach_hang