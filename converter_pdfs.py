from pathlib import Path

import pymupdf4llm


# ERRO CORRIGIDO 1: Aqui mantemos nomes genéricos de variáveis
def converter_pdfs_para_markdown(pasta_entrada, pasta_saida):
    # 1. Configura os caminhos (Paths)
    input_path = Path(pasta_entrada)
    output_path = Path(pasta_saida)

    # 2. Cria a pasta de saída se ela não existir
    if not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Pasta criada: {output_path}")

    # 3. Verifica se a pasta de entrada existe
    if not input_path.exists():
        print(f"❌ Erro: A pasta de entrada '{pasta_entrada}' não foi encontrada.")
        print(f"   (O script procurou em: {input_path.resolve()})")
        return

    # 4. Lista todos os arquivos .pdf
    arquivos_pdf = list(input_path.glob("*.pdf"))

    if not arquivos_pdf:
        print("⚠️ Nenhum arquivo PDF encontrado na pasta de entrada.")
        return

    print(
        f"🔄 Iniciando conversão de {len(arquivos_pdf)} arquivos de '{pasta_entrada}'...\n"
    )

    # 5. Loop de conversão
    for arquivo in arquivos_pdf:
        try:
            nome_arquivo_md = arquivo.stem + ".md"
            caminho_final = output_path / nome_arquivo_md

            print(f"📄 Convertendo: {arquivo.name}...")

            md_text = pymupdf4llm.to_markdown(str(arquivo))

            with open(caminho_final, "w", encoding="utf-8") as f:
                f.write(md_text)

            print(f"✅ Salvo em: {caminho_final}\n")

        except Exception as e:
            print(f"❌ Erro ao converter {arquivo.name}: {e}\n")

    print("🏁 Processo finalizado!")


# --- Configuração ---
if __name__ == "__main__":
    # ERRO CORRIGIDO 2: Removemos a barra "/" do começo.
    # Assim ele procura DENTRO da pasta do projeto, não na raiz do Linux.

    PASTA_ORIGEM = "Acer-pdf"
    PASTA_DESTINO = "Acer-md"

    converter_pdfs_para_markdown(PASTA_ORIGEM, PASTA_DESTINO)
