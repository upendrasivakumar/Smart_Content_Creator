# 🚀 Smart Content Creator

An AI-powered content generation application built using **Streamlit** and **FastAPI**. This tool helps users generate high-quality content such as blogs, LinkedIn posts, emails, Instagram captions, Twitter posts, and YouTube descriptions based on a selected topic, technology, and writing style.

---

## 📌 Features

* ✨ AI-generated content creation
* 📝 Generate content from a custom topic
* 💻 Technology-specific content generation
* 🎯 Multiple writing styles (Professional, Technical, Friendly, Marketing, Casual)
* 📄 Multiple content formats
* ⚡ Fast and responsive Streamlit interface
* 🔗 Integration with FastAPI backend

---

## 🛠️ Tech Stack

### Frontend

* Python
* Streamlit

### Backend

* FastAPI
* Python

### API Communication

* Requests Library

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/upendrasivakumar/Smart_Content_Creator.git
cd smart-content-creator
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Configuration

Create a file:

```text
.streamlit/secrets.toml
```

Add your backend URL:

```toml
be_server_url = "http://localhost:8000"
```

---

## ▶️ Running the Application

### Start FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

### Start Streamlit Frontend

```bash
streamlit run app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

## 🎯 How It Works

1. Enter a topic.
2. Select a technology.
3. Choose the content format.
4. Select a writing style.
5. Click **Generate**.
6. The frontend sends a request to the FastAPI backend.
7. The backend generates AI content.
8. Generated content is displayed in the Streamlit interface.

---

## 📸 Supported Content Types

* Blog Article
* LinkedIn Post
* Email
* Instagram Caption
* Twitter Post
* YouTube Description

---

## 🎨 Supported Writing Styles

* Professional
* Technical
* Friendly
* Marketing
* Casual

---

## 🔮 Future Enhancements

* Download generated content as PDF
* Copy-to-clipboard functionality
* Content history management
* User authentication
* Multiple AI model support
* Content length customization
* Dark/Light theme toggle

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Siva Madala

* GitHub: https://github.com/upendrasivakumar
* LinkedIn: https://www.linkedin.com/in/madalaupendrasivakumar

If you found this project useful, consider giving it a ⭐ on GitHub.
