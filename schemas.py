from pydantic import BaseModel
from datetime import date

# ========== KHÁCH HÀNG ==========
class KhachHangBase(BaseModel):
    CCCD: str
    Name: str
    Ngay_sinh: date
    Phone: str
    Email: str
    Dia_chỉ: str

class KhachHangCreate(KhachHangBase):
    pass

class KhachHang(KhachHangBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== TÀI KHOẢN ==========
class TaiKhoanBase(BaseModel):
    Ma_Chi_nhanh: int
    Ma_khach_hang: int
    Ma_tai_khoan: int
    Noi_cap: date  # Thêm trường này

class TaiKhoanCreate(TaiKhoanBase):
    pass

class TaiKhoan(TaiKhoanBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== LOẠI TÀI KHOẢN ==========
class LoaiTaiKhoanBase(BaseModel):
    Ten_loai: str
    Lai_suat: float

class LoaiTaiKhoanCreate(LoaiTaiKhoanBase):
    pass

class LoaiTaiKhoan(LoaiTaiKhoanBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== CHI NHÁNH ==========
class ChiNhanhBase(BaseModel):
    Name: str
    Dia_Chi: str
    Phone: str

class ChiNhanhCreate(ChiNhanhBase):
    pass

class ChiNhanh(ChiNhanhBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== PHÂN QUYỀN ==========
class PhanQuyenBase(BaseModel):
    Ten_chuc_vu: str
    Ten_quyen: str
    Mo_ta: str

class PhanQuyenCreate(PhanQuyenBase):
    pass

class PhanQuyen(PhanQuyenBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== ĐĂNG NHẬP ==========
class DangNhapBase(BaseModel):
    Ten_dang_nhap: str
    Mat_khau: str

class DangNhapCreate(DangNhapBase):
    pass

class DangNhap(DangNhapBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== NHÂN VIÊN ==========
class NhanVienBase(BaseModel):
    Name: str
    CCCD: str
    Phone: str
    Email: str
    Dia_chỉ: str
    Luong: int
    Ma_chi_nhanh: int  # Sửa tên trường
    Ma_chuc_vu: int

class NhanVienCreate(NhanVienBase):
    pass

class NhanVien(NhanVienBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== CHUYỂN KHOẢN ==========
class ChuyenKhoanBase(BaseModel):
    Ma_tk_gui: int
    Ma_tk_nhan: int
    Ngay: date  # Sửa kiểu thành `date`
    So_tien: float
    Noi_dung: str

class ChuyenKhoanCreate(ChuyenKhoanBase):
    pass

class ChuyenKhoan(ChuyenKhoanBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== SỔ TIẾT KIỆM ==========
class SoTietKiemBase(BaseModel):
    Ma_nhan_vien: int
    Ma_loai_tich_kiem: int
    Ngay_mo_so: date
    Ngay_het_han: date
    So_tien: float

class SoTietKiemCreate(SoTietKiemBase):
    pass

class SoTietKiem(SoTietKiemBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== LOẠI TIẾT KIỆM ==========
class LoaiTietKiemBase(BaseModel):
    Ten_loai: str
    Lai_suat: float
    Ky_han: int

class LoaiTietKiemCreate(LoaiTietKiemBase):
    pass

class LoaiTietKiem(LoaiTietKiemBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== THAO TÁC SỔ TK ==========
class ThaoTacSoTietKiemBase(BaseModel):
    Ma_so_tich_kiem: int
    Ma_nhan_vien: int
    Ma_thao_tac: int  # Thêm trường này
    ma_khach_hang: int
    Ngay_thao_tac: date
    Ghi_chu: str

class ThaoTacSoTietKiemCreate(ThaoTacSoTietKiemBase):
    pass

class ThaoTacSoTietKiem(ThaoTacSoTietKiemBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== THAO TÁC TK ==========
class ThaoTacTaiKhoanBase(BaseModel):
    Ma_so_tai_khoan: int
    Ma_nhan_vien: int
    Ma_thao_tac: int  # Thêm trường này
    Ngay_thao_tac: date
    Ghi_chu: str

class ThaoTacTaiKhoanCreate(ThaoTacTaiKhoanBase):
    pass

class ThaoTacTaiKhoan(ThaoTacTaiKhoanBase):
    id: int
    class Config:
        from_attributes = True  # Đã sửa

# ========== THAO TÁC ==========
class ThaoTacBase(BaseModel):
    Ten_thao_tac: str

class ThaoTacCreate(ThaoTacBase):
    pass

class ThaoTac(ThaoTacBase):
    id: int
    class Config:
        from_attributes = True