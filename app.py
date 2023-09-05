import json
import random
import subprocess
from PIL import Image, ImageSequence

bg_gif_names = ["Dark Net", "Dark Sky", "Flare Orbs", "Gradient Waves", "Lava", "Songbird Surge", "Stars", "Time Travel", "Trip", "Vortex"]
IMG_APES = 75
FRM_SIZE = (631, 631)

def output_ape_gif(bg_num, ape_num):
    gif_bg = Image.open('assets/gifbgs/' + bg_gif_names[bg_num] + '.gif')
    png_ape = Image.open('assets/pngapes/' + str(ape_num) + '.png')
    frames = [f.copy() for f in ImageSequence.Iterator(gif_bg)]
    gif_ape = []
    for frame in frames:
        frame2 = frame.resize(FRM_SIZE)
        frame2.paste(png_ape, (0, 0), mask = png_ape)
        gif_ape.append(frame2)
    gif_ape[1].save(
        'outputs/gifapes/' + str(ape_num) + '.gif',
        save_all = True,
        append_images = gif_ape[1:],
        loop = 0
    )
    print("Finished Ape No : " + str(ape_num))
    return

def update_ape_json(bg_num, ape_num):
    with open('assets/apesjson/' + str(ape_num) + '.json', 'r') as ape_json_file:
        file_contents = ape_json_file.read()
    parsed_json = json.loads(file_contents)
    parsed_json["attributes"][0]["value"] = bg_gif_names[bg_num]
    dumped_json = json.dumps(parsed_json, indent=2)

    with open('outputs/jsonapes/' + str(ape_num) + '.json', 'w') as ape_json_file2:
        ape_json_file2.write(dumped_json)
    return

def compress_ape_gif(ape_num):
    subprocess.run(['gifsicle/gifsicle', '-O2', '--lossy=80', 'outputs/gifapes/' + str(ape_num) + '.gif', '-o', 'outputs/gifapes-comp/' + str(ape_num) + '.gif'])

def create_ape_gifs():
    for k in range(IMG_APES):
        # rnd_bg = random.randint(0, 9)
        # output_ape_gif(rnd_bg, k + 1)
        # update_ape_json(rnd_bg, k + 1)
        compress_ape_gif(k + 1)
    return

create_ape_gifs()