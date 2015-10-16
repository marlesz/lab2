#  W    zorowane na przykładzie Rona Zacharskiego


from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0},
        }
def manhattan(rating1, rating2):
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają wspólnych elementów"""
    # TODO: wpisz kod
    distance = 0
    licz = 0
    for i,j in users[rating1].iteritems():
        for k, l in users[rating2].iteritems():
            if i == k:
                dist = abs(l-j)
                distance = distance + dist
                licz = licz +1
    if licz == 0:
        distance = -1
    return distance


def computeNearestNeighbor(username, users):
    """dla danego użytkownika username, zwróć ze słownika users nazwę użytkownika o najbliższych preferencjach"""
    nameOfNearestNeighbor = ""
    distances = []
    nn=[]
    # TODO: wpisz kod
    for u in users:
        if u!= username and manhattan(username, u)!=-1:
            distances.append(manhattan(username, u))
            nn.append(u)
    if nn:
        ind =distances.index(min(distances))
        nameOfNearestNeighbor = nn[ind]  # tym spoosbem nie da się wyłonić więcej niż jednego imienia w przypadku, gdy odległości są takie same do kilku osób, zwracana jest tylko jedna

    return nameOfNearestNeighbor

def recommend(username, users):
    """Zwróć listę rekomendacji dla użytkownika"""
    # znajdź preferencje najbliższego sąsiada
    nearest = computeNearestNeighbor(username, users)
    
    recommendations = []
    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiad
    # TODO: wpisz kod

    for ww, zz in users[nearest].iteritems():
        if ww not in users[username].keys():
            recommendations.append((ww,zz))
    return sorted([item[0] for item in recommendations], key=lambda artistTuple: artistTuple[1], reverse = True) #zwraca artystów, posortowane po ocenie - czy w liście recommendations mają być oceny?, co ma się wyświetlać?
    #return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True) #oryginał
    #print ([item[0] for item in recommendations])

# przykłady

print( recommend('Hela', users))
print( recommend('Ela', users))
#print ( computeNearestNeighbor('Hela', users))

