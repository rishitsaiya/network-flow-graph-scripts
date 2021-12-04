"""
Proceeding over the same idea, we just glanced over some
techniques to get some holistic idea of blacklisted IPs. We
developed a simple python script which would give a graph
diagram to get more idea on how those Blacklisted IPs/subnets
are connected over to DNS servers.
"""

# !/usr/bin/env python3
from scapy.all import *
hosts = ["<host 1>", "<host 2>", ...]
res,unans = traceroute(hosts)
res.graph(target="> traceroute_graph.svg")