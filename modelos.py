from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class ModeloDoItem(BaseModel):
    id: int # Se remover um atributo daqui, deixa de existir na response do request também
    titulo: str
    status: Optional[str]