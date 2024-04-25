Claro, aqui está a atualização do manual do usuário com o novo comando adicionado:

---

# Manual do Usuário: Dragon SSH Script

## Requisitos:

- Termux instalado no dispositivo Android.

## Instalação:

1. Abra o aplicativo Termux.

2. Instale o Git, caso ainda não esteja instalado:
   ```bash
   pkg install git
   ```

3. Clone o repositório Dragon SSH Script:
   ```bash
   git clone https://github.com/DragonSCP/dragonscriptproxy.git
   ```

4. Navegue até o diretório do repositório:
   ```bash
   cd dragonscriptproxy
   ```

5. Torne o script `setup.sh` executável:
   ```bash
   chmod +x setup.sh
   ```

6. Execute o script de instalação:
   ```bash
   ./setup.sh
   ```

## Utilização:

- Após a instalação, você pode executar a script Dragon SSH da seguinte maneira:
  
  ```bash
  python dragon_ssh_script.py
  ```

- **Menu Principal** oferece as seguintes opções:
  - **1 - Gerar e Testar Proxies a partir de um IP Base**
  - **2 - Gerar Payloads**
  - **3 - Testar Proxy Individual**
  - **4 - Gerar e Testar Proxies por Operadora e IP**
  - **5 - Verificar Atualizações**
  - **6 - Sair do Diretório**

- **Funcionalidades adicionais incluem:**
  - **Testar Proxy**: Testa a configuração do proxy baseada em dados de operadora específica e payloads customizados.
  - **Carregar e Testar Proxies com Configurações Específicas**: Permite carregar configurações de proxy e testá-las dinamicamente.
  - **Testar Proxies por Operadora**: Selecione uma operadora para testar todos os proxies relacionados àquela operadora.

## Atualização:

- Para atualizar a script, selecione a opção "Verificar Atualizações" no menu principal. A script verificará e aplicará automaticamente quaisquer atualizações disponíveis.

## Desinstalação:

- Se desejar desinstalar a script, você pode fazê-lo executando o seguinte comando no diretório do repositório clonado:

  ```bash
  rm -rf dragonscriptproxy
  ```

---

Este manual atualizado agora inclui o novo comando "Sair do Diretório" no menu principal, proporcionando uma maneira conveniente para os usuários saírem do diretório atual da script quando desejarem.
