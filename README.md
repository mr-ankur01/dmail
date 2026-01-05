# 📧 DMail — Disposable Email System

**DMail** is a web-based disposable email system built with **Django** and **Bootstrap**.  
It allows users to generate temporary email addresses, receive messages, and view them — helping protect privacy and reduce spam.

---

## 🚀 Features

- ✔ Generate temporary/disposable email addresses  
- ✔ Receive and view incoming emails  
- ✔ Auto-expiration of temporary inboxes  
- ✔ No user signup required  
- ✔ Responsive UI built with Bootstrap  
- ✔ Backend powered by Django  

---

## 🧱 Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python, Django          |
| Frontend  | HTML5, CSS3, Bootstrap  |
| Database  | SQLite (default)        |
| Deployment| Django Dev Server/WSGI  |

---

## 📁 Project Structure

```text
dmail/
├── mysite/         # Django project configurations
├── myapp/          # Main app (email generation & views)
├── staticfiles/    # Static CSS/JS
├── db.sqlite3      # Default local database
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🛠 Installation & Setup

### Clone the repository

```bash
git clone https://github.com/mr-ankur01/dmail.git
cd dmail
```

### Create & activate virtual environment

```bash
python -m venv venv
```

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run database migrations

```bash
python manage.py migrate
```

### Start the development server

```bash
python manage.py runserver
```

Open your browser and visit:
```
http://127.0.0.1:8000/
```

---

## ⚙️ How It Works

1. User opens the app in a browser  
2. Clicks **Generate Disposable Email**  
3. System creates a random email identifier  
4. Emails sent to that address appear in the UI  
5. Inboxes auto-expire after a configurable time  

---

## 🔧 Configuration

Edit:
```text
mysite/settings.py
```

Configurable options:
- EMAIL_HOST, EMAIL_PORT
- Inbox expiration duration
- Static files settings

---

## 🧩 Future Improvements

- Email attachments  
- WebSocket-based live updates  
- Multiple domain support  
- Configurable expiry time  
- Admin dashboard  

---

## 🤝 Contributing

Contributions are welcome!

```bash
git checkout -b feature/your-feature
```

Commit your changes and open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**.
