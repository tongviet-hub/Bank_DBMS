from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Thao_tac
from schemas import ThaoTacCreate




def create_thao_tac(db: Session, thao_tac: ThaoTacCreate):
    db_thao_tac = Thao_tac(**thao_tac.dict())
    db.add(db_thao_tac)
    db.commit()
    db.refresh(db_thao_tac)
    return db_thao_tac

def delete_thao_tac(db: Session, thao_tac_id: int = None, thao_tac_name: str = None):
    """
    Xóa thao tác theo ID hoặc tên.
    """
    if thao_tac_id:
        db_thao_tac = db.query(Thao_tac).filter(Thao_tac.id == thao_tac_id).first()
    elif thao_tac_name:
        db_thao_tac = db.query(Thao_tac).filter(Thao_tac.Name.ilike(f"%{thao_tac_name}%")).all()
    else:   
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên thao tác")
    if db_thao_tac is None:
        raise HTTPException(status_code=404, detail="Thao tác không tồn tại")
    db.delete(db_thao_tac)
    db.commit()
    return {"message": "Thao tác đã được xóa thành công"}

def get_thao_tac(db: Session, thao_tac_id: int = None, thao_tac_name: str = None):
    if thao_tac_id:
        db_thao_tac = db.query(Thao_tac).filter(Thao_tac.id == thao_tac_id).first()
    elif thao_tac_name:
        db_thao_tac = db.query(Thao_tac).filter(Thao_tac.Ten_thao_tac.ilike(f"%{thao_tac_name}%")).all()
    else:
        raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên thao tác")
    if db_thao_tac is None:
        raise HTTPException(status_code=404, detail="Thao tác không tồn tại")
    return db_thao_tac

def get_all_thao_tac(db: Session):
    """
    Lấy danh sách tất cả thao tác.
    """
    return db.query(Thao_tac).all()

def update_thao_tac(db: Session, thao_tac_id: int, thao_tac: ThaoTacCreate):
    db_thao_tac = db.query(Thao_tac).filter(Thao_tac.id == thao_tac_id).first()
    if db_thao_tac is None:
        raise HTTPException(status_code=404, detail="Thao tác không tồn tại")
    for key, value in thao_tac.model_dump().items():
        setattr(db_thao_tac, key, value)
    db.commit()
    db.refresh(db_thao_tac)
    return db_thao_tac