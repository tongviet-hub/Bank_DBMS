import random

def generate_otp(length: int = 6) -> str:
    """
    Tạo mã OTP ngẫu nhiên với độ dài tùy chỉnh (mặc định là 6 ký tự).
    """
    if length <= 0:
        raise ValueError("Độ dài OTP phải lớn hơn 0")
    return ''.join(random.choices("0123456789", k=length))