# ProjetAPI - API de Gestion de Projets Étudiants

API REST développée avec FastAPI pour gérer les soumissions de projets étudiants.

## 🚀 Installation

### Prérequis
- Python 3.11 ou supérieur
- pip

### Étapes d'installation

1. **Cloner le dépôt**
```bash
git clone <URL_DU_DEPOT>
cd final_git
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel**

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

4. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

5. **Installer les outils de développement**
```bash
pip install black flake8 isort pre-commit
```

6. **Installer les hooks pre-commit**
```bash
pre-commit install
```

## 🏃 Lancer le serveur

```bash
uvicorn main:app --reload
```

Le serveur sera accessible sur: `http://localhost:8000`

Documentation interactive (Swagger): `http://localhost:8000/docs`

## 📚 Endpoints de l'API

### 1. POST /projects
Soumettre un nouveau projet

**Body:**
```json
{
  "studentName": "John Doe",
  "course": "Versionning Git",
  "githubUrl": "https://github.com/user/repo"
}
```

### 2. GET /projects
Lister tous les projets soumis

### 3. GET /projects/{id}
Obtenir les détails d'un projet spécifique

### 4. PUT /projects/{id}/grade
Noter un projet

**Body:**
```json
{
  "grade": 18.5
}
```

### 5. DELETE /projects/{id}
Supprimer une soumission de projet

### 6. GET /projects/course/{courseName}
Filtrer les projets par cours

## 🔧 Développement

### Structure du projet
```
.
├── main.py                    # Application FastAPI principale
├── db.json                    # Base de données (fichier JSON)
├── requirements.txt           # Dépendances Python
├── pyproject.toml            # Configuration Black/isort
├── .flake8                   # Configuration Flake8
├── .pre-commit-config.yaml   # Configuration des hooks pre-commit
└── README.md                 # Ce fichier
```

### Git Flow

Ce projet utilise le modèle Git Flow:
- `main`: Branche de production (versions stables uniquement)
- `develop`: Branche de développement (branche par défaut)
- `feature/*`: Branches de fonctionnalités

### Workflow de développement

1. Toujours partir de `develop`:
```bash
git switch develop
git pull origin develop
```

2. Créer une branche de fonctionnalité:
```bash
git switch -c feature/nom-de-la-feature
```

3. Développer et commiter (les hooks pre-commit se déclenchent automatiquement):
```bash
git add .
git commit -m "Feat: Description de la fonctionnalité"
```

4. Pousser la branche:
```bash
git push origin feature/nom-de-la-feature
```

5. Créer une Pull Request sur GitHub vers `develop`

## 👥 Équipe

- Lead: [NOM]
- Membres: [NOMS]

## 📝 License

Projet académique - Bachelor 3 Informatique

