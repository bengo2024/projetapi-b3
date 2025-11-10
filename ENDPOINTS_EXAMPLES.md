# 📚 Guide d'Implémentation des Endpoints

Ce document fournit des exemples et des conseils pour implémenter chaque endpoint de l'API.

---

## 🎯 Issue #1 : POST /projects - Soumettre un nouveau projet

### Objectif
Créer un endpoint qui permet de soumettre un nouveau projet étudiant.

### Spécifications
- **Route :** `POST /projects`
- **Body :** JSON avec `studentName`, `course`, `githubUrl`
- **Validation :** Utiliser Pydantic (`ProjectCreate`)
- **Retour :** Le projet créé avec son `id` généré
- **Status Code :** 201 Created

### Exemple d'implémentation

```python
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
        "grade": None
    }

    # Ajouter à la liste
    db["projects"].append(new_project)
    db["next_id"] += 1

    # Sauvegarder
    write_db(db)

    return new_project
```

### Test avec curl

```bash
curl -X POST http://localhost:8000/projects \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "Alice Dupont",
    "course": "Versionning Git",
    "githubUrl": "https://github.com/alice/projet-git"
  }'
```

### Résultat attendu

```json
{
  "id": 1,
  "studentName": "Alice Dupont",
  "course": "Versionning Git",
  "githubUrl": "https://github.com/alice/projet-git",
  "grade": null
}
```

---

## 🎯 Issue #2 : GET /projects - Lister tous les projets

### Objectif
Récupérer la liste complète de tous les projets soumis.

### Spécifications
- **Route :** `GET /projects`
- **Paramètres :** Aucun
- **Retour :** Liste de tous les projets
- **Status Code :** 200 OK

### Exemple d'implémentation

```python
@app.get("/projects", response_model=List[Project])
def get_all_projects():
    """Récupérer tous les projets"""
    db = read_db()
    return db["projects"]
```

### Test avec curl

```bash
curl http://localhost:8000/projects
```

### Résultat attendu

```json
[
  {
    "id": 1,
    "studentName": "Alice Dupont",
    "course": "Versionning Git",
    "githubUrl": "https://github.com/alice/projet-git",
    "grade": null
  },
  {
    "id": 2,
    "studentName": "Bob Martin",
    "course": "DevOps",
    "githubUrl": "https://github.com/bob/projet-devops",
    "grade": 18.5
  }
]
```

---

## 🎯 Issue #3 : GET /projects/:id - Obtenir un projet par ID

### Objectif
Récupérer les détails d'un projet spécifique par son ID.

### Spécifications
- **Route :** `GET /projects/{id}`
- **Paramètres :** `id` (int) dans l'URL
- **Retour :** Le projet correspondant
- **Status Code :** 200 OK ou 404 Not Found
- **Erreur :** Si le projet n'existe pas, retourner 404

### Exemple d'implémentation

```python
@app.get("/projects/{project_id}", response_model=Project)
def get_project_by_id(project_id: int):
    """Récupérer un projet par son ID"""
    db = read_db()

    # Chercher le projet
    for project in db["projects"]:
        if project["id"] == project_id:
            return project

    # Si non trouvé, lever une exception 404
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Project with id {project_id} not found"
    )
```

### Test avec curl

```bash
# Projet existant
curl http://localhost:8000/projects/1

# Projet inexistant
curl http://localhost:8000/projects/999
```

### Résultat attendu (404)

```json
{
  "detail": "Project with id 999 not found"
}
```

---

## 🎯 Issue #4 : PUT /projects/:id/grade - Noter un projet

### Objectif
Permettre à un professeur d'ajouter ou modifier la note d'un projet.

### Spécifications
- **Route :** `PUT /projects/{id}/grade`
- **Paramètres :** `id` (int) dans l'URL
- **Body :** JSON avec `grade` (float)
- **Validation :** Note entre 0 et 20
- **Retour :** Le projet mis à jour
- **Status Code :** 200 OK ou 404 Not Found

### Exemple d'implémentation

```python
@app.put("/projects/{project_id}/grade", response_model=Project)
def update_project_grade(project_id: int, grade_update: GradeUpdate):
    """Mettre à jour la note d'un projet"""
    db = read_db()

    # Validation de la note
    if not 0 <= grade_update.grade <= 20:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Grade must be between 0 and 20"
        )

    # Chercher et mettre à jour le projet
    for project in db["projects"]:
        if project["id"] == project_id:
            project["grade"] = grade_update.grade
            write_db(db)
            return project

    # Si non trouvé
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Project with id {project_id} not found"
    )
```

### Test avec curl

```bash
curl -X PUT http://localhost:8000/projects/1/grade \
  -H "Content-Type: application/json" \
  -d '{"grade": 18.5}'
```

### Résultat attendu

```json
{
  "id": 1,
  "studentName": "Alice Dupont",
  "course": "Versionning Git",
  "githubUrl": "https://github.com/alice/projet-git",
  "grade": 18.5
}
```

