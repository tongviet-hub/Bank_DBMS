def create_tai_khoan(db: Session, tai_khoan: TaiKhoanCreate):
    db_tai_khoan = Tai_khoan(**tai_khoan.dict())
    db.add(db_tai_khoan)
    db.commit()
    db.refresh(db_tai_khoan)
    return db_tai_khoan
def get_tai_khoan(db: Session, tai_khoan_id: int):
    db_tai_khoan = db.query(Tai_khoan).filter(Tai_khoan.id == tai_khoan_id).first()
    if db_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Tài khoản không tồn tại")
    return db_tai_khoan