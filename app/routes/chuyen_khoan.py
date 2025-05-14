from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()

@router.post("/chuyen-khoan/", response_model=schemas.ChuyenKhoan)
def create_chuyen_khoan(chuyen_khoan: schemas.ChuyenKhoanCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một giao dịch chuyển khoản.
    """
    return crud.create_chuyen_khoan(db=db, chuyen_khoan=chuyen_khoan)

@router.get("/chuyen-khoan/", response_model=list[schemas.ChuyenKhoan])
def get_all_chuyen_khoan(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả các giao dịch chuyển khoản.
    """
    db_chuyen_khoan = crud.get_all_chuyen_khoan(db=db)
    return db_chuyen_khoan

@router.get("/chuyen-khoan/search/", response_model=list[schemas.ChuyenKhoan])
def search_chuyen_khoan(
    chuyen_khoan_id: int | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm giao dịch chuyển khoản theo ID.
    """
    if chuyen_khoan_id:
        db_chuyen_khoan = crud.get_chuyen_khoan(db=db, chuyen_khoan_id=chuyen_khoan_id)
        return [db_chuyen_khoan] if db_chuyen_khoan else []
    raise HTTPException(status_code=400, detail="Cần cung cấp ID")

@router.delete("/chuyen-khoan/{chuyen_khoan_id}")
def delete_chuyen_khoan(chuyen_khoan_id: int, db: Session = Depends(get_db)):
    """
    Xóa giao dịch chuyển khoản theo ID.
    """
    return crud.delete_chuyen_khoan(db=db, chuyen_khoan_id=chuyen_khoan_id)

@router.put("/chuyen-khoan/{chuyen_khoan_id}", response_model=schemas.ChuyenKhoan)
def update_chuyen_khoan(chuyen_khoan_id: int, chuyen_khoan: schemas.ChuyenKhoanCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin giao dịch chuyển khoản.
    """
    return crud.update_chuyen_khoan(db=db, chuyen_khoan_id=chuyen_khoan_id, chuyen_khoan=chuyen_khoan)