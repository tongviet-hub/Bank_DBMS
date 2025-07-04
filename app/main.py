from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Annotated
import models as models
import schemas as schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import crud as crud
from routes.chi_nhanh import router as chi_nhanh_router
from routes.dang_nhap import router as dang_nhap_router
from routes.chuyen_khoan import router as chuyen_khoan_router
from routes.khach_hang import router as khach_hang_router
from routes.loai_tai_khoan import router as loai_tai_khoan_router
from routes.loai_tiet_kiem import router as loai_tiet_kiem_router
from routes.thao_tac import router as thao_tac_router
from routes.thao_tac_stk import router as thao_tac_stk_router
from routes.phan_quyen import router as phan_quyen_router
from routes.thao_tac_tk import router as thao_tac_tk_router
from routes.phan_quyen import router as phan_quyen_router
from routes.so_tiet_kiem import router as so_tiet_kiem_router
from routes.tai_khoan import router as tai_khoan_router
from routes.nhan_vien import router as nhan_vien_router
from routes.loai_tien_te import router as loai_tien_te_router
from helper.security import hash_password, verify_password
from dependencies import get_db
app = FastAPI()

# Add CORS middleware before including routers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Specify allowed methods
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=600,  # Cache preflight requests for 10 minutes
)

models.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)] 
app.include_router(chi_nhanh_router, prefix="/chi-nhanh", tags=["Chi nhánh"])
app.include_router(chuyen_khoan_router, prefix="/chuyen-khoan", tags = ["Chuyển khoản"])
app.include_router(dang_nhap_router, prefix="/dang-nhap",tags=["Đăng nhập"])
app.include_router(khach_hang_router, prefix="/khach-hang", tags=["Khách hàng"])
app.include_router(loai_tai_khoan_router, prefix="/loai-tai-khoan", tags= ["Loại tài khoản"])
app.include_router(loai_tiet_kiem_router, prefix="/loai-tiet-kiem", tags= ["Loaị tích kiệm"])
app.include_router(thao_tac_router, prefix="/thao-tac", tags=["Thao tác"])
app.include_router(thao_tac_stk_router, prefix="/thao-tac-stk", tags=["Thao tác sổ tiết kiệm"])
app.include_router(thao_tac_tk_router, prefix="/thao-tac-tk", tags=["Thao tác tài khoản"])
app.include_router(phan_quyen_router, prefix="/phan-quyen", tags=["Phân quyền"])
app.include_router(so_tiet_kiem_router, prefix="/so-tiet-kiem", tags=["Sổ tiết kiệm"])
app.include_router(tai_khoan_router, prefix="/tai-khoan", tags=["Tài khoản"])
app.include_router(nhan_vien_router, prefix="/nhan-vien", tags=["Nhân viên"])
app.include_router(loai_tien_te_router, prefix="/loai-tien-te", tags=["Loại tiền tệ"])