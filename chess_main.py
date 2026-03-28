import csv
from tkinter import *
from tkinter import filedialog

from pieces import *
from REPLAY import *

class game_chess:
    def __init__ (self):
        #2 = noir et 1 blanc et 0 vide

        self.run = True
        self.screen = pygame.display.set_mode((800, 800))
        self.nomdevariable = pygame.key.get_pressed()
        self.height = self.screen.get_height()
        self.width  = self.screen.get_width()
        self.select_pion = [False,0,0]
        self.est_en_echeque = False
        self.dep_pion_poss =\
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
        self.dep_poss = \
            [
            [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
            [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
            [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
            [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
            [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
            [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
            [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
            [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]]
            ]
        self.color_playing = 1
        self.echiquier =\
            [
             [tour(2),cavalier(2),fou(2),reine(2),roi(2),fou(2),cavalier(2),tour(2)],
             [pions(2),pions(2),pions(2),pions(2),pions(2),pions(2),pions(2),pions(2)],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [pions(1),pions(1),pions(1),pions(1),pions(1),pions(1),pions(1),pions(1)],
             [tour(1),cavalier(1),fou(1),reine(1),roi(1),fou(1),cavalier(1),tour(1)]
             ]
        self.replay_game = 0
        self.old_pos = [0,0]
        self.menu = True
        self.Replaying = False
        self.img_play_button = pygame.transform.scale(
            pygame.image.load("file/textures/Play_button.png"), (200, 200))
        self.font = pygame.font.Font(None, 70)
        self.nb_counter_arrow = -1
        self.replay_content = 0
        self.max_coup = 0
        self.pressed_right = False
        self.pressed_left = False

        try:
            file = open("file/score.csv", "r", newline="")
            self.reader = csv.reader(file)
            next(self.reader, None)
            self.scores = []
            for ligne in self.reader:
                self.scores.append(ligne)
            file_write = open("file/score.csv", "w", newline="")
        except:
            file_write = open("file/score.csv", "w", newline="")
            file = open("file/score.csv", "r", newline="")
            self.reader = csv.reader(file)
            next(self.reader, None)
            self.scores = []
            for ligne in self.reader:
                self.scores.append(ligne)

        self.writer = csv.writer(file_write)
        self.writer.writerow(["white", "black"])

        self.white_score = 0
        self.black_score = 0

    def initialisation(self):
        if self.replay_game != 0:
            self.replay_game.end_replay()
        self.select_pion = [False, 0, 0]
        self.dep_pion_poss = \
            [
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],[False, False], [False, False]]
            ]
        self.dep_poss = \
            [
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],
                 [False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],
                 [False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],
                 [False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],
                 [False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],
                 [False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],
                 [False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],
                 [False, False], [False, False]],
                [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False],
                 [False, False], [False, False]]
            ]

        self.echiquier = \
            [
                [tour(2), cavalier(2), fou(2), reine(2), roi(2), fou(2), cavalier(2), tour(2)],
                [pions(2), pions(2), pions(2), pions(2), pions(2), pions(2), pions(2), pions(2)],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [pions(1), pions(1), pions(1), pions(1), pions(1), pions(1), pions(1), pions(1)],
                [tour(1), cavalier(1), fou(1), reine(1), roi(1), fou(1), cavalier(1), tour(1)]
            ]
        self.menu = False
        self.replay_game = Replay()
        self.white_score = 0
        self.black_score = 0


    def test_echeque(self):

        # Initialisation de dep_poss : tableau 8x8 de [False, False]
        self.dep_poss = [[[False, False] for _ in range(8)] for _ in range(8)]

        coo_roi = []

        for x in range(8):
            for y in range(8):
                pion = self.echiquier[y][x]
                if pion != 0:

                    # Si c'est un pion adverse
                    if pion.get_color() != self.color_playing:
                        tab = pion.dep_possible(x, y, self.echiquier)
                        for x_2 in range(8):
                            for y_2 in range(8):
                                if tab[y_2][x_2][0]:
                                    self.dep_poss[y_2][x_2] = tab[y_2][x_2]

                    # Sauvegarde des coordonnées du roi du joueur actuel
                    if pion.get_type() == "roi" and pion.get_color() == self.color_playing:
                        coo_roi = [x, y]

        # Vérifie si le roi est menacé
        if coo_roi and self.dep_poss[coo_roi[1]][coo_roi[0]][0]:
            self.est_en_echeque = True
            print("est en échec")
        else:
            self.est_en_echeque = False

    def coup_est_valide(self, start_x, start_y, end_x, end_y):
        # Sauvegarde l’état actuel
        piece_source = self.echiquier[start_y][start_x]
        piece_destination = self.echiquier[end_y][end_x]

        # Effectuer le déplacement fictif
        self.echiquier[end_y][end_x] = piece_source
        self.echiquier[start_y][start_x] = 0

        # Vérifie si le roi est en échec après le coup
        self.test_echeque()
        est_valide = not self.est_en_echeque

        # Annule le déplacement
        self.echiquier[start_y][start_x] = piece_source
        self.echiquier[end_y][end_x] = piece_destination

        # Rétablit l’état d’échec précédent
        self.test_echeque()

        return est_valide

    def inputs (self):


        self.nomdevariable = pygame.key.get_pressed()

        if self.menu == False :
            if not self.Replaying :
                for event in pygame.event.get():
                    cooX = int(pygame.mouse.get_pos()[0] / 800 * 8)
                    cooY = int(pygame.mouse.get_pos()[1] / 800 * 8)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Sélectionner un pion
                        if self.echiquier[cooY][cooX] != 0 and self.echiquier[cooY][
                            cooX].get_color() == self.color_playing:
                            self.select_pion = [True, cooX, cooY]
                            self.dep_pion_poss = self.echiquier[cooY][cooX].dep_possible(cooX, cooY, self.echiquier)

                        # Déplacer le pion
                        if self.select_pion[0] and self.dep_pion_poss[cooY][cooX][0]:
                            if self.coup_est_valide(self.select_pion[1], self.select_pion[2], cooX, cooY):
                                if self.dep_pion_poss[cooY][cooX][1] == False:
                                    # Déplacement simple
                                    self.echiquier[cooY][cooX] = self.echiquier[self.select_pion[2]][self.select_pion[1]]
                                    self.echiquier[self.select_pion[2]][self.select_pion[1]] = 0

                                    self.replay_game.main([self.select_pion[1], self.select_pion[2], cooX, cooY, False])

                                else:
                                    # Capture
                                    self.replay_game.main([self.select_pion[1], self.select_pion[2], cooX, cooY, True,self.echiquier[cooY][cooX].get_type(),self.echiquier[cooY][cooX].get_color()])

                                    piece_mange = self.echiquier[cooY][cooX]

                                    self.echiquier[cooY][cooX] = self.echiquier[self.select_pion[2]][self.select_pion[1]]
                                    self.echiquier[self.select_pion[2]][self.select_pion[1]] = 0

                                    if self.color_playing == 1:
                                        self.white_score += 1
                                    else:
                                        self.black_score += 1

                                    if piece_mange.get_type() == "roi":
                                        self.menu = True
                                        if self.replay_game != 0:
                                            self.replay_game.end_replay()
                                        self.replay_game = 0
                                        self.scores.append([self.white_score, self.black_score])

                            # Changer de joueur
                                if self.color_playing == 1:
                                    self.color_playing = 2
                                else:
                                    self.color_playing = 1

                            self.select_pion = [False, cooX, cooY]

                        # Annuler la sélection si la case est vide ou si on annule le déplacement
                        if self.select_pion[0] and self.echiquier[cooY][cooX] == 0 and not \
                        self.dep_pion_poss[cooY][cooX][
                            0]:
                            self.select_pion = [False, cooX, cooY]

                    if self.nomdevariable[pygame.K_ESCAPE]:
                        self.menu = True
                        if self.replay_game != 0:
                            self.replay_game.end_replay()
                        self.replay_game = 0
                        self.scores.append([self.white_score, self.black_score])

                    if event.type == pygame.QUIT:
                        self.run = False
                        if self.replay_game != 0:
                            self.replay_game.end_replay()
                        self.scores.append([self.white_score, self.black_score])
                        for score in self.scores:
                            self.writer.writerow(score)


                    if self.nomdevariable[pygame.K_DELETE]:
                        self.run = False
                        self.replay_game.end_replay()
                        self.replay_content.append(self.replay_game.get_name())
                        self.scores.append([self.white_score,self.black_score])
                        for score in self.scores:
                            self.writer.writerow(score)

            else :
                if self.replay_content == 0:
                    self.echiquier = \
                        [
                            [tour(2), cavalier(2), fou(2), reine(2), roi(2), fou(2), cavalier(2), tour(2)],
                            [pions(2), pions(2), pions(2), pions(2), pions(2), pions(2), pions(2), pions(2)],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [pions(1), pions(1), pions(1), pions(1), pions(1), pions(1), pions(1), pions(1)],
                            [tour(1), cavalier(1), fou(1), reine(1), roi(1), fou(1), cavalier(1), tour(1)]
                        ]
                    root = Tk()
                    root.withdraw()

                    # Ouvre la boîte de dialogue pour choisir un fichier CSV
                    fichier = filedialog.askopenfilename(
                        title="Choisir un fichier CSV de replay",
                        filetypes=[("Fichiers CSV", "*.csv")],
                    )
                    self.replay_content = []
                    with open(fichier, "r") as file:
                        reader = csv.reader(file)
                        next(reader, None)  # Skip l'en-tête
                        for contenu in reader:
                            self.replay_content.append(contenu)
                    print(self.replay_content)

                    self.max_coup = len(self.replay_content)

                if self.nomdevariable[pygame.K_q]:
                    if not self.pressed_left:
                        if not self.nb_counter_arrow <= 0:
                            self.nb_counter_arrow -= 1
                            self.echiquier[int(self.replay_content[self.nb_counter_arrow][1])][int(self.replay_content[self.nb_counter_arrow][0])] = self.echiquier[int(self.replay_content[self.nb_counter_arrow][3])][int(self.replay_content[self.nb_counter_arrow][2])]
                            if self.replay_content[self.nb_counter_arrow][4] == "True":
                                if self.replay_content[self.nb_counter_arrow][5] == "pions":
                                    self.echiquier[int(self.replay_content[self.nb_counter_arrow][3])][int(self.replay_content[self.nb_counter_arrow][2])] = pions(int(self.replay_content[self.nb_counter_arrow][6]))
                                if self.replay_content[self.nb_counter_arrow][5] == "roi":
                                    self.echiquier[int(self.replay_content[self.nb_counter_arrow][3])][int(self.replay_content[self.nb_counter_arrow][2])] = roi(int(self.replay_content[self.nb_counter_arrow][6]))
                                if self.replay_content[self.nb_counter_arrow][5] == "cavalier":
                                    self.echiquier[int(self.replay_content[self.nb_counter_arrow][3])][int(self.replay_content[self.nb_counter_arrow][2])] = cavalier(int(self.replay_content[self.nb_counter_arrow][6]))
                                if self.replay_content[self.nb_counter_arrow][5] == "reine":
                                    self.echiquier[int(self.replay_content[self.nb_counter_arrow][3])][int(self.replay_content[self.nb_counter_arrow][2])] = reine(int(self.replay_content[self.nb_counter_arrow][6]))
                                if self.replay_content[self.nb_counter_arrow][5] == "fou":
                                    self.echiquier[int(self.replay_content[self.nb_counter_arrow][3])][int(self.replay_content[self.nb_counter_arrow][2])] = fou(int(self.replay_content[self.nb_counter_arrow][6]))
                                if self.replay_content[self.nb_counter_arrow][5] == "tour":
                                    self.echiquier[int(self.replay_content[self.nb_counter_arrow][3])][int(self.replay_content[self.nb_counter_arrow][2])] = tour(int(self.replay_content[self.nb_counter_arrow][6]))
                            else:
                                self.echiquier[int(self.replay_content[self.nb_counter_arrow][3])][int(self.replay_content[self.nb_counter_arrow][2])] = 0
                    if not self.nb_counter_arrow <= 0:
                        self.pressed_left = True
                else: self.pressed_left = False

                if self.nomdevariable[pygame.K_d]:
                    if not self.pressed_right:
                        if self.nb_counter_arrow != self.max_coup-1:
                            self.nb_counter_arrow += 1
                            self.echiquier[int(self.replay_content[self.nb_counter_arrow][3])][int(self.replay_content[self.nb_counter_arrow][2])] = self.echiquier[int(self.replay_content[self.nb_counter_arrow][1])][int(self.replay_content[self.nb_counter_arrow][0])]
                            self.echiquier[int(self.replay_content[self.nb_counter_arrow][1])][int(self.replay_content[self.nb_counter_arrow][0])] = 0
                            print(self.replay_content[self.nb_counter_arrow])
                    self.pressed_right = True
                else: self.pressed_right = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                        for score in self.scores:
                            self.writer.writerow(score)

                if self.nomdevariable[pygame.K_DELETE]:
                    self.run = False
                    for score in self.scores:
                        self.writer.writerow(score)
                if self.nomdevariable[pygame.K_ESCAPE]:
                    self.menu = True
                    self.Replaying = False
                    self.replay_content = 0

        if self.menu:
            for event in pygame.event.get():
                if 3 * 100 <= pygame.mouse.get_pos()[0] <= 5 * 100 and 3 * 100 <= pygame.mouse.get_pos()[1] <= 5 * 100:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.menu = False
                        self.Replaying = False
                        self.initialisation()

                if 3 * 100 <= pygame.mouse.get_pos()[0] <= 5 * 100 <= pygame.mouse.get_pos()[1] <= 6 * 100:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.menu = False
                        self.Replaying = True

                if event.type == pygame.QUIT:
                    self.run = False
                    for score in self.scores:
                        self.writer.writerow(score)

                if self.nomdevariable[pygame.K_DELETE]:
                    self.run = False
                    for score in self.scores:
                        self.writer.writerow(score)

    def main_loop (self):
        while self.run:

            self.inputs()
            self.affichage()

    def maximum(self, liste,indice):
        # donne le chiffre le plus grand dans une liste
        maxi = int(liste[0][indice])
        for i in liste:
            if int(i[indice]) >= int(maxi):
                maxi = i[indice]
        return maxi


    def affichage(self):
        pygame.display.flip()
        self.screen.fill((0,0,0))

        violette = (113 ,109, 166)
        violette_claire = (151, 147, 198)
        selec_color = (171, 167, 218)

        for y in range(8):
            for x in range(8):
                if y % 2 == 0:
                    if x % 2 == 0:
                        if self.dep_pion_poss[y][x][0] and self.select_pion[0]:
                            pygame.draw.rect(self.screen, selec_color, (
                                x * (self.width / 8) + 2, y * (self.height / 8) + 2, self.width / 8 - 2,
                                self.height / 8 - 2
                            ))
                        else:
                            pygame.draw.rect(self.screen,violette,(
                            x*(self.width/8)+2,y*(self.height/8)+2,self.width/8-2,self.height/8-2
                        ))
                    else:
                        if self.dep_pion_poss[y][x][0] and self.select_pion[0]:
                            pygame.draw.rect(self.screen, selec_color, (
                                x * (self.width / 8) + 2, y * (self.height / 8) + 2, self.width / 8 - 2,
                                self.height / 8 - 2
                            ))
                        else:
                            pygame.draw.rect(self.screen, violette_claire, (
                            x * (self.width / 8) + 2, y * (self.height / 8) + 2, self.width / 8 - 2, self.height / 8 - 2
                        ))
                else:
                    if x % 2 == 0:
                        if self.dep_pion_poss[y][x][0] and self.select_pion[0]:
                            pygame.draw.rect(self.screen, selec_color, (
                                x * (self.width / 8) + 2, y * (self.height / 8) + 2, self.width / 8 - 2,
                                self.height / 8 - 2
                            ))
                        else:
                            pygame.draw.rect(self.screen,violette_claire,(
                            x*(self.width/8)+2,y*(self.height/8)+2,self.width/8-2,self.height/8-2
                        ))
                    else:
                        if self.dep_pion_poss[y][x][0] and self.select_pion[0]:
                            pygame.draw.rect(self.screen, selec_color, (
                                x * (self.width / 8) + 2, y * (self.height / 8) + 2, self.width / 8 - 2,
                                self.height / 8 - 2
                            ))
                        else:
                            pygame.draw.rect(self.screen, violette, (
                            x * (self.width / 8) + 2, y * (self.height / 8) + 2, self.width / 8 - 2, self.height / 8 - 2
                        ))
                if self.echiquier[y][x] != 0:
                    self.screen.blit(self.echiquier[y][x].obtenir_img(),(x*100,y*100))
        if self.menu:
            try:
                max_blanc = self.maximum(self.scores,0)
                max_noir = self.maximum(self.scores,1)
            except:
                if self.scores != []:
                    print(self.scores)
                    max_blanc = self.maximum(self.scores, 0)
                    max_noir = self.maximum(self.scores, 1)
                else:
                    max_blanc = 0
                    max_noir = 0
            self.screen.blit(self.img_play_button, (3 * 100, 3 * 100))
            replay_surface = self.font.render("REPLAY ", True, (148, 241, 164))
            replay_position = (305, 525)
            score_white_surface = self.font.render(f"Best White Score: {max_blanc}", True, (255, 255, 255))
            score_white_position = (0, 0)
            score_black_surface = self.font.render(f"Best Black Score: {max_noir}", True, (255, 255, 255))
            score_black_position = (0, 100)

            self.screen.blit(score_white_surface, score_white_position)
            self.screen.blit(score_black_surface, score_black_position)
            self.screen.blit(replay_surface, replay_position)

pygame.init()

Main_chess = game_chess()
Main_chess.main_loop()

pygame.quit()