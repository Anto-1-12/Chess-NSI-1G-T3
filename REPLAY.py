import csv
import datetime
import os
import time

class Replay:
    def __init__(self):
        os.makedirs("file/replay", exist_ok=True)
        self.date = str(datetime.date.today())+","+str(time.time())
        file = open("file/replay/replay_"+self.date+".csv", "w", newline="")
        self.writer = csv.writer(file)
        self.writer.writerow(["x_deb","y_deb","x_fin","y_fin","is_eating","type_of_pion","color"])
        self.coup_joue = []


    def main(self,coup_a_sauvegarder):
        self.coup_joue.append(coup_a_sauvegarder)
        print(coup_a_sauvegarder)

    def end_replay(self):
        for coup in self.coup_joue:
            self.writer.writerow(coup)
        print(self.coup_joue)

    def get_name(self):
        return "file/replay/replay_"+self.date+".csv"