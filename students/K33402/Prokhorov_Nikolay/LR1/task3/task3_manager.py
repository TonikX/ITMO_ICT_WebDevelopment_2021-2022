import argparse
import json

from typing import Dict
import requests
import tqdm

parser = argparse.ArgumentParser(description='Менеджер для задачи 3')
parser.add_argument('--host', help='IP хоста', default='localhost')
parser.add_argument('--port', help='Порт хоста', default=8888)

args = parser.parse_args()

with open('data.json', encoding='utf-8') as file:
    data: Dict[str, Dict[str, int]] = json.load(file)

for student in data.keys():
    for discipline in data[student].keys():
        mark = data[student][discipline]
        print('\r' + ' ' * 100, end='', flush=True)
        print(f'\rStudent {student} discipline "{discipline}" mark {mark}', end='', flush=True)

        response = requests.post(f'http://{args.host}:{args.port}/marks', params={
            'student': student,
            'discipline': discipline,
            'mark': mark
        })
        if response.status_code == 201:
            print(' Done!' + ' ' * 30, end='', flush=True)
        else:
            print(f' Error for user {student}!')
