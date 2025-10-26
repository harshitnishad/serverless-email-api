# 📧 Serverless Email API

This is a **Serverless REST API** built using Node.js that can **send emails**.  
It uses **Nodemailer** for sending emails and **Serverless Framework** for creating an HTTP endpoint.  
The API can be run **locally** using `serverless-offline`.

---

## 🛠 Features

- Send emails to any receiver email address
- Input parameters:
  - `receiver_email`
  - `subject`
  - `body_text`
- Error handling:
  - Returns `400` if required fields are missing
  - Returns `500` if sending fails
- CORS enabled for testing with frontend or Postman

---

## 📁 Project Structure

email-api/
├── handler.js # Main function code
├── serverless.yml # Serverless configuration
├── package.json # Node.js dependencies
├── .env # Email credentials (do NOT upload)
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Setup

1. Clone the repo or copy files to a folder.
2. Install dependencies:

```bash
npm install
Create a .env file in the root folder:

ini
Copy code
SENDER_EMAIL=yourgmail@gmail.com
SENDER_PASSWORD=your_app_password
Replace with your Gmail and App Password.
Do not upload .env to GitHub.

Start the API locally:

bash
Copy code
npx serverless offline
The API runs at: http://localhost:3000/send-email

📬 How to Test
Use Postman or curl:

POST → http://localhost:3000/send-email

Body (JSON):

json
Copy code
{
  "receiver_email": "someone@example.com",
  "subject": "Test Email",
  "body_text": "Hello from Serverless API!"
}
Success Response:

json
Copy code
{
  "message": "Email sent successfully!"
}
Error Responses:

Missing fields → 400

Wrong credentials → 500