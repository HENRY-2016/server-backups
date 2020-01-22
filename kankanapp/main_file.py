
print " "
print " "

print "\t==============================="
print "\tBEGIN ::: Initializing db models"
print "\t================================"
print " "

#===========================
# MAPEI DATA BASE MODELS
# ==========================

from db_models.mapei.adesilexP7 import *
from db_models.mapei.planiseal_grey import *
from db_models.mapei.planiseal_liquid import *
from db_models.mapei.plastimul_dpm import *
from db_models.mapei.keracolor import *


#===========================
# CHINT DATA BASE MODELS
# ==========================
from db_models.chint.mcb_1p import *
from db_models.chint.mcb_2p import *
from db_models.chint.mcb_3p import *
from db_models.chint.mcb_4p import *
from db_models.chint.mccb import *

from db_models.chint.led_bulbs import *
from db_models.chint.led_flood import *
from db_models.chint.led_ceiling import *
from db_models.chint.led_panel import *
from db_models.chint.contactor import *
from db_models.chint.cables import *
from db_models.chint.main_switch import *

from db_models.chint.gold import *
from db_models.chint.white import *
from db_models.chint.silver import *
from db_models.chint.industrial import *

#===========================
# SADOLIN DATA BASE MODELS
# ==========================
print " "
from db_models.sadolin.budget_gloss import *
from db_models.sadolin.silk import *
from db_models.sadolin.undercoat import *
from db_models.sadolin.super import *
from db_models.sadolin.weather import *
from db_models.sadolin.matt import *
from db_models.sadolin.emulsion import *
print " "
from db_models.sadolin.thinner import *
from db_models.sadolin.road_marking import *
from db_models.sadolin.wall_guard import *
from db_models.sadolin.roof_guard import *
from db_models.sadolin.rainshild import *
from db_models.sadolin.dampshild import * 
from db_models.sadolin.clear_varnish import *
from db_models.sadolin.colour_varnish import *
from db_models.sadolin.ceilling import *


# bases
print " "
from db_models.sadolin.base_silk import *
from db_models.sadolin.base_weather import *
from db_models.sadolin.base_super import *

"""
#=========================
# AGENCY DATA BASE MODELS
# ========================
"""
print " "
from db_models.agency.agency import *

"""
#=========================
# NAMES DATA BASE MODELS
# ========================
"""
from db_models.names.staffs import *
from db_models.names.sadolin import *
from db_models.names.mapei import *
from db_models.names.chint_names import *



print "\t=============================="
print "\tEND ::: Initializing db models"
print "\t=============================="

from flask import request, Flask
from flask import render_template, Response
import json
from sqlalchemy import and_



app = Flask(__name__)
""" key  """
app.config['SECRET_KEY'] = 'kankan'


def allow_cross_origin (reply):
    response = Response(reply)
    response.headers["Access-Control-Allow-Origin"] = "*" # allow all domains...
    return response

