
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey,DateTime, Float,Date
from sqlalchemy.orm import relationship
from database import Base

class Khach_hang(Base):
    __tablename__ = 'Khach_hang'
    CCCD = Column(String, primary_key=True, index=True)
    Name = Column(String, index=True)
    Ngay_sinh = Column(Date, index=True)
    Phone = Column(String, index=True)
    Email = Column(String, index=True)
    Địa_chỉ = Column(String, index=True)
    Mã_Chi_nhanh = Column(Integer, ForeignKey('Chi_nhanh.id'))
    
class Tai_Khoan(Base):
    __tablename__ = 'Accounts'
    id = Column(Integer, primary_key=True, index=True)
    Địa_chỉ = Column(String, index=True)
    Mã_Chi_nhanh = Column(Integer, ForeignKey('Chi_nhanh.id'))
    Mã_khach_hang = Column(Integer, ForeignKey('Khach_hang.id'))
    
class Loai_tai_khoan(Base):
    __tablename__ = 'Loai_tai_khoan'
    id = Column(Integer, primary_key=True, index=True)
    Ten_loai = Column(String, index=True)
    Lai_suat = Column(Float, index=True) 
    
class Chi_nhanh(Base):
    __tablename__ = 'Chi_nhanh'
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    Dia_Chi = Column(String, index=True)
    Phone = Column(String, index=True)

class Phan_quyen(Base):
    __tablename__ = 'Phan_quyen'
    id = Column(Integer, index=True)
    Ten_chuc_vu = Column(String, index=True)
    Ten_quyen = Column(String, index=True)
    Mo_ta = Column(String, index=True)

class Nhan_vien(Base):
    __tablename__ = 'Nhan_vien'
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    CCCD = Column(String, index=True)
    Phone = Column(String, index=True)
    Email = Column(String, index=True)
    Địa_chỉ = Column(String, index=True)
    Lương = Column(Integer, index=True)
    Mã_Chi_nhanh = Column(Integer, ForeignKey('Chi_nhanh.id'))
    Ma_chuc_vu = Column(Integer, ForeignKey('Phan_quyen.id'))
    


class Chuyen_khoan(Base):
    __tablename__ = 'Chuyen_khoan'
    id = Column(Integer, primary_key=True, index=True)
    Mã_TK_gui = Column(Integer, ForeignKey('Accounts.id'))
    Mã_TK_nhan = Column(Integer, ForeignKey('Accounts.id'))
    Ngày = Column(DateTime, index=True)
    Số_tiền = Column(Float, index=True)
    Nội_dung = Column(String, index=True)
    
class so_tich_kiem(Base):
    __tablename__ = 'So_tich_kiem'
    id = Column(Integer, primary_key=True, index =True)
    Ma_nhan_vien = Column(Integer, ForeignKey = 'Nhan_vien.id')
    Ma_loai_tich_kiem = Column(Integer, ForeignKey = 'Loai_tich_kiem.id')
    Ngay_mo_so = Column(Date)
    Ngay_het_han = Column(Date)
    So_tien = Column(Float)
    
class Loai_tich_kiem(Base):
    __tablename__ = 'Loai_tich_kiem'
    id = Column(Integer, primary_key=True, index=True)
    Ten_loai = Column(String, index=True)
    Lai_suat = Column(Float, index=True)
    Ky_han = Column(Integer, index=True)
    
class Thao_tac_so_tich_kiem(Base):
    __tablename__ = 'Thao_tac_so_tich_kiem'
    id = Column(Integer, primary_key=True, index=True)
    Ma_so_tich_kiem = Column(Integer, ForeignKey('So_tich_kiem.id'))
    Ma_nhan_vien = Column(Integer, ForeignKey('Nhan_vien.id'))
    Ma_thao_tac = Column(Integer, ForeignKey('Thao_tac.id'))
    Ma_khach_hang = Column(Integer, ForeignKey('Khach_hang.id'))
    Ngay_thao_tac = Column(DateTime, index=True)
    Ghi_chu = Column(String, index=True)
    
class Thao_tac_tai_khoan(Base):
    __tablename__ = 'Thao_tac_tai_khoan'
    id = Column(Integer, primary_key=True, index=True)
    Ma_so_tai_khoan = Column(Integer, ForeignKey('Accounts.id'))
    Ma_nhan_vien = Column(Integer, ForeignKey('Nhan_vien.id'))
    Ma_thao_tac = Column(Integer, ForeignKey('Thao_tac.id'))
    Ngay_thao_tac = Column(DateTime, index=True)
    Ghi_chu = Column(String, index=True)
    
class Thao_tac(Base):
    __tablename__ = 'Thao_tac'
    id = Column(Integer, primary_key=True, index=True)
    Ten_thao_tac = Column(String, index=True)
    
