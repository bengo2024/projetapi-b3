"""
ProjetAPI - API REST pour gérer les soumissions de projets étudiants
"""

import json
from typing import List, Optional  # noqa: F401 - Will be used in future endpoints

from fastapi import FastAPI, HTTPException, status  # noqa: F401
from pydantic import BaseModel, HttpUrl


# Modèles Pydantic pour la validation
class ProjectCreate(BaseModel):
    """Modèle pour créer un nouveau projet"""

    studentName: str
    course: str
    githubUrl: HttpUrl


class Project(BaseModel):
    """Modèle complet d'un projet"""

    id: int
    studentName: str
    course: str
    githubUrl: str
    grade: Optional[float] = None


class GradeUpdate(BaseModel):
    """Modèle pour mettre à jour la note d'un projet"""

    grade: float


# Initialisation de l'application FastAPI
app = FastAPI(
    title="ProjetAPI",
    description="API REST pour gérer les soumissions de projets étudiants",
    version="1.0.0",
)

# Chemin du fichier de base de données
DB_FILE = "db.json"


# Fonctions utilitaires pour gérer db.json
def read_db():
    """Lit le fichier db.json et retourne son contenu"""
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"projects": [], "next_id": 1}


def write_db(data):
    """Écrit les données dans le fichier db.json"""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# Routes de l'API
@app.get("/")
def root():
    """Route racine de l'API"""
    return {
        "message": "Bienvenue sur ProjetAPI",
        "version": "1.0.0",
        "endpoints": [
            "POST /projects",
            "GET /projects",
            "GET /projects/{id}",
            "PUT /projects/{id}/grade",
            "DELETE /projects/{id}",
            "GET /projects/course/{courseName}",
        ],
    }


@app.get("/health")
def health_check():
    """Vérification de l'état de l'API"""
    return {"status": "healthy"}


# ============================================================================
# ENDPOINTS DE L'API
# ============================================================================


@app.post("/projects", response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate):
    """Créer un nouveau projet"""
    db = read_db()

    # Générer un nouvel ID
    new_id = db["next_id"]

    # Créer le projet
    new_project = {
        "id": new_id,
        "studentName": project.studentName,
        "course": project.course,
        "githubUrl": str(project.githubUrl),
        "grade": None,
    }

    # Ajouter à la liste
    db["projects"].append(new_project)
    db["next_id"] += 1

    # Sauvegarder
    write_db(db)

    return new_project
