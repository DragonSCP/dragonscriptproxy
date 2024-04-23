import random
import os
import sys
import requests
import warnings
import time
import hashlib
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json  # Para processamento de JSON

# Ignorar avisos de certificados não verificados
warnings.simplefilter('ignore', InsecureRequestWarning)

# Versão atual da script
__version__ = "1.3.0"
payload_data = {}  # Define payload_data globalmente para evitar NameError

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def test_proxy(ip, port):
    proxy_url = f"http://{ip}:{port}" if port in [80, 8080] else f"https://{ip}:{port}"
    proxy_dict = {'http': proxy_url, 'https': proxy_url}
    try:
        response = requests.get('http://icanhazip.com', proxies=proxy_dict, timeout=5, verify=False)
        external_ip = response.text.strip()
        print(f"Proxy {ip}:{port} - IP Externo: {external_ip}")
        return True, external_ip
    except requests.exceptions.RequestException as e:
        print(f"Proxy {ip}:{port} - Falha na conexão: {e}")
        return False, None

def fetch_payload_data():
    url = "https://raw.githubusercontent.com/DragonSCP/dragonscriptproxy/main/payload_config.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            global payload_data
            payload_data = json.loads(response.text)
            print("Payloads atualizados com sucesso.")
        else:
            print("Falha ao atualizar payloads, status code:", response.status_code)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
    except Exception as e:
        print(f"Erro ao buscar dados de payload: {e}")

def generate_payloads():
    fetch_payload_data()
    if not payload_data:
        print("Dados de payload não carregados. Abortando geração de payloads.")
        return

    try:
        num_payloads = int(input("Quantas payloads deseja gerar? "))
    except ValueError:
        print("Entrada inválida, por favor insira um número inteiro.")
        return

    methods = payload_data.get('methods', [])
    custom_strings = payload_data.get('custom_strings', [])
    domains = payload_data.get('domains', [])

    for i in range(1, num_payloads + 1):
        method = random.choice(methods) if methods else "GET"
        custom_string = random.choice(custom_strings) if custom_strings else "HTTP/1.1"
        domain = random.choice(domains) if domains else "example.com"
        payload = f"{method} {domain} {custom_string}"
        print(f"Payload {i}\n{payload}\n")

    input("Pressione Enter para continuar...")
    clear_screen()

def update_script():
    script_url = "https://raw.githubusercontent.com/DragonSCP/dragonscriptproxy/main/dragon_ssh_script.py"
    local_script_path = "dragon_ssh_script.py"
    remote_script_content = requests.get(script_url).text
    with open(local_script_path, 'w') as file:
        file.write(remote_script_content)
    print("Script atualizado com sucesso. Reiniciando...")
    os.execv(sys.executable, ['python'] + sys.argv)

def main():
    clear_screen()
    while True:
        print("==== Menu Principal ====")
        print("1 - Gerar e Testar Proxies a partir de um IP Base")
        print("2 - Gerar Payloads")
        print("3 - Testar Proxy Individual")
        print("4 - Gerar e Testar Proxies por Operadora e IP")
        print("5 - Verificar Atualizações")
        choice = input("Escolha uma opção ou pressione Enter para sair: ")

        if choice == '':
            break
        elif choice == '1':
            # Lógica para Gerar e Testar Proxies a partir de um IP Base
            pass
        elif choice == '2':
            generate_payloads()
        elif choice == '3':
            # Lógica para Testar Proxy Individual
            pass
        elif choice == '4':
            # Lógica para Gerar e Testar Proxies por Operadora e IP
            pass
        elif choice == '5':
            update_script()
        else:
            print("Opção inválida. Por favor, tente novamente.")
            time.sleep(2)
        clear_screen()

if __name__ == "__main__":
    main()
