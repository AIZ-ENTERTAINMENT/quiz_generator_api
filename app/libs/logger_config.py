import logging
from os import environ

studio_be_logger_name = "quiz_generator_logger"


def set_logger(logger_name: str):
    """
    - profile:
        - "dev" : only print in terminal
        - "prod" : save logs in {logger_name}.log
    """
    logger = logging.getLogger(logger_name)

    # 로깅 레벨 설정 (INFO 이상) : DEBUG < INFO < WARNING < ERROR < CRITICAL
    logger.setLevel(logging.INFO)

    # 포맷터 생성 및 핸들러에 추가
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    if environ.get("DEPLOY_PHASE", "dev") in ["dev", "local"]:
        # StreamHandler 생성과 핸들러 추가 (콘솔 출력)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        # FileHandler 생성과 핸들러 추가 (파일 출력)
        file_handler = logging.FileHandler(logger_name + ".log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        # FileHandler 생성과 핸들러 추가 (파일 출력)
        file_handler = logging.FileHandler(logger_name + ".log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


logger = logging.getLogger(studio_be_logger_name)
