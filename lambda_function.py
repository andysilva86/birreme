import os
import sys
import jinja2 

def lambda_handler(event, context):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"), encoding="utf8"))
    my_name = False
    if event["queryStringParameters"] and "my_name" in event["queryStringParameters"]:
        my_name_query = event["queryStringParameters"]["my_name"]
    template = env.get_template("index.html")
    html = template.render(
        my_name=my_name_query
    )

    return response(html)

def response(myhtml):
    return {
        "statusCode": 200,
        "body": myhtml,
        "headers": {
            "Content-Type": "text/html",
        }
    }