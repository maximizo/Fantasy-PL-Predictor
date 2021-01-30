import json

# fake function that mocks a call to an external data source
def get_data():
    return(json.load(open("api/data/currentpoints.json")))



# fake function that mocks a call to an external data source
# def get_data2():
#     return {'onetwo': 34}