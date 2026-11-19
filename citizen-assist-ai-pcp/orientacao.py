class Orientacao:
    """Uma orientação validada da base JSON."""

    CAMPOS = ("id", "categoria", "titulo", "palavras_chave", "resposta",
              "documentos", "onde", "fonte", "verificado_em")

    def __init__(self, registro):
        for campo in self.CAMPOS:
            if campo not in registro:
                raise ValueError(f"Campo obrigatório ausente: {campo}")
        for campo in self.CAMPOS:
            setattr(self, campo, registro[campo])
        if not isinstance(self.palavras_chave, list) or len(self.palavras_chave) < 3:
            raise ValueError("Toda orientação precisa de 3 palavras-chave.")

    def exibir(self):
        print(f"\n>> {self.titulo} [{self.categoria}]")
        print(self.resposta)
        print("Documentos/requisitos:")
        for documento in self.documentos:
            print(f"  - {documento}")
        print(f"Onde: {self.onde}")
        print(f"Fonte: {self.fonte} (verificado em: {self.verificado_em})")
        print("Aviso: este assistente NÃO é um canal oficial.")
