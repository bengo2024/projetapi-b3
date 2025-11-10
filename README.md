# ProjetAPI - API de Gestion de Projets Étudiants

> **TP Versionning Git et GitHub - Bachelor 3 Informatique**
> API REST développée avec FastAPI pour gérer les soumissions de projets étudiants.

---

## ⚡ Démarrage Rapide

**Nouveau sur le projet ?** Consultez **[QUICKSTART.md](QUICKSTART.md)** pour démarrer en 5 minutes !

**Vous êtes le Lead ?** Suivez **[SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)** pour configurer le projet.

---

## 📚 Documentation

| Fichier | Description |
|---------|-------------|
| **[QUICKSTART.md](QUICKSTART.md)** | 🚀 Démarrage rapide (5 min) |
| **[SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)** | 📋 Guide d'installation complet |
| **[ENDPOINTS_EXAMPLES.md](ENDPOINTS_EXAMPLES.md)** | 💻 Exemples de code pour chaque endpoint |
| **[PHASE3_GITHUB_ACTIONS.md](PHASE3_GITHUB_ACTIONS.md)** | 🔧 Guide CI/CD avec GitHub Actions |
| **[RAPPORT_TEMPLATE.md](RAPPORT_TEMPLATE.md)** | 📄 Template pour le rapport final |
| **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** | 🎯 Vue d'ensemble du projet |

---

## 🎯 Objectifs du TP

Ce projet vous permet de maîtriser :

- ✅ **Git Flow** : Branches main, develop, feature
- ✅ **Git Hooks** : Validation automatique avec pre-commit
- ✅ **GitHub** : Issues, Pull Requests, Revues de code
- ✅ **CI/CD** : GitHub Actions pour l'automatisation
- ✅ **Revue IA** : Intégration de Gemini pour la revue de code
- ✅ **Collaboration** : Travail en équipe sur un projet versionné

---

## 🚀 Installation Rapide

### Prérequis
- Python 3.11 ou supérieur
- Git

### Pour les Membres de l'Équipe

```bash
# 1. Cloner le dépôt
git clone https://github.com/LEAD_USERNAME/projetapi-b3.git
cd projetapi-b3
git switch develop

# 2. Créer l'environnement virtuel
python -m venv venv

# 3. Activer l'environnement
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt
pip install black flake8 isort pre-commit

# 5. Installer les hooks pre-commit
pre-commit install

# 6. Lancer le serveur
uvicorn main:app --reload
```

Le serveur sera accessible sur: `http://localhost:8000`

Documentation interactive (Swagger): `http://localhost:8000/docs`

## 📚 Endpoints de l'API

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| POST | `/projects` | Soumettre un nouveau projet |
| GET | `/projects` | Lister tous les projets |
| GET | `/projects/{id}` | Obtenir un projet par ID |
| PUT | `/projects/{id}/grade` | Noter un projet |
| DELETE | `/projects/{id}` | Supprimer un projet |
| GET | `/projects/course/{courseName}` | Filtrer par cours |

**📖 Pour des exemples détaillés, consultez [ENDPOINTS_EXAMPLES.md](ENDPOINTS_EXAMPLES.md)**

### Exemple : Créer un projet

```bash
curl -X POST http://localhost:8000/projects \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "Alice Dupont",
    "course": "Versionning Git",
    "githubUrl": "https://github.com/alice/projet-git"
  }'
```

### Tester l'API

**Option 1 : Swagger UI (Recommandé)**
```bash
# Ouvrir dans le navigateur
http://localhost:8000/docs
```

**Option 2 : Script Python**
```bash
pip install requests
python test_api.py
```

**Option 3 : Script Bash**
```bash
bash test_api.sh
```

## 🔧 Développement

### Structure du Projet

```
final_git/
├── .github/workflows/        # GitHub Actions (CI/CD)
├── main.py                   # Application FastAPI
├── db.json                   # Base de données JSON
├── requirements.txt          # Dépendances Python
├── pyproject.toml           # Config Black/isort
├── .flake8                  # Config Flake8
├── .pre-commit-config.yaml  # Hooks pre-commit
├── test_api.py              # Tests Python
├── test_api.sh              # Tests Bash
└── *.md                     # Documentation
```

### Git Flow

Ce projet utilise le modèle **Git Flow** :

- **`main`** : Production (versions stables uniquement)
- **`develop`** : Développement (branche par défaut)
- **`feature/*`** : Fonctionnalités individuelles

### Workflow de Développement

```bash
# 1. Partir de develop
git switch develop
git pull origin develop

# 2. Créer une branche feature
git switch -c feature/nom-feature

# 3. Développer et commiter
git add .
git commit -m "Feat: Description (fixes #N)"

# 4. Pousser
git push origin feature/nom-feature

# 5. Créer une Pull Request sur GitHub
# - Vers develop
# - Lier l'Issue
# - Assigner 2 reviewers
```

**📖 Guide complet : [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)**

---

## 🧪 Tests

### Lancer les Tests

```bash
# Option 1: Script Python (recommandé)
pip install requests
python test_api.py

# Option 2: Script Bash
bash test_api.sh

# Option 3: Swagger UI
# Ouvrir http://localhost:8000/docs
```

---

## 🚀 CI/CD

Le projet utilise **GitHub Actions** pour :

- ✅ Linting (Flake8)
- ✅ Formatage (Black)
- ✅ Tri des imports (isort)
- ✅ Revue de code par IA (Gemini)
- ✅ Notifications par email

**📖 Guide complet : [PHASE3_GITHUB_ACTIONS.md](PHASE3_GITHUB_ACTIONS.md)**

---

## 👥 Équipe

- **Lead / Maintainer** : [NOM]
- **Développeurs** : [NOMS]

---

## 📄 Livrables

- ✅ Dépôt GitHub avec Git Flow
- ✅ 7 fonctionnalités implémentées
- ✅ Pipeline CI/CD fonctionnel
- ✅ Release v1.0.0
- ✅ Rapport PDF avec captures d'écran

**📖 Template de rapport : [RAPPORT_TEMPLATE.md](RAPPORT_TEMPLATE.md)**

---

## 📝 License

Projet académique - Bachelor 3 Informatique
Module : Versionning et Gestion de Projet

---

## 🆘 Besoin d'Aide ?

1. Consultez **[QUICKSTART.md](QUICKSTART.md)** pour démarrer
2. Lisez **[SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)** pour l'installation
3. Voir **[ENDPOINTS_EXAMPLES.md](ENDPOINTS_EXAMPLES.md)** pour des exemples de code
4. Contactez le Lead ou l'équipe

**Bon courage ! 🚀**
