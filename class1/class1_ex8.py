#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_maps = cisco_cfg.find_objects(r"crypto map CRYPTO")

for i in crypto_maps:
    print i.text
    for child in i.children:
        print child.text
