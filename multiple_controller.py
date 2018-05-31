from __future__ import print_function

from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_3

class MultipleController(app_mananger.RyuApp):
	OFP_VERSIONS =[ofproto_v1_3.OFP_VERSION]

	def __init__(self, *args, **kwargs):
		super(MultipleController, self).__init__(*args, **kwargs)
		