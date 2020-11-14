# TIAG

Korzystamy w pakietu graphviz, i jego podstawowej klasy Graph

W Graph wierzchołki wyglądają następująco:
 "\tname [label=label_name]"
 a krawędzie:
 "\t name -- name"

gdzie:
- name - unikalna nazwa wierzchołka
- label_name - co to wyświetla się na podglądzie grafu

Zdefiniowana została klasa Graph_Trainsformation zawierająca roszrzeczenie klasy graphviz.Graph i z niej będziemy korzystać
- Grafy są nieskierowane
- Po lewej stronie produkcji zawsze jeden wierzchołek
- Węzły nieterminalne mają label zapisany wielką literą
- Węzły terminalne mają label zapisany małą literą
- Krawędzie są bez attrybytów
- Dla wygody nazwy są kolejnymi liczbami naturalnymi (zapisane niestety jako stringi)
