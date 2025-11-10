# ✅ Checklist du Lead - ProjetAPI

Guide complet pour le Lead/Maintainer du projet.

---

## 🎯 Votre Rôle

En tant que **Lead**, vous êtes responsable de :

1. ✅ Créer et configurer le dépôt GitHub
2. ✅ Inviter les membres de l'équipe
3. ✅ Créer les Issues
4. ✅ Configurer les protections de branches
5. ✅ Configurer les Secrets GitHub
6. ✅ Superviser les merges
7. ✅ Créer la Release finale
8. ✅ Évaluer la participation des membres

---

## 📋 Phase 1 : Initialisation (Jour 1 - Matin)

### ✅ Étape 1.1 : Créer le Dépôt GitHub (5 min)

1. Allez sur : https://github.com/new
2. **Nom du dépôt** : `projetapi-b3` (ou autre)
3. **Visibilité** : ⚠️ **PRIVÉ** (très important !)
4. **NE PAS** cocher :
   - ❌ Add a README file
   - ❌ Add .gitignore
   - ❌ Choose a license
5. Cliquez sur **Create repository**

### ✅ Étape 1.2 : Pousser le Code (2 min)

```bash
# Le code est déjà prêt localement !
# Connectez simplement le dépôt distant :

git remote add origin https://github.com/VOTRE_USERNAME/projetapi-b3.git

# Pousser main
git push -u origin main

# Pousser develop
git push -u origin develop
```

### ✅ Étape 1.3 : Configurer la Branche par Défaut (1 min)

1. Sur GitHub, allez dans **Settings** > **Branches**
2. Dans "Default branch", cliquez sur les deux flèches ⇄
3. Sélectionnez **`develop`**
4. Cliquez sur **Update**
5. Confirmez en cliquant sur **I understand, update the default branch**

### ✅ Étape 1.4 : Inviter les Membres (3 min)

1. Sur GitHub, allez dans **Settings** > **Collaborators**
2. Cliquez sur **Add people**
3. Pour chaque membre :
   - Entrez son nom d'utilisateur GitHub ou email
   - Cliquez sur **Add [username] to this repository**
   - Sélectionnez le rôle **Write** (par défaut)
4. Les membres recevront une invitation par email

**📧 Envoyez un message à l'équipe :**
```
Bonjour l'équipe,

Je viens de créer le dépôt GitHub pour notre projet ProjetAPI :
https://github.com/VOTRE_USERNAME/projetapi-b3

Vous avez reçu une invitation par email. Acceptez-la pour accéder au dépôt.

Ensuite, suivez les instructions dans QUICKSTART.md pour installer le projet.

À bientôt !
```

### ✅ Étape 1.5 : Créer les 7 Issues (10 min)

Sur GitHub, allez dans **Issues** > **New issue**

**Issue #1**
```
Titre: [Feature] POST /projects - Soumettre un nouveau projet

Description:
Implémenter l'endpoint POST /projects pour soumettre un nouveau projet.

**Spécifications :**
- Route : POST /projects
- Body : JSON avec studentName, course, githubUrl
- Validation : Utiliser Pydantic (ProjectCreate)
- Retour : Le projet créé avec son id généré
- Status Code : 201 Created

**Voir :** ENDPOINTS_EXAMPLES.md pour un exemple de code

Labels: enhancement, feature
Assignees: (laisser vide pour l'instant)
```

**Issue #2**
```
Titre: [Feature] GET /projects - Lister tous les projets

Description:
Implémenter l'endpoint GET /projects pour récupérer la liste complète des projets.

**Spécifications :**
- Route : GET /projects
- Retour : Liste de tous les projets
- Status Code : 200 OK

**Voir :** ENDPOINTS_EXAMPLES.md pour un exemple de code

Labels: enhancement, feature
```

**Issue #3**
```
Titre: [Feature] GET /projects/:id - Obtenir un projet par ID

Description:
Implémenter l'endpoint GET /projects/{id} pour obtenir un projet spécifique.

**Spécifications :**
- Route : GET /projects/{id}
- Paramètre : id (int) dans l'URL
- Retour : Le projet correspondant
- Status Code : 200 OK ou 404 Not Found
- Erreur : Si le projet n'existe pas, retourner 404

**Voir :** ENDPOINTS_EXAMPLES.md pour un exemple de code

Labels: enhancement, feature
```

