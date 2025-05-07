def create_thao_tac(db: Session, thao_tac: ThaoTacCreate):
    db_thao_tac = Thao_tac(**thao_tac.dict())
    db.add(db_thao_tac)
    db.commit()
    db.refresh(db_thao_tac)
    return db_thao_tac

def delete_thao_tac(db: Session, thao_tac_id: int):
    db_thao_tac = db.query(Thao_tac).filter(Thao_tac.id == thao_tac_id).first()
    if db_thao_tac is None:
        raise HTTPException(status_code=404, detail="Thao tác không tồn tại")
    db.delete(db_thao_tac)
    db.commit()
    return {"message": "Thao tác đã được xóa thành công"}