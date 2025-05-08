def is_valid_email(email: str) -> bool:
    """
    Kiểm tra định dạng email hợp lệ.
    """
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None