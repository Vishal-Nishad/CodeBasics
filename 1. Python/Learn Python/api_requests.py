from fastapi import FastAPI
from enum import Enum
app=FastAPI()
@app.get('/')
def hello():
    return 'Hello world'

@app.get('/hello/{name}')
def hello(name):
    return f'Hello {name}'

food_items={
    'indian':['samosa','pani puri'],
    'italian':['pizza','coffee'],
    'french':['omellete','cookies']
}

@app.get('/get_items/{cuisine}')
def get_items(cuisine):
    items=food_items.get(cuisine)
    if not items:
        return f'{cuisine} is not available.'
    return food_items.get(cuisine)


coupon_code={
    1:'10%',
    2:'20%',
    3:'30%'
}
@app.get('/discount/{code}')
async def get_items(code: int):
    return {"discount offer":coupon_code.get(code)}

class AvailableCuisine(str,Enum):
    indian='indian'
    american='american'
    italian='italian'
@app.get('/get_item/{cuisine}')
def get_items(cuisine:AvailableCuisine):
    return food_items.get(cuisine)