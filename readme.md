# 👕 StyleBot – Apparel Store Chatbot (Google Gemini AI)

A smart, conversational AI chatbot built for online apparel stores.  
StyleBot helps customers with product recommendations, sizing guidance, shipping info, returns, and even fashion advice — all powered by **Google Gemini AI**.

* * *

## 🚀 Features

- 🛍️ **Product Recommendations** – Suggests outfits or styles based on user preferences
- 📏 **Sizing Guidance** – Helps users pick the perfect size
- 🚚 **Shipping Info** – Provides estimated delivery and shipping policies
- 🔄 **Returns & Exchanges** – Explains return policies and procedures
- 💳 **Payment Help** – Answers billing and payment queries
- 👗 **Fashion Advice** – Gives outfit ideas for various occasions
- 💬 **Clean Chat Interface** – Simple, responsive, and mobile-friendly

* * *

## 🧠 Tech Stack

| Component | Technology |
| --- | --- |
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask (Python) |
| AI Model | Google Gemini 1.5 Flash / 2.0 / 2.5 Pro |
| API | `google-generativeai` SDK |
| Hosting (optional) | Render / Hugging Face Spaces / Vercel |

* * *

## 🧩 Project Structure

```cd
📁 apparel-chatbot/  
│  
├── app.py # Flask backend server  
├── requirements.txt # Python dependencies  
├── template.html # Chat UI (HTML + CSS + JS)  
└── README.md

```

* * *

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/apparel-chatbot.git
cd apparel-chatbot
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # (Windows)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Example `requirements.txt`:**

```
flask
google-generativeai
```

* * *

### 4️⃣ Add Your Google Gemini API Key

1.  Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey).
    
2.  Open `app.py` and replace this line:
    

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

with your actual key.

* * *

### 5️⃣ Run the Application

```bash
python app.py
```

Visit → **[http://127.0.0.1:5000](http://127.0.0.1:5000/)**  
💬 Start chatting with **StyleBot**!

* * *

## 🖥️ Demo Screenshot

> <img width="1811" height="400" alt="image" src="https://github.com/user-attachments/assets/0b6a742b-36f2-4fae-88d9-c99678026792" />
> <img width="1811" alt="image" src="https://github.com/user-attachments/assets/aa3394fc-2f61-45d5-8184-4c32757ad826" />


* * *

## 🌐 Deployment

You can host this app easily on:

- **Render** → free Flask app hosting
    
- **Hugging Face Spaces** → via Gradio or Flask
    
- **Vercel / Railway** → for frontend + backend integration
    

**To deploy on Render:**

1.  Push your code to GitHub
    
2.  Go to [Render.com](https://render.com/) → “New Web Service”
    
3.  Connect your repo
    
4.  Set **Start Command:** `python app.py`
    
5.  Add **Environment Variable:**
    
    - `GEMINI_API_KEY = your_api_key_here`

* * *

## 🤖 Example Interactions

**User:** I need a casual outfit for summer  
**StyleBot:** Try pairing a light cotton shirt with chinos or shorts. You’ll stay cool and look sharp!

**User:** What’s your return policy?  
**StyleBot:** You can return any unworn item within 30 days for a full refund. Just contact our support team.

* * *

## 🧑‍💻 Author

**Your Name**  
🪪 [GitHub](https://github.com/YOUR_USERNAME)  
💼 [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)

* * *

## 📜 License

This project is licensed under the **MIT License** – feel free to modify and use it for your own store chatbot projects.

* * *

## 💡 Future Enhancements

- 🗣️ Add voice chat
    
- 🧾 Product catalog integration
    
- 💾 Chat history with database
    
- 🎨 Dark/light theme toggle
    
- 🌍 Multi-language support
    

* * *

### 💬 Made with ❤️ using Flask + Gemini AI
