# 🚀 Phase 3 : DevOps & Automatisation (GitHub Actions)

## 📋 Objectifs
- Mettre en place un pipeline CI/CD
- Automatiser les contrôles qualité
- Intégrer une revue de code par IA (LLM)
- Configurer les notifications par email

---

## ⚙️ Étape 1 : Configuration des Branch Protection Rules (Lead uniquement)

### Sur GitHub :

1. Allez dans **Settings** > **Branches**
2. Cliquez sur **Add rule** (ou **Add branch protection rule**)
3. Dans "Branch name pattern", entrez : `develop`
4. Cochez les options suivantes :
   - ✅ **Require a pull request before merging**
     - ✅ Require approvals: **2**
     - ✅ Dismiss stale pull request approvals when new commits are pushed
   - ✅ **Require status checks to pass before merging**
     - ✅ Require branches to be up to date before merging
     - Dans la recherche, ajoutez les checks suivants (ils apparaîtront après le premier run) :
       - `Lint with Flake8`
       - `Check Code Formatting (Black)`
       - `Check Import Sorting (isort)`
   - ✅ **Require conversation resolution before merging**
   - ✅ **Do not allow bypassing the above settings**
5. Cliquez sur **Create** ou **Save changes**

---

## 🔐 Étape 2 : Configuration des Secrets GitHub (Lead uniquement)

### 1. Obtenir une clé API Gemini

1. Allez sur : https://makersuite.google.com/app/apikey
2. Connectez-vous avec votre compte Google
3. Cliquez sur **Create API Key**
4. Copiez la clé (elle commence par `AIza...`)

### 2. Générer un mot de passe d'application Gmail

⚠️ **N'utilisez JAMAIS votre vrai mot de passe Gmail !**

1. Allez sur : https://myaccount.google.com/security
2. Activez la **validation en deux étapes** si ce n'est pas déjà fait
3. Recherchez **Mots de passe des applications**
4. Sélectionnez "Autre (nom personnalisé)" et entrez : `ProjetAPI GitHub Actions`
5. Cliquez sur **Générer**
6. Copiez le mot de passe de 16 caractères (format : `xxxx xxxx xxxx xxxx`)

### 3. Ajouter les Secrets sur GitHub

1. Sur GitHub, allez dans **Settings** > **Secrets and variables** > **Actions**
2. Cliquez sur **New repository secret**
3. Ajoutez les 3 secrets suivants :

**Secret 1 :**
- Name: `GEMINI_API_KEY`
- Secret: `[Votre clé API Gemini]`

**Secret 2 :**
- Name: `MAIL_USERNAME`
- Secret: `votre.email@gmail.com`

**Secret 3 :**
- Name: `MAIL_PASSWORD`
- Secret: `[Le mot de passe d'application de 16 caractères]`

**Secret 4 :**
- Name: `TEAM_EMAIL_LIST`
- Secret: `membre1@email.com,membre2@email.com,membre3@email.com`
  (Tous les emails séparés par des virgules, SANS espaces)

---

## 📝 Étape 3 : Activer les Workflows (Tous les membres)

Les fichiers de workflow sont déjà créés dans `.github/workflows/` :
- `ci.yml` : Pipeline de qualité (lint, format, type-check)
- `llm-review.yml` : Revue de code par IA + notifications email

### Pousser les workflows sur develop

```bash
# Se placer sur develop
git switch develop
git pull origin develop

# Ajouter les workflows
git add .github/workflows/
git commit -m "CI/CD: Add GitHub Actions workflows for quality checks and LLM review"
git push origin develop
```

---

## 🧪 Étape 4 : Tester le Pipeline CI

### Test 1 : CI qui PASSE (vert ✅)

1. Créer une branche de test :
```bash
git switch develop
git pull origin develop
git switch -c test/ci-success
```

2. Faire un petit changement propre dans `main.py` :
```python
# Ajouter un commentaire quelque part
# Test CI pipeline
```

3. Commiter et pousser :
```bash
git add main.py
git commit -m "Test: CI pipeline with clean code"
git push origin test/ci-success
```

4. Créer une PR sur GitHub vers `develop`
5. Observer les checks qui passent au vert ✅

### Test 2 : CI qui ÉCHOUE (rouge ❌)

**⚠️ IMPORTANT : Prenez une capture d'écran de ce test pour le rapport !**

1. Créer une branche de test :
```bash
git switch develop
git pull origin develop
git switch -c test/ci-failure
```

2. Créer un fichier Python mal formaté :
```bash
# Créer un fichier avec du code volontairement mal formaté
cat > bad_code.py << 'EOF'
def test(  ):
    x=1;y=2
    return x+y


def another_function(a,b,c):
        result=a+b+c
        return result
EOF
```

3. **DÉSACTIVER temporairement le hook pre-commit** :
```bash
# Renommer le hook pour le désactiver
mv .git/hooks/pre-commit .git/hooks/pre-commit.bak
```

4. Commiter et pousser :
```bash
git add bad_code.py
git commit -m "Test: Intentionally bad formatting to test CI"
git push origin test/ci-failure
```

5. Créer une PR sur GitHub vers `develop`
6. **📸 CAPTURE D'ÉCRAN** : Prenez une capture montrant les checks qui échouent (rouge ❌)
7. Observer que la PR ne peut PAS être mergée

