import subprocess
import os

def render_quarto_project():
    # Caminho completo para o executável do Quarto
    quarto_executable_path = r"C:\Users\teodo\AppData\Local\Programs\Quarto\bin\quarto.exe"
    
    # Descobre o diretório onde este script (render.py) está localizado.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f">>> O projeto está localizado em: {script_dir}")
    
    # O comando para renderizar.
    command = [quarto_executable_path, "render"]
    
    print(">>> Iniciando a renderização do projeto Quarto...")
    print(f">>> Executando o comando: {' '.join(command)}")
    
    try:
        # Usamos o parâmetro 'cwd' (current working directory) para dizer ao
        # subprocesso para rodar a partir da pasta do projeto.
        result = subprocess.run(
            command, 
            check=True, 
            capture_output=True, 
            text=True,
            encoding='utf-8',
            cwd=script_dir  # <--- ESSA É A LINHA MÁGICA
        )
        
        print("\n--- Saída do Quarto ---")
        print(result.stdout)
        print("-----------------------\n")
        print("✅ Projeto renderizado com sucesso!")

    except subprocess.CalledProcessError as e:
        print("❌ Erro ao renderizar o projeto Quarto.")
        print(f"O processo retornou o código de erro: {e.returncode}")
        print("\n--- Saída de Erro do Quarto ---")
        print(e.stderr) # Imprime a mensagem de erro do Quarto
        print("---------------------------------\n")

if __name__ == "__main__":
    render_quarto_project()