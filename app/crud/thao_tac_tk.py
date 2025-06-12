from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Thao_tac_tai_khoan
from schemas import ThaoTacTaiKhoanBase, ThaoTacTaiKhoan




def create_thao_tac_tai_khoan(db: Session, thao_tac_tai_khoan: ThaoTacTaiKhoan):
    db_thao_tac_tai_khoan = Thao_tac_tai_khoan(**thao_tac_tai_khoan.dict())
    db.add(db_thao_tac_tai_khoan)
    db.commit()
    db.refresh(db_thao_tac_tai_khoan)
    return db_thao_tac_tai_khoan
def get_thao_tac_tai_khoan(db: Session, thao_tac_tai_khoan_id: str = None):
    if thao_tac_tai_khoan_id:
        db_thao_tac_tai_khoan = db.query(Thao_tac_tai_khoan).filter(Thao_tac_tai_khoan.id == thao_tac_tai_khoan_id).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID để tìm kiếm thao tác tài khoản")
    if db_thao_tac_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Thao tác tài khoản không tồn tại")
    return db_thao_tac_tai_khoan

def get_all_thao_tac_tai_khoan(db: Session):
    """
    Lấy danh sách tất cả thao tác tài khoản.
    """
    return db.query(Thao_tac_tai_khoan).order_by(Thao_tac_tai_khoan.id).all()

def delete_thao_tac_tai_khoan(db: Session, thao_tac_tai_khoan_id: str = None, thao_tac_tai_khoan_name: str = None):
    """
    Xóa thao tác tài khoản theo ID.
    """
    if thao_tac_tai_khoan_id:
        db_thao_tac_tai_khoan = db.query(Thao_tac_tai_khoan).filter(Thao_tac_tai_khoan.id == thao_tac_tai_khoan_id).first()
    else:   
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên thao tác tài khoản")
    if db_thao_tac_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Thao tác tài khoản không tồn tại")
    db.delete(db_thao_tac_tai_khoan)
    db.commit()
    return {"message": "Thao tác tài khoản đã được xóa thành công"}

def update_thao_tac_tai_khoan(db: Session, thao_tac_tai_khoan_id: str, thao_tac_tai_khoan: ThaoTacTaiKhoanBase):
    db_thao_tac_tai_khoan = db.query(Thao_tac_tai_khoan).filter(Thao_tac_tai_khoan.id == thao_tac_tai_khoan_id).first()
    if db_thao_tac_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Thao tác tài khoản không tồn tại")
    for key, value in thao_tac_tai_khoan.model_dump().items():
        setattr(db_thao_tac_tai_khoan, key, value)
    db.commit()
    db.refresh(db_thao_tac_tai_khoan)
    return db_thao_tac_tai_khoan