**Issue #4**
```
Titre: [Feature] PUT /projects/:id/grade - Noter un projet

Description:
Implémenter l'endpoint PUT /projects/{id}/grade pour noter un projet.

**Spécifications :**
- Route : PUT /projects/{id}/grade
- Body : JSON avec grade (float)
- Validation : Note entre 0 et 20
- Retour : Le projet mis à jour
- Status Code : 200 OK ou 404 Not Found

**Voir :** ENDPOINTS_EXAMPLES.md pour un exemple de code

Labels: enhancement, feature
```

**Issue #5**
```
Titre: [Feature] DELETE /projects/:id - Supprimer un projet

Description:
Implémenter l'endpoint DELETE /projects/{id} pour supprimer un projet.

**Spécifications :**
- Route : DELETE /projects/{id}
- Retour : Message de confirmation
- Status Code : 200 OK ou 404 Not Found

**Voir :** ENDPOINTS_EXAMPLES.md pour un exemple de code

Labels: enhancement, feature
```

**Issue #6**
```
Titre: [Feature] GET /projects/course/:courseName - Filtrer par cours

Description:
Implémenter l'endpoint GET /projects/course/{courseName} pour filtrer les projets.

**Spécifications :**
- Route : GET /projects/course/{courseName}
- Retour : Liste des projets du cours
- Status Code : 200 OK
- Note : Retourne une liste vide si aucun projet trouvé

**Voir :** ENDPOINTS_EXAMPLES.md pour un exemple de code

Labels: enhancement, feature
```

**Issue #7**
```
Titre: [Documentation] Rédiger la documentation dans le Wiki GitHub

Description:
Créer la documentation complète du projet dans le Wiki GitHub.

**Pages à créer :**
1. Home : Présentation du projet
2. Installation : Guide d'installation
3. API Usage : Documentation des endpoints avec exemples
4. Development : Guide de contribution

**Voir :** Le README.md et ENDPOINTS_EXAMPLES.md pour le contenu

Labels: documentation
```

---

## 📋 Phase 2 : Supervision du Développement (Jour 1-2)

### ✅ Étape 2.1 : Répartir les Issues

1. Organisez une réunion d'équipe (ou discussion en ligne)
2. Chaque membre choisit une Issue
3. Chaque membre s'assigne son Issue sur GitHub

**Vérifiez que :**
- ✅ Chaque membre a au moins 1 Issue
- ✅ Toutes les Issues sont assignées
- ✅ Pas de doublon

### ✅ Étape 2.2 : Superviser les Pull Requests

Pour chaque PR que vous recevez :

