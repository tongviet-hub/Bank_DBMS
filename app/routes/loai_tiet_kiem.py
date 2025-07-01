from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()

@router.post("/loai-tiet-kiem/", response_model=schemas.LoaiTietKiem)
def create_loai_tiet_kiem(loai_tiet_kiem: schemas.LoaiTietKiemCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một loại tiết kiệm.
    """
    return crud.create_loai_tiet_kiem(db=db, loai_tiet_kiem=loai_tiet_kiem)

@router.get("/loai-tiet-kiem/", response_model=list[schemas.LoaiTietKiem])
def get_all_loai_tiet_kiem(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả các loại tiết kiệm.
    """
    db_loai_tiet_kiem = crud.get_all_loai_tiet_kiem(db=db)
    return db_loai_tiet_kiem
@router.get("/loai-tiet-kiem/search/", response_model=list[schemas.LoaiTietKiem])
def search_loai_tai_khoan(
    loai_tiet_kiem_id: str | None = None,
    name: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm loại tài khoản theo ID hoặc tên.
    """
    if loai_tiet_kiem_id:
        db_loai_tiet_kiem = crud.get_loai_tiet_kiem(db=db, loai_tiet_kiem_id=loai_tiet_kiem_id)
        return [db_loai_tiet_kiem] if db_loai_tiet_kiem else []
    if name:
        db_loai_tiet_kiem = crud.get_loai_tiet_kiem(db=db, loai_tiet_kiem_name=name)
        return db_loai_tiet_kiem
    raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên để tìm kiếm")

@router.delete("/loai-tiet-kiem/{loai_tiet_kiem_id}")
def delete_loai_tiet_kiem(loai_tiet_kiem_id: str, db: Session = Depends(get_db)):
    """
    Xóa loại tài khoản theo ID.
    """
    return crud.delete_loai_tiet_kiem(db=db, loai_tiet_kiem_id=loai_tiet_kiem_id)

@router.put("/loai-tiet-kiem/{loai_tiet_kiem_id}", response_model=schemas.LoaiTietKiem)
def update_loai_tiet_kiem(loai_tiet_kiem_id: str, loai_tiet_kiem: schemas.LoaiTietKiemCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin loại tài khoản.
    """
    return crud.update_loai_tiet_kiem(db=db, loai_tiet_kiem_id=loai_tiet_kiem_id, loai_tiet_kiem=loai_tiet_kiem)