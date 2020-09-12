import pandas as pd
from Bryggelogg.models import Bryggelogg

def avg_liter():
    get_data = Bryggelogg.objects.all()
    tot_volume = get.data.sluttvolum
    avg = tot_volume.mean()

    return avg
