from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():

    heure_actuelle = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mon Projet DevOps</title>
        <style>
            body {{
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                background-color: #161b22;
                padding: 40px;
                border-radius: 12px;
                border: 1px solid #30363d;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.8);
                text-align: center;
                max-width: 600px;
            }}
            h1 {{
                color: #58a6ff;
                margin-top: 0;
            }}
            .status {{
                display: inline-block;
                padding: 10px 20px;
                background-color: #50b4e6;
                color: white;
                border-radius: 30px;
                font-weight: bold;
                font-size: 1.1em;
                margin: 20px 0;
                box-shadow: 0 0 15px rgba(35, 134, 54, 0.4);
            }}
            .tech-stack {{
                margin-top: 20px;
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 10px;
            }}
            .tech-stack span {{
                padding: 6px 12px;
                background-color: #21262d;
                border: 1px solid #30363d;
                border-radius: 6px;
                font-size: 0.9em;
                color: #8b949e;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 0.85em;
                color: #8b949e;
                border-top: 1px solid #30363d;
                padding-top: 15px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Déploiement Réussi !</h1>
 
            <div class="status">✅ Pipeline CI/CD 100% Opérationnel</div>
            
            <div class="tech-stack">
                <span>🐍 FastAPI</span>
                <span>🐳 Docker</span>
                <span>⚙️ GitHub Actions</span>
                <span>🐧 Debian VM</span>
            </div>

            <div class="footer">
                Généré en direct par le serveur à : <strong>{heure_actuelle}</strong>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/api/status")
async def get_status():
    return {"status": "online", "message": "L'API est prête à recevoir des requêtes JSON !"}
