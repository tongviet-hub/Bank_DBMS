from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()

@router.post("/khach-hang/", response_model=schemas.KhachHang)
def create_khach_hang(khach_hang: schemas.KhachHangCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một khách hàng.
    """
    return crud.create_khach_hang(db=db, khach_hang=khach_hang)

@router.get("/khach-hang/", response_model=list[schemas.KhachHang])
def get_all_khach_hang(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả khách hàng.
    """
    db_khach_hang = crud.get_all_khach_hang(db=db)
    return db_khach_hang

@router.get("/khach-hang/search/", response_model=list[schemas.KhachHang])
def search_khach_hang(
    khach_hang_id: str | None = None,
    name: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm khách hàng theo ID hoặc tên.
    """
    if khach_hang_id:
        db_khach_hang = crud.get_khach_hang(db=db, khach_hang_id=khach_hang_id)
        return [db_khach_hang] if db_khach_hang else []
    if name:
        db_khach_hang = crud.get_khach_hang(db=db, khach_hang_name=name)
        return db_khach_hang
    raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên để tìm kiếm")

@router.delete("/khach-hang/{khach_hang_id}")
def delete_khach_hang(khach_hang_id: str, db: Session = Depends(get_db)):
    """
    Xóa khách hàng theo ID.
    """
    return crud.delete_khach_hang(db=db, khach_hang_id=khach_hang_id)

@router.put("/khach-hang/{khach_hang_id}", response_model=schemas.KhachHang)
def update_khach_hang(khach_hang_id: str, khach_hang: schemas.KhachHangCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin khách hàng.
    """
    return crud.update_khach_hang(db=db, khach_hang_id=khach_hang_id, khach_hang=khach_hang)

@router.get("/khach-hang/count")
def count_khach_hang(db: Session = Depends(get_db)):
    """
    Trả về tổng số khách hàng.
    """
    total = crud.count_khach_hang(db=db)
    return {"total": total}

