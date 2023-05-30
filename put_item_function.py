import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def lambda_handler(event, context):
    response_body = ""
    status_code = 0
    
    data = json.loads(event['body'])
    id = data['id']
    price = data['price']
    
    item = {
        'id': id,
        'price': price
    }
    
    try:
        table.put_item(Item=item)
        status_code = 200
        response_body = json.dumps('Item inserido com sucesso!')
    except Exception as e:
        status_code = 200
        response_body = json.dumps(str(e))
        
    response = {
        'statusCode': status_code,
        'body': response_body
    }
    
    return response
