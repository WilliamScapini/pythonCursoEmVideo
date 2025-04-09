from playsound import playsound

def reproduzir_audio(caminho_arquivo):
    """Tenta reproduzir o arquivo de áudio no caminho especificado."""
    try:
        playsound(caminho_arquivo)
        print(f"Reproduzindo: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao reproduzir {caminho_arquivo}: {e}")

if __name__ == "__main__":
    arquivo = input("Digite o caminho do arquivo de áudio (MP3 ou WAV): ")
    reproduzir_audio(arquivo)
    print("Reprodução concluída.")