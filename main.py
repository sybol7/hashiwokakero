
# The machines are gaining ground. Time to show them what we're really made of...
class Vertex:
    def __init__(self, node, lien):
        self.id = node  # adresse du noeud possiblement un tuple x, y
        self.lien = lien  # liens à trouver
        self.adjacent = {}  # liste des noeuds voisins

    def __str__(self):
        return str(self.id) + ' ' + str(self.lien) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def remove_neighbor(self, neighbor):
        self.adjacent.pop(neighbor)

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_lien(self):
        return self.lien

    def get_number_of_neighbor(self):
        return len(self.adjacent)

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.connections = ['0 0 0 1 2', '0 1 1 1 2']

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, lien):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node, lien)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


a = Graph()
#width = int(input())  # the number of cells on the X axis
#height = int(input())  # the number of cells on the Y axis
lines = ['2.', '42']  # [input() for i in range(height)]
# transposition des colonnes en lignes
tr_lines = [''.join(x) for x in zip(*lines)]

# Construction du graph des coodonnées des sommets
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if ch == '.':
            continue
        else:
            a.add_vertex((x, y), int(ch))

# ajout des voisins
x1 = y1 = x2 = y2 = -1
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if ch == '.':
            pass
        else:
            if (x1, y1) == (-1, -1):
                x1, y1 = x, y
            else:
                x2, y2 = x, y
                a.add_edge((x1, y1), (x2, y2))
                x1, y1 = x2, y2
    x1 = y1 = x2 = y2 = -1

x1 = y1 = x2 = y2 = -1
for y, line in enumerate(tr_lines):
    for x, ch in enumerate(line):
        if ch == '.':
            pass
        else:
            if (x1, y1) == (-1, -1):
                x1, y1 = y, x
            else:
                x2, y2 = y, x
                a.add_edge((x1, y1), (x2, y2))
                x1, y1 = x2, y2
    x1 = y1 = x2 = y2 = -1

# afichagecdu graph
for node in a:
    print(node)



