## 🗂️ Estrutura do Projeto

O projeto foi organizado de forma modular para facilitar a manutenção, leitura e escalabilidade do código:


📦 sistema-biblioteca
│
├── 📄 main.py
├── 📄 biblioteca.py
├── 📄 item.py
├── 📄 livro.py
├── 📄 revista.py
├── 📄 usuario.py (opcional)
├── 📄 utils.py (opcional)
├── 📄 README.md
│
└── 📁 pycache (gerado automaticamente pelo Python)


---

## 📄 Descrição dos Arquivos

### ▶️ main.py
Arquivo principal responsável por iniciar o sistema.  
Contém o menu interativo e gerencia a interação com o usuário via terminal.

---

### 📚 biblioteca.py
Responsável pela lógica central do sistema.  
Gerencia:
- Cadastro de itens  
- Listagem  
- Empréstimos  
- Devoluções  

---

### 🧩 item.py
Classe base do sistema.  
Define atributos e métodos comuns, como:
- código  
- título  
- status (disponível/emprestado)  

---

### 📖 livro.py
Classe que herda de `Item`.  
Representa livros e adiciona características específicas como:
- autor  
- número de páginas  

---

### 📰 revista.py
Classe que herda de `Item`.  
Representa revistas e pode incluir:
- número da edição  
- data de publicação  

---

### 👤 usuario.py *(opcional)*
Responsável por representar usuários do sistema.  
Pode ser usado para evoluir o projeto com:
- cadastro de usuários  
- controle de empréstimos por pessoa  

---

### 🛠️ utils.py *(opcional)*
Arquivo com funções auxiliares, como:
- validação de entrada  
- formatação de dados  
- geração de códigos  

---

## 🔄 Fluxo do Sistema

1. O usuário executa o arquivo `main.py`
2. O menu principal é exibido no terminal
3. O usuário escolhe uma opção:
   - Cadastrar item  
   - Listar itens  
   - Realizar empréstimo  
   - Realizar devolução  
4. O sistema processa a ação através da classe `Biblioteca`
5. O resultado é exibido na tela

---

## 🚀 Possíveis Melhorias

Para evoluir o projeto, você pode implementar:

- 💾 Persistência de dados com arquivos (`.json` ou `.csv`)
- 🗄️ Integração com banco de dados (SQLite, PostgreSQL)
- 🌐 Interface web com Flask ou FastAPI
- 🔐 Sistema de autenticação de usuários
- 📊 Relatórios de empréstimos
- 🎨 Interface gráfica (Tkinter ou PyQt)

---

## 📌 Observação

Este projeto é ideal para iniciantes que desejam praticar **Programação Orientada a Objetos (POO)** na prática