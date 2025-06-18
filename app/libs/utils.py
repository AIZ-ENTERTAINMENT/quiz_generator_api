"""
잡스러운 기능 모음
"""

import importlib
import inspect
import string
import time
from datetime import UTC, datetime
from functools import wraps
from pathlib import Path

import pytz

from app.libs.logger_config import logger


def seoul_tz_now_datetime():
    # UTC 시간 생성
    utc_time = datetime.now(UTC)
    # 한국 시간대 객체 얻기
    korea_timezone = pytz.timezone("Asia/Seoul")
    # UTC 시간을 한국 시간으로 변환
    now = utc_time.astimezone(korea_timezone)
    return now


def avg_datetime(dt1: datetime, dt2: datetime):
    dt = datetime.fromtimestamp((dt1.timestamp() + dt2.timestamp()) / 2)
    korea_timezone = pytz.timezone("Asia/Seoul")
    datetime_tz = dt.astimezone(korea_timezone)
    return datetime_tz


def app_format_datetime(dt):
    now = seoul_tz_now_datetime()
    if dt.date() == now.date():
        # 오늘 날짜이면 "H:MM" 형식으로 출력
        return dt.strftime("%-I:%M")
    elif dt.year == now.year:
        # 올해지만 오늘이 아니면 "MM월 DD일" 형식으로 출력
        return (
            dt.strftime("%m월 %d일").lstrip("0").replace(" 0", " ")
        )  # 01월 -> 1월 로 변환
    else:
        # 올해가 아니면 "YYYY. MM. DD." 형식으로 출력
        return dt.strftime("%Y. %m. %d.").replace(". 0", ". ")


def check_latency_time(func):
    if inspect.iscoroutinefunction(func):

        @wraps(func)
        async def wrapper(*args, **kwargs):
            logger.info(f"start: {func.__name__}")
            s_time = time.time()
            result = await func(*args, **kwargs)
            logger.info(f"{func.__name__}: {round(time.time() - s_time, 4)} s")
            return result

    else:

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"start: {func.__name__}")
            s_time = time.time()
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__}: {round(time.time() - s_time, 4)} s")
            return result

    return wrapper


def base62_encode(num):
    """
    int => Base62
    """
    base62_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
    if num == 0:
        return "0"
    base62 = []
    while num:
        num, rem = divmod(num, 62)
        base62.append(base62_chars[rem])
    return "".join(reversed(base62))

def get_time_ms():
    """
    ms(1/1000s) 단위로 현재 UNIX time 구하는 함수.
    """
    return int(time.time_ns() // 1_000_000)


def now_dttm_str():
    # UTC 시간 생성
    utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
    # 한국 시간대 객체 얻기
    korea_timezone = pytz.timezone("Asia/Seoul")
    # UTC 시간을 한국 시간으로 변환
    now = utc_time.astimezone(korea_timezone)

    # print("UTC 시간:", utc_time)
    # print("한국 시간:", now)
    # now.minute
    return f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분"


def load_class_from_module(module_path, class_name):
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


def load_agent_from_modules(module_paths, class_name):
    """
    여러 모듈 경로에서 클래스 로드
    """
    for path in module_paths:
        for file in Path(path).glob("*.py"):
            try:
                if file.name.startswith("__"):
                    continue
                return load_class_from_module(
                    ".".join(file.with_suffix("").parts), class_name
                )
            except (ImportError, AttributeError) as e:
                logger.debug(f"Error loading class: {e}")
                continue
    raise ImportError(f"{class_name}를 찾을 수 없습니다. 확인된 경로: {module_paths}")
