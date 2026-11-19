import csv
import json
import re
import time
from datetime import datetime
from pathlib import Path


def dado_pessoal(texto):
    """Recusa e não registra entradas contendo @ ou 8+ dígitos no total."""
    return "@" in texto or len(re.findall(r"\d", texto)) >= 8


def escolha(limite, mensagem="Opção: "):
    while True:
        opcao = input(mensagem).strip()
        if opcao.isdigit() and 0 <= int(opcao) <= limite:
            return int(opcao)
        print(f"Opção inválida. Digite um número de 0 a {limite}.")


class Assistente:
    COLUNAS = ["data", "origem", "pergunta", "id_orientacao", "encontrou",
               "ajudou", "tentativas", "tempo_segundos"]

    def __init__(self, nome, base, pasta_dados=None):
        self.nome = nome
        self.base = base
        self.pasta = Path(pasta_dados) if pasta_dados else base.caminho.parent
        self.pasta.mkdir(parents=True, exist_ok=True)
        self.arquivo_historico = self.pasta / "historico.json"
        self.arquivo_avaliacoes = self.pasta / "avaliacoes.json"
        self.historico = self._ler_lista(self.arquivo_historico)
        self.avaliacoes = self._ler_lista(self.arquivo_avaliacoes)

    @staticmethod
    def _ler_lista(caminho):
        try:
            with caminho.open(encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            return dados if isinstance(dados, list) else []
        except (OSError, ValueError, TypeError):
            return []

    @staticmethod
    def _salvar(caminho, dados):
        try:
            with caminho.open("w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, indent=2, ensure_ascii=False)
            return True
        except OSError as erro:
            print(f"Aviso: não foi possível salvar {caminho}: {erro}")
            return False

    def registrar(self, origem, pergunta, orientacao, encontrou, ajudou,
                  tentativas, tempo):
        # Proteção redundante: nenhum atendimento com dado sensível entra no histórico.
        if dado_pessoal(pergunta):
            return
        registro = {
            "data": datetime.now().isoformat(timespec="seconds"),
            "origem": origem,
            "pergunta": pergunta,
            "id_orientacao": orientacao.id if orientacao else None,
            "encontrou": bool(encontrou),
            "ajudou": ajudou,  # True/False; None quando não encontrou.
            "tentativas": tentativas,
            "tempo_segundos": round(tempo, 1)
        }
        self.historico.append(registro)
        self._salvar(self.arquivo_historico, self.historico)

    @staticmethod
    def _ajudou():
        while True:
            valor = input("Essa orientação respondeu sua dúvida? (s/n): ").strip().lower()
            if valor in ("s", "n"):
                return valor == "s"
            print("Resposta inválida. Digite s ou n.")

    def perguntar(self):
        tentativas = 0
        inicio = time.time()
        while True:
            pergunta = input("\nDigite sua dúvida (0 para voltar): ").strip()
            if pergunta == "0":
                return
            if not pergunta:
                print("Digite uma pergunta ou 0 para voltar.")
                continue
            if dado_pessoal(pergunta):
                print("Atenção: não informe CPF, telefone, e-mail ou outros dados pessoais. Reescreva.")
                continue
            tentativas += 1
            resultados = self.base.buscar(pergunta)
            if not resultados:
                print("Não encontrei uma orientação. Tente outras palavras ou navegue por categorias.")
                self.registrar("pergunta", pergunta, None, False, None,
                               tentativas, time.time()-inicio)
                tentativas, inicio = 0, time.time()
                continue
            pontos, orientacao = resultados[0]
            confianca = "ALTA" if pontos >= 6 else "MÉDIA"
            print(f"\nConfiança da resposta: {confianca} ({pontos} pontos)")
            orientacao.exibir()
            alternativas = resultados[1:3]
            if alternativas:
                print("\nOutras orientações possíveis:")
                for score, item in alternativas:
                    print(f"  - {item.titulo} ({score} pontos)")
            ajudou = self._ajudou()
            self.registrar("pergunta", pergunta, orientacao, True, ajudou,
                           tentativas, time.time()-inicio)
            tentativas, inicio = 0, time.time()

    def navegar(self):
        while True:
            categorias = self.base.categorias()
            if not categorias:
                print("A base está vazia. Cadastre orientações primeiro.")
                return
            print("\nCategorias:")
            for indice, categoria in enumerate(categorias, 1):
                print(f"{indice}. {categoria}")
            print("0. Voltar")
            escolha_categoria = escolha(len(categorias))
            if escolha_categoria == 0:
                return
            categoria = categorias[escolha_categoria-1]
            orientacoes = self.base.por_categoria(categoria)
            while True:
                print(f"\n{categoria}:")
                for indice, item in enumerate(orientacoes, 1):
                    print(f"{indice}. {item.titulo}")
                print("0. Voltar")
                indice = escolha(len(orientacoes))
                if indice == 0:
                    break
                inicio = time.time()
                item = orientacoes[indice-1]
                item.exibir()
                ajudou = self._ajudou()
                self.registrar("categoria", f"Categoria: {categoria} / {item.titulo}",
                               item, True, ajudou, 1, time.time()-inicio)

    def indicadores(self):
        total = len(self.historico)
        encontrados = [a for a in self.historico if a.get("encontrou")]
        avaliados = [a for a in encontrados if isinstance(a.get("ajudou"), bool)]
        uteis = sum(1 for a in avaliados if a["ajudou"])
        # Tempo de busca apenas para atendimentos encontrados.
        tempos = [float(a.get("tempo_segundos", 0)) for a in encontrados]
        tentativas = [int(a.get("tentativas", 0)) for a in self.historico]
        notas = [n for n in self.avaliacoes if isinstance(n, int) and 1 <= n <= 5]
        resultados = {
            "atendimentos": total,
            "resposta_encontrada_pct": round(100*len(encontrados)/total, 1) if total else 0,
            "taxa_ajudou_pct": round(100*uteis/len(avaliados), 1) if avaliados else 0,
            "tempo_medio_segundos": round(sum(tempos)/len(tempos), 1) if tempos else 0,
            "tentativas_por_atendimento": round(sum(tentativas)/total, 2) if total else 0,
            "facilidade_media": round(sum(notas)/len(notas), 2) if notas else None,
            "duvidas_sem_solucao": [a["pergunta"] for a in self.historico if not a.get("encontrou")],
        }
        print("\n--- INDICADORES ---")
        print(f"Atendimentos: {total}")
        print(f"Resposta encontrada: {resultados['resposta_encontrada_pct']}%")
        print(f"Taxa de acerto (ajudou): {resultados['taxa_ajudou_pct']}% dos avaliados")
        print(f"Tempo médio para encontrar: {resultados['tempo_medio_segundos']} s")
        print(f"Tentativas por atendimento: {resultados['tentativas_por_atendimento']}")
        print(f"Facilidade de uso: {resultados['facilidade_media'] if notas else 'sem avaliações'}")
        print("Dúvidas sem solução:", resultados["duvidas_sem_solucao"] or "nenhuma")
        return resultados

    def exportar_csv(self):
        caminho = self.pasta / "atendimentos.csv"
        try:
            with caminho.open("w", newline="", encoding="utf-8-sig") as arquivo:
                escritor = csv.DictWriter(arquivo, fieldnames=self.COLUNAS)
                escritor.writeheader()
                escritor.writerows(self.historico)
            print(f"CSV exportado: {caminho}")
        except OSError as erro:
            print(f"Não foi possível exportar o CSV: {erro}")

    def avaliar_saida(self):
        while True:
            nota = input("Facilidade de uso (1 a 5; 0 para pular): ").strip()
            if nota in ("0", "1", "2", "3", "4", "5"):
                if nota != "0":
                    self.avaliacoes.append(int(nota))
                    self._salvar(self.arquivo_avaliacoes, self.avaliacoes)
                return
            print("Digite um número de 0 a 5.")

    def executar(self):
        while True:
            print(f"\n=== {self.nome} ===")
            print("1. Fazer pergunta\n2. Navegar por categorias\n3. Indicadores\n4. Exportar CSV\n0. Sair")
            opcao = escolha(4)
            if opcao == 1:
                self.perguntar()
            elif opcao == 2:
                self.navegar()
            elif opcao == 3:
                self.indicadores()
            elif opcao == 4:
                self.exportar_csv()
            else:
                self.avaliar_saida()
                print("Até logo!")
                return
