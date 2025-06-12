from sqlalchemy import Column, Boolean, String, ForeignKey, DateTime, Float, Date, Text, Enum, Integer
from sqlalchemy.orm import relationship
from datetime import date
from database import Base
import enum

class GioiTinhEnum(enum.Enum):
    NAM = "NAM"
    NU = "NU"
    KHAC = "KHAC"

class Khach_hang(Base):
    __tablename__ = 'Khach_hang'
    id = Column(String(10), primary_key=True)
    Ho_va_ten = Column(String(100), nullable=False)
    Gioi_tinh = Column(Enum(GioiTinhEnum), nullable=False)
    Ngay_sinh = Column(Date, nullable=False)
    CCCD = Column(String(12), index=True, unique=True, nullable=False)
    Dia_chi = Column(String(255), nullable=False)
    SDT = Column(String(15), unique=True, nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    Ngay_cap_nhat = Column(Date)

    tai_khoans = relationship("Tai_khoan", back_populates="khach_hang")
    thao_tac_so_tiet_kiems = relationship("Thao_tac_so_tiet_kiem", back_populates="khach_hang")

    @property
    def tuoi(self):
        today = date.today()
        return today.year - self.Ngay_sinh.year - (
            (today.month, today.day) < (self.Ngay_sinh.month, self.Ngay_sinh.day)
        )

class Tai_khoan(Base):
    __tablename__ = 'Tai_khoan'
    id = Column(String(10), primary_key=True)
    Ma_khach_hang = Column(String(10), ForeignKey('Khach_hang.id'), index=True, nullable=False)
    Ma_loai_tai_khoan = Column(String(10), ForeignKey('Loai_tai_khoan.id'), nullable=False)
    Ma_chi_nhanh = Column(String(10), ForeignKey('Chi_nhanh.id'), index=True, nullable=False)
    Ngay_cap = Column(Date, nullable=False)
    Trang_thai = Column(Boolean, default=True, nullable=False)

    khach_hang = relationship("Khach_hang", back_populates="tai_khoans")
    loai_tai_khoan = relationship("Loai_tai_khoan", back_populates="tai_khoans")
    chi_nhanh = relationship("Chi_nhanh", back_populates="tai_khoans")
    so_tiet_kiems = relationship("So_tiet_kiem", back_populates="tai_khoan")
    chuyen_khoan_gui = relationship("Chuyen_khoan", foreign_keys="[Chuyen_khoan.Ma_tk_gui]", back_populates="tai_khoan_gui")
    chuyen_khoan_nhan = relationship("Chuyen_khoan", foreign_keys="[Chuyen_khoan.Ma_tk_nhan]", back_populates="tai_khoan_nhan")
    thao_tac_tai_khoans = relationship("Thao_tac_tai_khoan", back_populates="tai_khoan")

class Loai_tai_khoan(Base):
    __tablename__ = 'Loai_tai_khoan'
    id = Column(String(10), primary_key=True)
    Ten_loai_tai_khoan = Column(String(50), nullable=False)
    Chuc_nang_chinh = Column(String(255), nullable=False)
    Dieu_kien_mo_so = Column(String(255), nullable=False)
    So_du_toi_thieu = Column(Float, nullable=False)

    tai_khoans = relationship("Tai_khoan", back_populates="loai_tai_khoan")

class Chuyen_khoan(Base):
    __tablename__ = 'Chuyen_khoan'
    id = Column(String(10), primary_key=True)
    Ma_tk_gui = Column(String(10), ForeignKey('Tai_khoan.id'), index=True, nullable=False)
    Ma_tk_nhan = Column(String(10), ForeignKey('Tai_khoan.id'), index=True, nullable=False)
    So_tien = Column(Float, nullable=False)
    Thoi_gian = Column(Date, nullable=False)
    Ghi_chu = Column(Text)

    tai_khoan_gui = relationship("Tai_khoan", foreign_keys=[Ma_tk_gui], back_populates="chuyen_khoan_gui")
    tai_khoan_nhan = relationship("Tai_khoan", foreign_keys=[Ma_tk_nhan], back_populates="chuyen_khoan_nhan")

class So_tiet_kiem(Base):
    __tablename__ = 'So_tiet_kiem'
    id = Column(String(10), primary_key=True)
    Ma_tai_khoan = Column(String(10), ForeignKey('Tai_khoan.id'), index=True, nullable=False)
    Ma_loai_tien_te = Column(String(10), ForeignKey('Loai_tien_te.id'), nullable=False)
    Ma_loai_tiet_kiem = Column(String(10), ForeignKey('Loai_tiet_kiem.id'), nullable=False)
    Ngay_mo_so = Column(Date, nullable=False)
    Ngay_het_han = Column(Date, nullable=False)
    So_tien = Column(Float, nullable=False)

    tai_khoan = relationship("Tai_khoan", back_populates="so_tiet_kiems")
    loai_tien_te = relationship("Loai_tien_te", back_populates="so_tiet_kiems")
    loai_tiet_kiem = relationship("Loai_tiet_kiem", back_populates="so_tiet_kiems")
    thao_tac_so_tiet_kiems = relationship("Thao_tac_so_tiet_kiem", back_populates="so_tiet_kiem")

class Loai_tiet_kiem(Base):
    __tablename__ = 'Loai_tiet_kiem'
    id = Column(String(10), primary_key=True)
    Ten_loai_tiet_kiem = Column(String(100), nullable=False)
    Lai_suat = Column(Float, nullable=False)
    Ky_han = Column(Integer, nullable=False)

    so_tiet_kiems = relationship("So_tiet_kiem", back_populates="loai_tiet_kiem")

class Loai_tien_te(Base):
    __tablename__ = 'Loai_tien_te'
    id = Column(String(10), primary_key=True)
    Ten_loai_tien_te = Column(String(50), nullable=False)
    Ty_gia = Column(Float, nullable=False)

    so_tiet_kiems = relationship("So_tiet_kiem", back_populates="loai_tien_te")

class Nhan_vien(Base):
    __tablename__ = 'Nhan_vien'
    id = Column(String(10), primary_key=True)
    Ho_va_ten = Column(String(100), nullable=False)
    Gioi_tinh = Column(Enum(GioiTinhEnum), default=GioiTinhEnum.KHAC, nullable=False)
    Ngay_sinh = Column(Date, nullable=False)
    CCCD = Column(String(12), index=True, unique=True, nullable=False)
    Dia_chi = Column(String(255), nullable=False)
    SDT = Column(String(15), unique=True, nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    Ngay_cap_nhat = Column(Date)
    Ma_chuc_vu = Column(String(10), ForeignKey('Phan_quyen.id'), nullable=False)
    Ma_chi_nhanh = Column(String(10), ForeignKey('Chi_nhanh.id'), index=True, nullable=False)

    phan_quyen = relationship("Phan_quyen", back_populates="nhan_viens")
    chi_nhanh = relationship("Chi_nhanh", back_populates="nhan_viens")
    dang_nhap = relationship("Dang_nhap", back_populates="nhan_vien", uselist=False)
    thao_tac_so_tiet_kiems = relationship("Thao_tac_so_tiet_kiem", back_populates="nhan_vien")
    thao_tac_tai_khoans = relationship("Thao_tac_tai_khoan", back_populates="nhan_vien")

    @property
    def tuoi(self):
        today = date.today()
        return today.year - self.Ngay_sinh.year - (
            (today.month, today.day) < (self.Ngay_sinh.month, self.Ngay_sinh.day)
        )

class Chi_nhanh(Base):
    __tablename__ = 'Chi_nhanh'
    id = Column(String(10), primary_key=True)
    Ten_chi_nhanh = Column(String(100), nullable=False)
    Dia_chi = Column(String(255), nullable=False)
    SDT = Column(String(15), unique=True, nullable=False)

    tai_khoans = relationship("Tai_khoan", back_populates="chi_nhanh")
    nhan_viens = relationship("Nhan_vien", back_populates="chi_nhanh")

class Phan_quyen(Base):
    __tablename__ = 'Phan_quyen'
    id = Column(String(10), primary_key=True)
    Ten_chuc_vu = Column(String(100), nullable=False)
    Ten_quyen = Column(String(50), nullable=False)
    Mo_ta = Column(Text)

    nhan_viens = relationship("Nhan_vien", back_populates="phan_quyen")

class Dang_nhap(Base):
    __tablename__ = 'Dang_nhap'
    id = Column(String(10), ForeignKey('Nhan_vien.id'), primary_key=True)
    Ten_dang_nhap = Column(String(50), index=True, unique=True, nullable=False)
    Mat_khau = Column(String(255), nullable=False)

    nhan_vien = relationship("Nhan_vien", back_populates="dang_nhap")

class Thao_tac_so_tiet_kiem(Base):
    __tablename__ = 'Thao_tac_so_tiet_kiem'
    id = Column(String(10), primary_key=True)
    Ma_so_tiet_kiem = Column(String(10), ForeignKey('So_tiet_kiem.id'), index=True, nullable=False)
    Ma_nhan_vien = Column(String(10), ForeignKey('Nhan_vien.id'), nullable=False)
    Ma_thao_tac = Column(String(10), ForeignKey('Thao_tac.id'), nullable=False)
    Ma_khach_hang = Column(String(10), ForeignKey('Khach_hang.id'), nullable=False)
    Ngay_thuc_hien = Column(DateTime, nullable=False)
    Ghi_chu = Column(Text)

    so_tiet_kiem = relationship("So_tiet_kiem", back_populates="thao_tac_so_tiet_kiems")
    nhan_vien = relationship("Nhan_vien", back_populates="thao_tac_so_tiet_kiems")
    thao_tac = relationship("Thao_tac", back_populates="thao_tac_so_tiet_kiems")
    khach_hang = relationship("Khach_hang", back_populates="thao_tac_so_tiet_kiems")

class Thao_tac_tai_khoan(Base):
    __tablename__ = 'Thao_tac_tai_khoan'
    id = Column(String(10), primary_key=True)
    Ma_nhan_vien = Column(String(10), ForeignKey('Nhan_vien.id'), nullable=False)
    Ma_tai_khoan = Column(String(10), ForeignKey('Tai_khoan.id'), nullable=False)
    Ma_thao_tac = Column(String(10), ForeignKey('Thao_tac.id'), nullable=False)
    Ngay_thuc_hien = Column(DateTime, nullable=False)
    Ghi_chu = Column(Text)

    nhan_vien = relationship("Nhan_vien", back_populates="thao_tac_tai_khoans")
    tai_khoan = relationship("Tai_khoan", back_populates="thao_tac_tai_khoans")
    thao_tac = relationship("Thao_tac", back_populates="thao_tac_tai_khoans")

class Thao_tac(Base):
    __tablename__ = 'Thao_tac'
    id = Column(String(10), primary_key=True)
    Ten_thao_tac = Column(String(100), nullable=False)

    thao_tac_so_tiet_kiems = relationship("Thao_tac_so_tiet_kiem", back_populates="thao_tac")
    thao_tac_tai_khoans = relationship("Thao_tac_tai_khoan", back_populates="thao_tac")