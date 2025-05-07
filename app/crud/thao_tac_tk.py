def create_thao_tac_tai_khoan(db: Session, thao_tac_tai_khoan: ThaoTacTaiKhoanCreate):
    db_thao_tac_tai_khoan = Thao_tac_tai_khoan(**thao_tac_tai_khoan.dict())
    db.add(db_thao_tac_tai_khoan)
    db.commit()
    db.refresh(db_thao_tac_tai_khoan)
    return db_thao_tac_tai_khoan
def get_thao_tac_tai_khoan(db: Session, thao_tac_tai_khoan_id: int):
    db_thao_tac_tai_khoan = db.query(Thao_tac_tai_khoan).filter(Thao_tac_tai_khoan.id == thao_tac_tai_khoan_id).first()
    if db_thao_tac_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Thao tác tài khoản không tồn tại")
    return db_thao_tac_tai_khoan
