import json

import json_output
from create_svg import create_and_write_svg
from mod_data import ModData


def load_mods_from_json(filename: str) -> list[ModData]:
    with open(filename) as f:
        data = json.load(f)
        return [ModData(**mod) for mod in data["mods"]]


def main():
    mods = load_mods_from_json("data/mods.json")
    total_downloads = 0
    for mod in mods:
        total_downloads += mod.curseforge_downloads + mod.modrinth_downloads
        create_and_write_svg(
            "output/" + mod.modrinth_id + ".svg",
            mod.curseforge_downloads + mod.modrinth_downloads
        )
        create_and_write_svg(
            "output/" + mod.modrinth_id + "-dark.svg",
            mod.curseforge_downloads + mod.modrinth_downloads,
            dark_mode=True
        )

    create_and_write_svg("output/total.svg", total_downloads)
    create_and_write_svg("output/total-dark.svg", total_downloads, dark_mode=True)
    with open("output/mods.json", "w") as output:
        output.write(json_output.create_json_output(mods))


if __name__ == "__main__":
    main()
