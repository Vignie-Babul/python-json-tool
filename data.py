import json


def save(data: dict, path: str):
	with open(str(path), 'w') as file:
		json.dump(data, file)

def read(path: str) -> dict:
	with open(str(path), 'r') as file:
		data = json.load(file)
		return data
