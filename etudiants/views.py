from django.http import Http404 , JsonResponse
from django.shortcuts import render

ETUDIANTS = [
    {"id": 1, "nom": "Ali", "moyenne": 14.5,"filiere": "Informatique"},
    {"id": 2, "nom": "Sana", "moyenne": 16,"filiere": "Mathématiques"},
    {"id": 3, "nom": "Omar", "moyenne": 11.75,"filiere": "Physique"},
]

def liste(request):
    return render(request, "etudiants/liste.html", {"etudiants": ETUDIANTS})

def detail(request, id):
    etudiant = next((e for e in ETUDIANTS if e["id"] == id), None)
    if not etudiant:
        raise Http404("Étudiant non trouvé")
    return render(request, "etudiants/detail.html", {"etudiant": etudiant})


def recherche(request):
    query = request.GET.get('q', '') # Récupère la valeur de 'q' dans l'URL (ex: ?q=an)
    
    # Filtrer les étudiants dont le nom contient la recherche (en ignorant la casse)
    resultats = [e for e in ETUDIANTS if query.lower() in e['nom'].lower()] if query else []
    
    context = {
        "etudiants": resultats,
        "query": query
    }
    return render(request, "etudiants/recherche.html", context)


def etudiants_api(request):
    # safe=False est requis car on passe une liste (et non un dictionnaire) en premier argument
    return JsonResponse(ETUDIANTS, safe=False)

def introuvable(request):
    raise Http404("Page introuvable")
