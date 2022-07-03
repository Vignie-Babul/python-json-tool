import json


def save(data: dict, file_name: str, path='assets/data/'):
	with open(f'assets/data/{file_name}.json', 'w') as file:
		json.dump(data, file)

def read(file_name: str, path='assets/data/') -> dict:
	with open(f'assets/data/{file_name}.json', 'r') as file:
		data = json.load(file)
		return data