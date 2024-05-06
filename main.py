# import requests
import json
from fastapi import FastAPI
from pydantic import BaseModel


class Info(BaseModel):
    temperature: int
    pH: float

app = FastAPI()

@app.post('/test')
def test(datapoint: Info):
    return { "ph" : datapoint.pH}

@app.post('/')
def super_simple_alert(datapoint: Info):
    answer = ''
    if datapoint.temperature < 10:
        answer += 'temp too low '
    if datapoint.pH > 5.5:
        answer += 'pH too high '

    if answer == '':
        answer += 'all good'
    return {
        'statusCode' : 200,
        'body': {
            'status': answer
        }
    }