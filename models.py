from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime, Float, Date
from sqlalchemy.orm import relationship
from database import Base

class Khach_hang(Base):
    __tablename__ = 'Khach_hang'
    id = Column(Integer, primary_key=True,autoincrement=True)
    CCCD = Column(String(12), index=True)  # Căn cước công dân, giới hạn 12 ký tự
    Name = Column(String(100))  # Tên khách hàng, giới hạn 100 ký tự
    Ngay_sinh = Column(Date)
    Phone = Column(String(15))  # Số điện thoại, giới hạn 15 ký tự
    Email = Column(String(100))  # Email, giới hạn 100 ký tự
    Dia_chi = Column(String(255))  # Địa chỉ, giới hạn 255 ký tự

class Tai_khoan(Base):
    __tablename__ = 'Tai_khoan'
    id = Column(Integer, primary_key=True)
    Ma_chi_nhanh = Column(Integer, ForeignKey('Chi_nhanh.id'), index=True)
    Ma_khach_hang = Column(Integer, ForeignKey('Khach_hang.id'), index=True)
    Ma_tai_khoan = Column(Integer, ForeignKey('Loai_tai_khoan.id'))
    Noi_cap = Column(Date)

class Loai_tai_khoan(Base):
    __tablename__ = 'Loai_tai_khoan'
    id = Column(Integer, primary_key=True)
    Ten_loai = Column(String(50))  # Tên loại tài khoản, giới hạn 50 ký tự
    Lai_suat = Column(Float)

class Chi_nhanh(Base):
    __tablename__ = 'Chi_nhanh'
    id = Column(Integer, primary_key=True)
    Name = Column(String(100))  # Tên chi nhánh, giới hạn 100 ký tự
    Dia_chi = Column(String(255))  # Địa chỉ chi nhánh, giới hạn 255 ký tự
    Phone = Column(String(15))  # Số điện thoại chi nhánh, giới hạn 15 ký tự

class Phan_quyen(Base):
    __tablename__ = 'Phan_quyen'
    id = Column(Integer, primary_key=True)
    Ten_chuc_vu = Column(String(100))  # Tên chức vụ, giới hạn 100 ký tự
    Ten_quyen = Column(String(50))  # Tên quyền, giới hạn 50 ký tự
    Mo_ta = Column(String)  # Mô tả quyền, có thể dài, sử dụng TEXT

class Dang_nhap(Base):
    __tablename__ = 'Dang_nhap'
    id = Column(Integer, ForeignKey('Nhan_vien.id'), primary_key=True)
    Ten_dang_nhap = Column(String(50), index=True)  # Tên đăng nhập, giới hạn 50 ký tự
    Mat_khau = Column(String(255))  # Mật khẩu, giới hạn 255 ký tự

class Nhan_vien(Base):
    __tablename__ = 'Nhan_vien'
    id = Column(Integer, primary_key=True)
    Name = Column(String(100))  # Tên nhân viên, giới hạn 100 ký tự
    CCCD = Column(String(12), index=True)  # Căn cước công dân, giới hạn 12 ký tự
    Phone = Column(String(15))  # Số điện thoại nhân viên, giới hạn 15 ký tự
    Email = Column(String(100))  # Email nhân viên, giới hạn 100 ký tự
    Dia_chi = Column(String(255))  # Địa chỉ nhân viên, giới hạn 255 ký tự
    Luong = Column(Integer)
    Ma_chi_nhanh = Column(Integer, ForeignKey('Chi_nhanh.id'), index=True)
    Ma_chuc_vu = Column(Integer, ForeignKey('Phan_quyen.id'))

class Chuyen_khoan(Base):
    __tablename__ = 'Chuyen_khoan'
    id = Column(Integer, primary_key=True)
    Ma_tk_gui = Column(Integer, ForeignKey('Tai_khoan.id'), index=True)
    Ma_tk_nhan = Column(Integer, ForeignKey('Tai_khoan.id'), index=True)
    Ngay = Column(Date)
    So_tien = Column(Float)
    Noi_dung = Column(String(255))  # Nội dung chuyển khoản, giới hạn 255 ký tự

class So_tiet_kiem(Base):
    __tablename__ = 'So_tiet_kiem'
    id = Column(Integer, primary_key=True)
    Ma_nhan_vien = Column(Integer, ForeignKey('Nhan_vien.id'), index=True)
    Ma_loai_tiet_kiem = Column(Integer, ForeignKey('Loai_tiet_kiem.id'))
    Ngay_mo_so = Column(Date)
    Ngay_het_han = Column(Date)
    So_tien = Column(Float)

class Loai_tiet_kiem(Base):
    __tablename__ = 'Loai_tiet_kiem'
    id = Column(Integer, primary_key=True)
    Ten_loai = Column(String(100))  # Tên loại tiết kiệm, giới hạn 100 ký tự
    Lai_suat = Column(Float)
    Ky_han = Column(Integer)

class Thao_tac_so_tiet_kiem(Base):
    __tablename__ = 'Thao_tac_so_tiet_kiem'
    id = Column(Integer, primary_key=True)
    Ma_so_tiet_kiem = Column(Integer, ForeignKey('So_tiet_kiem.id'), index=True)
    Ma_nhan_vien = Column(Integer, ForeignKey('Nhan_vien.id'))
    Ma_thao_tac = Column(Integer, ForeignKey('Thao_tac.id'))
    Ma_khach_hang = Column(Integer, ForeignKey('Khach_hang.id'))
    Ngay_thao_tac = Column(DateTime)
    Ghi_chu = Column(String)  # Ghi chú thao tác có thể dài, sử dụng TEXT

class Thao_tac_tai_khoan(Base):
    __tablename__ = 'Thao_tac_tai_khoan'
    id = Column(Integer, primary_key=True)
    Ma_so_tai_khoan = Column(Integer, ForeignKey('Tai_khoan.id'))
    Ma_nhan_vien = Column(Integer, ForeignKey('Nhan_vien.id'))
    Ma_thao_tac = Column(Integer, ForeignKey('Thao_tac.id'))
    Ngay_thao_tac = Column(DateTime)
    Ghi_chu = Column(String)  # Ghi chú thao tác có thể dài, sử dụng TEXT

class Thao_tac(Base):
    __tablename__ = 'Thao_tac'
    id = Column(Integer, primary_key=True)
    Ten_thao_tac = Column(String(100))  # Tên thao tác, giới hạn 100 ký tự