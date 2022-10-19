from downloads import get_curseforge_downloads, get_modrinth_downloads


class ModData:
    name: str
    curseforge_id: str
    curseforge_downloads: int
    modrinth_id: str
    modrinth_downloads: int

    def __init__(
            self,
            name: str,
            curseforge_id: str,
            modrinth_id: str,
    ):
        self.name = name
        self.curseforge_id = curseforge_id
        self.modrinth_id = modrinth_id

        self.curseforge_downloads = get_curseforge_downloads(curseforge_id)
        self.modrinth_downloads = get_modrinth_downloads(modrinth_id)
