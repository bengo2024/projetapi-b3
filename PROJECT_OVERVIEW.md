# 🎓 ProjetAPI - Vue d'Ensemble du TP

## 📚 Contexte Académique

**Module :** Versionning et Gestion de Projet
**Niveau :** Bachelor 3 Informatique
**Durée :** 3 jours
**Type :** Travail en groupe (5-7 étudiants)

---

## 🎯 Objectifs Pédagogiques

Ce TP vous permet de maîtriser :

✅ **Git Flow** : Structure de branches (main, develop, feature)
✅ **Git Hooks** : Validation automatique du code (pre-commit)
✅ **Collaboration GitHub** : Issues, Pull Requests, Revues de code
✅ **Gestion de conflits** : Résolution de merge conflicts
✅ **CI/CD** : Automatisation avec GitHub Actions
✅ **Revue IA** : Intégration d'un LLM (Gemini) pour la revue de code
✅ **Secrets Management** : Gestion sécurisée des clés API
✅ **Releases** : Publication de versions (Tags & Releases)

---

## 📁 Structure du Projet

```
final_git/
├── .github/
│   └── workflows/
│       ├── ci.yml                    # Pipeline CI (lint, format, type-check)
│       └── llm-review.yml            # Revue IA + notifications email
├── main.py                           # Application FastAPI principale
├── db.json                           # Base de données (fichier JSON)
├── requirements.txt                  # Dépendances Python
├── pyproject.toml                    # Configuration Black/isort
├── .flake8                           # Configuration Flake8
├── .pre-commit-config.yaml           # Configuration hooks pre-commit
├── .gitignore                        # Fichiers à ignorer par Git
├── README.md                         # Documentation principale
├── SETUP_INSTRUCTIONS.md             # Guide d'installation détaillé
├── ENDPOINTS_EXAMPLES.md             # Exemples d'implémentation des endpoints
├── PHASE3_GITHUB_ACTIONS.md          # Guide pour la Phase 3 (CI/CD)
├── RAPPORT_TEMPLATE.md               # Template pour le rapport final
└── PROJECT_OVERVIEW.md               # Ce fichier
```

---

## 🗺️ Roadmap du Projet

### Phase 1 : Initialisation & Structure ✅ (COMPLÉTÉ)

**Responsable :** Lead du groupe

**Tâches :**
- [x] Initialiser le projet FastAPI
- [x] Configurer les outils de qualité (Black, Flake8, isort)
- [x] Initialiser Git et créer le commit initial
- [x] Créer la branche `develop`
- [x] Configurer les hooks pre-commit
- [x] Créer le dépôt GitHub privé
- [x] Inviter les membres de l'équipe

**Livrables :**
- Dépôt GitHub avec structure Git Flow
- Hooks pre-commit fonctionnels
- Documentation d'installation

---

### Phase 2 : Collaboration & Développement des Fonctionnalités

**Responsable :** Tous les membres

**Workflow :**

1. **Lead crée les 7 Issues sur GitHub**
   - Issue #1 : POST /projects
   - Issue #2 : GET /projects
   - Issue #3 : GET /projects/:id
   - Issue #4 : PUT /projects/:id/grade
   - Issue #5 : DELETE /projects/:id
   - Issue #6 : GET /projects/course/:courseName
   - Issue #7 : Documentation Wiki

2. **Chaque membre s'assigne une Issue**

3. **Développement en suivant Git Flow :**
   ```bash
   git switch develop
   git pull origin develop
   git switch -c feature/nom-feature
   # ... développement ...
   git commit -m "Feat: Description (fixes #N)"
   git push origin feature/nom-feature
   ```

4. **Créer une Pull Request**
   - Depuis `feature/*` vers `develop`
   - Lier l'Issue
   - Assigner 2 reviewers

5. **Revue de code**
   - Les reviewers examinent le code
   - Commentaires et suggestions
   - "Request changes" si nécessaire
   - Approbation finale (minimum 2)

6. **Résolution de conflits** (si nécessaire)
   ```bash
   git merge develop
   # Résoudre les conflits
   git commit -m "Resolve merge conflicts"
   git push
   ```

7. **Merge** (Lead ou auteur)
   - Utiliser "Squash and merge"

**Livrables :**
- 7 fonctionnalités implémentées
- Historique de PRs avec revues
- Documentation Wiki complète

---

