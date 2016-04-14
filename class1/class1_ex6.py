#!/usr/bin/env python
import yaml
import json

my_list = [1, 2, 3, 4, 5, 6, 7, 8, "Firewall", "Router", "Switch", {"network": "10.11.12.1", "subnet": "255.255.255.0",
                                                                    "gateway": "10.11.12.1"}, {"Model": "WS3560",
                                                                                               "Vendor": "Cisco"}]

# Write YAML file
with open("my_yaml_file.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

# Write JSON file
with open("my_json_file.json", "w") as f:
    json.dump(my_list, f)
