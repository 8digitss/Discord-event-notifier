from datetime import datetime

def format_time(time_str):
    try:
        return datetime.fromisoformat(time_str)
    except ValueError:
        return None
