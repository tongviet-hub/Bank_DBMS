from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Thao_tac_so_tiet_kiem
from schemas import ThaoTacSoTietKiemCreate



def create_thao_tac_so_tiet_kiem(db: Session, thao_tac_so_tiet_kiem: ThaoTacSoTietKiemCreate):
    db_thao_tac_so_tiet_kiem = Thao_tac_so_tiet_kiem(**thao_tac_so_tiet_kiem.dict())
    db.add(db_thao_tac_so_tiet_kiem)
    db.commit()
    db.refresh(db_thao_tac_so_tiet_kiem)
    return db_thao_tac_so_tiet_kiem
def get_thao_tac_so_tiet_kiem(db: Session, thao_tac_so_tiet_kiem_id: int = None, thao_tac_so_tiet_kiem_name: str = None):
    if thao_tac_so_tiet_kiem_id:
        db_thao_tac_so_tiet_kiem = db.query(Thao_tac_so_tiet_kiem).filter(Thao_tac_so_tiet_kiem.id == thao_tac_so_tiet_kiem_id).first()
    elif thao_tac_so_tiet_kiem_name:
        db_thao_tac_so_tiet_kiem = db.query(Thao_tac_so_tiet_kiem).filter(Thao_tac_so_tiet_kiem.Name == thao_tac_so_tiet_kiem_name).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên thao tác sổ tiết kiệm")
    if db_thao_tac_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Thao tác sổ tiết kiệm không tồn tại")
    return db_thao_tac_so_tiet_kiem

def get_all_thao_tac_so_tiet_kiem(db: Session):
    """
    Lấy danh sách tất cả thao tác sổ tiết kiệm.
    """
    return db.query(Thao_tac_so_tiet_kiem).all()

def delete_thao_tac_so_tiet_kiem(db: Session, thao_tac_so_tiet_kiem_id: int = None, thao_tac_so_tiet_kiem_name: str = None):
    """
    Xóa thao tác sổ tiết kiệm theo ID hoặc tên.
    """
    if thao_tac_so_tiet_kiem_id:
        db_thao_tac_so_tiet_kiem = db.query(Thao_tac_so_tiet_kiem).filter(Thao_tac_so_tiet_kiem.id == thao_tac_so_tiet_kiem_id).first()
    elif thao_tac_so_tiet_kiem_name:
        db_thao_tac_so_tiet_kiem = db.query(Thao_tac_so_tiet_kiem).filter(Thao_tac_so_tiet_kiem.Name.ilike(f"%{thao_tac_so_tiet_kiem_name}%")).all()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên thao tác sổ tiết kiệm")
    if db_thao_tac_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Thao tác sổ tiết kiệm không tồn tại")
    db.delete(db_thao_tac_so_tiet_kiem)
    db.commit()
    return {"message": "Thao tác sổ tiết kiệm đã được xóa thành công"}

def update_thao_tac_so_tiet_kiem(db: Session, thao_tac_so_tiet_kiem_id: int, thao_tac_so_tiet_kiem: ThaoTacSoTietKiemCreate):
    db_thao_tac_so_tiet_kiem = db.query(Thao_tac_so_tiet_kiem).filter(Thao_tac_so_tiet_kiem.id == thao_tac_so_tiet_kiem_id).first()
    if db_thao_tac_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Thao tác sổ tiết kiệm không tồn tại")
    for key, value in thao_tac_so_tiet_kiem.model_dump().items():
        setattr(db_thao_tac_so_tiet_kiem, key, value)
    db.commit()
    db.refresh(db_thao_tac_so_tiet_kiem)
    return db_thao_tac_so_tiet_kiem