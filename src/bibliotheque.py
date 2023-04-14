import numpy as np

## for changing the scraped ratings from tripadvisor
ratings = {
    '4,0 de 5 burbujas':4.0,
    '4,5 de 5 burbujas':4.5,
    '3,5 de 5 burbujas':3.5,
    '5,0 de 5 burbujas':5.0,
    '3,0 de 5 burbujas':3.0,
    '2,5 de 5 burbujas':2.5,
    '-1,0 de 5 burbujas':-1.0,
    '2,0 de 5 burbujas':2.0,
    '1,0 de 5 burbujas':1.0,
    '1,5 de 5 burbujas':1.5,
    '':np.nan,
    '0 opiniones':0
}

## equivalences for the hotels dataframe
accommodation = {
    'Alojamientos':'Accommodation'
}

accommodation_type = {
    'Hoteles':'Hotels',
    'Hostales':'Hostel',
    'Residencias universitarias':'Dorms',
    'Apartahoteles':'Apartments',
    'Pensiones':'Hostels',
    'Albergues':'Hostels',
    'Camping':'Camping' 
}

hotel_apartments_ratings = {
    '4 estrellas':4.0,
    '2 estrellas':2.0,
    '3 estrellas':3.0,
    '1 estrella':1.0,
    '5 estrellas':5.0,
    '3 llaves':3.0,
    '5 estrellas Gran Lujo':6.0,
    '1 llave':1.0,
    '4 llaves':4.0,
    '2 llaves':2.0     
}