### Phase 3 : DevOps & Automatisation

**Responsable :** Lead (configuration) + Tous (tests)

**Tâches :**

1. **Configuration des Branch Protection Rules**
   - Exiger 2 approbations
   - Exiger le passage de la CI
   - Bloquer le merge si checks échouent

2. **Configuration des Secrets GitHub**
   - `GEMINI_API_KEY` : Clé API Gemini
   - `MAIL_USERNAME` : Email Gmail
   - `MAIL_PASSWORD` : Mot de passe d'application
   - `TEAM_EMAIL_LIST` : Liste des emails de l'équipe

3. **Activation des Workflows**
   - `ci.yml` : Lint, format, type-check
   - `llm-review.yml` : Revue IA + email

4. **Tests**
   - Test CI qui passe (vert) ✅
   - Test CI qui échoue (rouge) ❌ → **Capture d'écran**
   - Test revue LLM → **Capture d'écran**
   - Test email → **Capture d'écran**

**Livrables :**
- Pipeline CI/CD fonctionnel
- Captures d'écran des tests
- Protections de branches actives

---

### Phase 4 : Release & Finalisation

**Responsable :** Lead

**Tâches :**

1. **Merger develop dans main**
   ```bash
   git switch main
   git merge develop
   git push origin main
   ```

