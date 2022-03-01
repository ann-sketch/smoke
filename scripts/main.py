from requests import get
from utils import prepare_values
from home import home
from ovrall_gt_80 import ovrall_gt_80

data = prepare_values(get("https://www.sonic-sports.eu/clients/sonic/apps/sonicai3/appApi.php").json())

if (__name__ == "__main__"):
    home(data)
    ovrall_gt_80(data)
