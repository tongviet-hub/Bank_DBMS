from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from enum import Enum

class GioiTinhEnum(str, Enum):
    NAM = "NAM"
    NU = "NU"
    KHAC = "KHAC"

class KhachHangBase(BaseModel):
    Ho_va_ten: str
    Gioi_tinh: GioiTinhEnum
    Ngay_sinh: date
    CCCD: str
    Dia_chi: str
    SDT: str
    Email: str
    Ngay_cap_nhat: Optional[date]

class KhachHangCreate(KhachHangBase):
    id: str

class KhachHang(KhachHangBase):
    id: str

    class Config:
        use_enum_values = True
        from_attributes = True

class TaiKhoanBase(BaseModel):
    Ma_khach_hang: str
    Ma_loai_tai_khoan: str
    Ma_chi_nhanh: str
    Ngay_cap: date
    Trang_thai: bool

class TaiKhoanCreate(TaiKhoanBase):
    id: str

class TaiKhoan(TaiKhoanBase):
    id: str

    class Config:
        from_attributes = True

class LoaiTaiKhoanBase(BaseModel):
    Ten_loai_tai_khoan: str
    Chuc_nang_chinh: str
    Dieu_kien_mo_so: str
    So_du_toi_thieu: float

class LoaiTaiKhoanCreate(LoaiTaiKhoanBase):
    id: str

class LoaiTaiKhoan(LoaiTaiKhoanBase):
    id: str

    class Config:
        from_attributes = True

class ChuyenKhoanBase(BaseModel):
    Ma_tk_gui: str
    Ma_tk_nhan: str
    So_tien: float
    Thoi_gian: date
    Ghi_chu: Optional[str]

class ChuyenKhoanCreate(ChuyenKhoanBase):
    id: str

class ChuyenKhoan(ChuyenKhoanBase):
    id: str

    class Config:
        from_attributes = True

class SoTietKiemBase(BaseModel):
    Ma_tai_khoan: str
    Ma_loai_tien_te: str
    Ma_loai_tiet_kiem: str
    Ngay_mo_so: date
    Ngay_het_han: date
    So_tien: float

class SoTietKiemCreate(SoTietKiemBase):
    id: str

class SoTietKiem(SoTietKiemBase):
    id: str

    class Config:
        from_attributes = True

class LoaiTietKiemBase(BaseModel):
    Ten_loai_tiet_kiem: str
    Lai_suat: float
    Ky_han: int

class LoaiTietKiemCreate(LoaiTietKiemBase):
    id: str

class LoaiTietKiem(LoaiTietKiemBase):
    id: str

    class Config:
        from_attributes = True

class LoaiTienTeBase(BaseModel):
    Ten_loai_tien_te: str
    Ty_gia: float

class LoaiTienTeCreate(LoaiTienTeBase):
    id: str

class LoaiTienTe(LoaiTienTeBase):
    id: str

    class Config:
        from_attributes = True

class NhanVienBase(BaseModel):
    Ho_va_ten: str
    Gioi_tinh: GioiTinhEnum
    Ngay_sinh: date
    CCCD: str
    Dia_chi: str
    SDT: str
    Email: str
    Ngay_cap_nhat: Optional[date]
    Ma_chuc_vu: str
    Ma_chi_nhanh: str

class NhanVienCreate(NhanVienBase):
    id: str

class NhanVien(NhanVienBase):
    id: str
    tuoi: int

    class Config:
        from_attributes = True

class ChiNhanhCreate(BaseModel):
    Ten_chi_nhanh: str
    Dia_chi: str
    SDT: str

class ChiNhanh(ChiNhanhCreate):
    id: str

    class Config:
        from_attributes = True

class PhanQuyenBase(BaseModel):
    Ten_chuc_vu: str
    Ten_quyen: str
    Mo_ta: Optional[str]

class PhanQuyenCreate(PhanQuyenBase):
    id: str

class PhanQuyen(PhanQuyenBase):
    id: str

    class Config:
        from_attributes = True

class DangNhapBase(BaseModel):
    Ten_dang_nhap: str
    Mat_khau: str

class DangNhapCreate(DangNhapBase):
    id: str

class DangNhap(DangNhapBase):
    id: str

    class Config:
        from_attributes = True

class ThaoTacSoTietKiemBase(BaseModel):
    Ma_so_tiet_kiem: str
    Ma_nhan_vien: str
    Ma_thao_tac: str
    Ma_khach_hang: str
    Ngay_thuc_hien: datetime
    Ghi_chu: Optional[str]

class ThaoTacSoTietKiemCreate(ThaoTacSoTietKiemBase):
    id: str

class ThaoTacSoTietKiem(ThaoTacSoTietKiemBase):
    id: str

    class Config:
        from_attributes = True

class ThaoTacTaiKhoanBase(BaseModel):
    Ma_nhan_vien: str
    Ma_tai_khoan: str
    Ma_thao_tac: str
    Ngay_thuc_hien: datetime
    Ghi_chu: Optional[str]

class ThaoTacTaiKhoanCreate(ThaoTacTaiKhoanBase):
    id: str

class ThaoTacTaiKhoan(ThaoTacTaiKhoanBase):
    id: str

    class Config:
        from_attributes = True

class ThaoTacBase(BaseModel):
    Ten_thao_tac: str

class ThaoTacCreate(ThaoTacBase):
    id: str

class ThaoTac(ThaoTacBase):
    id: str

    class Config:
        from_attributes = True