from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')
        for h in range(1, 4):
            host = self.addHost(f'h{h}')
            self.addLink(host, switch)

def run():
    net = Mininet(topo=SingleSwitchTopo(), controller=lambda name: RemoteController(name, ip='127.0.0.1'))
    net.start()
    print("Network is running. Use 'pingall' to test connectivity.")
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()