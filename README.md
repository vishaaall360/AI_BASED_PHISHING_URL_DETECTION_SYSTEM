# 🔐 AI-Based Phishing URL Detection System

The AI-Based Phishing URL Detection System is a cyber-security project that uses machine learning to identify phishing websites by analyzing the structural and lexical features of URLs. The system helps detect malicious links that are commonly used in phishing attacks and classifies URLs as either legitimate or phishing in real time.

This project demonstrates the practical use of artificial intelligence in cyber security and serves as a strong portfolio and academic project.

---

## 🚀 Features

- Detects phishing URLs using machine learning
- Classifies URLs as **Legitimate** or **Phishing**
- Extracts multiple URL-based features
- Displays prediction confidence score
- Simple and interactive Flask web interface
- Modular and extensible project structure

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **Pandas**
- **Scikit-learn**
- **Joblib**
- **HTML & CSS**

---

## 📁 Project Structure

ai-phishing-url-detector/
│
├── app.py
├── train_model.py
├── feature_extractor.py
├── predictor.py
├── requirements.txt
│
├── data/
│ └── phishing_urls.csv
│
├── model/
│ └── phishing_model.pkl
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css


## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Train the Machine Learning Model
python train_model.py

3️⃣ Run the Web Application
python app.py

4️⃣ Open in Browser
http://127.0.0.1:5000

🧪 Sample Test URLs
| URL                                                              | Result     |
| ---------------------------------------------------------------- | ---------- |
| [https://google.com](https://google.com)                         | Legitimate |
| [https://github.com](https://github.com)                         | Legitimate |
| [http://secure-login-paypal.com](http://secure-login-paypal.com) | Phishing   |
| [http://verify-account-now.org](http://verify-account-now.org)   | Phishing   |

👨‍💻 Author

Vishaal S
GitHub: https://github.com/vishaal360
