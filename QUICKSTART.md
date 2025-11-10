# ⚡ Quick Start - ProjetAPI

Guide de démarrage rapide pour commencer immédiatement !

---

## 🎯 Vous êtes le LEAD ?

### 1. Créer le dépôt GitHub (2 min)

```bash
# Le code est déjà prêt localement !
# Créez juste un dépôt PRIVÉ sur GitHub : https://github.com/new

# Puis connectez-le :
git remote add origin https://github.com/VOTRE_USERNAME/projetapi-b3.git
git push -u origin main
git push -u origin develop
```

### 2. Configurer GitHub (3 min)

1. **Settings** > **Branches** → Définir `develop` comme branche par défaut
2. **Settings** > **Collaborators** → Inviter les membres de l'équipe
3. **Issues** → Créer les 7 Issues (voir ci-dessous)

### 3. Les 7 Issues à créer

Copiez-collez ces titres et descriptions :

**Issue #1**
```
Titre: [Feature] POST /projects - Soumettre un nouveau projet
Description: Implémenter l'endpoint POST /projects pour soumettre un nouveau projet avec validation Pydantic (studentName, course, githubUrl)
Labels: enhancement, feature
```

**Issue #2**
```
Titre: [Feature] GET /projects - Lister tous les projets
Description: Implémenter l'endpoint GET /projects pour récupérer la liste complète des projets soumis
Labels: enhancement, feature
```

**Issue #3**
```
Titre: [Feature] GET /projects/:id - Obtenir un projet par ID
Description: Implémenter l'endpoint GET /projects/{id} avec gestion d'erreur 404 si le projet n'existe pas
Labels: enhancement, feature
```

**Issue #4**
```
Titre: [Feature] PUT /projects/:id/grade - Noter un projet
Description: Implémenter l'endpoint PUT /projects/{id}/grade pour permettre à un professeur d'ajouter une note (0-20)
Labels: enhancement, feature
```

**Issue #5**
```
Titre: [Feature] DELETE /projects/:id - Supprimer un projet
Description: Implémenter l'endpoint DELETE /projects/{id} pour supprimer une soumission de projet
Labels: enhancement, feature
```

**Issue #6**
```
Titre: [Feature] GET /projects/course/:courseName - Filtrer par cours
Description: Implémenter l'endpoint GET /projects/course/{courseName} pour filtrer et retourner tous les projets d'un cours spécifique
Labels: enhancement, feature
```

**Issue #7**
```
Titre: [Documentation] Rédiger la documentation dans le Wiki GitHub
Description: Documenter l'installation, le lancement du serveur, et l'utilisation de chaque endpoint avec des exemples dans le Wiki GitHub
Labels: documentation
```

---

## 👥 Vous êtes un MEMBRE de l'équipe ?

### 1. Cloner le dépôt (1 min)

```bash
git clone https://github.com/LEAD_USERNAME/projetapi-b3.git
cd projetapi-b3
git switch develop
```

### 2. Installer l'environnement (3 min)

**Windows :**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install black flake8 isort pre-commit
pre-commit install
```

**Linux/Mac :**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install black flake8 isort pre-commit
pre-commit install
```

### 3. Tester que tout fonctionne (1 min)

```bash
# Lancer le serveur
uvicorn main:app --reload

# Dans un autre terminal, tester
curl http://localhost:8000
```

Vous devriez voir :
```json
{
  "message": "Bienvenue sur ProjetAPI",
  "version": "1.0.0"
}
```

### 4. Tester le hook pre-commit (2 min)

```bash
# Créer un fichier mal formaté
echo "def test(  ):    x=1;return x" > test_hook.py

# Essayer de commiter
git add test_hook.py
git commit -m "Test hook"

# Le hook devrait corriger automatiquement !
# Prenez une CAPTURE D'ÉCRAN de la sortie

# Nettoyer
git reset HEAD test_hook.py
rm test_hook.py
```

---

## 🚀 Développer une fonctionnalité (10-20 min)

### Workflow complet

```bash
# 1. S'assigner une Issue sur GitHub (ex: Issue #1)

# 2. Partir de develop
git switch develop
git pull origin develop

# 3. Créer une branche feature
git switch -c feature/post-projects

# 4. Développer dans main.py
# Voir ENDPOINTS_EXAMPLES.md pour des exemples de code

# 5. Tester localement
uvicorn main:app --reload
# Tester avec curl ou le script test_api.py

# 6. Commiter (le hook se déclenche automatiquement)
git add main.py
git commit -m "Feat: Add POST /projects endpoint (fixes #1)"

# 7. Pousser
git push origin feature/post-projects

# 8. Créer une Pull Request sur GitHub
# - Depuis feature/post-projects vers develop
# - Lier l'Issue #1
# - Assigner 2 reviewers

# 9. Attendre les approbations et merger
```

