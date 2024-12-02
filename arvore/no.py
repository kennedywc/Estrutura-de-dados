from dataclasses import dataclass
from typing import Any

@dataclass
class No:
    valor: Any
    esquerda: 'No' = None
    direita: 'No' = None
