from fastapi import FastAPI , HTTPException
from schemas import GenreURLChoices, Band

app = FastAPI()

BANDS = [
    {'id':1,'name':'The Kinks','genre':'Rocks'},
    {'id':2,'name':'Aphex Twin','genre':'Electronics'},
    {'id':3,'name':'Slowdive','genre':'Shoegaze', 'albums':[
        {'title':'Master of reality','release_date':'1971-07-21'}
    ]},
    {'id':4,'name':'Wu-Tang Clan','genre':'Hip-Hop'},

]

@app.get('/bands')
async def bands() ->list[dict] :
    return [
        band(**b) for b in BANDS
     ]

@app.get('/bands/{band_id}')
async def band(band_id:int) -> Band:   # can define return type to maintain state
    band = next((Band(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        # return "404 not found"
        print("tester")
        raise HTTPException(status_code=404, detail='Band not found')
    else:
        return band 

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]



