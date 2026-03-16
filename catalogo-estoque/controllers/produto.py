from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.produto import ProdutoDB
from schemas.produto import ProdutoCreate

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/")
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ProdutoDB(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

@router.get("/")
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(ProdutoDB).all()
    return produtos