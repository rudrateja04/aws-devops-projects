import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UsersTable')

def lambda_handler(event, context):
    user_id = event.get("UserId", "U001")
    name = event.get("Name", "Rudra")

    # Insert item
    table.put_item(
        Item={
            "UserId": user_id,
            "Name": name
        }
    )

    # Read item
    response = table.get_item(
        Key={
            "UserId": user_id
        }
    )

    return {
        "statusCode": 200,
        "item": response.get("Item")
    }
