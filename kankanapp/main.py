
"""
 scp -r kan-kan-dir/* root@172.105.158.108:/home/desktop/flaskappsdir/kankanapp
===============================
	MAPEI WRITTING  SCRIPTS
===============================
"""

from write_to_db.mapei.adesilexp7 import *
from write_to_db.mapei.planiseal_grey import *
from write_to_db.mapei.planiseal_liquid import *
from write_to_db.mapei.plastimul_dpm import *
from write_to_db.mapei.keracolor import *



"""
================================
	AGENCY WRITTING  SCRIPTS
================================
"""


from write_to_db.agency.agency import *

"""
================================
	NAMES WRTING  SCRIPTS
================================
"""
from write_to_db.names.staffs import *
from write_to_db.names.sadolin import *
from write_to_db.names.mapei import *
from write_to_db.names.chint_names import *

"""
====================================
	CHINT NAMES READING  SCRIPTS
====================================
"""

from write_to_db.chint.mcb_1p import *
from write_to_db.chint.mcb_2p import *
from write_to_db.chint.mcb_3p import *
from write_to_db.chint.mcb_4p import *
from write_to_db.chint.led_panel import *
from write_to_db.chint.led_ceiling import *
from write_to_db.chint.led_flood import *
from write_to_db.chint.led_bulbs import *
from write_to_db.chint.mccb import *
from write_to_db.chint.main_switch import *
from write_to_db.chint.cables import *
from write_to_db.chint.contactor import *
from write_to_db.chint.industrial import *
from write_to_db.chint.gold import *
from write_to_db.chint.white import *
from write_to_db.chint.silver import *


"""
=================================
	SADOLIN WRITTING  SCRIPTS
=================================
"""

from write_to_db.sadolin.budget_gloss import *
from write_to_db.sadolin.silk import *
from write_to_db.sadolin.super import *
from write_to_db.sadolin.undercoat import *
from write_to_db.sadolin.weather import *
from write_to_db.sadolin.emulsion import *
from write_to_db.sadolin.matt import *

from write_to_db.sadolin.thinner import *
from write_to_db.sadolin.road_marking import *
from write_to_db.sadolin.wall_guard import *
from write_to_db.sadolin.roof_guard import *
from write_to_db.sadolin.rainshild import *
from write_to_db.sadolin.dampshild import *
from write_to_db.sadolin.clear_varnish import *
from write_to_db.sadolin.colour_varnish import *
from write_to_db.sadolin.ceilling import *
# bases
from write_to_db.sadolin.base_silk import *
from write_to_db.sadolin.base_super import *
from write_to_db.sadolin.base_weather import *



"""
===============================
	MAPEI WRITTING  SCRIPTS
===============================
"""

from read_from_db.mapei.adesilexp7 import *
from read_from_db.mapei.planiseal_grey import *
from read_from_db.mapei.planiseal_liquid import *
from read_from_db.mapei.plastimul_dpm import *
from read_from_db.mapei.keracolor import *

"""
===============================
	NAME READING  SCRIPTS
===============================
"""
from read_from_db.agency.agency import *
from read_from_db.names.staffs import *
from read_from_db.names.sadolin import *
from read_from_db.names.mapei import *
from read_from_db.names.ChintNames import *


"""
================================
	SADOLIN READING  SCRIPTS
================================
"""
from read_from_db.sadolin.emulsion import *
from read_from_db.sadolin.matt import *
from read_from_db.sadolin.budget_gloss import *
from read_from_db.sadolin.silk import *
from read_from_db.sadolin.super import *
from read_from_db.sadolin.undercoat import *
from read_from_db.sadolin.weather import *

from read_from_db.sadolin.ceilling import *
from read_from_db.sadolin.colour_varnish import *
from read_from_db.sadolin.clear_varnish import *
from read_from_db.sadolin.dampshild import *
from read_from_db.sadolin.rainshild import *
from read_from_db.sadolin.roofguard import *
from read_from_db.sadolin.wallguard import *
from read_from_db.sadolin.roadmarking import *
from read_from_db.sadolin.thinner import *

# bases
from read_from_db.sadolin.base_silk import *
from read_from_db.sadolin.base_super import *
from read_from_db.sadolin.base_weather import *


"""
====================================
	CHINT NAMES READING  SCRIPTS
====================================
"""

from read_from_db.chint.mcb1p import *
from read_from_db.chint.mcb2p import *
from read_from_db.chint.mcb3p import *
from read_from_db.chint.mcb4p import *
from read_from_db.chint.mccb import *
from read_from_db.chint.bulbs import *
from read_from_db.chint.cables import *
from read_from_db.chint.ceilling import *
from read_from_db.chint.contactor import *
from read_from_db.chint.flood import *
from read_from_db.chint.mainSwitch import *
from read_from_db.chint.surface import *

"""
============================
	CHINT ADMIN  SCRIPTS
============================
"""

from admin.admin import *


if __name__=="__main__":
	# app.debug=1
	# app.run()
	app.run('0.0.0.0', 4444, threaded=1)

#++++++++++++++++++++
