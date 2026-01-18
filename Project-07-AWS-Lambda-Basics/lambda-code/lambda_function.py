def lambda_handler(event, context):
    name = event.get("name", "User")

    return {
        "statusCode": 200,
        "message": f"Hello {name}, this response is from AWS Lambda"
    }
