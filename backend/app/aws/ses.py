import boto3

ses = boto3.client("ses")

def send_email(subject: str, body: str, to_email: str):
    ses.send_email(
        Source="alerts@industry.com",
        Destination={"ToAddresses": [to_email]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Text": {"Data": body}}
        }
    )