1. **Vérifier la qualité de la PR :**
   - ✅ Titre clair
   - ✅ Description complète
   - ✅ Issue liée (fixes #N)
   - ✅ 2 reviewers assignés

2. **Effectuer votre revue :**
   - Lisez le code attentivement
   - Testez localement si possible
   - Laissez des commentaires constructifs
   - Approuvez ou demandez des changements

3. **Merger la PR :**
   - Attendez 2 approbations minimum
   - Attendez que la CI passe au vert
   - Utilisez **"Squash and merge"**
   - Supprimez la branche après le merge

### ✅ Étape 2.3 : Gérer les Conflits

Si une PR a des conflits :

1. Demandez à l'auteur de résoudre les conflits
2. Guidez-le si nécessaire :
   ```bash
   git switch feature/sa-branche
   git merge develop
   # Résoudre les conflits
   git add .
   git commit -m "Resolve merge conflicts"
   git push
   ```

---

## 📋 Phase 3 : CI/CD et Automatisation (Jour 2)

### ✅ Étape 3.1 : Configurer les Branch Protection Rules (5 min)

1. Sur GitHub, allez dans **Settings** > **Branches**
2. Cliquez sur **Add rule**
3. Branch name pattern : `develop`
4. Cochez :
   - ✅ Require a pull request before merging
     - ✅ Require approvals: **2**
   - ✅ Require status checks to pass before merging
   - ✅ Require conversation resolution before merging
5. Cliquez sur **Create**

### ✅ Étape 3.2 : Obtenir une Clé API Gemini (3 min)

1. Allez sur : https://makersuite.google.com/app/apikey
2. Connectez-vous avec votre compte Google
3. Cliquez sur **Create API Key**
4. Copiez la clé (commence par `AIza...`)

### ✅ Étape 3.3 : Générer un Mot de Passe d'Application Gmail (5 min)

1. Allez sur : https://myaccount.google.com/security
2. Activez la **validation en deux étapes** (si pas déjà fait)
3. Recherchez **Mots de passe des applications**
4. Sélectionnez "Autre" et entrez : `ProjetAPI GitHub Actions`
5. Cliquez sur **Générer**
6. Copiez le mot de passe de 16 caractères

### ✅ Étape 3.4 : Configurer les Secrets GitHub (5 min)

1. Sur GitHub, allez dans **Settings** > **Secrets and variables** > **Actions**
2. Cliquez sur **New repository secret**
3. Ajoutez ces 4 secrets :

**Secret 1 :**
- Name: `GEMINI_API_KEY`
- Secret: [Votre clé API Gemini]

**Secret 2 :**
- Name: `MAIL_USERNAME`
- Secret: votre.email@gmail.com

**Secret 3 :**
- Name: `MAIL_PASSWORD`
- Secret: [Le mot de passe d'application de 16 caractères]

**Secret 4 :**
- Name: `TEAM_EMAIL_LIST`
- Secret: email1@univ.com,email2@univ.com,email3@univ.com
  (Tous les emails séparés par des virgules, SANS espaces)

### ✅ Étape 3.5 : Tester la CI/CD (10 min)

Suivez les instructions dans **PHASE3_GITHUB_ACTIONS.md**

---

## 📋 Phase 4 : Release Finale (Jour 3)

### ✅ Étape 4.1 : Vérifier que Tout est Prêt

- ✅ Toutes les Issues sont fermées
- ✅ Toutes les PRs sont mergées dans develop
- ✅ La CI passe au vert sur develop
- ✅ Le Wiki est complété

### ✅ Étape 4.2 : Merger develop dans main (5 min)

```bash
git switch main
git pull origin main
git merge develop
git push origin main
```

### ✅ Étape 4.3 : Créer le Tag v1.0.0 (2 min)

```bash
git tag -a v1.0.0 -m "Release v1.0.0 - ProjetAPI Complete"
git push origin v1.0.0
```

### ✅ Étape 4.4 : Créer la Release sur GitHub (5 min)

1. Sur GitHub, allez dans **Releases**
2. Cliquez sur **Create a new release**
3. Sélectionnez le tag `v1.0.0`
4. Titre : `v1.0.0 - ProjetAPI Complete`
5. Description : (voir PHASE3_GITHUB_ACTIONS.md pour un exemple)
6. Cliquez sur **Publish release**
7. **📸 CAPTURE D'ÉCRAN** de la page de la Release

---

## 📋 Phase 5 : Rapport Final (Jour 3)

### ✅ Étape 5.1 : Collecter les Captures d'Écran

Assurez-vous d'avoir :

- ✅ Hook pre-commit bloquant un commit
- ✅ Discussion de revue de code riche
- ✅ CI échouée (rouge)
- ✅ Commentaire généré par le LLM
- ✅ Email reçu
- ✅ Page de la Release v1.0.0

### ✅ Étape 5.2 : Évaluer la Participation

Créez un tableau avec le taux de participation de chaque membre :

| Membre | Présence | Communication | Travail | Taux Global |
|--------|----------|---------------|---------|-------------|
| Nom 1  | 100%     | Excellente    | Très bon| 100%        |
| Nom 2  | 90%      | Bonne         | Bon     | 90%         |
| ...    | ...      | ...           | ...     | ...         |

### ✅ Étape 5.3 : Rédiger le Rapport

Utilisez **RAPPORT_TEMPLATE.md** comme base.

---

## 📊 Checklist Complète

### Phase 1 : Initialisation
- [ ] Dépôt GitHub privé créé
- [ ] Code poussé (main + develop)
- [ ] develop = branche par défaut
- [ ] Membres invités et ont accepté
- [ ] 7 Issues créées

### Phase 2 : Développement
- [ ] Issues réparties
- [ ] Toutes les PRs revues et mergées
- [ ] Conflits résolus
- [ ] Wiki complété

### Phase 3 : CI/CD
- [ ] Branch Protection Rules configurées
- [ ] 4 Secrets GitHub ajoutés
- [ ] CI testée (vert et rouge)
- [ ] Revue LLM testée
- [ ] Emails testés

### Phase 4 : Release
- [ ] develop mergé dans main
- [ ] Tag v1.0.0 créé
- [ ] Release v1.0.0 publiée

### Phase 5 : Rapport
- [ ] Captures d'écran collectées
- [ ] Participation évaluée
- [ ] Rapport PDF rédigé

---

## 🎯 Conseils pour Réussir

1. **Communiquez** : Restez en contact avec l'équipe
2. **Soyez disponible** : Répondez aux questions rapidement
3. **Soyez bienveillant** : Guidez sans imposer
4. **Soyez rigoureux** : Vérifiez la qualité des PRs
5. **Documentez** : Prenez des notes pour le rapport
6. **Anticipez** : Préparez les phases suivantes à l'avance

---

**Bon courage ! Vous allez assurer ! 🚀**
