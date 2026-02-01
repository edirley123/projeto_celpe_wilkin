from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Nome da planilha onde os dados serão salvos
NOME_ARQUIVO = 'dados_clientes_wilkin.xlsx'

@app.route('/salvar-dados', methods=['POST'])
def salvar_dados():
    # 1. Recebe os dados enviados pelo formulário
    dados_cliente = request.json
    
    # 2. Se a planilha já existir, carrega ela. Se não, cria uma nova.
    if os.path.exists(NOME_ARQUIVO):
        df = pd.read_excel(NOME_ARQUIVO)
        # Adiciona o novo cliente
        df = pd.concat([df, pd.DataFrame([dados_cliente])], ignore_index=True)
    else:
        # Cria a planilha com os dados do primeiro cliente
        df = pd.DataFrame([dados_cliente])

    # 3. Salva no Excel
    df.to_excel(NOME_ARQUIVO, index=False)
    
    return jsonify({"status": "sucesso", "mensagem": "Dados salvos na planilha!"})

if __name__ == '__main__':
    app.run(debug=True)