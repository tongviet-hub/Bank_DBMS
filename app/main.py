
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import app.models as models,schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from helper import verify_password
import app.crud as crud
from app.helper.security import hash_password, verify_password
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)] 

#==========THAO TAC==========
@app.post("/thao-tac/", response_model=schemas.ThaoTac)
def create_thao_tac(thao_tac: schemas.ThaoTacCreate, db: Session = Depends(get_db)):
    return crud.create_thao_tac(db=db, thao_tac=thao_tac)

@app.delete("/thao-tac/{thao_tac_id}")
def delete_thao_tac(thao_tac_id: int, db: Session = Depends(get_db)):
    return crud.delete_thao_tac(db=db, thao_tac_id=thao_tac_id)

#==========KHACH HANG==========
@app.post("/khach-hang/", response_model=schemas.KhachHang)
def create_khach_hang(khach_hang: schemas.KhachHangCreate, db: Session = Depends(get_db)):
    return crud.create_khach_hang(db=db, khach_hang=khach_hang)

@app.get("/khach-hang/{khach_hang_id}", response_model=schemas.KhachHang)
def get_khach_hang(khach_hang_id: int, db: Session = Depends(get_db)):
    db_khach_hang = crud.get_khach_hang(db=db, khach_hang_id=khach_hang_id)
    if db_khach_hang is None:
        raise HTTPException(status_code=404, detail="Khách hàng không tồn tại")
    return db_khach_hang

#========== TÀI KHOẢN ==========
@app.post("/tai-khoan/", response_model=schemas.TaiKhoan)
def create_tai_khoan(tai_khoan: schemas.TaiKhoanCreate,db: Session = Depends(get_db)):
    return crud.create_tai_khoan(db=db, tai_khoan=tai_khoan)

@app.get("/tai-khoan/{tai_khoan_id}",response_model=schemas.TaiKhoan)
def get_tai_khoan(tai_khoan_id: int, db: Session = Depends(get_db)):
    db_tai_khoan = crud.get_tai_khoan(db=db, tai_khoan_id=tai_khoan_id)
    if db_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Tài khoản không tồn tại")
    return db_tai_khoan

#========== LOẠI TÀI KHOẢN ==========
@app.post("/loai-tai-khoan/", response_model=schemas.LoaiTaiKhoan)
def create_loai_tai_khoan(loai_tai_khoan: schemas.LoaiTaiKhoanCreate, db: Session = Depends(get_db)):
    return crud.create_loai_tai_khoan(db=db, loai_tai_khoan=loai_tai_khoan)

@app.get("/loai-tai-khoan/{loai_tai_khoan_id}", response_model=schemas.LoaiTaiKhoan)
def get_loai_tai_khoan(loai_tai_khoan_id: int, db: Session = Depends(get_db)):
    db_loai_tai_khoan = crud.get_loai_tai_khoan(db=db, loai_tai_khoan_id=loai_tai_khoan_id)
    if db_loai_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Loại tài khoản không tồn tại")
    return db_loai_tai_khoan

#========== CHI NHÁNH ==========
@app.post("/chi-nhanh/", response_model=schemas.ChiNhanh)
def create_chi_nhanh(chi_nhanh: schemas.ChiNhanhCreate, db: Session = Depends(get_db)):
    return crud.create_chi_nhanh(db=db, chi_nhanh=chi_nhanh)

@app.get("/chi-nhanh/{chi_nhanh_id}", response_model=schemas.ChiNhanh)
def get_chi_nhanh(chi_nhanh_id: int, db: Session = Depends(get_db)):
    db_chi_nhanh = crud.get_chi_nhanh(db=db, chi_nhanh_id=chi_nhanh_id)
    if db_chi_nhanh is None:
        raise HTTPException(status_code=404, detail="Chi nhánh không tồn tại")
    return db_chi_nhanh

#========== PHÂN QUYỀN ==========
@app.post("/phan-quyen/", response_model=schemas.PhanQuyen)
def create_phan_quyen(phan_quyen: schemas.PhanQuyenCreate, db: Session = Depends(get_db)):
    return crud.create_phan_quyen(db=db, phan_quyen=phan_quyen)

