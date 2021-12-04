# Network Flow Graph Scripts

We generated some fake packets which do not belong to conventional internet traffic but obey standard protocols like TCP, UDP, etc. We later went on to detect those newly added packets in systems connected under same LAN. Now, as a priority to keep your system safe (Mitigation Technique), we used the technique of Blacklisting those subnets which can pose a potential threat to all the system which are connected under same LAN. Now, in this section, we propose some basic Reconnaissance over the Blacklisted IPs obtained above.

## Network Reconnaissance on Blacklists

1. Proceeding over the same idea, we just glanced over some techniques to get some holistic idea of blacklisted IPs. We developed a simple python script which would give a graph diagram to get more idea on how those Blacklisted IPs/subnets are connected over to DNS servers. The following script is mentioned in [blacklist-subnet-connection.py](https://github.com/nikunjpansari/network-flow-graph-scripts/tree/main/Scripts/blacklist-subnet-connection.py) <br>
*Steps to run:* `python3 blacklist-subnet-connection.py`

2. We tried the following example where we tried to include the Attacker Blacklisted IP address in the hosts array. The following script is mentioned in [destination_ip.py](https://github.com/nikunjpansari/network-flow-graph-scripts/tree/main/Scripts/destination_ip.py) <br>
*Steps to run:* `python3 destination_ip.py`

3. We also tried following example of sub domains under IIT Dharwad to get to know about incoming traffic and its sources among various Internet Service providers and their DNS servers. The following script is mentioned in [iit-subdomains.py](https://github.com/nikunjpansari/network-flow-graph-scripts/tree/main/Scripts/iit-subdomains.py) <br>
*Steps to run:* `python3 iit-subdomains.py`
