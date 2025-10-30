import json

def send_email(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        receiver_email = body.get('receiver_email')
        subject = body.get('subject')
        body_text = body.get('body_text')

        if not all([receiver_email, subject, body_text]):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing required fields"})
            }

        # Mock sending email (for offline testing)
        print(f"Email would be sent to {receiver_email} with subject '{subject}' and body '{body_text}'")

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully (mock)"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
