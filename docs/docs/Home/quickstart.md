# 快速开始

## 构建后端

本项目后端采用 Python 的 FastAPI 框架, 请确保已安装 Python 3.10+版本。虚拟环境项目管理推荐使用[uv](https://github.com/astral-sh/uv)

```bash
git clone https://github.com/ZenCoder-art/ofd.git
cd ofd/backend
uv venv
uv pip install -r pyproject.toml

uvicorn main:app --reload
```

## 构建前端

本项目前端采用 Vue3+Vite 框架, 请确保已安装 Node.js 16+版本。

```bash
git clone https://github.com/ZenCoder-art/ofd.git
cd ofd/frontend
npm install

npm run dev
```
