# 🚀 AI-EDN CORE: Intelligent Code Analysis

A high-performance, AI-driven code analysis dashboard designed for hackathons. This project leverages **FastAPI**, **React**, and **scikit-learn** to provide real-time insights into code complexity and structure.

## ✨ Features
- **Real-time Parsing**: uses Python's `ast` (Abstract Syntax Trees) to decompose code components.
- **AI-Powered Insights**: Predicts code complexity using a Machine Learning model.
- **Premium UI**: Modern dark-mode dashboard with Glassmorphism aesthetics and smooth animations.
- **Data Persistence**: Integrated with **PostgreSQL** via **SQLAlchemy** for historical analysis tracking.
- **Production Ready**: Fully containerized with **Docker**.

## 🏗️ Technical Stack
- **Frontend**: React 18, Vite, Framer Motion, Lucide Icons.
- **Backend API**: FastAPI, Pydantic, Uvicorn.
- **AI Module**: Scikit-Learn, Joblib, AST.
- **Database**: PostgreSQL with SQLAlchemy ORM.
- **Infrastructure**: Docker & Docker Compose.

## 🛠️ Quick Start

### 1. Start Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### 2. Start Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3. Docker Deployment
```bash
docker build -t ai-edu-backend ./backend
docker run -p 8000:8000 ai-edu-backend
```

## 📊 Evaluation Module
The project includes a built-in `evaluation.py` to calculate Accuracy, Precision, and Recall, ensuring technical transparency for the ML models used.

## 🤝 Authors
- Created for Hackathon 2026.
