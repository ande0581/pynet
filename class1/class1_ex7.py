#!/usr/bin/env python
import yaml
import json
from pprint import pprint as pp

# open json file
with open("my_json_file.json") as f:
    json_list = json.load(f)

# open yaml file
with open("my_yaml_file.yml", "r") as f:
    yaml_list = yaml.load(f)


print "JSON:"
print pp(json_list)


print "YAML:"
print pp(yaml_list)
