def create_loai_tai_khoan(db: Session, loai_tai_khoan: LoaiTaiKhoanCreate):
    db_loai_tai_khoan = Loai_tai_khoan(**loai_tai_khoan.dict())
    db.add(db_loai_tai_khoan)
    db.commit()
    db.refresh(db_loai_tai_khoan)
    return db_loai_tai_khoan
def get_loai_tai_khoan(db: Session, loai_tai_khoan_id: int):
    db_loai_tai_khoan = db.query(Loai_tai_khoan).filter(Loai_tai_khoan.id == loai_tai_khoan_id).first()
    if db_loai_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Loại tài khoản không tồn tại")
    return db_loai_tai_khoan
