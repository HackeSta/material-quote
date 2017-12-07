import json
import random
import os
def get_random_color():
    dir = os.path.dirname(__file__)

    colors = json.load(open(os.path.join(dir,'data/material-colors.json')))
    color = random.choice(list(colors.keys()))
    return colors[color]['500']