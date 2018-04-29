from flask import Flask
import json
from flask import Blueprint

app = Flask(__name__)
bp = Blueprint('v2ray', __name__, subdomain='v2ray')


@bp.route('/biforstv/<cfg_name>')
def bfv(cfg_name):
    try:
        with open("config.json", 'r') as load_f:
            load_dict = json.load(load_f)
            return load_dict["bfv"][cfg_name]
    except:
        return "No This Config!"


@bp.route('/v2rayn/<cfg_name>')
def v2r(cfg_name):
    try:
        with open("config.json", 'r') as load_f:
            load_dict = json.load(load_f)
            return load_dict["v2rayn"][cfg_name]
    except:
        return "No This Config!"


app.register_blueprint(bp)
app.config.update({
    'SERVER_NAME':'artrix.tech'
})
app.run(host="**.**.**.**", port=80)
