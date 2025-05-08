from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()

@router.post("/so-tiet-kiem/", response_model=schemas.SoTietKiem)
def create_so_tiet_kiem(so_tiet_kiem: schemas.SoTietKiemCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một sổ tiết kiệm.
    """
    return crud.create_so_tiet_kiem(db=db, so_tiet_kiem=so_tiet_kiem)

@router.get("/so-tiet-kiem/", response_model=list[schemas.SoTietKiem])
def get_all_so_tiet_kiem(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả các sổ tiết kiệm.
    """
    db_so_tiet_kiem = crud.get_all_so_tiet_kiem(db=db)
    return db_so_tiet_kiem

@router.get("/so-tiet-kiem/search/", response_model=list[schemas.SoTietKiem])
def search_so_tiet_kiem(
    so_tiet_kiem_id: int | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm sổ tiết kiệm theo ID.
    """
    if so_tiet_kiem_id:
        db_so_tiet_kiem = crud.get_so_tiet_kiem(db=db, so_tiet_kiem_id=so_tiet_kiem_id)
        return [db_so_tiet_kiem] if db_so_tiet_kiem else []
    raise HTTPException(status_code=400, detail="Cần cung cấp ID để tìm kiếm")

@router.delete("/so-tiet-kiem/{so_tiet_kiem_id}")
def delete_so_tiet_kiem(so_tiet_kiem_id: int, db: Session = Depends(get_db)):
    """
    Xóa sổ tiết kiệm theo ID.
    """
    return crud.delete_so_tiet_kiem(db=db, so_tiet_kiem_id=so_tiet_kiem_id)

@router.put("/so-tiet-kiem/{so_tiet_kiem_id}", response_model=schemas.SoTietKiem)
def update_so_tiet_kiem(so_tiet_kiem_id: int, so_tiet_kiem: schemas.SoTietKiemCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin sổ tiết kiệm.
    """
    return crud.update_so_tiet_kiem(db=db, so_tiet_kiem_id=so_tiet_kiem_id, so_tiet_kiem=so_tiet_kiem)