import json


def save(data: dict, path: str):
	with open(path, 'w') as file:
		json.dump(data, file)

def read(path: str) -> dict:
	with open(path, 'r') as file:
		data = json.load(file)
		return data
