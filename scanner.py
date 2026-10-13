import subprocess
import sys

def run_nmap(target_ip):
    print(f"Iniciando escaneo de Nmap en el objetivo: {target_ip}")
    comando = [r"C:\Program Files (x86)\Nmap\nmap.exe", "-sS", "-sV", "-p-", target_ip]

    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print("\n Resultados del escaneo:")
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f" Error al ejecutar Nmap: {e}")
    except FileNotFoundError:
        print("Nmap no está instalado o no se encuentra en el sistema")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("Ingrese la IP objetivo: ")
    run_nmap(target)
