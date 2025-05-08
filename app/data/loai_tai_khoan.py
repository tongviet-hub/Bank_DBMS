from sqlalchemy.orm import Session
from models import Loai_tai_khoan
from database import SessionLocal

# Giả sử session SQLAlchemy đã có
ds_loai_tai_khoan = [
    Loai_tai_khoan(
        Ten_loai="Tài khoản thanh toán",
        Chuc_nang_chinh="Dùng để nhận/chuyển tiền, thanh toán online, rút tiền tại ATM.",
        Dieu_kien_mo_so="Công dân đủ 15 tuổi có CCCD/CMND hợp lệ.",
        So_du_toi_thieu=0.0
    ),
    Loai_tai_khoan(
        Ten_loai="Tài khoản tiết kiệm",
        Chuc_nang_chinh="Gửi tiền có kỳ hạn để nhận lãi suất theo thời gian.",
        Dieu_kien_mo_so="Công dân có CCCD/CMND, tối thiểu 100.000 VNĐ.",
        So_du_toi_thieu=100000.0
    ),
    Loai_tai_khoan(
        Ten_loai="Tài khoản tín dụng",
        Chuc_nang_chinh="Mua sắm trước, trả tiền sau trong hạn mức tín dụng.",
        Dieu_kien_mo_so="Người từ 18 tuổi, có thu nhập ổn định và lịch sử tín dụng tốt.",
        So_du_toi_thieu=0.0
    ),
    Loai_tai_khoan(
        Ten_loai="Tài khoản ngoại tệ",
        Chuc_nang_chinh="Giao dịch và lưu trữ bằng USD, EUR... thay vì VNĐ.",
        Dieu_kien_mo_so="Có CCCD/CMND và nguồn tiền hợp pháp bằng ngoại tệ.",
        So_du_toi_thieu=50.0  # Giả định tối thiểu 50 đơn vị ngoại tệ
    ),
    Loai_tai_khoan(
        Ten_loai="Tài khoản đầu tư",
        Chuc_nang_chinh="Dùng để giao dịch chứng khoán, quỹ, hoặc tiết kiệm linh hoạt.",
        Dieu_kien_mo_so="Cần mở qua ngân hàng hoặc công ty chứng khoán có liên kết.",
        So_du_toi_thieu=500000.0
    )
]

# Thêm vào session
session.add_all(ds_loai_tai_khoan)
session.commit()
