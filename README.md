# Agente de Qualidade

Este projeto demonstra como utilizar a biblioteca **CrewAI** com o modelo da Azure OpenAI para analisar arquivos de teste em um projeto Python.

## Pré‑requisitos

- Python 3.11+
- Dependências listadas em `requirements.txt`
- Variáveis de ambiente configuradas para acesso ao Azure OpenAI:
  - `AZURE_OPENAI_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_DEPLOYMENT`
  - `AZURE_OPENAI_API_VERSION` (opcional)

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

Execute o script principal informando o diretório do projeto a ser analisado:

```bash
python -m src.main caminho/do/projeto
```

O agente irá localizar todos os arquivos de teste (`test_*.py` ou `*_test.py`) e utilizará o Azure OpenAI para verificar se seguem boas práticas de mercado, gerando um relatório resumido.

## Estrutura

- `src/config.py` – configuração do acesso ao Azure OpenAI.
- `src/tools.py` – ferramentas usadas pelos agentes (listar arquivos e ler conteúdo).
- `src/analyzer.py` – ferramenta que utiliza o modelo da Azure OpenAI.
- `src/main.py` – definição dos agentes, tarefas e ponto de entrada da aplicação.
