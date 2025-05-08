from datetime import datetime

def calculate_time_difference(start: datetime, end: datetime) -> str:
    """
    Tính khoảng cách thời gian giữa hai datetime.
    """
    delta = end - start
    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{days} ngày, {hours} giờ, {minutes} phút"