@app.get("/phan-quyen/{phan_quyen_id}", response_model=schemas.PhanQuyen)
def get_phan_quyen(phan_quyen_id: int, db: Session = Depends(get_db)):
    db_phan_quyen = crud.get_phan_quyen(db=db, phan_quyen_id=phan_quyen_id)
    if db_phan_quyen is None:
        raise HTTPException(status_code=404, detail="Phân quyền không tồn tại")
    return db_phan_quyen

#========== NHÂN VIÊN ==========
@app.post("/nhan-vien/", response_model=schemas.NhanVien)
def create_nhan_vien(nhan_vien: schemas.NhanVienCreate, db: Session = Depends(get_db)):
    return crud.create_nhan_vien(db=db, nhan_vien=nhan_vien)

@app.get("/nhan-vien/{nhan_vien_id}", response_model=schemas.NhanVien)
def get_nhan_vien(nhan_vien_id: int, db: Session = Depends(get_db)):
    db_nhan_vien = crud.get_nhan_vien(db=db, nhan_vien_id=nhan_vien_id)
    if db_nhan_vien is None:
        raise HTTPException(status_code=404, detail="Nhân viên không tồn tại")
    return db_nhan_vien

#========== KHÁCH HÀNG ==========
@app.post("/khach-hang/", response_model=schemas.KhachHang)
def create_khach_hang(khach_hang: schemas.KhachHangCreate, db: Session = Depends(get_db)):
    return crud.create_khach_hang(db=db, khach_hang=khach_hang)

@app.get("/khach-hang/{khach_hang_id}", response_model=schemas.KhachHang)
def get_khach_hang(khach_hang_id: int, db: Session = Depends(get_db)):
    db_khach_hang = crud.get_khach_hang(db=db, khach_hang_id=khach_hang_id)
    if db_khach_hang is None:
        raise HTTPException(status_code=404, detail="Khách hàng không tồn tại")
    return db_khach_hang

#==========Thao tác tai khoan==========
@app.post("/thao-tac-tai-khoan/", response_model=schemas.ThaoTacTaiKhoan)
def create_thao_tac_tai_khoan(thao_tac_tai_khoan: schemas.ThaoTacTaiKhoanCreate, db: Session = Depends(get_db)):
    return crud.create_thao_tac_tai_khoan(db=db, thao_tac_tai_khoan=thao_tac_tai_khoan)

@app.get("/thao-tac-tai-khoan/{thao_tac_tai_khoan_id}", response_model=schemas.ThaoTacTaiKhoan)
def get_thao_tac_tai_khoan(thao_tac_tai_khoan_id: int, db: Session = Depends(get_db)):
    db_thao_tac_tai_khoan = crud.get_thao_tac_tai_khoan(db=db, thao_tac_tai_khoan_id=thao_tac_tai_khoan_id)
    if db_thao_tac_tai_khoan is None:
        raise HTTPException(status_code=404, detail="Thao tác tài khoản không tồn tại")
    return db_thao_tac_tai_khoan

#========== SO TICH KIEM ==========
@app.post("/so-tich-kiem/", response_model=schemas.SoTietKiem)
def create_so_tiet_kiem(so_tiet_kiem: schemas.SoTietKiemCreate, db: Session = Depends(get_db)):
    return crud.create_so_tiet_kiem(db=db, so_tiet_kiem=so_tiet_kiem)

@app.get("/so-tich-kiem/{so_tiet_kiem_id}", response_model=schemas.SoTietKiem)
def get_so_tiet_kiem(so_tiet_kiem_id: int, db: Session = Depends(get_db)):
    db_so_tiet_kiem = crud.get_so_tiet_kiem(db=db, so_tiet_kiem_id=so_tiet_kiem_id)
    if db_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Sổ tiết kiệm không tồn tại")
    return db_so_tiet_kiem

#========== DANG NHAP ==========
@app.post("/dang-nhap/", response_model=schemas.DangNhap)
def create_dang_nhap(dang_nhap: schemas.DangNhapCreate, db: Session = Depends(get_db)):
    return crud.create_dang_nhap(db=db, dang_nhap=dang_nhap)

