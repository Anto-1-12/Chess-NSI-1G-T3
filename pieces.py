import pygame

class pieces :
    def __init__(self):
        self.texture = 0
        self.color = 0
        self.type = ""

    def dep_possible (self,x,y,echiquier):
        return []

    def obtenir_img(self):
        return self.texture

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

class pions (pieces):
    def __init__(self,color):
        super().__init__()
        self.type = "pions"
        self.color = color
        self.texture = pygame.transform.scale(
            pygame.image.load("file/textures/pion_"+str(color)+".png"), (100,100))

    def dep_possible(self,x,y,echiquier):
        depY = 0
        #si le premier est faux c est que ce n est pas un deplacement
        #Si le second est faux alors c est pas un mangeage
        echiquier_dep =\
            [
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]]
             ] 
         
        if self.color == 2:
            depY = 1
        else:
            depY = -1

        if echiquier[y + depY][x] == 0:
            echiquier_dep[y + depY][x] = [True,False]


        if -1 < x+1 < 8 and echiquier[y + depY][x + 1] != 0 and echiquier[y + depY][x + 1].get_color() != self.color:
            echiquier_dep[y + depY][x + 1] = [True, True]

        if -1 < x-1 < 8 and echiquier[y + depY][x - 1] != 0 and echiquier[y + depY][x - 1].get_color() != self.color:
            echiquier_dep[y + depY][x - 1] = [True, True]

        return echiquier_dep


class tour(pieces):
    def __init__(self, color):
        super().__init__()
        self.type = "tour"
        self.color = color
        self.texture = pygame.transform.scale(
            pygame.image.load("file/textures/tour_" + str(color) + ".png"), (100, 100))

    def dep_possible(self, x, y, echiquier):
        # si le premier est faux c est que ce n est pas un deplacement
        # Si le second est faux alors c est pas un mangeage
        echiquier_dep =\
            [
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]]
             ]

        vecteur_dep = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for vec in range(4):
            x_boucle = x
            y_boucle = y
            while -1 < x_boucle < 8 and -1 < y_boucle < 8:

                if echiquier[y_boucle][x_boucle] != 0:
                    if echiquier[y_boucle][x_boucle].get_color() != self.color:
                        echiquier_dep[y_boucle][x_boucle] = [True, True]
                        break
                    if echiquier[y_boucle][x_boucle].get_color() == self.color:
                        if vecteur_dep[vec][0] == 0:
                            if y_boucle != y:
                                break
                        if vecteur_dep[vec][1] == 0:
                            if x_boucle != x:
                                break
                if vecteur_dep[vec][0] == 0:
                    if y_boucle != y:
                        echiquier_dep[y_boucle][x_boucle] = [True, False]
                if vecteur_dep[vec][1] == 0:
                    if x_boucle != x:
                        echiquier_dep[y_boucle][x_boucle] = [True, False]
                x_boucle += vecteur_dep[vec][0]
                y_boucle += vecteur_dep[vec][1]

        return echiquier_dep

class fou(pieces):
    def __init__(self, color):
        super().__init__()
        self.type = "fou"
        self.color = color
        self.texture = pygame.transform.scale(
            pygame.image.load("file/textures/fou_" + str(color) + ".png"), (100, 100))

    def dep_possible(self, x, y, echiquier):
        # si le premier est faux c est que ce n est pas un deplacement
        # Si le second est faux alors c est pas un mangeage
        echiquier_dep =\
            [
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]]
             ]

        vecteur_dep = [[1,1],[-1,1],[1,-1],[-1,-1]]

        for vec in range(4):
            x_boucle = x
            y_boucle = y
            while -1 < x_boucle < 8 and -1 < y_boucle < 8:

                if echiquier[y_boucle][x_boucle] != 0:
                    if echiquier[y_boucle][x_boucle].get_color() != self.color:
                        echiquier_dep[y_boucle][x_boucle] = [True, True]
                        break
                    if echiquier[y_boucle][x_boucle].get_color() == self.color and (x_boucle != x and y_boucle != y):
                        break
                elif x_boucle != x and y_boucle != y:
                    echiquier_dep[y_boucle][x_boucle] = [True, False]
                x_boucle += vecteur_dep[vec][0]
                y_boucle += vecteur_dep[vec][1]

        return echiquier_dep

