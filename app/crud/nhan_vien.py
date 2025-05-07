


def create_nhan_vien(db: Session, nhan_vien: NhanVienCreate):
    db_nhan_vien = Nhan_vien(**nhan_vien.dict())
    db.add(db_nhan_vien)
    db.commit()
    db.refresh(db_nhan_vien)
    return db_nhan_vien
def get_nhan_vien(db: Session, nhan_vien_id: int):
    db_nhan_vien = db.query(Nhan_vien).filter(Nhan_vien.id == nhan_vien_id).first()
    if db_nhan_vien is None:
        raise HTTPException(status_code=404, detail="Nhân viên không tồn tại")
    return db_nhan_vien