---

## 🎯 Issue #5 : DELETE /projects/:id - Supprimer un projet

### Objectif
Supprimer une soumission de projet.

### Spécifications
- **Route :** `DELETE /projects/{id}`
- **Paramètres :** `id` (int) dans l'URL
- **Retour :** Message de confirmation
- **Status Code :** 200 OK ou 404 Not Found

### Exemple d'implémentation

```python
@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    """Supprimer un projet"""
    db = read_db()

    # Chercher l'index du projet
    for i, project in enumerate(db["projects"]):
        if project["id"] == project_id:
            deleted_project = db["projects"].pop(i)
            write_db(db)
            return {
                "message": f"Project {project_id} deleted successfully",
                "deleted_project": deleted_project
            }

    # Si non trouvé
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Project with id {project_id} not found"
    )
```

### Test avec curl

```bash
curl -X DELETE http://localhost:8000/projects/1
```

### Résultat attendu

```json
{
  "message": "Project 1 deleted successfully",
  "deleted_project": {
    "id": 1,
    "studentName": "Alice Dupont",
    "course": "Versionning Git",
    "githubUrl": "https://github.com/alice/projet-git",
    "grade": 18.5
  }
}
```

---

## 🎯 Issue #6 : GET /projects/course/:courseName - Filtrer par cours

### Objectif
Récupérer tous les projets d'un cours spécifique.

### Spécifications
- **Route :** `GET /projects/course/{courseName}`
- **Paramètres :** `courseName` (string) dans l'URL
- **Retour :** Liste des projets du cours
- **Status Code :** 200 OK
- **Note :** Retourne une liste vide si aucun projet trouvé

### Exemple d'implémentation

```python
@app.get("/projects/course/{course_name}", response_model=List[Project])
def get_projects_by_course(course_name: str):
    """Récupérer tous les projets d'un cours spécifique"""
    db = read_db()

    # Filtrer les projets par cours (insensible à la casse)
    filtered_projects = [
        project for project in db["projects"]
        if project["course"].lower() == course_name.lower()
    ]

    return filtered_projects
```

### Test avec curl

```bash
curl http://localhost:8000/projects/course/Versionning%20Git
```

### Résultat attendu

```json
[
  {
    "id": 1,
    "studentName": "Alice Dupont",
    "course": "Versionning Git",
    "githubUrl": "https://github.com/alice/projet-git",
    "grade": 18.5
  },
  {
    "id": 3,
    "studentName": "Charlie Durand",
    "course": "Versionning Git",
    "githubUrl": "https://github.com/charlie/projet-git",
    "grade": null
  }
]
```

---

## 🎯 Issue #7 : Documentation Wiki

### Objectif
Rédiger une documentation complète dans le Wiki GitHub.

### Contenu à créer

#### Page 1 : Home (Accueil)
- Présentation du projet
- Technologies utilisées
- Lien vers les autres pages

#### Page 2 : Installation
- Prérequis
- Étapes d'installation
- Configuration de l'environnement

#### Page 3 : Utilisation de l'API
- Liste des endpoints
- Exemples de requêtes pour chaque endpoint
- Codes de retour possibles

#### Page 4 : Développement
- Workflow Git Flow
- Comment contribuer
- Standards de code

### Exemple de structure Wiki

```markdown
# ProjetAPI - Documentation

## 🏠 Accueil

Bienvenue dans la documentation de ProjetAPI !

### Navigation
- [Installation](Installation)
- [Utilisation de l'API](API-Usage)
- [Guide de Développement](Development)

---

## 📦 Installation

### Prérequis
- Python 3.11+
- Git

### Étapes
1. Cloner le dépôt
2. Créer l'environnement virtuel
3. Installer les dépendances
4. Lancer le serveur

[Voir les détails dans README.md]

---

## 📚 Utilisation de l'API

### POST /projects
Soumettre un nouveau projet...

[Exemples détaillés pour chaque endpoint]
```

---

## 💡 Conseils Généraux

### 1. Validation des Données
Toujours utiliser Pydantic pour valider les entrées :
```python
class ProjectCreate(BaseModel):
    studentName: str
    course: str
    githubUrl: HttpUrl  # Valide automatiquement le format URL
```

### 2. Gestion des Erreurs
Utiliser `HTTPException` pour les erreurs :
```python
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Resource not found"
)
```

### 3. Documentation Automatique
FastAPI génère automatiquement la documentation Swagger.
Accédez-y sur : `http://localhost:8000/docs`

### 4. Tests Manuels
Utilisez Swagger UI ou curl pour tester chaque endpoint avant de créer la PR.

### 5. Messages de Commit
Suivez le format :
```
Feat: Add POST /projects endpoint (fixes #1)
Fix: Correct validation in PUT /projects/:id/grade (fixes #4)
Docs: Update API documentation in Wiki (fixes #7)
```

---

**Bon développement ! 🚀**
