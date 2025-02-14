from ..functions import createFolder
from ..functions import writeJsonContent

def setupAllThings():
    createFolder("Json")
    writeJsonContent("Json/INEXJD.json", {"tables": {}})
