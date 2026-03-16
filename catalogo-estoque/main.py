from fastapi import FastAPI
from database import engine, Base
from controllers.produto import router as produto_router
from models.produto import ProdutoDB

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Catalogo de estoque - Monólito")

app.include_router(produto_router)