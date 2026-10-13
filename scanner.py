# red_team/scanner.py
import subprocess
import sys

def run_nmap(target_ip):
    print(f"[*] Iniciando escaneo Nmap en el objetivo: {target_ip}")
    # Comando Nmap: -sS (TCP SYN scan), -sV (Detección de versiones), -p- (Todos los puertos)
    command = [r"C:\Program Files (x86)\Nmap\nmap.exe", "-sS", "-sV", "-p-", target_ip]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("\n[+] Resultados del escaneo:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error al ejecutar Nmap: {e}")
    except FileNotFoundError:
        print("[!] Nmap no está instalado o no se encuentra en el PATH del sistema.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("Ingrese la IP objetivo: ")
    run_nmap(target)