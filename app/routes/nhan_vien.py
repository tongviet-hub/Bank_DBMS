from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()

@router.post("/nhan-vien/", response_model=schemas.NhanVien)
def create_nhan_vien(nhan_vien: schemas.NhanVienCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một nhân viên.
    """
    return crud.create_nhan_vien(db=db, nhan_vien=nhan_vien)

@router.get("/nhan-vien/", response_model=list[schemas.NhanVien])
def get_all_nhan_vien(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả nhân viên.
    """
    db_nhan_vien = crud.get_all_nhan_vien(db=db)
    return db_nhan_vien

@router.get("/nhan-vien/search/", response_model=list[schemas.NhanVien])
def search_nhan_vien(
    nhan_vien_id: str | None = None,
    name: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm nhân viên theo ID hoặc tên.
    """
    if nhan_vien_id:
        db_nhan_vien = crud.get_nhan_vien(db=db, nhan_vien_id=nhan_vien_id)
        return [db_nhan_vien] if db_nhan_vien else []
    if name:
        db_nhan_vien = crud.get_nhan_vien(db=db, nhan_vien_name=name)
        return db_nhan_vien
    raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên để tìm kiếm")

@router.delete("/nhan-vien/{nhan_vien_id}")
def delete_nhan_vien(nhan_vien_id: str, db: Session = Depends(get_db)):
    """
    Xóa nhân viên theo ID.
    """
    return crud.delete_nhan_vien(db=db, nhan_vien_id=nhan_vien_id)

@router.put("/nhan-vien/{nhan_vien_id}", response_model=schemas.NhanVien)
def update_nhan_vien(nhan_vien_id: str, nhan_vien: schemas.NhanVienCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin nhân viên.
    """
    return crud.update_nhan_vien(db=db, nhan_vien_id=nhan_vien_id, nhan_vien=nhan_vien)