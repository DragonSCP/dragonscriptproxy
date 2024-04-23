Aqui está um guia completo desde a instalação inicial do Termux até a execução do seu script, pronto para ser incluído no seu arquivo `README.md`:

```markdown
# Manual de Instalação e Uso do Dragon SSH Script

Este manual orienta você na instalação e execução do Dragon SSH Script no Termux, um emulador de terminal para Android.

## Pré-requisitos

Antes de começar, certifique-se de que o Termux está instalado em seu dispositivo Android. Você pode baixar o Termux da F-Droid ou da Play Store.

## Configuração Inicial

1. **Atualizar o sistema do Termux**:
   Abra o Termux e execute os seguintes comandos para atualizar o sistema:
   ```bash
   pkg update && pkg upgrade
   ```

2. **Instalar o Git**:
   O Git é necessário para clonar o repositório do script.
   ```bash
   pkg install git
   ```

3. **Instalar o Python**:
   Python é necessário para executar o script.
   ```bash
   pkg install python
   ```

4. **Instalar o pip** (se necessário):
   Pip é o gerenciador de pacotes do Python, usado para instalar outras bibliotecas necessárias.
   ```bash
   pkg install python-pip
   ```

## Clonando e Preparando o Script

1. **Clonar o repositório**:
   Use o comando Git para clonar o repositório do script.
   ```bash
   git clone https://github.com/DragonSCP/dragonscriptproxy.git
   ```

2. **Navegar para o diretório do script**:
   Após clonar, mude para o diretório do script.
   ```bash
   cd dragonscriptproxy
   ```

3. **Instalar as dependências**:
   Instale as bibliotecas necessárias listadas no arquivo `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

## Executando o Script

1. **Executar o script**:
   Com todas as dependências instaladas, você está pronto para executar o script.
   ```bash
   python dragon_ssh_script.py
   ```

Siga as instruções na tela para utilizar as funcionalidades do script.

## Dúvidas e Suporte

Para dúvidas e suporte, abra uma issue no repositório do GitHub ou entre em contato com o desenvolvedor.

---

Este manual deve ajudar os usuários a configurar e executar o Dragon SSH Script no Termux sem problemas. Certifique-se de seguir todos os passos para evitar erros de execução.
