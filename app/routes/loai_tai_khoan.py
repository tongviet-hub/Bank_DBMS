
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()

@router.post("/loai-tai-khoan/", response_model=schemas.LoaiTaiKhoan)
def create_loai_tai_khoan(loai_tai_khoan: schemas.LoaiTaiKhoanCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một loại tài khoản.
    """
    return crud.create_loai_tai_khoan(db=db, loai_tai_khoan=loai_tai_khoan)

@router.get("/loai-tai-khoan/", response_model=list[schemas.LoaiTaiKhoan])
def get_all_loai_tai_khoan(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả các loại tài khoản.
    """
    db_loai_tai_khoan = crud.get_all_loai_tai_khoan(db=db)
    return db_loai_tai_khoan

@router.get("/loai-tai-khoan/search/", response_model=list[schemas.LoaiTaiKhoan])
def search_loai_tai_khoan(
    loai_tai_khoan_id: str | None = None,
    name: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm loại tài khoản theo ID hoặc tên.
    """
    if loai_tai_khoan_id:
        db_loai_tai_khoan = crud.get_loai_tai_khoan(db=db, loai_tai_khoan_id=loai_tai_khoan_id)
        return [db_loai_tai_khoan] if db_loai_tai_khoan else []
    if name:
        db_loai_tai_khoan = crud.get_loai_tai_khoan(db=db, loai_tai_khoan_name=name)
        return db_loai_tai_khoan
    raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên để tìm kiếm")

@router.delete("/loai-tai-khoan/{loai_tai_khoan_id}")
def delete_loai_tai_khoan(loai_tai_khoan_id: str, db: Session = Depends(get_db)):
    """
    Xóa loại tài khoản theo ID.
    """
    return crud.delete_loai_tai_khoan(db=db, loai_tai_khoan_id=loai_tai_khoan_id)

@router.put("/loai-tai-khoan/{loai_tai_khoan_id}", response_model=schemas.LoaiTaiKhoan)
def update_loai_tai_khoan(loai_tai_khoan_id: str, loai_tai_khoan: schemas.LoaiTaiKhoanCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin loại tài khoản.
    """
    return crud.update_loai_tai_khoan(db=db, loai_tai_khoan_id=loai_tai_khoan_id, loai_tai_khoan=loai_tai_khoan)