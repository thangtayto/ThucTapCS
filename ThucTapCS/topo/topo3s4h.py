from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        "Create custom topo."
        Topo.__init__(self)
        
        # add host
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # add switch
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # add connections
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s2, h1)
        self.addLink(s2, h2)
        self.addLink(s3, h3)
        self.addLink(s3, h4)

topos = {'tp': (lambda: MyTopo())}