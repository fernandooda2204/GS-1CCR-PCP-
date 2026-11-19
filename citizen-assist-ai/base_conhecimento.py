import json
import re
import unicodedata
from pathlib import Path
from orientacao import Orientacao


def normalizar(texto):
    texto = unicodedata.normalize("NFD", str(texto).lower())
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9]+", " ", texto)
    return " " + " ".join(texto.split()) + " "


class BaseConhecimento:
    def __init__(self, caminho):
        self.caminho = Path(caminho)
        self.orientacoes = []

    def carregar(self):
        try:
            with self.caminho.open(encoding="utf-8") as arquivo:
                registros = json.load(arquivo)
            if not isinstance(registros, list):
                raise ValueError("A base deve ser uma lista JSON.")
            novas = [Orientacao(item) for item in registros]
            self.orientacoes = novas
            return True
        except (OSError, ValueError, TypeError, KeyError) as erro:
            print(f"Aviso: não foi possível carregar a base: {erro}")
            self.orientacoes = []
            return False

    def categorias(self):
        return sorted({item.categoria for item in self.orientacoes})

    def por_categoria(self, categoria):
        return [item for item in self.orientacoes if item.categoria == categoria]

    def pontuar(self, pergunta, orientacao):
        pergunta_norm = normalizar(pergunta)
        titulo_norm = normalizar(orientacao.titulo)
        pontos = 0
        # Cada expressão-chave presente vale +3; não contam repetições.
        for chave in set(normalizar(c).strip() for c in orientacao.palavras_chave):
            if chave and f" {chave} " in pergunta_norm:
                pontos += 3
        # Cada palavra distinta da pergunta (>=4 caracteres) no título vale +1.
        for palavra in set(pergunta_norm.split()):
            if len(palavra) >= 4 and f" {palavra} " in titulo_norm:
                pontos += 1
        return pontos

    def buscar(self, pergunta):
        resultados = [(self.pontuar(pergunta, item), item)
                      for item in self.orientacoes]
        resultados.sort(key=lambda par: (-par[0], par[1].id))
        return [par for par in resultados if par[0] >= 3]
