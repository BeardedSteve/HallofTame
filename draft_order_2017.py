import random

import time

TEAMS = [
    "Gisele's Brazilian",
    "RubberMuffins17",
    "The Random Chance",
    "Watto's Winners",
    "what_is_going_on",
    "Sheffield Sabres",
    "The Bearded Keane's",
    "The Hulkamaniacs",
    "GONZO FOOTBALL",
    "West coast offence",
    "No luck no judgement",
    "Team 12"
]

RUNNERS = [
    (4081, "Sheila Chepkirui KIPROTICH"),
    (3703, "Kalkidan GEZAHEGNE"),
    (4343, "Molly HUDDLE"),
    (3845, "Letesenbet GIDEY"),
    (3898, "Eilish MCCOLGAN"),
    (4080, "Margaret Chelimo KIPKEMBOI"),
    (4127, "Sifan HASSAN"),
    (4086, "Hellen Onsando OBIRI"),
    (3900, "Laura MUIR"),
    (4153, "Karoline Bjerkeli GRØVDAL"),
    (4366, "Shannon ROWBURY"),
    (3849, "Senbere TEFERI"),
    (4342, "Shelby HOULIHAN"),
    (4130, "Susan KRUMINS"),
    (3839, "Almaz AYANA")
]

assert (len(RUNNERS) > len(TEAMS)) and (len(TEAMS) == 12)
random.shuffle(RUNNERS)
random.shuffle(TEAMS)
with open("2017_runner.txt", "w") as f:
    for team in TEAMS:
        time.sleep(random.randint(1, 5))
        bib, runner = RUNNERS.pop()
        selection = "{:<30} {:<30} (bib {})".format(team, runner, bib)
        f.write(selection + "\n")
        print(selection)
