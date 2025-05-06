from sqlalchemy.orm import Session
from database import SessionLocal
from models import Khach_hang, Tai_khoan, Loai_tai_khoan, Chi_nhanh, Phan_quyen, Dang_nhap, Nhan_vien

def seed_data():
    db: Session = SessionLocal()
    try:
        khach_hang_list = [
                    Khach_hang(
                        CCCD="123456789012",
                        Name="Nguyen Van A",
                        Ngay_sinh="1990-01-01",
                        Phone="0123456789",
                        Email="nguyenvana@example.com",
                        Dia_chi="123 Đường ABC, TP.HCM"
                    ),
                    Khach_hang(
                        CCCD="987654321098",
                        Name="Tran Thi B",
                        Ngay_sinh="1995-05-05",
                        Phone="0987654321",
                        Email="tranthib@example.com",
                        Dia_chi="456 Đường XYZ, Hà Nội"
                    ),
                    Khach_hang(
                        CCCD="111122223333",
                        Name="Le Van C",
                        Ngay_sinh="1988-03-15",
                        Phone="0912345678",
                        Email="levanc@example.com",
                        Dia_chi="789 Đường DEF, Đà Nẵng"
                    ),
                    Khach_hang(
                        CCCD="222233334444",
                        Name="Pham Thi D",
                        Ngay_sinh="1992-07-20",
                        Phone="0934567890",
                        Email="phamthid@example.com",
                        Dia_chi="321 Đường GHI, Hải Phòng"
                    ),
                    Khach_hang(
                        CCCD="333344445555",
                        Name="Hoang Van E",
                        Ngay_sinh="1985-11-11",
                        Phone="0945678901",
                        Email="hoangvane@example.com",
                        Dia_chi="654 Đường JKL, Cần Thơ"
                    ),
                    Khach_hang(
                        CCCD="444455556666",
                        Name="Nguyen Thi F",
                        Ngay_sinh="1998-02-28",
                        Phone="0956789012",
                        Email="nguyenthif@example.com",
                        Dia_chi="987 Đường MNO, Đà Lạt"
                    ),
                    Khach_hang(
                        CCCD="555566667777",
                        Name="Tran Van G",
                        Ngay_sinh="1993-06-10",
                        Phone="0967890123",
                        Email="tranvang@example.com",
                        Dia_chi="123 Đường PQR, Nha Trang"
                    ),
                    Khach_hang(
                        CCCD="666677778888",
                        Name="Le Thi H",
                        Ngay_sinh="1991-09-25",
                        Phone="0978901234",
                        Email="lethih@example.com",
                        Dia_chi="456 Đường STU, Huế"
                    ),
                    Khach_hang(
                        CCCD="777788889999",
                        Name="Pham Van I",
                        Ngay_sinh="1987-12-05",
                        Phone="0989012345",
                        Email="phamvani@example.com",
                        Dia_chi="789 Đường VWX, Quảng Ninh"
                    ),
                    Khach_hang(
                        CCCD="888899990000",
                        Name="Hoang Thi J",
                        Ngay_sinh="1994-04-18",
                        Phone="0990123456",
                        Email="hoangthij@example.com",
                        Dia_chi="321 Đường YZ, Bình Dương"
                    ),
                    Khach_hang(
                        CCCD="999900001111",
                        Name="Nguyen Van K",
                        Ngay_sinh="1990-08-30",
                        Phone="0901234567",
                        Email="nguyenvank@example.com",
                        Dia_chi="654 Đường ABC, Đồng Nai"
                    ),
                    Khach_hang(
                        CCCD="000011112222",
                        Name="Tran Thi L",
                        Ngay_sinh="1996-01-15",
                        Phone="0912345678",
                        Email="tranthil@example.com",
                        Dia_chi="987 Đường DEF, Vũng Tàu"
                    ),
                    Khach_hang(
                        CCCD="111122223333",
                        Name="Le Van M",
                        Ngay_sinh="1989-03-10",
                        Phone="0923456789",
                        Email="levanm@example.com",
                        Dia_chi="123 Đường GHI, Bình Phước"
                    ),
                    Khach_hang(
                        CCCD="222233334444",
                        Name="Pham Thi N",
                        Ngay_sinh="1997-07-22",
                        Phone="0934567890",
                        Email="phamthin@example.com",
                        Dia_chi="456 Đường JKL, Long An"
                    ),
                    Khach_hang(
                        CCCD="333344445555",
                        Name="Hoang Van O",
                        Ngay_sinh="1992-11-30",
                        Phone="0945678901",
                        Email="hoangvano@example.com",
                        Dia_chi="789 Đường MNO, Tiền Giang"
                    )
                ]
        db.add_all(khach_hang_list)
        chi_nhanh_1 = Chi_nhanh(
            Name="Chi nhánh TP.HCM",
            Dia_chi="123 Đường ABC, TP.HCM",
            Phone="0123456789"
        )
        chi_nhanh_2 = Chi_nhanh(
            Name="Chi nhánh Hà Nội",
            Dia_chi="456 Đường XYZ, Hà Nội",
            Phone="0987654321"
        )
        db.add_all([chi_nhanh_1, chi_nhanh_2])

        # Thêm dữ liệu mẫu cho bảng Loại tài khoản
        loai_tai_khoan_1 = Loai_tai_khoan(
            Ten_loai="Tài khoản tiết kiệm",
            Lai_suat=3.5
        )
        loai_tai_khoan_2 = Loai_tai_khoan(
            Ten_loai="Tài khoản thanh toán",
            Lai_suat=1.2
        )
        db.add_all([loai_tai_khoan_1, loai_tai_khoan_2])

        # Thêm dữ liệu mẫu cho bảng Nhân viên
        nhan_vien_1 = Nhan_vien(
            Name="Le Van C",
            CCCD="111122223333",
            Phone="0912345678",
            Email="levanc@example.com",
            Dia_chi="789 Đường DEF, Đà Nẵng",
            Luong=15000000,
            Ma_chi_nhanh=1,
            Ma_chuc_vu=1
        )
        db.add(nhan_vien_1)

        # Thêm dữ liệu mẫu cho bảng Đăng nhập
        dang_nhap_1 = Dang_nhap(
            id=1,
            Ten_dang_nhap="admin",
            Mat_khau="hashed_password_here"  # Thay bằng mật khẩu đã mã hóa
        )
        db.add(dang_nhap_1)

        # Commit dữ liệu vào database
        db.commit()
        print("Dữ liệu mẫu đã được thêm thành công!")
    except Exception as e:
        db.rollback()
        print(f"Lỗi khi thêm dữ liệu mẫu: {e}")
    finally:
        db.close()
