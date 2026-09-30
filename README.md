# 🛡️ Pwned Password Checker (Python)

Um utilitário em linha de comando (CLI) desenvolvido em Python para verificar se uma senha já foi exposta em vazamentos de dados públicos, utilizando a API oficial do **[Have I Been Pwned](https://haveibeenpwned.com/)** e o modelo de privacidade **k-Anonymity**.

---

## 📌 Funcionalidades

- **🔒 Privacidade Total (k-Anonymity):** A sua senha em texto puro ou o seu hash completo **nunca** trafegam pela internet. Apenas os 5 primeiros caracteres do hash SHA-1 são enviados para a API.
- **👁️ Digitação Segura:** Utiliza a biblioteca `getpass` para ocultar os caracteres da senha na tela durante a digitação.
- **⚡ Resiliência e Tratamento de Erros:** Identifica e trata erros de conexão com a internet, limites de requisições da API (*rate limiting*) e falhas de servidor.
- **📊 Retorno Preciso:** Exibe a quantidade exata de vezes que a senha apareceu em bases de dados vazadas.

---

## 🚀 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:

* **[Python 3.8+](https://www.python.org/downloads/)**
* Gerenciador de pacotes **pip** (normalmente incluído na instalação do Python)

---

## 📦 Instalação

1. **Clone ou baixe este repositório:**

   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio
   ```

2. **Instale as dependências necessárias:**

   O projeto utiliza a biblioteca `requests` para comunicação com a API. Instale rodando:

   ```bash
   pip install requests
   ```

---

## 🛠️ Como Executar

Com as dependências instaladas, basta executar o arquivo principal do projeto:

```bash
python main.py
```

Você verá um prompt no terminal solicitando a digitação da sua senha. Digite a senha e pressione `Enter` (os caracteres não aparecerão na tela por questões de segurança).

---

## 🧠 Como Funciona o k-Anonymity?

1. O script gera o hash **SHA-1** da senha informada (ex: `5FD2A692542880C8B500C9E8DF41B1F54E18...`).
2. O hash é dividido em duas partes:
   - **Prefixo:** Os primeiros 5 caracteres (`5FD2A`).
   - **Sufixo:** Os caracteres restantes.
3. O script faz uma requisição `GET` enviando **apenas o prefixo** para a API do *Have I Been Pwned*.
4. A API retorna uma lista de todos os sufixos de senhas vazadas conhecidas que começam com aquele mesmo prefixo.
5. O script compara localmente, na sua máquina, se o seu sufixo está contido na lista retornada e exibe o número de ocorrências.

---

## 📄 Licença

Este projeto é voltado para fins educacionais e de estudo sobre segurança e consumo de APIs. Sinta-se livre para usar, modificar e contribuir!
