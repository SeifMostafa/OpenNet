#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Node, Switch, RemoteController
from mininet.link import Link, Intf
from mininet.log import setLogLevel, info
from mininet.cli import CLI

import mininet.ns3
from mininet.ns3 import WifiSegment

import ns.core
import ns.network
import ns.wifi
import ns.csma
import ns.wimax
import ns.uan
import ns.netanim

from mininet.opennet import *

def main():

    net = Mininet()
    net.addController('c0', controller=RemoteController, ip="127.0.0.1", port=6633)

    wifi = WifiSegment()

    # About AP
    ap0 = net.addAP("ap0", wifi, channelNumber=6, ssid="opennet_ap", positions=(0, 0, 0))

    # Check mininet.node.AP
    if isinstance(ap0, mininet.node.AP):
        print("I'm a AP")

    # About Station
    sta0 = net.addStation("sta0", wifi, channelNumber=6, ssid="opennet_ap", positions=(0, 0, 0))

    #Check mininet.node.Station
    if isinstance(sta0, mininet.node.Station):
        print("I'm a station")

    print("APs list: {0}\nSTAs list: {1}\n".format(wifi.aps, wifi.stas))

    # About OVSSwitch
    s0 = net.addSwitch('s0')

    # About Host
    h0 = net.addHost('h0', ip="1.1.1.1")

    # Ignore warning message: "defaultIntf: warning: h0 has no interfaces"
    net.addLink(s0, h0)

    print("Switches list: {0}\nHosts list: {1}\n".format(net.switches, net.hosts))

    mininet.ns3.start()
    net.start()
    CLI(net)
    mininet.ns3.stop()
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    main()
