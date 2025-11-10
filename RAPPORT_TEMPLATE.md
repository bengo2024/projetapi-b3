# Rapport de TP - ProjetAPI
## Versionning Git et GitHub - Bachelor 3 Informatique

---

## 📋 Page de Garde

**Titre du Projet :** ProjetAPI - API de Gestion de Projets Étudiants

**Module :** Versionning et Gestion de Projet

**Niveau :** Bachelor 3 Informatique

**Technologie Choisie :** Python / FastAPI + Pydantic

**Date :** [Date de soumission]

### 👥 Membres de l'Équipe

| Nom Complet | Rôle | Email |
|-------------|------|-------|
| [Nom 1] | Lead / Maintainer | [email1@univ.com] |
| [Nom 2] | Développeur | [email2@univ.com] |
| [Nom 3] | Développeur | [email3@univ.com] |
| [Nom 4] | Développeur | [email4@univ.com] |
| [Nom 5] | Développeur | [email5@univ.com] |
| [Nom 6] | Développeur | [email6@univ.com] |
| [Nom 7] | Développeur | [email7@univ.com] |

**URL du Dépôt GitHub :** https://github.com/[USERNAME]/projetapi-b3

---

## 📊 Tableau de Participation

### Répartition des Issues et Pull Requests

| Membre | Issue(s) Assignée(s) | PR(s) Créée(s) | Revues Effectuées | Statut |
|--------|---------------------|----------------|-------------------|--------|
| [Nom 1] | #1 - POST /projects | PR #X | PR #Y, PR #Z | ✅ Complété |
| [Nom 2] | #2 - GET /projects | PR #X | PR #Y, PR #Z | ✅ Complété |
| [Nom 3] | #3 - GET /projects/:id | PR #X | PR #Y, PR #Z | ✅ Complété |
| [Nom 4] | #4 - PUT /projects/:id/grade | PR #X | PR #Y, PR #Z | ✅ Complété |
| [Nom 5] | #5 - DELETE /projects/:id | PR #X | PR #Y, PR #Z | ✅ Complété |
| [Nom 6] | #6 - GET /projects/course/:courseName | PR #X | PR #Y, PR #Z | ✅ Complété |
| [Nom 7] | #7 - Documentation Wiki | PR #X | PR #Y, PR #Z | ✅ Complété |

**Note :** Chaque membre a été l'auteur principal d'au moins une Pull Request et a participé à au moins 2 revues de code.

---

## 📸 Captures d'Écran Obligatoires

### 1. Hook Pre-Commit Bloquant un Commit

**Description :** Démonstration du hook pre-commit qui détecte et corrige automatiquement du code mal formaté.

```
[INSÉRER CAPTURE D'ÉCRAN ICI]
```

**Commande exécutée :**
```bash
git commit -m "Test hook"
```

**Résultat :** Le hook a détecté des erreurs de formatage et a automatiquement corrigé le code avec Black.

---

### 2. Discussion de Revue de Code Riche

**Description :** Pull Request montrant une discussion de revue de code avec commentaires, "Request changes", et approbations multiples.

```
[INSÉRER CAPTURE D'ÉCRAN ICI]
```

**PR concernée :** PR #[X] - [Titre de la PR]

**Éléments visibles :**
- ✅ Commentaires constructifs des reviewers
- ✅ "Request changes" avec justification
- ✅ Réponses de l'auteur
- ✅ Approbations finales (minimum 2)

---

### 3. CI (GitHub Actions) Échouée Bloquant le Merge

**Description :** Pull Request montrant le pipeline CI qui échoue (rouge) et empêche le merge.

```
[INSÉRER CAPTURE D'ÉCRAN ICI]
```

**PR concernée :** PR #[X] - Test CI Failure

**Checks échoués :**
- ❌ Lint with Flake8
- ❌ Check Code Formatting (Black)

**Résultat :** Le bouton "Merge" est désactivé tant que les checks ne passent pas.

---

### 4. Commentaire Généré par le LLM (IA)

**Description :** Pull Request montrant le commentaire automatique généré par Gemini AI avec mention de l'auteur.

```
[INSÉRER CAPTURE D'ÉCRAN ICI]
```

