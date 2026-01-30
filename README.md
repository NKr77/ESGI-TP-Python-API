# TP API Python - Gestion de Serveurs (cours ESGI)

Ce projet implémente une API RESTful avec FastAPI pour la gestion d'un parc de serveurs.

## Installation et Lancement

1. Installation des dépendances
```bash
pip install fastapi uvicorn

```

2. Lancement du serveur

```bash
python -m uvicorn main:app --reload

```

L'API est accessible à l'adresse : http://127.0.0.1:8000

## Documentation des Endpoints

| Méthode | Route | Description |
| --- | --- | --- |
| GET | /servers | Liste tous les serveurs. |
| POST | /servers | Ajoute ou met à jour un serveur. |
| PUT | /servers/{id} | Modifie un serveur spécifique. |
| DELETE | /servers/{id} | Supprime un serveur spécifique. |

## Tests Postman

La collection de tests incluant les requêtes pré-configurées est disponible via le lien suivant :
[Collection Postman - NK Team's Workspace](https://krusicnicolas-8422704.postman.co/workspace/NK-Team's-Workspace~55c351b5-2b5b-41e0-823a-09f811529620/collection/51921457-e59ea812-e6eb-4feb-a508-1ccbdf1f9316?action=share&creator=51921457)

## Modèle de données

```json
{
    "id": 1,
    "name": "TEST-NAME",
    "ip": "192.168.1.1",
    "ram": "16GB",
    "size": "500GB"
}

```

## Documentation

Une interface Swagger est disponible pour tester les routes : http://127.0.0.1:8000/docs