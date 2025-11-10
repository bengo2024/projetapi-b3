# 🎓 COMMENCEZ ICI - ProjetAPI

> **Bienvenue dans le projet ProjetAPI !**
> Ce fichier vous guide vers la bonne documentation selon votre rôle.

---

## 🚀 Démarrage Rapide (5 minutes)

### Vous êtes le LEAD du groupe ?

👉 **Lisez : [LEAD_CHECKLIST.md](LEAD_CHECKLIST.md)**

Ce fichier contient TOUT ce que vous devez faire, étape par étape :
- ✅ Créer le dépôt GitHub
- ✅ Inviter les membres
- ✅ Créer les Issues
- ✅ Configurer la CI/CD
- ✅ Créer la Release

**Temps estimé :** 30-45 minutes de configuration initiale

---

### Vous êtes un MEMBRE de l'équipe ?

👉 **Lisez : [QUICKSTART.md](QUICKSTART.md)**

Ce fichier vous permet de démarrer en 5 minutes :
- ✅ Cloner le dépôt
- ✅ Installer l'environnement
- ✅ Tester que tout fonctionne
- ✅ Commencer à développer

**Temps estimé :** 5-10 minutes d'installation

---

## 📚 Documentation Complète

| Fichier | Pour Qui ? | Contenu |
|---------|------------|---------|
| **[QUICKSTART.md](QUICKSTART.md)** | 👥 Tous | Démarrage rapide (5 min) |
| **[LEAD_CHECKLIST.md](LEAD_CHECKLIST.md)** | 👑 Lead | Checklist complète du Lead |
| **[SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)** | 👥 Tous | Guide d'installation détaillé |
| **[ENDPOINTS_EXAMPLES.md](ENDPOINTS_EXAMPLES.md)** | 💻 Développeurs | Exemples de code pour chaque endpoint |
| **[PHASE3_GITHUB_ACTIONS.md](PHASE3_GITHUB_ACTIONS.md)** | 👑 Lead + 👥 Tous | Guide CI/CD avec GitHub Actions |
| **[RAPPORT_TEMPLATE.md](RAPPORT_TEMPLATE.md)** | 👑 Lead | Template pour le rapport final |
| **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** | 👥 Tous | Vue d'ensemble du projet |
| **[README.md](README.md)** | 👥 Tous | Documentation principale |

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

## 📋 Les 3 Phases du Projet

### Phase 1 : Initialisation & Structure ✅ (DÉJÀ FAIT !)

Le code est déjà prêt ! Il vous suffit de :
- Créer le dépôt GitHub (Lead)
- Cloner et installer (Membres)

**Durée :** 30 minutes

---

### Phase 2 : Développement des Fonctionnalités

Chaque membre développe une fonctionnalité :

1. POST /projects - Soumettre un projet
2. GET /projects - Lister les projets
3. GET /projects/:id - Obtenir un projet
4. PUT /projects/:id/grade - Noter un projet
5. DELETE /projects/:id - Supprimer un projet
6. GET /projects/course/:courseName - Filtrer par cours
7. Documentation Wiki

**Durée :** 1 jour

---

### Phase 3 : CI/CD & Release

- Configuration des GitHub Actions
- Tests de la CI/CD
- Création de la Release v1.0.0
- Rédaction du rapport

**Durée :** 1 jour

---

## 🛠️ Technologies Utilisées

### Backend
- **FastAPI** : Framework web moderne
- **Pydantic** : Validation de données
- **Uvicorn** : Serveur ASGI

### Qualité de Code
- **Black** : Formatage automatique
- **Flake8** : Linting
- **isort** : Tri des imports
- **pre-commit** : Hooks Git

### DevOps
- **GitHub Actions** : CI/CD
- **Gemini AI** : Revue de code
- **Gmail SMTP** : Notifications

---

## 📸 Captures d'Écran Requises

Pour le rapport PDF, vous devez fournir :

1. ✅ Hook pre-commit bloquant un commit
2. ✅ Discussion de revue de code riche
3. ✅ CI échouée (rouge) bloquant le merge
4. ✅ Commentaire généré par le LLM
5. ✅ Email reçu par un membre
6. ✅ Page de la Release v1.0.0

**💡 Conseil :** Prenez les captures au fur et à mesure !

---

## 🎓 Livrables Finaux

À la fin du TP, vous devez soumettre :

### 1. URL du Dépôt GitHub

Le dépôt doit contenir :
- ✅ Code source complet
- ✅ Structure Git Flow (main/develop/feature)
- ✅ Historique des Pull Requests
- ✅ Issues fermées et liées
- ✅ Wiki complété
- ✅ Release v1.0.0
- ✅ Workflows GitHub Actions

### 2. Rapport PDF

Un rapport par groupe contenant :
- ✅ Page de garde avec noms des membres
- ✅ Tableau de participation
- ✅ 6 captures d'écran obligatoires
- ✅ Difficultés rencontrées
- ✅ Compétences acquises
- ✅ Taux de participation de chaque membre

