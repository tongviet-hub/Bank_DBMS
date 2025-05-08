import re


def is_password_strong(password: str) -> bool:
    """
    Kiểm tra mật khẩu có đủ mạnh hay không.
    Mật khẩu được coi là mạnh nếu:
    - Có ít nhất 8 ký tự
    - Có ít nhất 1 chữ cái viết hoa
    - Có ít nhất 1 chữ cái viết thường
    - Có ít nhất 1 số
    - Có ít nhất 1 ký tự đặc biệt
    """
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False

    if not re.search(r'[@$!%*?&]', password):
        return False

    return True