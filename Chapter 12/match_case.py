# Match case is switch case of python 
# But python required is 3.10 or more

def http_status(status:int) -> str:
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not found"
        case 500:
            return "Internal Server error"
        case _:
            return "Error status not found"

print(http_status(200))