8. Nettoyer et réactiver le hook :
```bash
# Réactiver le hook
mv .git/hooks/pre-commit.bak .git/hooks/pre-commit

# Fermer la PR sur GitHub sans merger
# Supprimer la branche locale
git switch develop
git branch -D test/ci-failure
```

---

## 🤖 Étape 5 : Tester la Revue LLM et l'Email

1. Créer une vraie feature (par exemple, POST /projects) :
```bash
git switch develop
git pull origin develop
git switch -c feature/post-projects
```

2. Implémenter la fonctionnalité dans `main.py`

3. Commiter et pousser :
```bash
git add main.py
git commit -m "Feat: Add POST /projects endpoint (fixes #1)"
git push origin feature/post-projects
```

4. Créer une PR sur GitHub vers `develop`

5. Observer :
   - ✅ Le workflow `llm-review.yml` se lance
   - ✅ Un commentaire de l'IA apparaît sur la PR mentionnant @vous
   - ✅ Tous les membres de l'équipe reçoivent un email

6. **📸 CAPTURES D'ÉCRAN à prendre** :
   - Le commentaire de l'IA sur la PR
   - L'email reçu dans votre boîte mail

---

## 🎯 Étape 6 : Workflow Complet de Développement

Maintenant que tout est en place, voici le workflow complet :

```bash
# 1. Partir de develop
git switch develop
git pull origin develop

# 2. Créer une branche feature
git switch -c feature/nom-feature

# 3. Développer
# ... coder ...

# 4. Commiter (hook pre-commit se déclenche)
git add .
git commit -m "Feat: Description (fixes #N)"

# 5. Pousser
git push origin feature/nom-feature

# 6. Créer une PR sur GitHub
# - Vers develop
# - Lier l'Issue
# - Assigner 2 reviewers

# 7. Attendre :
# - ✅ CI passe au vert
# - ✅ Commentaire de l'IA
# - ✅ 2 approbations humaines
# - ✅ Résolution des conflits si nécessaire

# 8. Merger (Lead ou auteur)
# - Utiliser "Squash and merge"
```

---

## 🏷️ Étape 7 : Créer la Release v1.0.0 (Lead uniquement)

Une fois TOUTES les features mergées dans `develop` :

### 1. Merger develop dans main

```bash
# Se placer sur main
git switch main
git pull origin main

# Merger develop
git merge develop

# Pousser
git push origin main
```

### 2. Créer le tag

```bash
# Créer le tag v1.0.0
git tag -a v1.0.0 -m "Release v1.0.0 - ProjetAPI Complete"

# Pousser le tag
git push origin v1.0.0
```

### 3. Créer la Release sur GitHub

1. Sur GitHub, allez dans **Releases**
2. Cliquez sur **Create a new release**
3. Sélectionnez le tag `v1.0.0`
4. Titre : `v1.0.0 - ProjetAPI Complete`
5. Description :
```markdown
## 🎉 ProjetAPI v1.0.0

API REST complète pour la gestion des projets étudiants.

### ✨ Fonctionnalités

- ✅ POST /projects - Soumettre un nouveau projet
- ✅ GET /projects - Lister tous les projets
- ✅ GET /projects/:id - Obtenir un projet par ID
- ✅ PUT /projects/:id/grade - Noter un projet
- ✅ DELETE /projects/:id - Supprimer un projet
- ✅ GET /projects/course/:courseName - Filtrer par cours

### 🛠️ Technologies

- FastAPI + Pydantic
- Python 3.11
- Black + Flake8 + isort
- GitHub Actions (CI/CD)
- Revue de code par IA (Gemini)

### 👥 Équipe

- [Noms des membres]

### 📚 Documentation

Consultez le Wiki pour la documentation complète.
```
6. Cliquez sur **Publish release**
7. **📸 CAPTURE D'ÉCRAN** : Prenez une capture de la page de la Release

---

## ✅ Checklist Phase 3

- [ ] Branch Protection Rules configurées sur `develop`
- [ ] Les 4 Secrets GitHub ajoutés
- [ ] Workflows poussés sur `develop`
- [ ] Test CI réussi (vert) effectué
- [ ] Test CI échoué (rouge) effectué + capture d'écran
- [ ] Test revue LLM effectué + capture d'écran du commentaire
- [ ] Email reçu + capture d'écran
- [ ] Toutes les features développées et mergées
- [ ] Release v1.0.0 créée + capture d'écran

---

## 🆘 Dépannage

### Le workflow ne se déclenche pas
- Vérifiez que les fichiers sont bien dans `.github/workflows/`
- Vérifiez que vous créez une PR vers `develop`

### Erreur "API key not valid"
- Vérifiez que `GEMINI_API_KEY` est bien configuré dans les Secrets
- Vérifiez que la clé est valide sur https://makersuite.google.com/

### Email non reçu
- Vérifiez `MAIL_USERNAME` et `MAIL_PASSWORD` dans les Secrets
- Vérifiez que le mot de passe est bien un "mot de passe d'application"
- Vérifiez `TEAM_EMAIL_LIST` (pas d'espaces, virgules uniquement)
- Vérifiez vos spams

### CI bloque le merge alors que le code est bon
- Lancez `black .` localement
- Lancez `flake8 .` localement
- Lancez `isort .` localement
- Commitez les corrections

---

**Bon courage pour la Phase 3 ! 🚀**

