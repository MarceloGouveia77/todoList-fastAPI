import sys
from fastapi import FastAPI
from typing import List, Dict, Any, Optional
from data import AFazer
from modelos import ModeloDoItem

app = FastAPI()

a_fazer = AFazer()



@app.get("/a-fazer", response_model=List[ModeloDoItem])
async def listar_a_fazer():
    """
    retorna todas as coisas a fazer
    """
    
    return a_fazer.listar()

@app.post("/a-fazer", response_model=ModeloDoItem, status_code=201)
async def inserir_a_fazer(item_a_inserir: ModeloDoItem):
    """
    View que insere item na lista a fazer
    """
    return a_fazer.inserir(item_a_inserir.dict())