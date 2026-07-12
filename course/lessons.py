import json
import os

_dir = os.path.dirname(os.path.abspath(__file__))
_data_path = os.path.join(_dir, 'data.json')

def _load():
    with open(_data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['part1'], data['part2']

PART1_PSEUDOCODE, PART2_PYTHON = _load()
