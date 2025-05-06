from sqlalchemy.orm import Session
from models import Khach_hang,Thao_tac, Tai_khoan
from models import Loai_tai_khoan, Chi_nhanh, Phan_quyen, Nhan_vien, Chuyen_khoan, Dang_nhap
from schemas import KhachHangCreate,ThaoTacCreate, TaiKhoanCreate, LoaiTaiKhoanCreate, ChiNhanhCreate, PhanQuyenCreate, NhanVienCreate, ChuyenKhoanCreate,DangNhapCreate
from fastapi import HTTPException
from datetime import datetime
from models import Thao_tac_so_tiet_kiem, Thao_tac_tai_khoan, So_tiet_kiem, Loai_tiet_kiem
from schemas import ThaoTacSoTietKiemCreate, ThaoTacTaiKhoanCreate, SoTietKiemCreate, LoaiTietKiemCreate
from helper import hash_password

#========== KHÁCH HÀNG ==========
def create_khach_hang(db: Session, khach_hang: KhachHangCreate):
    db_khach_hang = Khach_hang(**khach_hang.dict())
    db.add(db_khach_hang)
    db.commit()
    db.refresh(db_khach_hang)
    return db_khach_hang

def get_khach_hang(db: Session, khach_hang_id: int):
    db_khach_hang = db.query(Khach_hang).filter(Khach_hang.id == khach_hang_id).first()
    if db_khach_hang is None:
        raise HTTPException(status_code=404, detail="Khách hàng không tồn tại")
    return db_khach_hang


#========== TÀI KHOẢN ==========

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

#========== LOẠI TÀI KHOẢN ==========
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

#========== CHI NHÁNH ==========
def create_chi_nhanh(db: Session, chi_nhanh: ChiNhanhCreate):
    db_chi_nhanh = Chi_nhanh(**chi_nhanh.dict())
    db.add(db_chi_nhanh)
    db.commit()
    db.refresh(db_chi_nhanh)
    return db_chi_nhanh
def get_chi_nhanh(db: Session, chi_nhanh_id: int):
    db_chi_nhanh = db.query(Chi_nhanh).filter(Chi_nhanh.id == chi_nhanh_id).first()
    if db_chi_nhanh is None:
        raise HTTPException(status_code=404, detail="Chi nhánh không tồn tại")
    return db_chi_nhanh

#========== PHÂN QUYỀN ==========
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

#========== NHÂN VIÊN ==========
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

#========== CHUYỂN KHOẢN ==========
def create_chuyen_khoan(db: Session, chuyen_khoan: ChuyenKhoanCreate):
    db_chuyen_khoan = Chuyen_khoan(**chuyen_khoan.dict())
    db.add(db_chuyen_khoan)
    db.commit()
    db.refresh(db_chuyen_khoan)
    return db_chuyen_khoan
def get_chuyen_khoan(db: Session, chuyen_khoan_id: int):
    db_chuyen_khoan = db.query(Chuyen_khoan).filter(Chuyen_khoan.id == chuyen_khoan_id).first()
    if db_chuyen_khoan is None:
        raise HTTPException(status_code=404, detail="Chuyển khoản không tồn tại")
    return db_chuyen_khoan

#========== ĐĂNG NHẬP ==========
def create_dang_nhap(db: Session, dang_nhap: DangNhapCreate):
    # Mã hóa mật khẩu trước khi lưu
    dang_nhap.password = hash_password(dang_nhap.password)
    db_dang_nhap = Dang_nhap(**dang_nhap.dict())
    db.add(db_dang_nhap)
    db.commit()
    db.refresh(db_dang_nhap)
    return db_dang_nhap
def get_dang_nhap(db: Session, dang_nhap_id: int):
    db_dang_nhap = db.query(Dang_nhap).filter(Dang_nhap.id == dang_nhap_id).first()
    if db_dang_nhap is None:
        raise HTTPException(status_code=404, detail="Đăng nhập không tồn tại")
    return db_dang_nhap

