def create_phan_quyen(db: Session, phan_quyen: PhanQuyenCreate):
    db_phan_quyen = Phan_quyen(**phan_quyen.dict())
    db.add(db_phan_quyen)
    db.commit()
    db.refresh(db_phan_quyen)
    return db_phan_quyen
def get_phan_quyen(db: Session, phan_quyen_id: int):
    db_phan_quyen = db.query(Phan_quyen).filter(Phan_quyen.id == phan_quyen_id).first()
    if db_phan_quyen is None:
        raise HTTPException(status_code=404, detail="Phân quyền không tồn tại")
    return db_phan_quyen