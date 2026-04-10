# API Support Console (Flask)

A simple API testing tool built using Flask. It allows users to send GET and POST requests and stores logs in a SQLite database.

---

## 🚀 Features

- Send GET and POST API requests  
- View API responses  
- Measure response time  
- Store request logs in SQLite database  
- Clear logs  

---

## 📁 Project Structure

api_console/

├── app.py  
├── database.py  
├── api_console.db  
├── templates/  
│   └── index.html  
└── venv/  

---

## ⚙️ How to Run the Project

### 1. Open the project in VS Code

Open folder:
api_console

---

### 2. Open terminal

Shortcut:
Control + `

---

### 3. Activate virtual environment

source venv/bin/activate

You should see:
(venv)

---

### 4. Run the app

python app.py

---

### 5. Open in browser

http://127.0.0.1:5000

---

## 🛑 How to Stop the Server

Press:
Control + C

---

## 🧪 Example APIs to Test

## 🧪 Example APIs to Test

### 🔹 GET Requests

https://jsonplaceholder.typicode.com/posts/1  
https://jsonplaceholder.typicode.com/users  
https://api.github.com/users/octocat  
https://official-joke-api.appspot.com/random_joke  
https://api.ipify.org?format=json  
https://httpbin.org/get  

---

### 🔹 POST Requests

https://jsonplaceholder.typicode.com/posts  
https://httpbin.org/post  
https://reqres.in/api/users  

---

### 🔹 POST Request Sample Bodies

Use these JSON bodies when testing POST requests:

{
  "title": "test",
  "body": "hello world",
  "userId": 1
}

{
  "name": "Ketan",
  "role": "developer"
}

{
  "name": "Ketan",
  "job": "Engineer"
}

---

### 🔹 Same API for GET & POST (Recommended)

https://httpbin.org/get  
https://httpbin.org/post  

https://jsonplaceholder.typicode.com/posts  (GET & POST both supported)

---

### ⚠️ Note

Do NOT use websites like:
https://www.youtube.com  
https://google.com  

These are not APIs and will return HTML instead of JSON.
---

## 🗄️ Database

- SQLite database (api_console.db)
- Stores:
  - URL  
  - Method  
  - Request body  
  - Status code  
  - Response  
  - Response time  

---

## ⚠️ Notes

- Use API URLs (not full websites like YouTube)  
- This is a development server  

---

## 👨‍💻 Author

Ketan Devraj