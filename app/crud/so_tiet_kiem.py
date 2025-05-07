def create_so_tiet_kiem(db: Session, so_tiet_kiem: SoTietKiemCreate):
    db_so_tiet_kiem = So_tiet_kiem(**so_tiet_kiem.dict())
    db.add(db_so_tiet_kiem)
    db.commit()
    db.refresh(db_so_tiet_kiem)
    return db_so_tiet_kiem
def get_so_tiet_kiem(db: Session, so_tiet_kiem_id: int):
    db_so_tiet_kiem = db.query(So_tiet_kiem).filter(So_tiet_kiem.id == so_tiet_kiem_id).first()
    if db_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Sổ tiết kiệm không tồn tại")
    return db_so_tiet_kiem
