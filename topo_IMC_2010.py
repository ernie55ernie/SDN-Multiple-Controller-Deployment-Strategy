from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import OVSController
from mininet.cli import CLI

topo_file = 'topology/uv1.cdp.txt'

class IMCTopo(Topo):
	def __init__(self, **opts):
		Topo.__init__(self, **opts)

		self.switches = {}

		# columns of topology file:
		#  source_device 
		#  source_interface 
		#  destination_device 
		#  destination_interface
		with open(topo_file, 'r') as f:
			for line in f:
				list_of_line = line.split()
				source_device, source_interface, destination_device, destination_interface = list_of_line[0], list_of_line[1], list_of_line[2], list_of_line[3]
				
				if source_device not in self.switches:
					source_switch = self.addSwitch(source_device)
				else:
					source_switch = self.switches[source_device]

				if destination_device not in self.switches:
					destination_switch = self.addSwitch(destination_device)
				else:
					destination_switch = self.switches[destination_deivce]

				self.addLink(source_switch, destination_switch, source_interface, destination_interface)

if __name__ == '__main__':
	setLogLevel('info')

	topo = IMCTopo()
	net = Mininet(topo = topo, link = TCLink, autoSetMacs = True, autoStaticArp = True, controller = OVSController)

	net.start()

	CLI(net)

	net.stop()