class reine(pieces):
    def __init__(self, color):
        super().__init__()
        self.type = "reine"
        self.color = color
        self.texture = pygame.transform.scale(
            pygame.image.load("file/textures/reine_" + str(color) + ".png"), (100, 100))

    def dep_possible(self, x, y, echiquier):
        # si le premier est faux c est que ce n est pas un deplacement
        # Si le second est faux alors c est pas un mangeage
        echiquier_dep =\
            [
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]]
             ]

        vecteur_dep = [[1,1],[-1,1],[1,-1],[-1,-1]]

        for vec in range(4):
            x_boucle = x
            y_boucle = y
            while -1 < x_boucle < 8 and -1 < y_boucle < 8:

                if echiquier[y_boucle][x_boucle] != 0:
                    if echiquier[y_boucle][x_boucle].get_color() != self.color:
                        echiquier_dep[y_boucle][x_boucle] = [True, True]
                        break
                    if echiquier[y_boucle][x_boucle].get_color() == self.color and (x_boucle != x and y_boucle != y):
                        break
                elif x_boucle != x and y_boucle != y:
                    echiquier_dep[y_boucle][x_boucle] = [True, False]
                x_boucle += vecteur_dep[vec][0]
                y_boucle += vecteur_dep[vec][1]

            vecteur_dep_2 = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for vec_2 in range(4):
                x_boucle = x
                y_boucle = y
                while -1 < x_boucle < 8 and -1 < y_boucle < 8:

                    if echiquier[y_boucle][x_boucle] != 0:
                        if echiquier[y_boucle][x_boucle].get_color() != self.color:
                            echiquier_dep[y_boucle][x_boucle] = [True, True]
                            break
                        if echiquier[y_boucle][x_boucle].get_color() == self.color:
                            if vecteur_dep_2[vec_2][0] == 0:
                                if y_boucle != y:
                                    break
                            if vecteur_dep_2[vec_2][1] == 0:
                                if x_boucle != x:
                                    break
                    if vecteur_dep_2[vec_2][0] == 0:
                        if y_boucle != y:
                            echiquier_dep[y_boucle][x_boucle] = [True, False]
                    if vecteur_dep_2[vec_2][1] == 0:
                        if x_boucle != x:
                            echiquier_dep[y_boucle][x_boucle] = [True, False]
                    x_boucle += vecteur_dep_2[vec_2][0]
                    y_boucle += vecteur_dep_2[vec_2][1]

        return echiquier_dep


class cavalier(pieces):
    def __init__(self, color):
        super().__init__()
        self.type = "cavalier"
        self.color = color
        self.texture = pygame.transform.scale(
            pygame.image.load("file/textures/cavalier_" + str(color) + ".png"), (100, 100))

    def dep_possible(self, x, y, echiquier):
        # si le premier est faux c est que ce n est pas un deplacement
        # Si le second est faux alors c est pas un mangeage
        echiquier_dep =\
            [
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]]
             ]

        vecteur_dep = [
             [-1,-2],[1,-2]
            ,[2,-1],[2,1]
            ,[-1,2],[1,2]
            ,[-2,1],[-2,-1]
                       ]
        for vec in vecteur_dep:
            x_case = x + vec[0]
            y_case = y + vec[1]
            if -1 < x_case < 8 and -1 < y_case < 8:
                if echiquier[y_case][x_case] == 0:
                    echiquier_dep[y_case][x_case] = [True, False]
                if echiquier[y_case][x_case] != 0 and echiquier[y_case][x_case].get_color() != self.color:
                    echiquier_dep[y_case][x_case] = [True, True]

        return echiquier_dep

class roi(pieces):
    def __init__(self, color):
        super().__init__()
        self.type = "roi"
        self.color = color
        self.texture = pygame.transform.scale(
            pygame.image.load("file/textures/roi_" + str(color) + ".png"), (100, 100))

    def dep_possible(self, x, y, echiquier):
        # si le premier est faux c est que ce n est pas un deplacement
        # Si le second est faux alors c est pas un mangeage
        echiquier_dep =\
            [
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]],
             [[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False]]
             ]

        vecteur_dep = [
             [-1,-1],[0,-1],[1,-1]
            ,[-1,0] ,       [1,0]
            ,[-1,1] ,[0,1] ,[1,1]
                       ]
        for vec in vecteur_dep:
            x_case = x + vec[0]
            y_case = y + vec[1]
            if -1 < x_case < 8 and -1 < y_case < 8:
                if echiquier[y_case][x_case] == 0:
                    echiquier_dep[y_case][x_case] = [True, False]
                if echiquier[y_case][x_case] != 0 and echiquier[y_case][x_case].get_color() != self.color:
                    echiquier_dep[y_case][x_case] = [True, True]

        return echiquier_dep