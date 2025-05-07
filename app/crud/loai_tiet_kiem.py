def create_loai_tiet_kiem(db: Session, loai_tiet_kiem: LoaiTietKiemCreate):
    db_loai_tiet_kiem = Loai_tiet_kiem(**loai_tiet_kiem.dict())
    db.add(db_loai_tiet_kiem)
    db.commit()
    db.refresh(db_loai_tiet_kiem)
    return db_loai_tiet_kiem
def get_loai_tiet_kiem(db: Session, loai_tiet_kiem_id: int):
    db_loai_tiet_kiem = db.query(Loai_tiet_kiem).filter(Loai_tiet_kiem.id == loai_tiet_kiem_id).first()
    if db_loai_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Loại tiết kiệm không tồn tại")
    return db_loai_tiet_kiem
