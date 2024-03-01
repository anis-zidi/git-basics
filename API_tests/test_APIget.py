import requests
import pytest
from API_functions.API_pets import getPetById, postAPIDate

baseURL ="https://petstore.swagger.io/v2/pet/"
petId = '1'


@pytest.fixture()
def add_pet():
    url = baseURL
    payload = {"id": int(petId), "name": "Dog", "status": "pending"}
    resp = postAPIDate(url, payload)
    pet_ID = resp.json()['id']
    yield pet_ID

def test_getPetById(add_pet):
    url = baseURL + str(add_pet)
    response = getPetById(url)
    assert response.json()
    assert response.status_code == 200