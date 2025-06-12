from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas
from typing import List

router = APIRouter()

@router.get("/thao-tac/", response_model=List[schemas.ThaoTac])
def get_all_thao_tac(db: Session = Depends(get_db)):
    """Danh sách thao tác"""
    return crud.get_all_thao_tac(db=db)

@router.post("/thao-tac/", response_model=schemas.ThaoTac)
def create_thao_tac(thao_tac: schemas.ThaoTac, db: Session = Depends(get_db)):
    """Tạo mới một thao tác"""
    return crud.create_thao_tac(thao_tac=thao_tac, db=db)

@router.get("/thao-tac/search", response_model=List[schemas.ThaoTac])
def search_thao_tac(
    thao_tac_id: str | None = None,
    ten_thao_tac: str | None = None,
    db: Session = Depends(get_db)
):
    """Tìm kiếm thao tác theo ID hoặc tên."""
    if thao_tac_id:
        db_thao_tac = crud.get_thao_tac(thao_tac_id=thao_tac_id, db=db)
        return [db_thao_tac] if db_thao_tac else []
    if ten_thao_tac:
        db_thao_tac = crud.get_thao_tac(thao_tac_name=ten_thao_tac, db=db)
        return db_thao_tac if db_thao_tac else []
    raise HTTPException(status_code=400, detail="Cần cung cấp ID hoặc tên để tìm kiếm")

@router.delete("/thao-tac/{thao_tac_id}")
def delete_thao_tac(thao_tac_id: str, db: Session = Depends(get_db)):
    """Xóa thao tác theo ID."""
    return crud.delete_thao_tac(thao_tac_id=thao_tac_id, db=db)

@router.put("/thao-tac/{thao_tac_id}", response_model=schemas.ThaoTac)
def update_thao_tac(thao_tac_id: str, thao_tac: schemas.ThaoTacBase, db: Session = Depends(get_db)):
    """Cập nhật thông tin thao tác."""
    return crud.update_thao_tac(thao_tac_id=thao_tac_id, thao_tac=thao_tac, db=db)