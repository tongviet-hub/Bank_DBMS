INSERT INTO "Loai_tai_khoan" (
    "id", 
    "Ten_loai_tai_khoan", 
    "Chuc_nang_chinh", 
    "Dieu_kien_mo_so", 
    "So_du_toi_thieu"
) VALUES
('LTK001', 'Tài khoản thanh toán', 
 'Dùng để thực hiện các giao dịch hàng ngày như chuyển tiền, rút tiền, thanh toán hóa đơn, quẹt thẻ...', 
 'Cá nhân đủ 18 tuổi, có CMND/CCCD hợp lệ', 
 50000.0),

('LTK002', 'Tài khoản tiết kiệm', 
 'Dùng để gửi tiết kiệm, sinh lãi định kỳ theo kỳ hạn; không dùng cho giao dịch hàng ngày.', 
 'Cá nhân đủ 18 tuổi, có CMND/CCCD hợp lệ; cần duy trì số dư tối thiểu để sinh lãi', 
 1000000.0);
