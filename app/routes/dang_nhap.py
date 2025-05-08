from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()

@router.post("/dang-nhap/", response_model=schemas.DangNhap)
def create_dang_nhap(dang_nhap: schemas.DangNhapCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một thông tin đăng nhập.
    """
    return crud.create_dang_nhap(db=db, dang_nhap=dang_nhap)

@router.get("/dang-nhap/", response_model=list[schemas.DangNhap])
def get_all_dang_nhap(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả thông tin đăng nhập.
    """
    db_dang_nhap = crud.get_all_dang_nhap(db=db)
    return db_dang_nhap

@router.get("/dang-nhap/search/", response_model=list[schemas.DangNhap])
def search_dang_nhap(
    dang_nhap_id: int | None = None,
    username: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm thông tin đăng nhập theo ID hoặc tên người dùng.
    """
    if dang_nhap_id:
        db_dang_nhap = crud.get_dang_nhap(db=db, dang_nhap_id=dang_nhap_id)
        return [db_dang_nhap] if db_dang_nhap else []
    if username:
        db_dang_nhap = crud.get_dang_nhap_by_username(db=db, username=username)
        return db_dang_nhap
    raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên người dùng để tìm kiếm")

@router.delete("/dang-nhap/{dang_nhap_id}")
def delete_dang_nhap(dang_nhap_id: int, db: Session = Depends(get_db)):
    """
    Xóa thông tin đăng nhập theo ID.
    """
    return crud.delete_dang_nhap(db=db, dang_nhap_id=dang_nhap_id)

@router.put("/dang-nhap/{dang_nhap_id}", response_model=schemas.DangNhap)
def update_dang_nhap(dang_nhap_id: int, dang_nhap: schemas.DangNhapCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin đăng nhập.
    """
    return crud.update_dang_nhap(db=db, dang_nhap_id=dang_nhap_id, dang_nhap=dang_nhap)