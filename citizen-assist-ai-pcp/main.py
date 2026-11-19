from pathlib import Path
from base_conhecimento import BaseConhecimento
from assistente import Assistente


def main():
    raiz = Path(__file__).resolve().parent
    base = BaseConhecimento(raiz / "data" / "base_conhecimento.json")
    base.carregar()
    assistente = Assistente("Citizen Assist AI", base)
    try:
        assistente.executar()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma encerrado.")


if __name__ == "__main__":
    main()
