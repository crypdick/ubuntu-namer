"""
AWS Lambda handler that generates Ubuntu Names

To install this to AWS Lambda, you need to create a new function and upload the zip file created by `make build-lambda`
to the function.

You can then test the function by creating a test event with the following JSON: {"letter": "a"} or simply {} to use a
random letter.
"""

import json
import logging

from ubuntu_namer import generate_name

logger = logging.getLogger()


def lambda_handler(event, context):
    """AWS Lambda handler that generates Ubuntu Names"""
    logger.info("Received event: %s", json.dumps(event))
    letter = event.get("letter", None)
    name = generate_name(letter)
    return {
        "statusCode": 200,
        "body": json.dumps({"name": name}),
    }
