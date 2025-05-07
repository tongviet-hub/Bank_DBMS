from sqlalchemy.orm import Session
from database import SessionLocal
from app.models import Khach_hang, Tai_khoan, Loai_tai_khoan, Chi_nhanh, Phan_quyen, Dang_nhap, Nhan_vien

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

chi_nhanh_list = [
    Chi_nhanh(
        Name="Chi nhánh 1",
        Dia_chi="123 Đường A, TP.HCM",
        Phone="0123456789"
    ),
    Chi_nhanh(
        Name="Chi nhánh 2",
        Dia_chi="456 Đường B, Hà Nội",
        Phone="0987654321"
    ),
    Chi_nhanh(
        Name="Chi nhánh 3",
        Dia_chi="789 Đường C, Đà Nẵng",
        Phone="0912345678"
    ),
    Chi_nhanh(
        Name="Chi nhánh 4",
        Dia_chi="321 Đường D, Hải Phòng",
        Phone="0934567890"
    ),
    Chi_nhanh(
        Name="Chi nhánh 5",
        Dia_chi="654 Đường E, Cần Thơ",
        Phone="0945678901"
    )
]

