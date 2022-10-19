import json

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

    print(f"Total downloads: {total_downloads}")


if __name__ == "__main__":
    main()
