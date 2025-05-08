from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()

@router.post("/phan-quyen/", response_model=schemas.PhanQuyen)
def create_phan_quyen(phan_quyen: schemas.PhanQuyenCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một phân quyền.
    """
    return crud.create_phan_quyen(db=db, phan_quyen=phan_quyen)

@router.get("/phan-quyen/", response_model=list[schemas.PhanQuyen])
def get_all_phan_quyen(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả phân quyền.
    """
    return crud.get_all_phan_quyen(db=db)

@router.get("/phan-quyen/search/", response_model=list[schemas.PhanQuyen])
def search_phan_quyen(
    phan_quyen_id: int | None = None,
    name: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm phân quyền theo ID hoặc tên.
    """
    if phan_quyen_id:
        db_phan_quyen = crud.get_phan_quyen(db=db, phan_quyen_id=phan_quyen_id)
        return [db_phan_quyen] if db_phan_quyen else []
    if name:
        db_phan_quyen = crud.get_phan_quyen(db=db, phan_quyen_name=name)
        return db_phan_quyen if db_phan_quyen else []
    raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên để tìm kiếm")

@router.delete("/phan-quyen/{phan_quyen_id}")
def delete_phan_quyen(phan_quyen_id: int, db: Session = Depends(get_db)):
    """
    Xóa phân quyền theo ID.
    """
    return crud.delete_phan_quyen(db=db, phan_quyen_id=phan_quyen_id)

@router.put("/phan-quyen/{phan_quyen_id}", response_model=schemas.PhanQuyen)
def update_phan_quyen(phan_quyen_id: int, phan_quyen: schemas.PhanQuyenCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin phân quyền.
    """
    return crud.update_phan_quyen(db=db, phan_quyen_id=phan_quyen_id, phan_quyen=phan_quyen)