from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class AFazer:
    a_fazer: List[Dict[str, Any]] = [
        {"id": 1,
        "titulo": "Lavar o cabelo",
        "descrição": "qualquer uma",
        "status": "a fazer"
        },
        {"id": 2,
        "titulo": "Programar",
        "descrição": "qualquer uma",
        "status": "a fazer"
        },
        {"id": 3,
        "titulo": "Pintar a casa",
        "descrição": "qualquer uma",
        "status": "a fazer"
        },
    ]

    id_atual = 3 # APENAS PARA TESTE DO POST 

    def listar(self):
        return self.a_fazer

    def inserir(self, item: Dict[str, Any]) -> Dict[str, Any]:
        self.id_atual += 1
        item["id"] = self.id_atual
        self.a_fazer.append(item)
        return item