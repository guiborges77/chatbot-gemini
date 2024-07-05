## Passo a Passo para Rodar a Aplicação

### 1. Navegar até o Diretório do Projeto

Abra seu terminal e navegue até o diretório do seu projeto:

## Criar um Ambiente Virtual

python3 -m venv venv

## Ativar o Ambiente Virtual

No macOS/Linux: source venv/bin/activate
No Windows: .\venv\Scripts\activate

## Instalar Dependências

pip install -r requirements.txt
streamlit run app.py

## Resolvendo Problemas de Módulos Faltando

pip install python-dotenv
pip install google-generativeai
