import random
import os
import sys
import requests
import warnings
from subprocess import call
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Ignorar avisos de certificados não verificados
warnings.simplefilter('ignore', InsecureRequestWarning)

# Versão atual da script
__version__ = "1.1.0"

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
            payload_data = eval(response.text.split("=")[1].strip())
            print("Payloads atualizados com sucesso.")
        else:
            print("Falha ao atualizar payloads.")
    except Exception as e:
        print(f"Erro ao buscar dados de payload: {e}")

def generate_payloads():
    fetch_payload_data()
    methods = payload_data['methods']
    custom_strings = payload_data['custom_strings']
    domains = payload_data['domains']
    method = random.choice(methods)
    custom_string = random.choice(custom_strings)
    domain = random.choice(domains)
    payload = f"{method} {domain} {custom_string}"
    print(f"Payload gerado: {payload}")
    input("Pressione Enter para continuar...")

def check_for_updates():
    print("Verificando atualizações...")
    fetch_payload_data()  # Atualizar dados de payload durante a verificação de atualizações
    try:
        local_repo_path = os.path.dirname(os.path.abspath(__file__))
        result = call(["git", "-C", local_repo_path, "pull", "origin", "master"])
        if result == 0:
            print("Atualização realizada com sucesso. Por favor, reinicie o script.")
        else:
            print("A script já está atualizada ou ocorreu um erro.")
    except Exception as e:
        print(f"Erro ao atualizar: {e}")

def show_version():
    print(f"Versão da script: {__version__}")

def uninstall_script():
    try:
        files_to_remove = ['config.json', 'data.db']  # Adicione outros arquivos se necessário
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
            # Implementação existente...
            pass  # Adicione o código apropriado aqui
        elif choice == '2':
            generate_payloads()
        elif choice == '3':
            # Implementação existente...
            pass  # Adicione o código apropriado aqui
        elif choice == '4':
            # Implementação existente...
            pass  # Adicione o código apropriado aqui
        elif choice == '5':
            check_for_updates()
        elif choice == '6':
            show_version()
        elif choice == '7':
            uninstall_script()

if __name__ == '__main__':
    main_menu()

