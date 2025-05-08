from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
import schemas

router = APIRouter()

@router.get("/thao-tac-stk/", response_model=list[schemas.ThaoTac])
def get_all_thao_tac_stk(db: Session = Depends(get_db)):
    """Danh sách thao tác sổ tiết kiệm"""
    return crud.get_all_thao_tac_so_tiet_kiem(db=db)

@router.post("/thao-tac-stk/", response_model=schemas.ThaoTac)
def create_thao_tac_stk(thao_tac_stk: schemas.ThaoTacSoTietKiemCreate, db: Session = Depends(get_db)):
    """Tạo thao tác sổ tiết kiệm"""
    return crud.create_thao_tac_so_tiet_kiem(db=db, thao_tac_so_tiet_kiem=thao_tac_stk)

@router.get("/thao-tac-stk/{thao_tac_stk_id}", response_model=schemas.ThaoTac)
def get_thao_tac_stk(thao_tac_stk_id: int, db: Session = Depends(get_db)):
    """Lấy thông tin thao tác sổ tiết kiệm theo ID"""
    return crud.get_thao_tac_so_tiet_kiem(db=db, thao_tac_so_tiet_kiem_id=thao_tac_stk_id)

@router.delete("/thao-tac-stk/{thao_tac_stk_id}", response_model=dict)
def delete_thao_tac_stk(thao_tac_stk_id: int, db: Session = Depends(get_db)):
    """Xóa thao tác sổ tiết kiệm theo ID"""
    return crud.delete_thao_tac_so_tiet_kiem(db=db, thao_tac_so_tiet_kiem_id=thao_tac_stk_id)

@router.put("/thao-tac-stk/{thao_tac_stk_id}", response_model=schemas.ThaoTac)
def update_thao_tac_stk(thao_tac_stk_id: int, thao_tac_stk: schemas.ThaoTacSoTietKiemCreate, db: Session = Depends(get_db)):
    """Cập nhật thao tác sổ tiết kiệm"""
    return crud.update_thao_tac_so_tiet_kiem(db=db, thao_tac_so_tiet_kiem_id=thao_tac_stk_id, thao_tac_so_tiet_kiem=thao_tac_stk)