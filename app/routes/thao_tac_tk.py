from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas
from typing import List

router = APIRouter()

@router.get("/thao-tac-tk/", response_model=List[schemas.ThaoTacTaiKhoan])
def get_all_thao_tac_tk(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả thao tác tài khoản.
    """
    return crud.get_all_thao_tac_tai_khoan(db=db)

@router.post("/thao-tac-tk/", response_model=schemas.ThaoTacTaiKhoan)
def create_thao_tac_tk(thao_tac_tai_khoan: schemas.ThaoTacTaiKhoanCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một thao tác tài khoản.
    """
    return crud.create_thao_tac_tai_khoan(db=db, thao_tac_tai_khoan=thao_tac_tai_khoan)

@router.get("/thao-tac-tk/search/", response_model=List[schemas.ThaoTacTaiKhoan])
def search_thao_tac_tk(
    thao_tac_tai_khoan_id: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm thao tác tài khoản theo ID hoặc tên.
    """
    if thao_tac_tai_khoan_id:
        db_thao_tac_tk = crud.get_thao_tac_tai_khoan(db=db, thao_tac_tai_khoan_id=thao_tac_tai_khoan_id)
        return [db_thao_tac_tk] if db_thao_tac_tk else []
    raise HTTPException(status_code=400, detail="Cần cung cấp ID để tìm kiếm")

@router.delete("/thao-tac-tk/{thao_tac_tai_khoan_id}", response_model=dict)
def delete_thao_tac_tk(thao_tac_tai_khoan_id: str, db: Session = Depends(get_db)):
    """
    Xóa thao tác tài khoản theo ID.
    """
    return crud.delete_thao_tac_tai_khoan(db=db, thao_tac_tai_khoan_id=thao_tac_tai_khoan_id)

@router.put("/thao-tac-tk/{thao_tac_tai_khoan_id}", response_model=schemas.ThaoTacTaiKhoan)
def update_thao_tac_tk(thao_tac_tai_khoan_id: str, thao_tac_tai_khoan: schemas.ThaoTacTaiKhoanCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin thao tác tài khoản.
    """
    return crud.update_thao_tac_tai_khoan(db=db, thao_tac_tai_khoan_id=thao_tac_tai_khoan_id, thao_tac_tai_khoan=thao_tac_tai_khoan)
    

