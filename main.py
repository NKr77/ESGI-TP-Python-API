from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Création de l'application
app = FastAPI()

# Définition de ce qu'est un "Serveur" à partir de l'exemple donné du TP
class Server(BaseModel):
    id: int
    name: str
    ip: str
    ram: str
    size: str

# Liste vide pour stocker nos serveurs
servers_db = []

# --- ENDPOINTS ---

# Lire la liste des serveurs
@app.get("/servers", response_model=List[Server])
def get_all_servers():
    return servers_db

# Ajouter ou modifier un serveur
@app.post("/servers", status_code=201)
def add_or_update_server(new_server: Server):
    # On cherche si l'ID existe déjà dans notre liste
    for index, s in enumerate(servers_db):
        if s["id"] == new_server.id:
            # Si trouvé, on remplace les anciennes données
            servers_db[index] = new_server.model_dump()
            return {"message": "Serveur mis à jour", "data": servers_db[index]}
    
    # Si non trouvé, on ajoute le nouveau serveur à la liste
    servers_db.append(new_server.model_dump())
    return {"message": "Serveur ajouté avec succès", "data": new_server}

# Modifier un serveur existant
@app.put("/servers/{server_id}")
def update_server(server_id: int, updated_server: Server):
    for index, s in enumerate(servers_db):
        if s["id"] == server_id:
            servers_db[index] = updated_server.model_dump()
            return {"message": "Serveur modifié", "data": servers_db[index]}
    
    # Si l'ID n'existe pas, on renvoie une erreur 404
    raise HTTPException(status_code=404, detail="Serveur non trouvé")

# Supprimer un serveur
@app.delete("/servers/{server_id}")
def delete_server(server_id: int):
    for index, s in enumerate(servers_db):
        if s["id"] == server_id:
            # On retire le serveur de la liste
            deleted_server = servers_db.pop(index)
            return {"message": "Serveur supprimé", "data": deleted_server}
            
    # Si l'ID n'existe pas, on renvoie une erreur 404
    raise HTTPException(status_code=404, detail="Serveur non trouvé")

# Lancement du serveur
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)