@app.get("/dang-nhap/{dang_nhap_id}", response_model=schemas.DangNhap)
def get_dang_nhap(dang_nhap_id: int, db: Session = Depends(get_db)):
    db_dang_nhap = crud.get_dang_nhap(db=db, dang_nhap_id=dang_nhap_id)
    if db_dang_nhap is None:
        raise HTTPException(status_code=404, detail="Đăng nhập không tồn tại")
    return db_dang_nhap

@app.post("/dang-nhap/verify/")
def verify_dang_nhap(username: str, password: str, db: Session = Depends(get_db)):
    db_dang_nhap = db.query(models.Dang_nhap).filter(models.Dang_nhap.Ten_dang_nhap == username).first()
    if not db_dang_nhap or not verify_password(password, db_dang_nhap.password):
        raise HTTPException(status_code=401, detail="Tên đăng nhập hoặc mật khẩu không đúng")
    return {"message": "Đăng nhập thành công"}

#========== CHUYEN KHOAN ==========
@app.post("/chuyen-khoan/", response_model=schemas.ChuyenKhoan)
def create_chuyen_khoan(chuyen_khoan: schemas.ChuyenKhoanCreate, db: Session = Depends(get_db)):
    return crud.create_chuyen_khoan(db=db, chuyen_khoan=chuyen_khoan)

@app.get("/chuyen-khoan/{chuyen_khoan_id}", response_model=schemas.ChuyenKhoan)
def get_chuyen_khoan(chuyen_khoan_id: int, db: Session = Depends(get_db)):
    db_chuyen_khoan = crud.get_chuyen_khoan(db=db, chuyen_khoan_id=chuyen_khoan_id)
    if db_chuyen_khoan is None:
        raise HTTPException(status_code=404, detail="Chuyển khoản không tồn tại")
    return db_chuyen_khoan

#========== LOAI TICH KIEM ==========
@app.post("/loai-tiet-kiem/", response_model=schemas.LoaiTietKiem)
def create_loai_tiet_kiem(loai_tiet_kiem: schemas.LoaiTietKiemCreate, db: Session = Depends(get_db)):
    return crud.create_loai_tiet_kiem(db=db, loai_tiet_kiem=loai_tiet_kiem)

@app.get("/loai-tiet-kiem/{loai_tiet_kiem_id}", response_model=schemas.LoaiTietKiem)
def get_loai_tiet_kiem(loai_tiet_kiem_id: int, db: Session = Depends(get_db)):
    db_loai_tiet_kiem = crud.get_loai_tiet_kiem(db=db, loai_tiet_kiem_id=loai_tiet_kiem_id)
    if db_loai_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Loại tiết kiệm không tồn tại")
    return db_loai_tiet_kiem

#========== THAO TAC SO TIET KIEM ==========
@app.post("/thao-tac-so-tiet-kiem/", response_model=schemas.ThaoTacSoTietKiem)
def create_thao_tac_so_tiet_kiem(thao_tac_so_tiet_kiem: schemas.ThaoTacSoTietKiemCreate, db: Session = Depends(get_db)):
    return crud.create_thao_tac_so_tiet_kiem(db=db, thao_tac_so_tiet_kiem=thao_tac_so_tiet_kiem)

@app.get("/thao-tac-so-tiet-kiem/{thao_tac_so_tiet_kiem_id}", response_model=schemas.ThaoTacSoTietKiem)
def get_thao_tac_so_tiet_kiem(thao_tac_so_tiet_kiem_id: int, db: Session = Depends(get_db)):
    db_thao_tac_so_tiet_kiem = crud.get_thao_tac_so_tiet_kiem(db=db, thao_tac_so_tiet_kiem_id=thao_tac_so_tiet_kiem_id)
    if db_thao_tac_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Thao tác sổ tiết kiệm không tồn tại")
    return db_thao_tac_so_tiet_kiem


