from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas
from typing import List

router = APIRouter()

@router.post("/tai-khoan/", response_model=schemas.TaiKhoan)
def create_tai_khoan(tai_khoan: schemas.TaiKhoanCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một tài khoản.
    """
    return crud.create_tai_khoan(db=db, tai_khoan=tai_khoan)

@router.get("/tai-khoan/", response_model=List[schemas.TaiKhoan])
def get_all_tai_khoan(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả tài khoản.
    """
    return crud.get_all_tai_khoan(db=db)

@router.get("/tai-khoan/search/", response_model=List[schemas.TaiKhoan])
def search_tai_khoan(
    tai_khoan_id: int | None = None,
    tai_khoan_name: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm tài khoản theo ID hoặc tên.
    """
    if tai_khoan_id:
        db_tai_khoan = crud.get_tai_khoan(db=db, tai_khoan_id=tai_khoan_id)
        return [db_tai_khoan] if db_tai_khoan else []
    if tai_khoan_name:
        db_tai_khoan = crud.get_tai_khoan(db=db, tai_khoan_name=tai_khoan_name)
        return [db_tai_khoan] if db_tai_khoan else []
    raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên để tìm kiếm")

@router.delete("/tai-khoan/{tai_khoan_id}", response_model=dict)
def delete_tai_khoan(tai_khoan_id: int, db: Session = Depends(get_db)):
    """
    Xóa tài khoản theo ID.
    """
    return crud.delete_tai_khoan(db=db, tai_khoan_id=tai_khoan_id)

@router.put("/tai-khoan/{tai_khoan_id}", response_model=schemas.TaiKhoan)
def update_tai_khoan(tai_khoan_id: int, tai_khoan: schemas.TaiKhoanCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin tài khoản.
    """
    return crud.update_tai_khoan(db=db, tai_khoan_id=tai_khoan_id, tai_khoan=tai_khoan)