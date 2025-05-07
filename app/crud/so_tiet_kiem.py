from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import So_tiet_kiem
from app.schemas import SoTietKiemCreate




def create_so_tiet_kiem(db: Session, so_tiet_kiem: SoTietKiemCreate):
    db_so_tiet_kiem = So_tiet_kiem(**so_tiet_kiem.dict())
    db.add(db_so_tiet_kiem)
    db.commit()
    db.refresh(db_so_tiet_kiem)
    return db_so_tiet_kiem
def get_so_tiet_kiem(db: Session, so_tiet_kiem_id: int = None, so_tiet_kiem_name: str = None):
    if so_tiet_kiem_id:
        db_so_tiet_kiem = db.query(So_tiet_kiem).filter(So_tiet_kiem.id == so_tiet_kiem_id).first()
    elif so_tiet_kiem_name:
        db_so_tiet_kiem = db.query(So_tiet_kiem).filter(So_tiet_kiem.Name == so_tiet_kiem_name).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên sổ tiết kiệm")
    if db_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Sổ tiết kiệm không tồn tại")
    return db_so_tiet_kiem

def get_all_so_tiet_kiem(db: Session):
    """
    Lấy danh sách tất cả sổ tiết kiệm.
    """
    return db.query(So_tiet_kiem).all()

def delete_so_tiet_kiem(db: Session, so_tiet_kiem_id: int = None, so_tiet_kiem_name: str = None):
    """
    Xóa sổ tiết kiệm theo ID hoặc tên.
    """
    if so_tiet_kiem_id:
        db_so_tiet_kiem = db.query(So_tiet_kiem).filter(So_tiet_kiem.id == so_tiet_kiem_id).first()
    elif so_tiet_kiem_name:
        db_so_tiet_kiem = db.query(So_tiet_kiem).filter(So_tiet_kiem.Name == so_tiet_kiem_name).first()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên sổ tiết kiệm")
    if db_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Sổ tiết kiệm không tồn tại")
    db.delete(db_so_tiet_kiem)
    db.commit()
    return {"message": "Sổ tiết kiệm đã được xóa thành công"}

def update_so_tiet_kiem(db: Session, so_tiet_kiem_id: int, so_tiet_kiem: SoTietKiemCreate):
    db_so_tiet_kiem = db.query(So_tiet_kiem).filter(So_tiet_kiem.id == so_tiet_kiem_id).first()
    if db_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Sổ tiết kiệm không tồn tại")
    for key, value in so_tiet_kiem.model_dump().items():
        setattr(db_so_tiet_kiem, key, value)
    db.commit()
    db.refresh(db_so_tiet_kiem)
    return db_so_tiet_kiem