
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models,schemas,crud
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import crud
app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)] 

# @app.post("/Questions/")
# async def create_question(question: QuestionBase, db: db_dependency):
#     db_question = db.query(models.Question).filter(models.Question.question_text == question.question_text).first()
#     if db_question:
#         raise HTTPException(status_code=400, detail="Question already exists")

#     db_question = models.Question(question_text=question.question_text)
#     db.add(db_question)

#     # Thêm lựa chọn cho câu hỏi
#     for choice in question.choices:
#         db_choice = models.Choice(choice_text=choice.choice_text, 
#                                   is_correct=choice.is_correct, 
#                                   question_id=db_question.id)
#         db.add(db_choice)
    
#     db.commit()
#     db.refresh(db_question)

#     return {"question_text": db_question.question_text, 
#             "choices": [{"choice_text": choice.choice_text, "is_correct": choice.is_correct} for choice in db_question.choices]}



# @app.post("/khachhang/", response_model=schemas.KhachHang)
# def them_khach_hang(khach_hang: schemas.KhachHangCreate, db: Session = Depends(get_db)):
#     # Kiểm tra xem khách hàng có bị trùng CCCD không (nếu muốn)
#     db_khach = db.query(models.Khach_hang).filter(models.Khach_hang.CCCD == khach_hang.CCCD).first()
#     if db_khach:
#         raise HTTPException(status_code=400, detail="Khách hàng đã tồn tại")
    
#     return crud.create_khach_hang(db=db, khach_hang=khach_hang)

@app.post("/thao-tac/", response_model=schemas.ThaoTac)
def create_thao_tac(thao_tac: schemas.ThaoTacCreate, db: Session = Depends(get_db)):
    return crud.create_thao_tac(db=db, thao_tac=thao_tac)
