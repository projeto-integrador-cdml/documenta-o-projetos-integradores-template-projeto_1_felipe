import subprocess
import os

def render_quarto_project():
    """
    Executa 'quarto render' confiando que o Quarto está no PATH do sistema.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f">>> O projeto está localizado em: {script_dir}")
    
    # Comando simplificado, sem caminho fixo
    command = ["quarto", "render"]
    
    print(">>> Iniciando a renderização do projeto Quarto...")
    print(f">>> Executando o comando: {' '.join(command)}")
    
    try:
        result = subprocess.run(
            command, 
            check=True, 
            capture_output=True, 
            text=True,
            encoding='utf-8',
            cwd=script_dir
        )
        
        print("\n--- Saída do Quarto ---")
        print(result.stdout)
        print("-----------------------\n")
        print("✅ Projeto renderizado com sucesso!")

    except FileNotFoundError:
        print("❌ Erro: O comando 'quarto' não foi encontrado.")
        print("Verifique se o Quarto está instalado e se o seu diretório 'bin' foi adicionado ao PATH do sistema.")
        print("Pode ser necessário reiniciar o VS Code ou o computador após a instalação.")

    except subprocess.CalledProcessError as e:
        print("❌ Erro ao renderizar o projeto Quarto.")
        print(f"O processo retornou o código de erro: {e.returncode}")
        print("\n--- Saída de Erro do Quarto ---")
        print(e.stderr)
        print("---------------------------------\n")

if __name__ == "__main__":
    render_quarto_project()