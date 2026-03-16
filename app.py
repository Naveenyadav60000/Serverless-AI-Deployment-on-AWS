import json

# Linear model coefficients for house price
INTERCEPT = 50000.0
B_BED = 20000.0      # bedrooms
B_BATH = 15000.0     # bathrooms
B_SQFT = 120.0       # square feet
B_AGE = -500.0       # age in years
B_CITY = 30000.0     # city index (0,1,2)

def predict_price(bedrooms, bathrooms, sqft, age, city):
    return (
        INTERCEPT
        + B_BED * bedrooms
        + B_BATH * bathrooms
        + B_SQFT * sqft
        + B_AGE * age
        + B_CITY * city
    )

def lambda_handler(event, context):
    try:
        body = event.get("body", "{}")
        if isinstance(body, str):
            data = json.loads(body)
        else:
            data = body

        bedrooms = float(data.get("bedrooms"))
        bathrooms = float(data.get("bathrooms"))
        sqft = float(data.get("sqft"))
        age = float(data.get("age"))
        city = float(data.get("city"))

        prediction = predict_price(bedrooms, bathrooms, sqft, age, city)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "prediction": prediction,
                "inputs": {
                    "bedrooms": bedrooms,
                    "bathrooms": bathrooms,
                    "sqft": sqft,
                    "age": age,
                    "city": city
                }
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"error": str(e)})
        }
