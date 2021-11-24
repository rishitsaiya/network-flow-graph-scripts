"""
We tried the following example where we tried to include the
Attacker Blacklisted IP address in the hosts array. The script
for the same is as follows:
"""
# !/usr/bin/env python3
from scapy.all import *
hosts = ["<dst IP>"]
res,unans = traceroute(hosts)
res.graph(target="> traceroute_graph.svg")