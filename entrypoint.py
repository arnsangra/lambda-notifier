#!/usr/bin/env python3
"""A lambda function to notify events"""

import os

import json
import requests


def entrypoint(event, context):
    """Lambda function entrypoint"""
    slack_endpoint = "https://hooks.slack.com/services/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"
    msg = massage(event)
    response = requests.post(slack_endpoint, json=msg)
    print(response)

def massage(message):
    print(message)
    return message

if __name__ == "__main__":
    entrypoint({"text": "aaa"}, "")