**Template disponible :** [RAPPORT_TEMPLATE.md](RAPPORT_TEMPLATE.md)

---

## 🚦 Par Où Commencer ?

### Si vous êtes le LEAD :

```bash
# 1. Lisez LEAD_CHECKLIST.md
# 2. Créez le dépôt GitHub (privé)
# 3. Poussez le code :

git remote add origin https://github.com/VOTRE_USERNAME/projetapi-b3.git
git push -u origin main
git push -u origin develop

# 4. Suivez le reste de LEAD_CHECKLIST.md
```

---

### Si vous êtes un MEMBRE :

```bash
# 1. Attendez l'invitation GitHub du Lead
# 2. Clonez le dépôt :

git clone https://github.com/LEAD_USERNAME/projetapi-b3.git
cd projetapi-b3

# 3. Suivez QUICKSTART.md pour l'installation
```

---

## 🆘 Besoin d'Aide ?

### Questions Fréquentes

**Q : Je ne sais pas par où commencer**
R : Lisez ce fichier (START_HERE.md) puis QUICKSTART.md

**Q : Comment implémenter un endpoint ?**
R : Consultez ENDPOINTS_EXAMPLES.md pour des exemples de code

**Q : Comment configurer la CI/CD ?**
R : Suivez PHASE3_GITHUB_ACTIONS.md étape par étape

**Q : Comment résoudre un conflit de merge ?**
R : Voir la section "Conflits de merge" dans QUICKSTART.md

**Q : Où trouver les captures d'écran à prendre ?**
R : Voir RAPPORT_TEMPLATE.md et PHASE3_GITHUB_ACTIONS.md

---

## 📞 Support

1. **Documentation** : Consultez les fichiers .md
2. **Lead** : Contactez le Lead de votre groupe
3. **Équipe** : Discutez sur votre canal de communication
4. **Issues GitHub** : Utilisez les Issues pour tracker les problèmes

---

## ✨ Conseils pour Réussir

1. **Lisez la documentation** : Tout est déjà écrit !
2. **Communiquez** : Créez un groupe WhatsApp/Discord
3. **Testez** : Avant de pousser, testez votre code
4. **Capturez** : Prenez les screenshots au fur et à mesure
5. **Synchronisez** : Faites `git pull` régulièrement
6. **Amusez-vous** : C'est un projet d'apprentissage !

---

## 🎯 Prochaines Étapes

### Pour le Lead :
1. ✅ Lire [LEAD_CHECKLIST.md](LEAD_CHECKLIST.md)
2. ✅ Créer le dépôt GitHub
3. ✅ Inviter les membres
4. ✅ Créer les 7 Issues

### Pour les Membres :
1. ✅ Lire [QUICKSTART.md](QUICKSTART.md)
2. ✅ Accepter l'invitation GitHub
3. ✅ Cloner le dépôt
4. ✅ Installer l'environnement
5. ✅ S'assigner une Issue

---

## 📊 Planning Suggéré (3 jours)

### Jour 1
- **Matin** : Phase 1 (setup complet)
- **Après-midi** : Début Phase 2 (3-4 features)

### Jour 2
- **Matin** : Fin Phase 2 (toutes les features)
- **Après-midi** : Phase 3 (CI/CD et tests)

### Jour 3
- **Matin** : Release v1.0.0
- **Après-midi** : Rédaction du rapport PDF

---

## 🎉 Vous êtes Prêt !

Tout est en place pour réussir ce TP. La documentation est complète, le code de base est prêt, il ne vous reste plus qu'à :

1. **Lire la documentation appropriée** selon votre rôle
2. **Suivre les instructions** étape par étape
3. **Collaborer avec votre équipe**
4. **Apprendre et vous amuser** !

---

**Bon courage et bon développement ! 🚀**

---

## 📄 Fichiers du Projet

```
final_git/
├── START_HERE.md                 ⭐ CE FICHIER (commencez ici !)
├── QUICKSTART.md                 🚀 Démarrage rapide (5 min)
├── LEAD_CHECKLIST.md             👑 Checklist du Lead
├── SETUP_INSTRUCTIONS.md         📋 Installation détaillée
├── ENDPOINTS_EXAMPLES.md         💻 Exemples de code
├── PHASE3_GITHUB_ACTIONS.md      🔧 Guide CI/CD
├── RAPPORT_TEMPLATE.md           📄 Template de rapport
├── PROJECT_OVERVIEW.md           🎯 Vue d'ensemble
├── README.md                     📚 Documentation principale
├── .github/workflows/            🤖 GitHub Actions
│   ├── ci.yml                    ✅ Pipeline CI
│   └── llm-review.yml            🤖 Revue IA + Email
├── main.py                       🐍 Application FastAPI
├── db.json                       💾 Base de données
├── requirements.txt              📦 Dépendances
├── test_api.py                   🧪 Tests Python
├── test_api.sh                   🧪 Tests Bash
└── ...                           ⚙️ Configuration
```

---

**Prêt ? Allez-y ! 🎓**