**PR concernée :** PR #[X] - [Titre de la PR]

**Éléments visibles :**
- ✅ Commentaire de l'IA avec analyse du code
- ✅ Mention de l'auteur (@username)
- ✅ Suggestions d'amélioration ou détection de bugs

---

### 5. Email Reçu par un Membre de l'Équipe

**Description :** Email de notification envoyé automatiquement par GitHub Actions à toute l'équipe.

```
[INSÉRER CAPTURE D'ÉCRAN ICI]
```

**Contenu de l'email :**
- ✅ Sujet : "🔔 Revue LLM pour PR #[X] par @[username]"
- ✅ Détails de la PR
- ✅ Revue générée par l'IA
- ✅ Lien vers la PR

**Preuve :** Capture montrant l'email dans la boîte de réception d'un membre.

---

### 6. Page de la Release v1.0.0

**Description :** Page GitHub de la Release v1.0.0 avec notes de version.

```
[INSÉRER CAPTURE D'ÉCRAN ICI]
```

**Éléments visibles :**
- ✅ Tag v1.0.0
- ✅ Notes de version complètes
- ✅ Liste des fonctionnalités
- ✅ Informations sur l'équipe

---

## 🔄 Workflow Git Flow Utilisé

### Structure des Branches

```
main (production)
  └── develop (développement)
       ├── feature/post-projects
       ├── feature/get-projects
       ├── feature/get-project-by-id
       ├── feature/put-grade
       ├── feature/delete-project
       ├── feature/filter-by-course
       └── feature/documentation
```

### Processus de Développement

1. **Création de branche :** Chaque fonctionnalité part de `develop`
2. **Développement :** Code + commits avec messages clairs
3. **Hook pre-commit :** Validation automatique du formatage
4. **Push :** Envoi de la branche sur GitHub
5. **Pull Request :** Création de PR vers `develop` avec lien vers l'Issue
6. **CI/CD :** Exécution automatique des checks qualité
7. **Revue IA :** Commentaire automatique par Gemini
8. **Revue humaine :** Minimum 2 approbations requises
9. **Merge :** Squash and merge dans `develop`
10. **Release :** Merge final de `develop` vers `main` + tag

---

## 🛠️ Technologies et Outils Utilisés

### Backend
- **FastAPI** : Framework web moderne pour Python
- **Pydantic** : Validation des données
- **Uvicorn** : Serveur ASGI

### Qualité de Code
- **Black** : Formatage automatique du code
- **Flake8** : Linting et détection d'erreurs
- **isort** : Tri automatique des imports
- **pre-commit** : Hooks Git pour validation locale

### DevOps
- **GitHub Actions** : CI/CD automatisé
- **Gemini AI** : Revue de code automatique
- **Gmail SMTP** : Notifications par email

### Stockage
- **db.json** : Fichier JSON pour simuler une base de données

---

## 🎯 Fonctionnalités Implémentées

### Endpoints de l'API

| Endpoint | Méthode | Description | Statut |
|----------|---------|-------------|--------|
| `/projects` | POST | Soumettre un nouveau projet | ✅ |
| `/projects` | GET | Lister tous les projets | ✅ |
| `/projects/{id}` | GET | Obtenir un projet par ID | ✅ |
| `/projects/{id}/grade` | PUT | Noter un projet | ✅ |
| `/projects/{id}` | DELETE | Supprimer un projet | ✅ |
| `/projects/course/{courseName}` | GET | Filtrer par cours | ✅ |

### Validation des Données

Tous les endpoints utilisent Pydantic pour valider :
- Types de données
- Formats (URLs GitHub)
- Champs obligatoires
- Contraintes métier

---

## 🚧 Difficultés Rencontrées et Solutions

### 1. Conflits de Merge sur db.json

**Problème :** Plusieurs membres modifiant `db.json` simultanément ont créé de nombreux conflits.

**Solution :**
- Synchronisation régulière avec `develop` avant de pousser
- Résolution manuelle des conflits en fusionnant les tableaux JSON
- Communication dans l'équipe pour éviter les modifications simultanées

### 2. Configuration des Secrets GitHub

**Problème :** Difficulté à générer le mot de passe d'application Gmail.

