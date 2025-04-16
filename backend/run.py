import uvicorn

if __name__ == "__main__":
    try:
        config = uvicorn.Config(app="app.main:app", reload=True)
        server = uvicorn.Server(config)
        server.run()
    except Exception as e:
        raise e
