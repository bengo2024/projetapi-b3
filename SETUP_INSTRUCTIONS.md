# 📋 Instructions de Configuration - ProjetAPI

## ✅ Phase 1 Complétée : Initialisation & Structure

### Ce qui a été fait :
- ✅ Projet FastAPI initialisé
- ✅ Outils de qualité configurés (Black, Flake8, isort)
- ✅ Git initialisé avec Git Flow (branches `main` et `develop`)
- ✅ Fichiers de configuration créés

---

## 🚀 Prochaines Étapes pour le Lead

### 1. Créer le dépôt GitHub (PRIVÉ)

1. Allez sur GitHub : https://github.com/new
2. **Nom du dépôt** : `projetapi-b3` (ou autre nom de votre choix)
3. **Visibilité** : ⚠️ **PRIVÉ** (très important !)
4. **NE PAS** initialiser avec README, .gitignore ou license (déjà créés)
5. Cliquez sur "Create repository"

### 2. Pousser le code sur GitHub

Après avoir créé le dépôt, GitHub vous donnera des commandes. Utilisez celles-ci :

```bash
# Remplacez <USERNAME> par votre nom d'utilisateur GitHub
git remote add origin https://github.com/<USERNAME>/projetapi-b3.git

# Pousser la branche main
git push -u origin main

# Pousser la branche develop
git push -u origin develop
```

### 3. Définir `develop` comme branche par défaut sur GitHub

1. Sur GitHub, allez dans **Settings** > **Branches**
2. Dans "Default branch", cliquez sur le bouton avec les deux flèches
3. Sélectionnez `develop`
4. Cliquez sur "Update" puis confirmez

### 4. Inviter les membres de l'équipe

1. Sur GitHub, allez dans **Settings** > **Collaborators**
2. Cliquez sur "Add people"
3. Entrez les noms d'utilisateur GitHub de chaque membre
4. Envoyez les invitations

---

## 👥 Prochaines Étapes pour TOUS les Membres

### 1. Cloner le dépôt

```bash
# Remplacez <USERNAME> par le nom d'utilisateur du Lead
git clone https://github.com/<USERNAME>/projetapi-b3.git
cd projetapi-b3

# Vérifier que vous êtes sur develop
git branch
# Devrait afficher : * develop
```

### 2. Créer l'environnement virtuel Python

**Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac :**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
# Dépendances du projet
pip install -r requirements.txt

# Outils de développement
pip install black flake8 isort pre-commit
```

### 4. ⚠️ IMPORTANT : Installer les hooks pre-commit

```bash
pre-commit install
```

Vous devriez voir :
```
pre-commit installed at .git/hooks/pre-commit
```

### 5. Tester que les hooks fonctionnent

Créons un fichier Python mal formaté pour tester :

```bash
# Créer un fichier de test mal formaté
echo "def test(  ):    x=1;y=2;return x+y" > test_bad_format.py

