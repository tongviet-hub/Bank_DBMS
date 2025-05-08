
def mask_sensitive_info(info: str, visible_chars: int = 4)-> str:
    """
    Mã hoá thông tin nhạy cảm bằng cách chỉ hiển thị một số ký tự đầu và cuối.
    """
    if len(info) <= visible_chars * 2:
        return info
    return info[:visible_chars] + '*' * (len(info) - visible_chars * 2) + info[-visible_chars:]