---

## 📚 Documentation Disponible

| Fichier | Contenu |
|---------|---------|
| **README.md** | Documentation principale |
| **QUICKSTART.md** | Ce fichier (démarrage rapide) |
| **SETUP_INSTRUCTIONS.md** | Guide d'installation détaillé |
| **ENDPOINTS_EXAMPLES.md** | Exemples de code pour chaque endpoint |
| **PHASE3_GITHUB_ACTIONS.md** | Guide pour la CI/CD |
| **RAPPORT_TEMPLATE.md** | Template pour le rapport final |
| **PROJECT_OVERVIEW.md** | Vue d'ensemble complète du projet |

---

## 🧪 Tester l'API

### Avec curl (simple)

```bash
# POST - Créer un projet
curl -X POST http://localhost:8000/projects \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "Alice",
    "course": "Git",
    "githubUrl": "https://github.com/alice/repo"
  }'

# GET - Lister tous les projets
curl http://localhost:8000/projects

# GET - Obtenir un projet par ID
curl http://localhost:8000/projects/1

# PUT - Noter un projet
curl -X PUT http://localhost:8000/projects/1/grade \
  -H "Content-Type: application/json" \
  -d '{"grade": 18.5}'

# DELETE - Supprimer un projet
curl -X DELETE http://localhost:8000/projects/1
```

### Avec le script Python (complet)

```bash
# Installer requests
pip install requests

# Lancer le serveur dans un terminal
uvicorn main:app --reload

# Dans un autre terminal, lancer les tests
python test_api.py
```

### Avec Swagger UI (interactif)

```bash
# Lancer le serveur
uvicorn main:app --reload

# Ouvrir dans le navigateur
http://localhost:8000/docs
```

---

## 🆘 Problèmes Courants

### "command not found: uvicorn"
```bash
# Vérifier que l'environnement virtuel est activé
# Vous devriez voir (venv) au début de votre ligne de commande

# Réinstaller
pip install uvicorn
```

### "pre-commit: command not found"
```bash
# Vérifier que l'environnement virtuel est activé
pip install pre-commit
pre-commit install
```

### Le hook ne se déclenche pas
```bash
# Réinstaller
pre-commit uninstall
pre-commit install

# Vérifier
pre-commit run --all-files
```

### Conflits de merge
```bash
# Sur votre branche feature
git merge develop

# Ouvrir les fichiers en conflit (souvent db.json)
# Résoudre manuellement
# Puis :
git add .
git commit -m "Resolve merge conflicts with develop"
git push
```

---

## 📋 Checklist Rapide

### Pour le Lead
- [ ] Dépôt GitHub privé créé
- [ ] Code poussé (main + develop)
- [ ] develop = branche par défaut
- [ ] Membres invités
- [ ] 7 Issues créées

### Pour Tous
- [ ] Dépôt cloné
- [ ] Environnement virtuel créé
- [ ] Dépendances installées
- [ ] Hooks pre-commit installés
- [ ] Serveur lance correctement
- [ ] Hook testé + capture d'écran

### Pour Chaque Feature
- [ ] Issue assignée
- [ ] Branche feature créée depuis develop
- [ ] Code développé
- [ ] Testé localement
- [ ] Commité (hook OK)
- [ ] Poussé
- [ ] PR créée
- [ ] 2 reviewers assignés
- [ ] Approbations reçues
- [ ] Mergé dans develop

---

## 🎯 Objectif Final

À la fin du TP, vous devez avoir :

✅ Un dépôt GitHub avec Git Flow
✅ 7 fonctionnalités implémentées
✅ Historique de PRs avec revues
✅ Pipeline CI/CD fonctionnel
✅ Release v1.0.0 publiée
✅ Rapport PDF avec captures d'écran

---

## 💡 Conseils

1. **Communiquez** : Créez un groupe WhatsApp/Discord
2. **Synchronisez** : `git pull origin develop` régulièrement
3. **Testez** : Avant de pousser, testez votre code
4. **Documentez** : Commentez votre code
5. **Capturez** : Prenez les screenshots au fur et à mesure
6. **Amusez-vous** : C'est un projet d'apprentissage !

---

## 📞 Besoin d'Aide ?

1. Consultez la documentation dans les fichiers `.md`
2. Regardez les exemples dans `ENDPOINTS_EXAMPLES.md`
3. Demandez au Lead ou à l'équipe
4. Utilisez les Issues GitHub pour tracker les problèmes

---

**Prêt ? C'est parti ! 🚀**

```bash
# Première commande à exécuter :
git status
```
