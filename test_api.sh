#!/bin/bash

# Script de test pour ProjetAPI
# Ce script teste tous les endpoints de l'API

echo "🧪 Test de l'API ProjetAPI"
echo "=========================="
echo ""

BASE_URL="http://localhost:8000"

# Couleurs pour l'affichage
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonction pour afficher les résultats
print_test() {
    echo -e "${BLUE}$1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Test 1: Health check
print_test "Test 1: Health Check"
response=$(curl -s -w "\n%{http_code}" $BASE_URL/health)
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "200" ]; then
    print_success "Health check OK"
    echo "$body" | jq .
else
    print_error "Health check failed (HTTP $http_code)"
fi
echo ""

# Test 2: POST /projects - Créer un projet
print_test "Test 2: POST /projects - Créer un nouveau projet"
response=$(curl -s -w "\n%{http_code}" -X POST $BASE_URL/projects \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "Alice Dupont",
    "course": "Versionning Git",
    "githubUrl": "https://github.com/alice/projet-git"
  }')
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "201" ]; then
    print_success "Projet créé avec succès"
    echo "$body" | jq .
    PROJECT_ID=$(echo "$body" | jq -r '.id')
else
    print_error "Échec de création (HTTP $http_code)"
fi
echo ""

# Test 3: POST /projects - Créer un deuxième projet
print_test "Test 3: POST /projects - Créer un deuxième projet"
response=$(curl -s -w "\n%{http_code}" -X POST $BASE_URL/projects \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "Bob Martin",
    "course": "DevOps",
    "githubUrl": "https://github.com/bob/projet-devops"
  }')
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "201" ]; then
    print_success "Deuxième projet créé"
    echo "$body" | jq .
else
    print_error "Échec de création (HTTP $http_code)"
fi
echo ""

# Test 4: GET /projects - Lister tous les projets
print_test "Test 4: GET /projects - Lister tous les projets"
response=$(curl -s -w "\n%{http_code}" $BASE_URL/projects)
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "200" ]; then
    print_success "Liste récupérée"
    echo "$body" | jq .
else
    print_error "Échec de récupération (HTTP $http_code)"
fi
echo ""

# Test 5: GET /projects/:id - Obtenir un projet par ID
print_test "Test 5: GET /projects/$PROJECT_ID - Obtenir un projet par ID"
response=$(curl -s -w "\n%{http_code}" $BASE_URL/projects/$PROJECT_ID)
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "200" ]; then
    print_success "Projet récupéré"
    echo "$body" | jq .
else
    print_error "Échec de récupération (HTTP $http_code)"
fi
echo ""

# Test 6: GET /projects/:id - Projet inexistant (404)
print_test "Test 6: GET /projects/999 - Projet inexistant (doit retourner 404)"
response=$(curl -s -w "\n%{http_code}" $BASE_URL/projects/999)
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "404" ]; then
    print_success "404 correctement retourné"
    echo "$body" | jq .
else
    print_error "Code HTTP incorrect (attendu 404, reçu $http_code)"
fi
echo ""

# Test 7: PUT /projects/:id/grade - Noter un projet
print_test "Test 7: PUT /projects/$PROJECT_ID/grade - Noter un projet"
response=$(curl -s -w "\n%{http_code}" -X PUT $BASE_URL/projects/$PROJECT_ID/grade \
  -H "Content-Type: application/json" \
  -d '{"grade": 18.5}')
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "200" ]; then
    print_success "Note ajoutée"
    echo "$body" | jq .
else
    print_error "Échec de notation (HTTP $http_code)"
fi
echo ""

# Test 8: GET /projects/course/:courseName - Filtrer par cours
print_test "Test 8: GET /projects/course/Versionning%20Git - Filtrer par cours"
response=$(curl -s -w "\n%{http_code}" "$BASE_URL/projects/course/Versionning%20Git")
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "200" ]; then
    print_success "Projets filtrés"
    echo "$body" | jq .
else
    print_error "Échec de filtrage (HTTP $http_code)"
fi
echo ""

# Test 9: DELETE /projects/:id - Supprimer un projet
print_test "Test 9: DELETE /projects/$PROJECT_ID - Supprimer un projet"
response=$(curl -s -w "\n%{http_code}" -X DELETE $BASE_URL/projects/$PROJECT_ID)
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "200" ]; then
    print_success "Projet supprimé"
    echo "$body" | jq .
else
    print_error "Échec de suppression (HTTP $http_code)"
fi
echo ""

# Test 10: Vérifier que le projet est bien supprimé
print_test "Test 10: Vérifier que le projet est bien supprimé"
response=$(curl -s -w "\n%{http_code}" $BASE_URL/projects/$PROJECT_ID)
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "404" ]; then
    print_success "Projet bien supprimé (404)"
    echo "$body" | jq .
else
    print_error "Le projet existe encore (HTTP $http_code)"
fi
echo ""

echo "=========================="
echo "🎉 Tests terminés !"
echo "=========================="

