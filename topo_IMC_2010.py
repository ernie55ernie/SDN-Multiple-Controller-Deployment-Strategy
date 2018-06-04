from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import RemoteController#OVSController
from mininet.cli import CLI

topo_file = 'topology/unv1.cdp.txt'

class IMCTopo(Topo):
	def __init__(self, **opts):
		Topo.__init__(self, **opts)

		self.switch_names = {}

		# columns of topology file:
		#  source_device 
		#  source_interface 
		#  destination_device 
		#  destination_interface
		with open(topo_file, 'r') as f:
			for line in f:
				list_of_line = line.split()
				source_device, source_interface, destination_device, destination_interface = list_of_line[0], list_of_line[1], list_of_line[2], list_of_line[3]
				print(source_device, source_interface, destination_device, destination_interface)
				if source_device not in self.switch_names:
					source_switch = self.addSwitch(source_device)
					self.switch_names[source_device] = source_switch
				else:
					source_switch = self.switch_names[source_device]

				if destination_device not in self.switch_names:
					destination_switch = self.addSwitch(destination_device)
					self.switch_names[destination_device] = destination_switch
				else:
					destination_switch = self.switch_names[destination_device]

				self.addLink(source_switch, destination_switch)#, intfName1 = source_interface, intfName2 = destination_interface) # wan mesh

		h0 = self.addHost('h0')
		h1 = self.addHost('h1')
		self.addLink(h0, destination_switch)
		self.addLink(h1, destination_switch)

if __name__ == '__main__':
	setLogLevel('info')

	# calculate where to deploy controllers

	topo = IMCTopo()
	net = Mininet(topo = topo, link = TCLink, autoSetMacs = True, autoStaticArp = True)
	net.addController('c0', controller = RemoteController, ip = '10.0.0.1')

	net.start()

	CLI(net)

	net.stop()
