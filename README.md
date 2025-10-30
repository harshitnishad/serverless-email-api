🧾 README.md
# 📧 Serverless Email API (Python)

This project implements a simple REST API using the **Serverless Framework** with **Python 3.9** runtime.  
The API accepts a recipient email address, subject, and message body, and responds with a success message.  
It is built and tested locally using the `serverless-offline` plugin — no AWS subscription or deployment is required.

---

## 🚀 Features
- REST API built using **Serverless Framework**
- **POST /dev/send-email** endpoint
- Accepts JSON body with:
  ```json
  {
    "receiver_email": "test@example.com",
    "subject": "Hello from Serverless",
    "body_text": "This is a test email."
  }



Validates input and handles errors gracefully


Returns proper HTTP response codes


Includes mock email sending logic for offline testing (no AWS SES required)



⚙️ Setup Instructions


Install dependencies
npm install



Activate Python virtual environment
python -m venv venv
venv\Scripts\activate   # For Windows



Run Serverless locally
npx serverless offline



Test using Postman


Method: POST


URL: http://localhost:3000/dev/send-email


Body (JSON):
{
  "receiver_email": "test@example.com",
  "subject": "Test Subject",
  "body_text": "This is a test email."
}



Header:
Content-Type: application/json






🧠 Notes


For real email sending, AWS SES integration can be enabled by setting:
environment:
  SOURCE_EMAIL: "your_verified_email@example.com"
  AWS_REGION: "ap-south-1"



In this mock version, the function only simulates sending email and returns a success message for offline testing.



📄 Author
Harshit Nishad
Built as part of a Serverless Framework assignment using Python & AWS Lambda (offline mode).

