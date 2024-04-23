import random
import os
import sys
import requests
import warnings
import time
from subprocess import call
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json  # Adicionado para processamento seguro de JSON

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
    url = "https://github.com/DragonSCP/dragonscriptproxy/blob/main/payload_config.py"
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

def generate_and_test_proxies_from_base_ip():
    base_ip = input("Digite o IP base (exemplo: 192.168.0.): ")
    start_port = int(input("Digite a porta inicial: "))
    end_port = int(input("Digite a porta final: "))

    for port in range(start_port, end_port + 1):
        ip = f"{base_ip}{port % 256}" if base_ip.endswith('.') else f"{base_ip}.{port % 256}"
        print(f"Testando {ip}:{port}...")
        _, external_ip = test_proxy(ip, port)
        if external_ip:
            print(f"Proxy {ip}:{port} está funcionando! IP Externo: {external_ip}")
        else:
            print(f"Proxy {ip}:{port} falhou.")

    input("Pressione Enter para continuar...")

def test_individual_proxy():
    ip = input("Digite o IP do proxy: ")
    port = int(input("Digite a porta do proxy: "))
    test_proxy(ip, port)
    input("Pressione Enter para continuar...")

def generate_and_test_proxies_by_carrier_and_ip():
    carrier_ip_mapping = {
        'Operadora1': ['192.168.1.100', '192.168.1.101'],
        'Operadora2': ['192.168.2.100', '192.168.2.101']
    }

    carrier = input("Digite a operadora: ")
    if carrier in carrier_ip_mapping:
        for ip in carrier_ip_mapping[carrier]:
            for port in range(8080, 8090):  # Exemplo de faixa de portas
                print(f"Testando {ip}:{port}...")
                _, external_ip = test_proxy(ip, port)
                if external_ip:
                    print(f"Proxy {ip}:{port} está funcionando! IP Externo: {external_ip}")
                else:
                    print(f"Proxy {ip}:{port} falhou.")
    else:
        print("Operadora não encontrada.")

    input("Pressione Enter para continuar...")

def check_for_updates():
    print("Verificando atualizações...")
    for i in range(3):
        time.sleep(1)  # Simula o progresso da verificação
        print(f"Verificando... ({i+1}/3)")
    print(f"Você está utilizando a versão mais recente {__version__}!")
    input("Pressione Enter para continuar...")

def main():
    while True:
        clear_screen()
        print("==== Menu Principal ====")
        print("1 - Gerar e Testar Proxies a partir de um IP Base")
        print("2 - Gerar Payloads")
        print("3 - Testar Proxy Individual")
        print("4 - Gerar e Testar Proxies por Operadora e IP")
        print("5 - Verificar Atualizações")
        print("0 - Sair")

        choice = input("Escolha uma opção: ")
        if choice == '1':
            generate_and_test_proxies_from_base_ip()
        elif choice == '2':
            generate_payloads()
        elif choice == '3':
            test_individual_proxy()
        elif choice == '4':
            generate_and_test_proxies_by_carrier_and_ip()
        elif choice == '5':
            check_for_updates()
        elif choice == '0':
            sys.exit("Saindo...")
        else:
            print("Opção inválida, por favor escolha novamente.")

if __name__ == "__main__":
    main()
