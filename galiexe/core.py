# abhaya/gali.py

import random

def galiexe():
    gali_list = [
        "Machikne",
        "Randi",
        "Randa",
        "Baal",
        "Gadha",
        "Khopdi",
        "Kutu",
        "Bhuddu",
        "Harayo",
        "Tarkari",
        "Jhatkaa",
        "Bhari",
        "Khatti",
        "Dhaago"
    ]
    return random.choice(gali_list)

if __name__ == "__main__":
    gali_list = [
        "Machikne",
        "Randi",
        "Randa",
        "Baal",
        "Gadha",
        "Khopdi",
        "Kutu",
        "Bhuddu",
        "Harayo",
        "Tarkari",
        "Jhatkaa",
        "Bhari",
        "Khatti",
        "Dhaago"
    ]
    print("All Gali List:")
    for gali in gali_list:
        print(gali)
