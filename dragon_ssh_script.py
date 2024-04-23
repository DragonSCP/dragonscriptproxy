import random
import os
import sys
import requests
import warnings
from subprocess import call
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from payload_config import payload_data  # Adicionando importação do novo módulo com as configurações

# Ignorar avisos de certificados não verificados
warnings.simplefilter('ignore', InsecureRequestWarning)

allowed_words = set([
    "http", "GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH",
    "wikipedia.org", "youtube.com", "google.com", "bing.com", "vivo.com.br",
    "plus.google.com", "myspace.com", "spotify.com", "playwaze.com",
])

# Versão atual da script
__version__ = "1.0.0"

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def filter_text(text):
    words = set(text.split())
    if not words.isdisjoint(allowed_words):
        return text
    return None

def test_proxy(ip, port):
    proxy_url = f"http://{ip}:{port}" if port in [80, 8080] else f"https://{ip}:{port}"
    proxy_dict = {
        'http': proxy_url,
        'https': proxy_url
    }
    try:
        response = requests.get('http://icanhazip.com', proxies=proxy_dict, timeout=5, verify=False)
        response_text = response.text.strip()
        filtered_text = filter_text(response_text)
        if filtered_text:
            print(f"Proxy {ip}:{port} - {filtered_text}")
            return True, filtered_text
        elif '403 Forbidden' in response_text:
            print(f"Proxy {ip}:{port} - Acesso negado.")
            return False, None
        else:
            external_ip = response_text
            print(f"Proxy {ip}:{port} - IP Externo: {external_ip}")
            return True, external_ip
    except requests.exceptions.RequestException as e:
        print(f"Proxy {ip}:{port} - Falha na conexão: {e}")
        return False, None

def generate_payloads():
    methods = payload_data['methods']
    custom_strings = payload_data['custom_strings']
    domains = payload_data['domains']
    method = random.choice(methods)
    custom_string = random.choice(custom_strings)
    domain = random.choice(domains)
    payload = f"{method} {domain} {custom_string}"
    print(f"Payload gerado: {payload}")

def check_for_updates():
    print("Verificando atualizações...")
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
    successful_proxies = []
    common_ports = [80, 8080, 443]
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
            ip_base = input("Informe o IP base (e.g., 192.168.1.0): ")
            num_ips = int(input("Quantos IPs deseja gerar? "))
            ips = generate_ip_range(ip_base, num_ips)
            for ip in ips:
                for port in common_ports:
                    result, external_ip = test_proxy(ip, port)
                    if result:
                        successful_proxies.append((ip, port, external_ip))
            display_results(successful_proxies)
        elif choice == '2':
            generate_payloads()
        elif choice == '3':
            ips_input = input("Informe os Proxy IPs para testar (separados por '#'): ")
            ips = ips_input.split('#')
            for ip_port_str in ips:
                ip, port = ip_port_str.split(':')
                port = int(port)
                test_proxy(ip, port)
        elif choice == '4':
            generate_proxies_by_operator_and_ip()
        elif choice == '5':
            check_for_updates()
        elif choice == '6':
            show_version()
        elif choice == '7':
            uninstall_script()

if __name__ == '__main__':
    main_menu()
