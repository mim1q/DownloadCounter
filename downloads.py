import urllib.request
from urllib.request import urlopen
import json

CURSEFORGE_PREFIX = "https://api.cfwidget.com/"
MODRINTH_PREFIX = "https://api.modrinth.com/v2/project/"


def get_modrinth_downloads(mod_id: str) -> int:
    url = MODRINTH_PREFIX + mod_id
    with urlopen(url) as response:
        data = json.loads(response.read())
        return data["downloads"]


def get_curseforge_downloads(mod_id: str) -> int:
    url = CURSEFORGE_PREFIX + mod_id

    # Workaround for CFWidget
    user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
    headers = {"User-Agent": user_agent, }

    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read())

    return data["downloads"]["total"]

