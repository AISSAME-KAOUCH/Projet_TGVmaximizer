import uvicorn
from fastapi import FastAPI
from DAO.profilDAO import ProfilDAO

app = FastAPI()

@app.get("/profil/{email}")
async def get_profil(email):
    return ProfilDAO().find_by_id(email)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
