# 🤖 Automação Python para SAP

Sistema de automação desenvolvido em Python para integração com SAP, com interface gráfica moderna e geração de executável standalone.

## 📋 Descrição

Este projeto oferece uma solução completa de automação para SAP, permitindo aos usuários executar tarefas repetitivas de forma automatizada através de uma interface gráfica intuitiva desenvolvida com PySide6.

## ✨ Funcionalidades

- Interface gráfica moderna e responsiva
- Automação de processos SAP
- Processamento de dados com Pandas
- Manipulação de arquivos Excel
- Executável standalone (não requer Python instalado)

## 🛠️ Tecnologias Utilizadas

- **Python** - Linguagem principal
- **PySide6** - Framework para interface gráfica (Qt for Python)
- **pywin32** - Automação Windows
- **Pandas** - Manipulação de dados
- **openpyxl** - Leitura/escrita de arquivos Excel
- **PyInstaller** - Geração de executável
- **Qt Designer** - Design da interface

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Windows OS (devido ao pywin32)
- SAP GUI instalado

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone [url-do-repositorio]
cd [nome-do-projeto]
```

### 2. Crie o ambiente virtual
```bash
python -m venv venv
```

### 3. Ative o ambiente virtual
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install PySide6
pip install pywin32
pip install pandas
pip install openpyxl
pip install pyinstaller
```

#### 🔧 Solução de problemas na instalação

Se ocorrer erro ao instalar o PySide6, tente:
```bash
pip install PySide6 --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org
```

### 5. Instale ferramentas de design (opcional)
```bash
pip install pyqt6-tools
```

## 🎨 Desenvolvimento da Interface

### Editar interface gráfica
```bash
pyqt6-tools designer
```

### Converter arquivo .ui para Python
```bash
pyside6-uic sap3.ui -o ui_main.py
```

### Converter recursos (imagens/ícones) para Python
```bash
pyside6-rcc icons.qrc -o icons_rc.py
```

## 📱 Telas da Aplicação

### Tela Principal
*[Primeira tela do executável - interface de login/início]*

### Tela de Operação
*[Segunda tela do executável - interface de automação]*

## 🔨 Gerar Executável

Para criar o executável standalone:

```bash
pyinstaller --onefile --windowed --icon=icon.ico main.py
```

O executável será gerado na pasta `dist/`.

### Opções adicionais do PyInstaller:
- `--onefile`: Cria um único arquivo executável
- `--windowed`: Remove o console (interface gráfica pura)
- `--icon=icon.ico`: Define o ícone do executável
- `--name=SeuNome`: Define o nome do executável

## 💻 Como Usar

1. Execute o arquivo principal:
   ```bash
   python main.py
   ```
   
2. Ou utilize o executável gerado (após build):
   ```
   dist/main.exe
   ```

3. Siga as instruções na interface gráfica

## 📁 Estrutura do Projeto

```
projeto/
├── venv/                  # Ambiente virtual
├── sap3.ui               # Arquivo de interface Qt Designer
├── ui_main.py            # Interface convertida para Python
├── icons.qrc             # Arquivo de recursos Qt
├── icons_rc.py           # Recursos convertidos para Python
├── main.py               # Arquivo principal
├── requirements.txt      # Dependências
└── README.md            # Este arquivo
```

## 📝 Notas Importantes

- ⚠️ Certifique-se de que o SAP GUI está instalado e configurado
- ⚠️ Alguns antivírus podem bloquear o executável gerado - adicione exceção se necessário
- ⚠️ O pywin32 funciona apenas em Windows
- ⚠️ Mantenha o ambiente virtual ativado durante o desenvolvimento

## 🔄 Atualizar Dependências

Para gerar/atualizar o arquivo requirements.txt:
```bash
pip freeze > requirements.txt
```

Para instalar a partir do requirements.txt:
```bash
pip install -r requirements.txt
```

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença [MIT/GPL/Outro] - veja o arquivo LICENSE para detalhes.

## 👥 Autores

- Seu Nome - *Trabalho Inicial*

## 🙏 Agradecimentos

- Comunidade Python
- Documentação PySide6/Qt
- Contribuidores do projeto

---

**Desenvolvido com ❤️ para automação SAP**