# Essayer de le commiter
git add test_bad_format.py
git commit -m "Test hook"
```

**Résultat attendu :** Le hook pre-commit devrait :
1. Détecter le mauvais formatage
2. Corriger automatiquement avec Black
3. Vous demander de re-commiter

**Capture d'écran à prendre :** Prenez une capture de la sortie du terminal montrant le hook qui bloque/corrige le commit. Cette capture sera nécessaire pour le rapport PDF !

Ensuite, nettoyez :
```bash
# Supprimer le fichier de test
git reset HEAD test_bad_format.py
rm test_bad_format.py
```

### 6. Vérifier que tout fonctionne

```bash
# Lancer le serveur
uvicorn main:app --reload
```

Ouvrez votre navigateur sur : http://localhost:8000

Vous devriez voir :
```json
{
  "message": "Bienvenue sur ProjetAPI",
  "version": "1.0.0",
  ...
}
```

---

## 📝 Prochaine Phase : Créer les Issues

Le **Lead** doit maintenant créer les 7 Issues sur GitHub :

### Issues à créer :

1. **Issue #1** : `[Feature] POST /projects - Soumettre un nouveau projet`
   - Description : Implémenter l'endpoint POST /projects pour soumettre un nouveau projet avec validation Pydantic

2. **Issue #2** : `[Feature] GET /projects - Lister tous les projets`
   - Description : Implémenter l'endpoint GET /projects pour récupérer la liste complète des projets

3. **Issue #3** : `[Feature] GET /projects/:id - Obtenir un projet par ID`
   - Description : Implémenter l'endpoint GET /projects/{id} avec gestion d'erreur 404

4. **Issue #4** : `[Feature] PUT /projects/:id/grade - Noter un projet`
   - Description : Implémenter l'endpoint PUT /projects/{id}/grade pour ajouter une note

5. **Issue #5** : `[Feature] DELETE /projects/:id - Supprimer un projet`
   - Description : Implémenter l'endpoint DELETE /projects/{id} avec gestion d'erreur 404

6. **Issue #6** : `[Feature] GET /projects/course/:courseName - Filtrer par cours`
   - Description : Implémenter l'endpoint GET /projects/course/{courseName} pour filtrer les projets

7. **Issue #7** : `[Documentation] Rédiger la documentation dans le Wiki GitHub`
   - Description : Documenter l'installation, le lancement et l'utilisation de chaque endpoint avec exemples

---

## 🎯 Workflow de Développement (pour chaque fonctionnalité)

Chaque membre s'assigne une Issue et suit ce processus :

```bash
# 1. Se placer sur develop et récupérer les dernières modifications
git switch develop
git pull origin develop

# 2. Créer une branche de fonctionnalité
git switch -c feature/nom-de-la-feature
# Exemple : git switch -c feature/post-projects

# 3. Développer la fonctionnalité dans main.py

# 4. Tester localement
uvicorn main:app --reload
# Tester avec curl ou Postman

# 5. Commiter (le hook pre-commit se déclenche automatiquement)
git add .
git commit -m "Feat: Add POST /projects endpoint (fixes #1)"

# 6. Pousser la branche
git push origin feature/nom-de-la-feature

# 7. Créer une Pull Request sur GitHub
# - Depuis votre branche vers develop
# - Lier l'Issue (#1, #2, etc.)
# - Assigner 2 reviewers
```

---

## ✅ Checklist Phase 1

- [ ] Dépôt GitHub privé créé
- [ ] Code poussé sur `main` et `develop`
- [ ] `develop` défini comme branche par défaut
- [ ] Tous les membres invités comme collaborateurs
- [ ] Tous les membres ont cloné le dépôt
- [ ] Tous les membres ont installé les dépendances
- [ ] Tous les membres ont installé les hooks pre-commit
- [ ] Tous les membres ont testé que les hooks fonctionnent
- [ ] Capture d'écran du hook pre-commit prise
- [ ] Les 7 Issues créées sur GitHub

---

## 🆘 Problèmes Courants

### Le hook pre-commit ne se déclenche pas
```bash
# Réinstaller
pre-commit uninstall
pre-commit install

# Vérifier
ls -la .git/hooks/
# Vous devriez voir un fichier "pre-commit"
```

### Erreur "command not found: pre-commit"
```bash
# Vérifier que l'environnement virtuel est activé
# Vous devriez voir (venv) au début de votre ligne de commande

# Réinstaller
pip install pre-commit
```

### Conflits de merge
Cela arrivera souvent (c'est voulu pédagogiquement) ! Quand ça arrive :
```bash
# Sur votre branche feature
git merge develop

# Résoudre les conflits dans les fichiers (notamment db.json)
# Puis :
git add .
git commit -m "Resolve merge conflicts with develop"
git push origin feature/votre-branche
```

---

## 📞 Contact

Pour toute question, contactez le Lead du groupe ou discutez sur votre canal de communication d'équipe.

**Bon courage ! 🚀**
