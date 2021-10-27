from src.dependency.container import Container
from src.handler.api_handler.v1 import v1_modules

container = Container()

container.wire(modules=v1_modules)
