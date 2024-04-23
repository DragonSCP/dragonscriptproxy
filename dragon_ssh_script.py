import random
import os
import sys
import requests
import warnings
import time
import hashlib
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json  # Para processamento de JSON

# Ignorar avisos de certificados nÃ£o verificados
warnings.simplefilter('ignore', InsecureRequestWarning)

# VersÃ£o atualizada da script
__version__ = "1.4.0"
payload_data = {}  # Define payload_data globalmente para evitar NameError

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def test_proxy(ip, port):
    proxy_url = f"http://{ip}:{port}" if port in [80, 8080] else f"https://{ip}:{port}"
    proxy_dict = {'http': proxy_url, 'https': proxy_url}
    try:
        response = requests.get('http://icanhazip.com', proxies=proxy_dict, timeout=5, verify=False)
        if response.status_code == 200:
            external_ip = response.text.strip()
            return True, external_ip
        else:
            return False, None
    except requests.exceptions.RequestException:
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
        print("Dados de payload nÃ£o carregados. Abortando geraÃ§Ã£o de payloads.")
        return

    try:
        num_payloads = int(input("Quantas payloads deseja gerar? "))
    except ValueError:
        print("Entrada invÃ¡lida, por favor insira um nÃºmero inteiro.")
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

def test_individual_proxy():
    input_proxies = input("Insira os IPs dos proxies separados por '#': ")
    proxies = input_proxies.split('#')
    ports = [80, 8080, 443]
    proxy_results = {}

    print("Testando proxies, por favor aguarde...")
    for ip in proxies:
        successful_ports = []
        for port in ports:
            result, external_ip = test_proxy(ip, port)
            if result:
                if port not in successful_ports:
                    successful_ports.append(port)
        if successful_ports:
            proxy_results[ip] = {'external_ip': external_ip, 'ports': sorted(successful_ports)}

    if proxy_results:
        print("\nProxies que funcionaram:")
        for ip, details in proxy_results.items():
            print(f"{ip}\nIP Externo: {details['external_ip']}\nPortas que pegaram: {', '.join(map(str, details['ports']))}")
    else:
        print("\nNenhum proxy funcionou. Tente outros IPs.")

    input("Pressione Enter para continuar...")
    clear_screen()

def main():
    clear_screen()
    while True:
        print("==== Menu Principal ====")
        print("1 - Gerar e Testar Proxies a partir de um IP Base")
        print("2 - Gerar Payloads")
        print("3 - Testar Proxy Individual")
        print("4 - Gerar e Testar Proxies por Operadora e IP")
        print("5 - Verificar AtualizaÃ§Ãµes")
        choice = input("Escolha uma opÃ§Ã£o ou pressione Enter para sair: ")

        if choice == '':
            break
        elif choice == '1':
            # LÃ³gica para Gerar e Testar Proxies a partir de um IP Base
            pass
        elif choice == '2':
            generate_payloads()
        elif choice == '3':
            test_individual_proxy()
        elif choice == '4':
            # LÃ³gica para Gerar e Testar Proxies por Operadora e IP
            pass
        elif choice == '5':
            update_script()
        else:
            print("OpÃ§Ã£o invÃ¡lida. Por favor, tente novamente.")
            time.sleep(2)
        clear_screen()

if __name__ == "__main__":
    main()
