import bcrypt

def hash_password(plain_password: str) -> str:
    """
    Mã hoá mật khẩu bằng bcrypt.
    Trả về chuỗi đã mã hoá.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Kiểm tra mật khẩu người dùng nhập có khớp với mật khẩu đã mã hoá không.
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
