from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from osuapi import OsuApi, ReqConnector
import requests
from pprint import pprint

# Easy way to test card designs
osuapi = OsuApi("your key", connector=ReqConnector())

rank = "C"


def create_card(map_id=131891):
    raw = "Hidden spunout nofail"
    score_mods = raw.split(" ")

    card_name = f"{map_id}{discord_id}"
    map_object = osuapi.get_beatmaps(mode=0, beatmap_id=map_id, limit=30)[0]
    response = requests.get(f"https://assets.ppy.sh/beatmaps/{map_object.beatmapset_id}/covers/cover.jpg")
    pprint("Grabbed map image")
    file = open(f"cards/{card_name}.png", "wb")
    file.write(response.content)
    file.close()
    img = Image.open(f"cards/{card_name}.png")
    img2 = Image.open(f"bace/cardbace{rank}.png")
    img2.paste(img, (15,55))
    draw = ImageDraw.Draw(img2)
    font = ImageFont.truetype("font/Exo2.0-Regular.otf", 24)
    combo_font = ImageFont.truetype("font/Overpass-Regular.ttf", 70)
    Score_font = ImageFont.truetype("font/Overpass-Regular.ttf", 60)
    pprint("Opened resources")

    draw.text((658, 320), f"Obtained by BrandonH", (0, 0, 0), font=font)  # name
    draw.text((390, 320), f"ACC", (0, 0, 0), font=font)  # ACC
    draw.text((483, 320), f"SSS", (0, 0, 0), font=font)  # SSS
    draw.text((20,10), f"{map_object.title}", (0, 0, 0), font=font)# Title
    draw.text((900, 10), f"{map_object.version}", (0, 0, 0), font=font, anchor="ra")# difficulty
    draw.text((25, 320), f"AR: {round(map_object.diff_approach)}", (0, 0, 0), font=font)  # ar
    draw.text((116, 320), f"CS: {round(map_object.diff_size)}", (0, 0, 0), font=font)  # cs
    draw.text((206, 320), f"OD: {round(map_object.diff_overall)}", (0, 0, 0), font=font)  # od
    draw.text((296, 320), f"HP: {round(map_object.diff_drain)}", (0, 0, 0), font=font)  # HP
    draw.text((576, 320), f"{round(map_object.difficultyrating,2)}", (0, 0, 0), font=font)  # star
    draw.text((140, 245), f"1000x", (0, 0, 0), font=combo_font,stroke_width=4, stroke_fill=(240,240,240), anchor="ma")  # Combo
    draw.text((30, 70), f"1,100,000", (0, 0, 0), font=Score_font, stroke_width=2, stroke_fill=(240, 240, 240))  # Combo

    for i, mods in enumerate(score_mods):
        pprint(mods.lower())
        try:
            mod_image = Image.open(f"mods/{mods.lower()}.png")
            img2.paste(mod_image, ((810- (45 * i) ,70)), mod_image)
            pprint("Success")
        except:
            pass


    rank_image = Image.open(f"rank/{rank}.png")
    img2.paste(rank_image, (810,180), mask = rank_image)
    img2.save(f'cards/{card_name}.png')


    return card_name

create_card(0, 1145198)