# Import classique
import uvicorn
from fastapi import FastAPI
from DAO.profilDAO import ProfilDAO
# On instancie le webservice
app = FastAPI()

# Défintion du endpoint get /todo
@app.get("/profil")
async def get_profil():
    # Vous devez récupérer les attaques en base en utilisant votre DAO
    return ProfilDAO().find_by_id(1)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