#========== THAO TÁC SỔ TIẾT KIỆM ==========
def create_thao_tac_so_tiet_kiem(db: Session, thao_tac_so_tiet_kiem: ThaoTacSoTietKiemCreate):
    db_thao_tac_so_tiet_kiem = Thao_tac_so_tiet_kiem(**thao_tac_so_tiet_kiem.dict())
    db.add(db_thao_tac_so_tiet_kiem)
    db.commit()
    db.refresh(db_thao_tac_so_tiet_kiem)
    return db_thao_tac_so_tiet_kiem
def get_thao_tac_so_tiet_kiem(db: Session, thao_tac_so_tiet_kiem_id: int):
    db_thao_tac_so_tiet_kiem = db.query(Thao_tac_so_tiet_kiem).filter(Thao_tac_so_tiet_kiem.id == thao_tac_so_tiet_kiem_id).first()
    if db_thao_tac_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Thao tác sổ tiết kiệm không tồn tại")
    return db_thao_tac_so_tiet_kiem

#========== THAO TÁC TÀI KHOẢN ==========
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

#========== SỔ TIẾT KIỆM ==========
def create_so_tiet_kiem(db: Session, so_tiet_kiem: SoTietKiemCreate):
    db_so_tiet_kiem = So_tiet_kiem(**so_tiet_kiem.dict())
    db.add(db_so_tiet_kiem)
    db.commit()
    db.refresh(db_so_tiet_kiem)
    return db_so_tiet_kiem
def get_so_tiet_kiem(db: Session, so_tiet_kiem_id: int):
    db_so_tiet_kiem = db.query(So_tiet_kiem).filter(So_tiet_kiem.id == so_tiet_kiem_id).first()
    if db_so_tiet_kiem is None:
        raise HTTPException(status_code=404, detail="Sổ tiết kiệm không tồn tại")
    return db_so_tiet_kiem

#========== LOẠI TIẾT KIỆM ==========
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

# ========== THAO TÁC ==========
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

#========== KHÁCH HÀNG ==========
def get_all_khach_hang(db: Session):
    return db.query(Khach_hang).all()

#========== TÀI KHOẢN ==========
def get_all_tai_khoan(db: Session):
    return db.query(Tai_khoan).all()

#========== LOẠI TÀI KHOẢN ==========
def get_all_loai_tai_khoan(db: Session):
    return db.query(Loai_tai_khoan).all()

#========== CHI NHÁNH ==========
def get_all_chi_nhanh(db: Session):
    return db.query(Chi_nhanh).all()

#========== PHÂN QUYỀN ==========
def get_all_phan_quyen(db: Session):
    return db.query(Phan_quyen).all()

#========== NHÂN VIÊN ==========
def get_all_nhan_vien(db: Session):
    return db.query(Nhan_vien).all()

#========== CHUYỂN KHOẢN ==========
def get_all_chuyen_khoan(db: Session):
    return db.query(Chuyen_khoan).all()

#========== ĐĂNG NHẬP ==========
def get_all_dang_nhap(db: Session):
    return db.query(Dang_nhap).all()

#========== THAO TÁC SỔ TIẾT KIỆM ==========
def get_all_thao_tac_so_tiet_kiem(db: Session):
    return db.query(Thao_tac_so_tiet_kiem).all()

#========== THAO TÁC TÀI KHOẢN ==========
def get_all_thao_tac_tai_khoan(db: Session):
    return db.query(Thao_tac_tai_khoan).all()

#========== SỔ TIẾT KIỆM ==========
def get_all_so_tiet_kiem(db: Session):
    return db.query(So_tiet_kiem).all()

#========== LOẠI TIẾT KIỆM ==========
def get_all_loai_tiet_kiem(db: Session):
    return db.query(Loai_tiet_kiem).all()

#========== THAO TÁC ==========
def get_all_thao_tac(db: Session):
    return db.query(Thao_tac).all()

