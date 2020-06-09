import os
import requests

def test_get_all_drgustore():
    response = requests.get("http://localhost:5000/drugstores")
    assert response.status_code == 200

def test_get_local_name_drugstore():
    response = requests.get("http://localhost:5000/drugstores?local_name=AHUMADA")
    assert response.status_code == 200

def test_get_commune_name_drugstore():
    response = requests.get("http://localhost:5000/drugstores?comuna_nombre=BUIN")
    assert response.status_code == 200

def test_get_commune_name_and_local_name_drugstore():
    response = requests.get("http://localhost:5000/drugstores?comuna_nombre=BUIN&local_name=AHUMADA")
    assert response.status_code == 200