def create_thao_tac_so_tiet_kiem(db: Session, thao_tac_so_tiet_kiem: ThaoTacSoTietKiemCreate):
    db_thao_tac_so_tiet_kiem = Thao_tac_so_tiet_kiem(**thao_tac_so_tiet_kiem.dict())
    db.add(db_thao_tac_so_tiet_kiem)
    db.commit()
    db.refresh(db_thao_tac_so_tiet_kiem)
    return db_thao_tac_so_tiet_kiem
def get_thao_tac_so_tiet_kiem(db: Session, thao_tac_so_tiet_kiem_id: int):
    db_thao_tac_so_tiet_kiem = db.query(Thao_tac_so_tiet_kiem).filter(Thao_tac_so_tiet_kiem.id == thao_tac_so_tiet_kiem_id).first()
    if db_thao_tac_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Thao tác sổ tiết kiệm không tồn tại")
    return db_thao_tac_so_tiet_kiem
