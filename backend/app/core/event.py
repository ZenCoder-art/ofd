async def startup_event():
    """应用启动时的初始化事件"""
    print("应用启动中...")


async def shutdown_event():
    """应用关闭时的清理事件"""
    print("应用关闭中...")
