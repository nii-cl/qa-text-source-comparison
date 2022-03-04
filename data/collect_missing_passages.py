import csv
import glob
import json

source_path = 'data/release_data.json'
target_path = 'data/complete_data.json'

mctest_path = 'data/mctest'
race_path = 'data/race'
reclor_path = 'data/reclor'

def read_mctest_data():
    if glob.glob(f"{mctest_path}/mc500.train.tsv") == []:
        print(f"put `mc{160,500}.train.tsv` in {mctest_path}")
        exit(1)
    if glob.glob(f"{mctest_path}/mc160.train.tsv") == []:
        print(f"put `mc{160,500}.train.tsv` in {mctest_path}")
        exit(1)
    items  = {}
    with open(f'{mctest_path}/mc160.train.tsv') as f:
        for row in csv.reader(f, delimiter='\t'):
            items[row[0]] = row[2]
    with open(f'{mctest_path}/mc500.train.tsv') as f:
        for row in csv.reader(f, delimiter='\t'):
            items[row[0]] = row[2]
    return items


def read_race_data():
    if glob.glob("data/race/train/*") == []:
        print(f"put `train` directory in {race_path}")
        exit(1)
    items = {}
    for filepath in glob.glob("data/race/train/*/*.txt"):
        with open(filepath) as f:
            data = json.load(f)
            pas_id = '/'.join(filepath.split('/')[2:])
            items[f'race/{pas_id}'] = data['article']
    return items


def read_reclor_data():
    if glob.glob("data/reclor/train.json") == []:
        print(f"put `train.json` in {reclor_path}")
        exit(1)
    reclor_data = json.load(open(f"{reclor_path}/train.json"))
    return {f"reclor_{v['id_string']}": v['context'] for v in reclor_data}


passage_data = {}
passage_data.update(read_mctest_data())
passage_data.update(read_race_data())
passage_data.update(read_reclor_data())

source_data = json.load(open(source_path))
for qdata in source_data:
    if qdata['source'] in ['mctest', 'race', 'reclor']:
        qdata['passage'] = passage_data[qdata['passage_id']]

with open(target_path, 'w') as f:
    json.dump(source_data, f)
print(f'wrote {target_path}')
