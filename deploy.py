import os
import requests
import shutil
import tempfile

ASSET_ID = os.getenv("ASSET_ID")  # ID ассета
LOGIN = os.getenv("ASSET_LIBRALY_LOGIN")
PASSWORD = os.getenv("ASSET_LIBRALY_PASSWORD")
BASE_URL = "https://godotengine.org/asset-library/api/"
COMMIT_SHA = os.getenv("COMMIT_SHA")
RELEASE_TAG = os.getenv("RELEASE_TAG")

def login() -> str:
	""" Авторизуется и получает токен """
	data = {"username": USERNAME, "password": PASSWORD}
	url = BASE_URL + "/login"
	response = requests.post(url, json=data)
	
	if response.status_code == 200 and response.json().get("authenticated"):
		return response.json()["token"]
	else:
		print("❌ Login failed:", response.text)
		exit(1)


def asset_edit(token:str):
	data = {"token": token,
		    "version_string": RELEASE_TAG,
			"download_commit": COMMIT_SHA,
		    }
	url = BASE_URL + "/asset/" + ASSET_ID
	response = requests.post(url, json=data)
	if response.status_code == 200:
		print("✅ Upload successful!")
	else:
		print(f"❌ Upload failed: {response.text}")
		exit(1)


if __name__ == "__main__":
	token = login()
	asset_edit(token)
