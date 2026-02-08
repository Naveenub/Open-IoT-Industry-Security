import boto3

sns = boto3.client("sns")

def send_sms(message: str, phone: str):
    sns.publish(
        PhoneNumber=phone,
        Message=message
    )
