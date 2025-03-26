import os
from typing import ClassVar, List

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    # 加载环境变量
    load_dotenv(find_dotenv(), override=True)
    # 调试模式
    APP_DEBUG: bool = True
    # 认证信息
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3
    ALGORITHM: str = "HS256"
    APIKEY: str = "yunzhi"
    # 项目信息
    VERSION: str = "1.0.0"
    PROJECT_NAME: str = "基于多模型融合的在线招聘欺诈检测"
    DESCRIPTION: str = (
        '接口详细文档可以参考:<a href="/redoc" target="_blank">redoc</a><br/>接口JSON文档可以参考:<a href="/openapi.json" target="_blank">openapi</a>'
    )
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static/")
    TEMPLATE_DIR: str = os.path.join(os.getcwd(), "templates/")
    DOCS_DIR: str = os.path.join(os.getcwd(), "docs/")
    # 安全密钥, 用于session会话
    SECRET_KEY: ClassVar[str] = "session"
    SESSION_COOKIE: str = "session_id"
    SESSION_MAX_AGE: int = 14 * 24 * 60 * 60
    # 跨域请求
    CORS_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]
    # MySQL数据库
    MYSQL_HOST: str = "localhost"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "root"
    MYSQL_PORT: int = 3306
    MYSQL_DBNAME: str = "api"
    MYSQL_DB_URL: str = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DBNAME}"
    )


settings = Config()
