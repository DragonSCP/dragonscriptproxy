Claro, aqui está o manual de usuário atualizado para a script:

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

- Siga as instruções exibidas no menu para gerar e testar proxies, gerar payloads, testar proxies individuais ou gerar e testar proxies por operadora e IP.

## Desinstalação:

- Se desejar desinstalar a script, você pode fazê-lo executando o seguinte comando no diretório do repositório clonado:

  ```bash
  rm -rf dragonscriptproxy
  ```

---

Esse manual oferece instruções claras sobre como instalar, utilizar e desinstalar a script Dragon SSH, permitindo que os usuários realizem facilmente essas operações.
