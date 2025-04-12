import importlib
import pkgutil

import shutup
from app import app

shutup.please()


def load_routers(package_name: str):
    package = importlib.import_module(package_name)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package_name}.{module_name}")
        if hasattr(module, "router"):
            app.include_router(module.router)


load_routers("app.api")