**Solution :**
- Activation de la validation en deux étapes
- Utilisation de la section "Mots de passe des applications" dans les paramètres Google
- Documentation claire pour les autres membres

### 3. Hooks Pre-Commit Non Installés

**Problème :** Certains membres oubliaient d'installer les hooks, causant des échecs CI.

**Solution :**
- Ajout d'une checklist dans le README
- Vérification systématique lors de l'onboarding
- Documentation détaillée dans SETUP_INSTRUCTIONS.md

### 4. Revues de Code Superficielles

**Problème :** Premières revues trop rapides sans commentaires constructifs.

**Solution :**
- Formation sur les bonnes pratiques de revue de code
- Utilisation de la revue IA comme guide
- Exigence de commentaires justifiés pour les "Request changes"

---

## 📚 Compétences Acquises

### Techniques

- ✅ Maîtrise de Git Flow (main, develop, feature)
- ✅ Utilisation avancée de Git (merge, rebase, résolution de conflits)
- ✅ Configuration et utilisation de hooks Git
- ✅ Création de pipelines CI/CD avec GitHub Actions
- ✅ Intégration d'APIs externes (Gemini AI)
- ✅ Gestion des secrets et sécurité
- ✅ Développement d'API REST avec FastAPI
- ✅ Validation de données avec Pydantic

### Méthodologiques

- ✅ Travail en équipe sur un projet versionné
- ✅ Revue de code collaborative
- ✅ Gestion de projet avec Issues et Pull Requests
- ✅ Communication asynchrone via GitHub
- ✅ Documentation technique (Wiki, README)
- ✅ Gestion des releases et versioning sémantique

### Soft Skills

- ✅ Communication dans une équipe de développement
- ✅ Résolution de conflits (techniques et humains)
- ✅ Feedback constructif lors des revues
- ✅ Respect des processus et des règles d'équipe
- ✅ Autonomie et prise d'initiative

---

## 📊 Taux de Participation des Membres

**Évaluation par le Lead du groupe**

| Membre | Présence aux séances | Communication | Travail effectif | Taux Global |
|--------|---------------------|---------------|------------------|-------------|
| [Nom 1] | 100% | Excellente | Très bon | **100%** |
| [Nom 2] | 100% | Bonne | Bon | **95%** |
| [Nom 3] | 90% | Bonne | Bon | **90%** |
| [Nom 4] | 100% | Excellente | Très bon | **100%** |
| [Nom 5] | 80% | Moyenne | Moyen | **80%** |
| [Nom 6] | 100% | Bonne | Bon | **95%** |
| [Nom 7] | 100% | Excellente | Très bon | **100%** |

**Critères d'évaluation :**
- **Présence aux séances** : Assiduité lors des sessions de travail en groupe
- **Communication** : Réactivité et qualité des échanges (présentiel et en ligne)
- **Travail effectif** : Qualité et quantité du travail fourni (commits, revues, documentation)

---

## 🎓 Conclusion

Ce projet nous a permis de mettre en pratique l'ensemble du cycle de vie d'un projet logiciel moderne, de l'initialisation du dépôt Git jusqu'à la publication d'une release en production.

### Points Forts

- Excellente collaboration grâce à Git Flow et aux Pull Requests
- Automatisation efficace avec GitHub Actions
- Qualité de code maintenue grâce aux hooks et à la CI
- Documentation complète et accessible

### Axes d'Amélioration

- Anticiper davantage les conflits de merge
- Améliorer la planification des tâches en amont
- Renforcer la communication synchrone pour les décisions importantes

### Perspectives

Les compétences acquises durant ce TP sont directement applicables en entreprise et constituent une base solide pour tout projet collaboratif futur. La maîtrise de Git Flow, des revues de code et de la CI/CD sont des compétences essentielles pour tout développeur professionnel.

---

**Signatures des Membres de l'Équipe**

| Nom | Signature | Date |
|-----|-----------|------|
| [Nom 1] | | |
| [Nom 2] | | |
| [Nom 3] | | |
| [Nom 4] | | |
| [Nom 5] | | |
| [Nom 6] | | |
| [Nom 7] | | |

---

**Fin du Rapport**