#========== KHÁCH HÀNG ==========
@app.get("/all-khach-hang/", response_model=List[schemas.KhachHang], operation_id="get_all_khach_hang")
def get_all_khach_hang(db: Session = Depends(get_db)):
    return crud.get_all_khach_hang(db=db)

#========== TÀI KHOẢN ==========
@app.get("/all-tai-khoan/", response_model=List[schemas.TaiKhoan], operation_id="get_all_tai_khoan")
def get_all_tai_khoan(db: Session = Depends(get_db)):
    return crud.get_all_tai_khoan(db=db)

#========== LOẠI TÀI KHOẢN ==========
@app.get("/all-loai-tai-khoan/", response_model=List[schemas.LoaiTaiKhoan], operation_id="get_all_loai_tai_khoan")
def get_all_loai_tai_khoan(db: Session = Depends(get_db)):
    return crud.get_all_loai_tai_khoan(db=db)

#========== CHI NHÁNH ==========
@app.get("/all-chi-nhanh/", response_model=List[schemas.ChiNhanh], operation_id="get_all_chi_nhanh")
def get_all_chi_nhanh(db: Session = Depends(get_db)):
    return crud.get_all_chi_nhanh(db=db)

#========== PHÂN QUYỀN ==========
@app.get("/all-phan-quyen/", response_model=List[schemas.PhanQuyen], operation_id="get_all_phan_quyen")
def get_all_phan_quyen(db: Session = Depends(get_db)):
    return crud.get_all_phan_quyen(db=db)

#========== NHÂN VIÊN ==========
@app.get("/all-nhan-vien/", response_model=List[schemas.NhanVien], operation_id="get_all_nhan_vien")
def get_all_nhan_vien(db: Session = Depends(get_db)):
    return crud.get_all_nhan_vien(db=db)

#========== CHUYỂN KHOẢN ==========
@app.get("/all-chuyen-khoan/", response_model=List[schemas.ChuyenKhoan], operation_id="get_all_chuyen_khoan")
def get_all_chuyen_khoan(db: Session = Depends(get_db)):
    return crud.get_all_chuyen_khoan(db=db)

#========== ĐĂNG NHẬP ==========
@app.get("/all-dang-nhap/", response_model=List[schemas.DangNhap], operation_id="get_all_dang_nhap")
def get_all_dang_nhap(db: Session = Depends(get_db)):
    return crud.get_all_dang_nhap(db=db)

#========== THAO TÁC SỔ TIẾT KIỆM ==========
@app.get("/all-thao-tac-so-tiet-kiem/", response_model=List[schemas.ThaoTacSoTietKiem], operation_id="get_all_thao_tac_so_tiet_kiem")
def get_all_thao_tac_so_tiet_kiem(db: Session = Depends(get_db)):
    return crud.get_all_thao_tac_so_tiet_kiem(db=db)

#========== THAO TÁC TÀI KHOẢN ==========
@app.get("/all-thao-tac-tai-khoan/", response_model=List[schemas.ThaoTacTaiKhoan], operation_id="get_all_thao_tac_tai_khoan")
def get_all_thao_tac_tai_khoan(db: Session = Depends(get_db)):
    return crud.get_all_thao_tac_tai_khoan(db=db)

#========== SỔ TIẾT KIỆM ==========
@app.get("/all-so-tiet-kiem/", response_model=List[schemas.SoTietKiem], operation_id="get_all_so_tiet_kiem")
def get_all_so_tiet_kiem(db: Session = Depends(get_db)):
    return crud.get_all_so_tiet_kiem(db=db)

#========== LOẠI TIẾT KIỆM ==========
@app.get("/all-loai-tiet-kiem/", response_model=List[schemas.LoaiTietKiem], operation_id="get_all_loai_tiet_kiem")
def get_all_loai_tiet_kiem(db: Session = Depends(get_db)):
    return crud.get_all_loai_tiet_kiem(db=db)

#========== THAO TÁC ==========
@app.get("/all-thao-tac/", response_model=List[schemas.ThaoTac], operation_id="get_all_thao_tac")
def get_all_thao_tac(db: Session = Depends(get_db)):
    return crud.get_all_thao_tac(db=db)