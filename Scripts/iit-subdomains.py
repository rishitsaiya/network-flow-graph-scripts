"""
We also tried following example of sub domains under IIT
Dharwad to get to know about incoming traffic and its sources
among various Internet Service providers and their DNS
servers.
"""

# !/usr/bin/env python3
from scapy.all import *
hosts = ["moodle.iitdh.ac.in",
"iitdh.ac.in", "smp.iitdh.ac.in",
"cdc.iitdh.ac.in", "gitea.iitdh.ac.in"]
res,unans = traceroute(hosts)
res.graph(target="> traceroute_graph.svg")