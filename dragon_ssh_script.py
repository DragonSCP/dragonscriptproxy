import random
import os
import sys
import requests
import warnings
import time
from subprocess import call
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import shutil  # Adicionado para suportar operações de remoção do diretório

# Ignorar avisos de certificados não verificados
warnings.simplefilter('ignore', InsecureRequestWarning)

# Versão atual da script
__version__ = "1.2.0"

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def test_proxy(ip, port):
    proxy_url = f"http://{ip}:{port}" if port in [80, 8080] else f"https://{ip}:{port}"
    proxy_dict = {
        'http': proxy_url,
        'https': proxy_url
    }
    try:
        response = requests.get('http://icanhazip.com', proxies=proxy_dict, timeout=5, verify=False)
        external_ip = response.text.strip()
        print(f"Proxy {ip}:{port} - IP Externo: {external_ip}")
        return True, external_ip
    except requests.exceptions.RequestException as e:
        print(f"Proxy {ip}:{port} - Falha na conexão: {e}")
        return False, None

def fetch_payload_data():
    url = "https://raw.githubusercontent.com/DragonSCP/dragonscriptproxy/main/payload_config.py"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            global payload_data
            payload_data = json.loads(response.text)
            print("Payloads atualizados com sucesso.")
        else:
            print("Falha ao atualizar payloads.")
    except Exception as e:
        print(f"Erro ao buscar dados de payload: {e}")

def generate_payloads():
    fetch_payload_data()
    try:
        num_payloads = int(input("Quantas payloads deseja gerar? "))
    except ValueError:
        print("Entrada inválida, por favor insira um número inteiro.")
        return

    methods = payload_data['methods']
    custom_strings = payload_data['custom_strings']
    domains = payload_data['domains']

    for i in range(1, num_payloads + 1):
        method = random.choice(methods)
        custom_string = random.choice(custom_strings)
        domain = random.choice(domains)
        payload = f"{method} {domain} {custom_string}"
        print(f"Payload{i}\n{payload}\n")

    input("Pressione Enter para continuar...")

def check_for_updates():
    print("Verificando atualizações...")
    for i in range(3):
        time.sleep(1)  # Simula o progresso da atualização
        print(".", end="", flush=True)
    print()

    local_repo_path = os.path.dirname(os.path.abspath(__file__))
    repo_url = "https://github.com/DragonSCP/dragonscriptproxy.git"

    try:
        # Removendo a script atual completamente
        base_path = os.path.dirname(local_repo_path)  # Obtém o diretório pai
        if os.path.exists(local_repo_path):
            shutil.rmtree(local_repo_path)
            print("\nScript atual removida com sucesso.")

        # Reinstalando a versão mais recente do repositório
        result = call(["git", "clone", repo_url, local_repo_path])
        if result == 0:
            print("\nScript reinstalada com sucesso. Por favor, reinicie o script.")
        else:
            print("\nErro ao reinstalar a script.")
    except Exception as e:
        print(f"\nErro ao atualizar: {e}")

def show_version():
    print(f"Versão da script: {__version__}")

def uninstall_script():
    try:
        files_to_remove = ['config.json', 'data.db']
        for file in files_to_remove:
            os.remove(file)
            print(f"Arquivo {file} removido com sucesso.")
        os.remove("dragon_ssh_script.py")
        sys.exit("Script desinstalado com sucesso.")
    except OSError as e:
        sys.exit(f"Erro ao desinstalar script: {e}")

def main_menu():
    while True:
        clear_screen()
        print("Dragon SSH Script Generator")
        print("1. Gerar e Testar Proxies a partir de um IP Base")
        print("2. Gerar Payloads")
        print("3. Testar Proxies Individuais")
        print("4. Gerar e Testar Proxies por Operadora e IP")
        print("5. Verificar Atualizações")
        print("6. Exibir Versão do Script")
        print("7. Desinstalar Script")

        choice = input("Escolha uma opção: ").strip()
        if choice == '':
            continue
        elif choice == '1':
            pass
        elif choice == '2':
            generate_payloads()
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            check_for_updates()
        elif choice == '6':
            show_version()
        elif choice == '7':
            uninstall_script()

if __name__ == '__main__':
    main_menu()
