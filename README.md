# 🚀 AI-EDN CORE: Intelligent AI Tutor Platform
**Track 4: AI for Education - ASEAN AI Hackathon 2026**

AI-EDN CORE is a high-fidelity educational platform designed to empower ASEAN students in learning software development through AI-driven insights. This project demonstrates a production-grade architecture combining **FastAPI**, **React**, and **Deep Code Analysis**.

---

## 🏗️ Project Architecture & Achievements

This repository represents the **Final Innovation Portfolio**. While the prototype is functional, the internal documentation reflects the full scalability and future intelligence roadmap designed for the competition.

### 🌟 Implemented Features (Phase 1)
- **Premium UI/UX**: A modern dark-mode dashboard with Glassmorphism and Framer Motion animations.
- **AST-Based Analysis**: Uses Abstract Syntax Trees to decompose Python code—far more robust than simple pattern matching.
- **AI Tutor Feedback**: Real-time educational suggestions based on code structure (loops, functions, docstrings).
- **Skill Level Prediction**: Categorizes developer profiles (Beginner/Intermediate/Advanced) using rule-based AI logic.
- **Persistence Layer**: Integrated with PostgreSQL (and SQLite fallback) for tracking student progress.
- **Dockerization**: Fully containerized environment for seamless regional deployment.

### 🧠 Future Roadmap (Phases 2-4)
*The project is architected to support the following planned enhancements:*

#### Phase 2: AI Intelligence (Multi-modal Learning)
- **Natural Language Explainer**: Integration with lightweight LLMs (Mistral/Llama) to explain complex logic in native ASEAN languages (Vietnamese, Thai, Malay, etc.).
- **Smart Refactoring**: A "Fix it for me" engine that suggests cleaner, more efficient versions of student code.

#### Phase 3: Regional Scalability
- **Distributed Processing**: Using Celery + Redis to handle thousands of concurrent analysis requests from students across the region.
- **Historical Benchmarking**: Analytics dashboards for universities to track regional performance trends.

#### Phase 4: Final Impact
- **Problem-Solution Fit**: Addressing the shortage of technical mentors in remote ASEAN regions via automated feedback.
- **Ethical AI**: Implementation of data privacy standards to protect student IP.

---

## 🛠️ Technical Stack
- **Frontend**: React 18, Vite, Framer Motion, Lucide Icons.
- **Backend**: FastAPI, Pydantic, SQLAlchemy.
- **AI/ML**: Python AST Module, Scikit-learn (Evaluation).
- **Infrastructure**: Docker & Docker Compose.

---

## 🚀 Quick Start (Local Run)

### Setup Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### Setup Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## 🤝 Competition Metadata
- **Track**: AI for Education
- **Format**: Functional Prototype + Scalability Roadmap
- **Key Focus**: Human-centric AI interaction and regional resilience through education.

*Developed for the ASEAN AI Hackathon 2026.*
