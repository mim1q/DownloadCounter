import json

from mod_data import ModData


def create_json_output(mods: [ModData]) -> str:
    total_dl = sum(mod.curseforge_downloads + mod.modrinth_downloads for mod in mods)
    output = {
        'total_downloads': total_dl,
        'mods': [{
            'name': mod.name,
            'curseforge_id': mod.curseforge_id,
            'modrinth_id': mod.modrinth_id,
            'curseforge_downloads': mod.curseforge_downloads,
            'modrinth_downloads': mod.modrinth_downloads,
            'downloads': mod.modrinth_downloads + mod.curseforge_downloads
        } for mod in mods]
    }
    return json.dumps(output, indent=2)