2. **Créer le tag v1.0.0**
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin v1.0.0
   ```

3. **Créer la Release sur GitHub**
   - Basée sur le tag v1.0.0
   - Notes de version complètes
   - **Capture d'écran**

4. **Rédiger le rapport PDF**
   - Utiliser `RAPPORT_TEMPLATE.md`
   - Inclure toutes les captures d'écran
   - Tableau de participation
   - Conclusion

**Livrables :**
- Release v1.0.0 publiée
- Rapport PDF complet

---

## 📊 Répartition des Rôles

### Lead / Maintainer (1 personne)

**Responsabilités :**
- Créer et configurer le dépôt GitHub
- Inviter les membres
- Créer les Issues
- Configurer les protections de branches
- Configurer les Secrets GitHub
- Merger les PRs finales
- Créer la Release
- Évaluer la participation des membres

### Développeurs (4-6 personnes)

**Responsabilités :**
- S'assigner une Issue
- Développer la fonctionnalité
- Créer une Pull Request
- Effectuer des revues de code (minimum 2 par membre)
- Résoudre les conflits de merge
- Participer aux tests de la CI/CD
- Contribuer à la documentation

---

## 🛠️ Technologies Utilisées

### Backend
- **FastAPI** : Framework web moderne et rapide
- **Pydantic** : Validation de données avec types
- **Uvicorn** : Serveur ASGI haute performance

### Qualité de Code
- **Black** : Formatage automatique (PEP 8)
- **Flake8** : Linting et détection d'erreurs
- **isort** : Tri automatique des imports
- **pre-commit** : Hooks Git pour validation locale

### DevOps
- **GitHub Actions** : CI/CD automatisé
- **Gemini AI** : Revue de code par IA
- **Gmail SMTP** : Notifications par email

### Versionning
- **Git** : Contrôle de version
- **Git Flow** : Modèle de branches
- **GitHub** : Hébergement et collaboration

---

## 📋 Checklist Complète du Projet

### Phase 1 : Initialisation
- [ ] Projet FastAPI initialisé
- [ ] Outils de qualité configurés
- [ ] Git initialisé avec Git Flow
- [ ] Dépôt GitHub privé créé
- [ ] Membres invités
- [ ] Hooks pre-commit installés par tous
- [ ] Test du hook → Capture d'écran

### Phase 2 : Développement
- [ ] 7 Issues créées
- [ ] Issue #1 (POST /projects) → PR mergée
- [ ] Issue #2 (GET /projects) → PR mergée
- [ ] Issue #3 (GET /projects/:id) → PR mergée
- [ ] Issue #4 (PUT /projects/:id/grade) → PR mergée
- [ ] Issue #5 (DELETE /projects/:id) → PR mergée
- [ ] Issue #6 (GET /projects/course/:courseName) → PR mergée
- [ ] Issue #7 (Documentation Wiki) → Complétée
- [ ] Chaque membre a créé au moins 1 PR
- [ ] Chaque membre a effectué au moins 2 revues
- [ ] Capture d'écran d'une revue de code riche

### Phase 3 : CI/CD
- [ ] Branch Protection Rules configurées
- [ ] 4 Secrets GitHub ajoutés
- [ ] Workflows poussés sur develop
- [ ] Test CI vert effectué
- [ ] Test CI rouge → Capture d'écran
- [ ] Test revue LLM → Capture d'écran
- [ ] Email reçu → Capture d'écran

### Phase 4 : Release
- [ ] develop mergé dans main
- [ ] Tag v1.0.0 créé
- [ ] Release v1.0.0 publiée → Capture d'écran
- [ ] Rapport PDF rédigé
- [ ] Tableau de participation complété

---

## 📸 Captures d'Écran Requises

Pour le rapport PDF, vous devez fournir :

1. ✅ **Hook pre-commit bloquant un commit**
2. ✅ **Discussion de revue de code riche** (commentaires, Request changes, approbations)
3. ✅ **CI échouée** (rouge) bloquant le merge
4. ✅ **Commentaire généré par le LLM** (avec mention @)
5. ✅ **Email reçu** par un membre de l'équipe
6. ✅ **Page de la Release v1.0.0**

---

## 🆘 Ressources et Aide

### Documentation
- **README.md** : Documentation principale du projet
- **SETUP_INSTRUCTIONS.md** : Guide d'installation pas à pas
- **ENDPOINTS_EXAMPLES.md** : Exemples de code pour chaque endpoint
- **PHASE3_GITHUB_ACTIONS.md** : Guide détaillé pour la Phase 3
- **RAPPORT_TEMPLATE.md** : Template pour le rapport final

### Liens Utiles
- FastAPI Documentation : https://fastapi.tiangolo.com/
- Git Flow : https://nvie.com/posts/a-successful-git-branching-model/
- GitHub Actions : https://docs.github.com/en/actions
- Gemini API : https://makersuite.google.com/

### Support
- Discutez avec votre équipe
- Consultez le Lead pour les questions de configuration
- Utilisez les Issues GitHub pour tracker les problèmes

---

## 🎓 Compétences Développées

À la fin de ce TP, vous aurez acquis :

### Techniques
- Maîtrise de Git et Git Flow
- Développement d'API REST avec FastAPI
- Validation de données avec Pydantic
- Configuration de pipelines CI/CD
- Intégration d'APIs externes (LLM)
- Gestion de secrets et sécurité

### Méthodologiques
- Travail collaboratif sur un projet versionné
- Revue de code professionnelle
- Gestion de projet avec Issues/PRs
- Documentation technique
- Résolution de conflits (techniques et humains)

### Professionnelles
- Communication en équipe
- Respect des processus
- Feedback constructif
- Autonomie et initiative
- Rigueur et qualité

---

## 🏆 Critères d'Évaluation

### Technique (40%)
- Qualité du code (formatage, linting, structure)
- Fonctionnalités implémentées correctement
- Tests et validation
- Documentation

### Processus (40%)
- Respect du Git Flow
- Qualité des revues de code
- Gestion des conflits
- Utilisation de la CI/CD

### Collaboration (20%)
- Participation active
- Communication
- Entraide
- Respect des délais

---

## 📅 Planning Suggéré (3 jours)

### Jour 1 : Initialisation & Premières Features
- Matin : Phase 1 (setup complet)
- Après-midi : Début Phase 2 (3-4 features)

### Jour 2 : Développement & CI/CD
- Matin : Fin Phase 2 (toutes les features)
- Après-midi : Phase 3 (CI/CD et tests)

### Jour 3 : Finalisation & Rapport
- Matin : Release v1.0.0
- Après-midi : Rédaction du rapport PDF

---

## ✨ Conseils pour Réussir

1. **Communiquez** : Utilisez un canal de communication (Discord, Slack, WhatsApp)
2. **Synchronisez-vous** : Faites des `git pull` réguliers
3. **Testez localement** : Avant de pousser, testez votre code
4. **Revues constructives** : Soyez bienveillants mais rigoureux
5. **Documentez** : Commentez votre code et mettez à jour le Wiki
6. **Prenez des captures** : N'oubliez pas les screenshots pour le rapport
7. **Amusez-vous** : C'est un projet d'apprentissage !

---

**Bon courage et bon développement ! 🚀**

*Ce projet a été conçu pour vous préparer aux pratiques professionnelles de développement logiciel en équipe.*
