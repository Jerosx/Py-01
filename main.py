from fastapi import FastAPI
from utils.router_loader import register_routers

app = FastAPI()

register_routers(app)
