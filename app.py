import uvicorn
from fastapi import FastAPI
from DAO.profilDAO import ProfilDAO

app = FastAPI()

@app.get("/profil")
async def get_profil():
    return ProfilDAO().find_by_id(1)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
