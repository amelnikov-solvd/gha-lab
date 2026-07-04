import json, datetime

def lambda_handler(event, context):
    now = datetime.datetime.utcnow().isoformat()
    print(f"Hello from Lambda! event={json.dumps(event)}")
    print(f"request_id={context.aws_request_id} time={now}Z")
    return {"statusCode": 200, "body": f"executed at {now}Z"}