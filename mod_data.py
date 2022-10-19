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

        self.curseforge_downloads = self.get_curseforge_downloads()
        self.modrinth_downloads = self.get_modrinth_downloads()

    def get_curseforge_downloads(self) -> int:
        return 0

    def get_modrinth_downloads(self) -> int:
        return 0
