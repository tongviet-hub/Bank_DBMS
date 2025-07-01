from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()

@router.post("/chi-nhanh/", response_model=schemas.ChiNhanh)
def create_chi_nhanh(chi_nhanh: schemas.ChiNhanh, db: Session = Depends(get_db)):
    """Tạo mới một chi nhánh."""
    existing_chi_nhanh = crud.get_chi_nhanh(db=db, chi_nhanh_name=chi_nhanh.Ten_chi_nhanh)
    if existing_chi_nhanh:
        raise HTTPException(status_code=400, detail="Chi nhánh đã tồn tại")
    return crud.create_chi_nhanh(db=db, chi_nhanh=chi_nhanh)

@router.get("/chi-nhanh/", response_model=list[schemas.ChiNhanh])
def get_all_chi_nhanh(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả các chi nhánh.
    """
    db_chi_nhanh = crud.get_all_chi_nhanh(db=db)
    return db_chi_nhanh

@router.get("/chi-nhanh/search/", response_model= list[schemas.ChiNhanh])
def search_chi_nhanh(
    chi_nhanh_id: str | None = None,
    name: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm chi nhánh theo ID hoặc tên.
    """
    if chi_nhanh_id:
        db_chi_nhanh = crud.get_chi_nhanh(db=db, chi_nhanh_id=chi_nhanh_id)
        return [db_chi_nhanh] if db_chi_nhanh else []
    if name:
        db_chi_nhanh = crud.get_chi_nhanh(db=db, chi_nhanh_name=name)
        return db_chi_nhanh
    raise HTTPException(status_code=400, detail= "Cần cung cấp id hoặc tên để tìm kiếm")

@router.delete("/chi-nhanh/{chi_nhanh_id}")
def delete_chi_nhanh(chi_nhanh_id: str, db: Session = Depends(get_db)):
    """Xóa chi nhánh theo ID.
    """
    return crud.delete_chi_nhanh(db=db, chi_nhanh_id=chi_nhanh_id)

@router.put("/chi-nhanh/{chi_nhanh_id}", response_model=schemas.ChiNhanh)
def update_chi_nhanh(chi_nhanh_id: str, chi_nhanh: schemas.ChiNhanhCreate, db: Session = Depends(get_db)):
    """Cập nhật thông tin chi nhánh."""
    return crud.update_chi_nhanh(db=db, chi_nhanh_id=chi_nhanh_id, chi_nhanh=chi_nhanh)