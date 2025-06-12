
import pandas as pd
import numpy as np

def preprocess_user_input(airline, source_country, source_city, destination_country, destination_city, date, time, stops, duration):
    day = date.day
    month = date.month
    hour = time.hour
    data = pd.DataFrame({
        'Airline': [airline],
        'Source_Country': [source_country],
        'Source_City': [source_city],
        'Destination_Country': [destination_country],
        'Destination_City': [destination_city],
        'Stops': [stops],
        'Duration': [duration],
        'Day': [day],
        'Month': [month],
        'Hour': [hour]
    })
    return data
