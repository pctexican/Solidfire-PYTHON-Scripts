(venv)piops@cldadm-wc-a01:~/SF/venv$ cat listqos.py
#!/usr/bin/env python
# Solidfire Storage python script to list qos values for all volumes
# Paul Clifton
# February 10, 2017

from solidfire import Element
import argparse
import re
import logging
from solidfire import common

common.setLogLevel(logging.ERROR)

parser = argparse.ArgumentParser(description='List QoS on volumes.')

parser.add_argument('cluster', help='SolidFire cluster to act on')
parser.add_argument('username', help='Cluster admin login to use')
parser.add_argument('password', help='Cluster admin password')
args = parser.parse_args()

sf = Element(args.cluster, args.username, args.password, '7.0', verify_ssl=False)

result = sf.list_active_volumes()

for volume in result.volumes:
    print volume.volume_id,
    print volume.name,
    qos = volume.qos
    print 'minIOPS: ', qos.min_iops,
    print 'maxIOPS: ', qos.max_iops,
    print 'burstIOPS: ', qos.burst_iops
