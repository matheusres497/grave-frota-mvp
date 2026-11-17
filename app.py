from flask import Flask, render_template_string, request

app = Flask(__name__)

# Base HTML com suporte a alternância de telas e alto contraste
TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>GRAVE - Frota Operacional (ODS 3)</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background-color: {{ bg_color }}; color: {{ text_color }}; }
        header { background: {{ header_bg }}; color: white; padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; }
        nav a { color: white; margin-left: 20px; text-decoration: none; font-weight: bold; }
        .container { padding: 30px; max-width: 900px; margin: auto; }
        .card { background: {{ card_bg }}; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px; border: {{ card_border }}; }
        .badge { background: #28a745; color: white; padding: 5px 10px; border-radius: 4px; font-size: 0.9em; }
        table { width: 100%%; border-collapse: collapse; margin-top: 10px; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
        th { background-color: {{ th_bg }}; }
        .btn { display: inline-block; padding: 8px 15px; background: #007bff; color: white; text-decoration: none; border-radius: 4px; margin-top: 10px; }
    </style>
</head>
<body>
    <header>
        <h2>GRAVE - MVP ODS 3 ({{ titulo_pagina }})</h2>
        <nav>
            <a href="/">Painel (Tela 1)</a>
            <a href="/veiculos">Veículos (Tela 2)</a>
            <a href="/acessibilidade">Alto Contraste (Tela 3)</a>
        </nav>
    </header>
    <div class="container">
        {{ conteudo | safe }}
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    conteudo = """
        <div class="card">
            <h3>Visão Geral da Frota e Emergências</h3>
            <p>Status do Sistema: <span class="badge">Operacional</span></p>
            <p>Ambulâncias ativas conectadas ao suporte de saúde (ODS 3): <strong>4 unidades</strong></p>
            <p>Campanhas PIX de apoio humanitário: <strong>Ativas</strong></p>
            <a class="btn" href="/veiculos">Acessar Gestão de Veículos &rarr;</a>
        </div>
    """
    return render_template_string(TEMPLATE, titulo_pagina="Painel Principal", conteudo=conteudo,
                                  bg_color="#f4f6f9", text_color="#333", header_bg="#1b2a4a", card_bg="white", card_border="none", th_bg="#f2f2f2")

@app.route("/veiculos")
def veiculos():
    conteudo = """
        <div class="card">
            <h3>Fluxo Secundário: Controle de Veículos e Manutenção Preventiva</h3>
            <p>Listagem de frotas vinculadas aos chamados de urgência:</p>
            <table>
                <tr><th>Veículo / Placa</th><th>Quilometragem</th><th>Status Manutenção</th></tr>
                <tr><td>Ambulância Alfa 01 (ABC-1234)</td><td>144.000 km</td><td>Revisada (OK)</td></tr>
                <tr><td>Unidade Resgate Beta (XYZ-9876)</td><td>152.300 km</td><td>Pendente Revisão</td></tr>
            </table>
            <a class="btn" href="/acessibilidade">Testar Modo Acessibilidade &rarr;</a>
        </div>
    """
    return render_template_string(TEMPLATE, titulo_pagina="Gestão de Veículos", conteudo=conteudo,
                                  bg_color="#f4f6f9", text_color="#333", header_bg="#1b2a4a", card_bg="white", card_border="none", th_bg="#e9ecef")

@app.route("/acessibilidade")
def acessibilidade():
    conteudo = """
        <div class="card">
            <h3>Recurso de Acessibilidade: Modo de Alto Contraste (WCAG AA)</h3>
            <p>Interface adaptada com inversão de cores de alto contraste, garantindo legibilidade absoluta para operadores com baixa visão ou em ambientes de alta luminosidade externa.</p>
            <p><strong>Conexão ODS 3:</strong> Assegura que socorristas e gestores operem o sistema sem falhas visuais em situações críticas de saúde pública e resgate.</p>
            <a class="btn" href="/">Retornar ao Painel Principal</a>
        </div>
    """
    return render_template_string(TEMPLATE, titulo_pagina="Modo Acessibilidade", conteudo=conteudo,
                                  bg_color="#000000", text_color="#00ff00", header_bg="#222222", card_bg="#111111", card_border="2px solid #00ff00", th_bg="#222222")

if __name__ == "__main__":
    app.run(debug=True)
