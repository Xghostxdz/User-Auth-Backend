```markdown
# User-Auth-Backend 🔐

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)
![License](https://img.shields.io/badge/License-MIT-orange)

**User-Auth-Backend** is a simple and efficient user management and authentication system built using **Flask** and **SQLite**. This project allows users to register, log in, and delete their accounts securely.

---

## Features ✨

- **User Registration**: Add new users with encrypted passwords.
- **User Login**: Authenticate users with secure credentials.
- **Account Deletion**: Delete user accounts after identity verification.
- **Secure Encryption**: Uses **SHA-256** hashing for password encryption.
- **RESTful API**: Easy-to-use API endpoints for interacting with the system.

---

## Installation ⚙️

### Prerequisites
- Python 3.11 or later.
- Flask (`pip install flask`).
- SQLite3 (built-in with Python).

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Xghostxdz/User-Auth-Backend.git
   cd User-Auth-Backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. The API will be available at `http://127.0.0.1:5000`.

---

## API Endpoints 🌐

### Register a New User
- **Endpoint**: `/register`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "response": "User added successfully"
  }
  ```

### User Login
- **Endpoint**: `/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "response": "Login successful"
  }
  ```

### Delete User Account
- **Endpoint**: `/deleteaccount`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "response": "Account deleted successfully"
  }
  ```

---

## Project Structure 📂

```
User-Auth-Backend/
├── app.py               # Main application file
├── users.db             # SQLite database file
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
└── venv/                # Virtual environment (optional)
```

---

## Contributing 🤝

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License 📜

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact 📧

For questions or feedback, feel free to reach out:

- **GitHub**: [Xghostxdz](https://github.com/Xghostxdz)
- **Telegram**: [Telegram Group](https://t.me/XTOOLPYCHAT)

---

## Acknowledgments 🙏

- Thanks to the **Flask** team for an amazing framework.
- Inspired by secure authentication systems.

```
