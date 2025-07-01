from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()
@router.post("/loai-tien-te/", response_model=schemas.LoaiTienTe)
def create_loai_tien_te(loai_tien_te: schemas.LoaiTienTeCreate, db: Session = Depends(get_db)):
    """
    Tạo mới một loại tiền tệ.
    """
    return crud.create_loai_tien_te(db=db, loai_tien_te=loai_tien_te)

@router.get("/loai-tien-te/", response_model=list[schemas.LoaiTienTe])
def get_all_loai_tien_te(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả các loại tiền tệ.
    """
    db_loai_tien_te = crud.get_all_loai_tien_te(db=db)
    return db_loai_tien_te

@router.get("/loai-tien-te/search/", response_model=list[schemas.LoaiTienTe])
def search_loai_tien_te(
    loai_tien_te_id: str | None = None,
    name: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Tìm kiếm loại tiền tệ theo ID hoặc tên.
    """
    if loai_tien_te_id:
        db_loai_tien_te = crud.get_loai_tien_te(db=db, loai_tien_te_id=loai_tien_te_id)
        return [db_loai_tien_te] if db_loai_tien_te else []
    if name:
        db_loai_tien_te = crud.get_loai_tien_te(db=db, loai_tien_te_name=name)
        return db_loai_tien_te
    raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên để tìm kiếm")

@router.delete("/loai-tien-te/{loai_tien_te_id}")
def delete_loai_tien_te(loai_tien_te_id: str, db: Session = Depends(get_db)):
    """
    Xóa loại tiền tệ theo ID.
    """
    return crud.delete_loai_tien_te(db=db, loai_tien_te_id=loai_tien_te_id)
@router.put("/loai-tien-te/{loai_tien_te_id}", response_model=schemas.LoaiTienTe)
def update_loai_tien_te(loai_tien_te_id: str, loai_tien_te: schemas.LoaiTienTeCreate, db: Session = Depends(get_db)):
    """
    Cập nhật thông tin loại tiền tệ.
    """
    return crud.update_loai_tien_te(db=db, loai_tien_te_id=loai_tien_te_id, loai_tien_te=loai_tien_te)

