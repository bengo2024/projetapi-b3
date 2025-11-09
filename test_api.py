"""
Script de test pour ProjetAPI
Teste tous les endpoints de l'API
"""

import requests
import json

BASE_URL = "http://localhost:8000"


def print_test(message):
    """Affiche le nom du test"""
    print(f"\n🧪 {message}")
    print("=" * 60)


def print_success(message):
    """Affiche un message de succès"""
    print(f"✅ {message}")


def print_error(message):
    """Affiche un message d'erreur"""
    print(f"❌ {message}")


def print_response(response):
    """Affiche la réponse formatée"""
    try:
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except Exception:
        print(response.text)


def test_health_check():
    """Test 1: Health check"""
    print_test("Test 1: Health Check")
    response = requests.get(f"{BASE_URL}/health")

    if response.status_code == 200:
        print_success(f"Health check OK (HTTP {response.status_code})")
        print_response(response)
    else:
        print_error(f"Health check failed (HTTP {response.status_code})")


def test_create_project():
    """Test 2: POST /projects - Créer un projet"""
    print_test("Test 2: POST /projects - Créer un nouveau projet")

    data = {
        "studentName": "Alice Dupont",
        "course": "Versionning Git",
        "githubUrl": "https://github.com/alice/projet-git",
    }

    response = requests.post(f"{BASE_URL}/projects", json=data)

    if response.status_code == 201:
        print_success(f"Projet créé avec succès (HTTP {response.status_code})")
        print_response(response)
        return response.json()["id"]
    else:
        print_error(f"Échec de création (HTTP {response.status_code})")
        print_response(response)
        return None


def test_create_second_project():
    """Test 3: POST /projects - Créer un deuxième projet"""
    print_test("Test 3: POST /projects - Créer un deuxième projet")

    data = {
        "studentName": "Bob Martin",
        "course": "DevOps",
        "githubUrl": "https://github.com/bob/projet-devops",
    }

    response = requests.post(f"{BASE_URL}/projects", json=data)

    if response.status_code == 201:
        print_success(f"Deuxième projet créé (HTTP {response.status_code})")
        print_response(response)
    else:
        print_error(f"Échec de création (HTTP {response.status_code})")
        print_response(response)


def test_get_all_projects():
    """Test 4: GET /projects - Lister tous les projets"""
    print_test("Test 4: GET /projects - Lister tous les projets")

    response = requests.get(f"{BASE_URL}/projects")

    if response.status_code == 200:
        print_success(f"Liste récupérée (HTTP {response.status_code})")
        print_response(response)
    else:
        print_error(f"Échec de récupération (HTTP {response.status_code})")
        print_response(response)


def test_get_project_by_id(project_id):
    """Test 5: GET /projects/:id - Obtenir un projet par ID"""
    print_test(f"Test 5: GET /projects/{project_id} - Obtenir un projet par ID")

    response = requests.get(f"{BASE_URL}/projects/{project_id}")

    if response.status_code == 200:
        print_success(f"Projet récupéré (HTTP {response.status_code})")
        print_response(response)
    else:
        print_error(f"Échec de récupération (HTTP {response.status_code})")
        print_response(response)


def test_get_nonexistent_project():
    """Test 6: GET /projects/:id - Projet inexistant (404)"""
    print_test("Test 6: GET /projects/999 - Projet inexistant (doit retourner 404)")

    response = requests.get(f"{BASE_URL}/projects/999")

    if response.status_code == 404:
        print_success(f"404 correctement retourné (HTTP {response.status_code})")
        print_response(response)
    else:
        print_error(
            f"Code HTTP incorrect (attendu 404, reçu {response.status_code})"
        )
        print_response(response)


def test_update_grade(project_id):
    """Test 7: PUT /projects/:id/grade - Noter un projet"""
    print_test(f"Test 7: PUT /projects/{project_id}/grade - Noter un projet")

    data = {"grade": 18.5}

    response = requests.put(f"{BASE_URL}/projects/{project_id}/grade", json=data)

    if response.status_code == 200:
        print_success(f"Note ajoutée (HTTP {response.status_code})")
        print_response(response)
    else:
        print_error(f"Échec de notation (HTTP {response.status_code})")
        print_response(response)


def test_filter_by_course():
    """Test 8: GET /projects/course/:courseName - Filtrer par cours"""
    print_test(
        "Test 8: GET /projects/course/Versionning Git - Filtrer par cours"
    )

    response = requests.get(f"{BASE_URL}/projects/course/Versionning Git")

    if response.status_code == 200:
        print_success(f"Projets filtrés (HTTP {response.status_code})")
        print_response(response)
    else:
        print_error(f"Échec de filtrage (HTTP {response.status_code})")
        print_response(response)


def test_delete_project(project_id):
    """Test 9: DELETE /projects/:id - Supprimer un projet"""
    print_test(f"Test 9: DELETE /projects/{project_id} - Supprimer un projet")

    response = requests.delete(f"{BASE_URL}/projects/{project_id}")

    if response.status_code == 200:
        print_success(f"Projet supprimé (HTTP {response.status_code})")
        print_response(response)
    else:
        print_error(f"Échec de suppression (HTTP {response.status_code})")
        print_response(response)


def test_verify_deletion(project_id):
    """Test 10: Vérifier que le projet est bien supprimé"""
    print_test("Test 10: Vérifier que le projet est bien supprimé")

    response = requests.get(f"{BASE_URL}/projects/{project_id}")

    if response.status_code == 404:
        print_success(f"Projet bien supprimé (HTTP {response.status_code})")
        print_response(response)
    else:
        print_error(f"Le projet existe encore (HTTP {response.status_code})")
        print_response(response)


def main():
    """Fonction principale"""
    print("\n" + "=" * 60)
    print("🧪 Test de l'API ProjetAPI")
    print("=" * 60)

    try:
        # Test 1: Health check
        test_health_check()

        # Test 2: Créer un projet
        project_id = test_create_project()

        if project_id is None:
            print_error("Impossible de continuer sans ID de projet")
            return

        # Test 3: Créer un deuxième projet
        test_create_second_project()

        # Test 4: Lister tous les projets
        test_get_all_projects()

        # Test 5: Obtenir un projet par ID
        test_get_project_by_id(project_id)

        # Test 6: Projet inexistant
        test_get_nonexistent_project()

        # Test 7: Noter un projet
        test_update_grade(project_id)

        # Test 8: Filtrer par cours
        test_filter_by_course()

        # Test 9: Supprimer un projet
        test_delete_project(project_id)

        # Test 10: Vérifier la suppression
        test_verify_deletion(project_id)

        print("\n" + "=" * 60)
        print("🎉 Tests terminés !")
        print("=" * 60 + "\n")

    except requests.exceptions.ConnectionError:
        print_error(
            "\n❌ Impossible de se connecter à l'API. "
            "Assurez-vous que le serveur est lancé :\n"
            "   uvicorn main:app --reload\n"
        )
    except Exception as e:
        print_error(f"\n❌ Erreur inattendue : {e}\n")


if __name__ == "__main__":
    main()

