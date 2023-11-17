import random
import math
import pyxel

# Função para gerar a "teia" de pontos aleatórios
def generate_web(tamanho):
    teia = []
    for x in range(tamanho):
        linha = []
        for y in range(tamanho):
            number = random.randint(0, 100)
            if number >= 99:
                number = 1
            else:
                number = 0

            linha.append(number)
        teia.append(linha)

    return teia

# Função para calcular a distância euclidiana entre dois pontos
def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Função para obter os pontos a partir da "teia"
def get_points(teia):
    points = []
    tamanho = len(teia)

    for x in range(tamanho):
        for y in range(tamanho):
            if teia[x][y] == 1:
                points.append((x, y))

    return points

# Classe principal da aplicação
class App:
    def __init__(self):
        # Tamanho da "teia" e inicialização dos atributos
        self.tamanho = 25
        self.teia = generate_web(self.tamanho)
        self.points = get_points(self.teia)
        self.point1 = None
        self.point2 = None
        self.found = False

        # Inicialização do Pyxel
        pyxel.init(25, 25, fps=10)

    def draw(self):
        # Limpa a tela e desenha os pontos
        pyxel.cls(0)
        self.draw_points()

        # Se os pontos mais próximos foram encontrados, destaca-os em verde-água
        if self.point1 is not None and self.point2 is not None:
            pyxel.rect(self.point1[0], self.point1[1], 1, 1, 11)
            pyxel.rect(self.point2[0], self.point2[1], 1, 1, 11)

    def update(self):
        # Se os pontos mais próximos ainda não foram encontrados
        if not self.found:
            # Encontra os pontos mais próximos
            min_distance, self.point1, self.point2 = self.find_closest_points(
                self.points)

            # Destaca os pontos mais próximos em verde-água
            pyxel.rect(self.point1[0], self.point1[1], 1, 1, 11)
            pyxel.rect(self.point2[0], self.point2[1], 1, 1, 11)

            # Atualiza a tela
            pyxel.flip()
            pyxel.cls(0)

            # Verifica se a distância encontrada é igual a 1
            if min_distance == 1:
                self.found = True
                print("Os pontos mais próximos foram encontrados! Aqui:",
                      self.point1, self.point2)

    def draw_points(self):
        # Desenha os pontos na tela
        for point in self.points:
            pyxel.rect(point[0], point[1], 1, 1, 7)

    def run(self):
        # Executa o loop principal do Pyxel
        pyxel.run(self.update, self.draw)

    def find_closest_points(self, points):
        # Encontra os pontos mais próximos
        if len(points) < 2:
            return int('inf'), None, None

        if len(points) == 2:
            point1 = points[0]
            point2 = points[1]
            dist = calculate_distance(point1, point2)
            return dist, point1, point2

        min_distance = float('inf')
        point1 = None
        point2 = None

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = calculate_distance(points[i], points[j])
                if dist < min_distance:
                    min_distance = dist
                    point1 = points[i]
                    point2 = points[j]

                # Exibe as comparações dos pontos
                pyxel.rect(points[i][0], points[i][1], 1, 1, 7)
                pyxel.rect(points[j][0], points[j][1], 1, 1, 7)
                pyxel.flip()
                pyxel.cls(0)

        self.found = True
        print(point1)
        print(point2)
        return min_distance, point1, point2

# Executa a aplicação se este script for o principal
if __name__ == "__main__":
    App().run()
