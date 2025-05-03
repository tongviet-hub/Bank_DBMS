from pydantic import BaseModel, Field
from datetime import date
class Khach_hang(BaseModel):
    CCCD: str
    Name: str
    Ngay_sinh: str
    Phone: str
    Email: str
    Địa_chỉ: str
    Mã_Chi_nhanh: int
    
class Tai_Khoan(BaseModel):
    id: int
    Địa_chỉ: str
    Mã_Chi_nhanh: int
    Mã_khach_hang: int 
    
class Loai_tai_khoan(BaseModel):
    id: int
    Ten_loai: str
    Lai_suat: float
    
class Chi_nhanh(BaseModel):
    id: int
    Name: str
    Dia_Chi: str
    Phone: str

class Phan_quyen(BaseModel):
    id: int
    Ten_chuc_vu: str
    Ten_quyen: str
    Mo_ta: str

class Dang_nhap(BaseModel):
    id: int
    Ten_dang_nhap: str
    Mat_khau: str

class Nhan_vien(BaseModel):
    id: int
    Name: str
    CCCD: str
    Phone: str
    Email: str
    Địa_chỉ: str
    Lương: int
    Mã_Chi_nhanh: int
    Ma_chuc_vu: int
    
class Chuyen_khoan(BaseModel):
    id: int
    So_tien: float
    Thoi_gian: str
    Ma_tai_khoan: int
    Ma_chi_nhanh: int
    Mo_ta: str
    
class So_tich_kiem(BaseModel):
    id: int
    Ma_nhan_vien: int
    Ma_loai_tich_kiem: int
    Ngay_mo_so: date
    Ngay_het_han: date
    So_tien: float
    
class Loai_tich_kiem(BaseModel):
    id : int
    Ten_loai : str
    Lai_suat : float
    Ky_han : int
    
class Thao_tac_so_tich_kiem(BaseModel):
    id: int
    Ma_so_tich_kiem: int
    Ma_nhan_vien: int
    Ma_khach_hang: int
    Ngay_thao_tac: date
    Ghi_chu: str
    
class Thao_tac_tai_khoan(BaseModel):
    id: int
    Ma_so_tai_khoan: int
    Ma_nhan_vien: int
    Ngay_thao_tac: date
    Ghi_chu: str

class Thao_tac(BaseModel):
    id: int
    Ten_thao_tac: str
    
    