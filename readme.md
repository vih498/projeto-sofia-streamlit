# Projeto SofIA - Configuração Local

---

## 1. Criar e ativar o ambiente virtual
### Windows
python -m venv venv
.\venv\Scripts\activate

## 2. Atualizar o pip
python -m pip install --upgrade pip

## 3. Instalar pacotes necessários
pip install streamlit
pip install langchain
pip install langchain-groq
pip install openai
pip install pandas
pip install PyPDF2
pip install faiss-cpu
pip install tiktoken
pip install openpyxl
pip install python-dotenv
pip install plotly
pip install --upgrade langchain
pip install -U langchain-community
pip install load_dotenv

### Dica: você também pode instalar todos de uma vez:
pip install streamlit langchain openai pandas PyPDF2 faiss-cpu tiktoken

## 4. Criar arquivo requirements.txt
pip freeze > requirements.txt

## 5. Rodar o projeto
streamlit run app.py