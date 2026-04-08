# 🕵️ MarketScout Agent

**MarketScout Agent** is an enterprise-grade AI competitor intelligence platform. It automates the process of gathering, analyzing, and summarizing the latest developments of any competitor company within a 7-day window.

Built for strategy teams and market analysts, it leverages the power of **Google Gemini 1.5 Flash** for deep analysis and **Tavily AI** for real-time web intelligence.

---

## 🚀 Core Features

-   **Real-time Intelligence**: Fetches the latest 7 days of news, product launches, and updates about any competitor.
-   **AI-Powered Summarization**: Uses Gemini 1.5 Flash to generate executive summaries and categorize updates (funding, leadership, product, etc.).
-   **Interactive Dashboard**: Visualize competitive activity, technical trends, and alert history.
-   **Alert Center**: Automated severity-graded alerts (Critical/Warning/Info) based on competitor activity.
-   **PDF Report Generation**: Generate and download professional intelligence reports instantly.
-   **Secure Authentication**: Fully integrated with Google OAuth for a seamless login experience.

---

## 🛠️ Tech Stack

### Backend
-   **FastAPI**: High-performance web framework.
-   **Tortoise ORM**: Async ORM for Python.
-   **Supabase / PostgreSQL**: Scalable database for persistence.
-   **Gemini 1.5 Flash**: SOTA AI for natural language analysis.
-   **Tavily AI**: Optimized search engine for LLMs.
-   **Authlib**: Secure OAuth2 implementation.

### Frontend
-   **React + Vite**: Modern, ultra-fast frontend tooling.
-   **Tailwind CSS**: Premium, responsive UI design.
-   **Zustand**: Lightweight state management.
-   **Recharts / Chart.js**: Advanced data visualization.
-   **Lucide React**: Beautiful iconography.

---

## 🚢 Deployment Guide

### Backend (Render)
1.  **Source**: Connect your GitHub repository.
2.  **Environment**: `Python`.
3.  **Build Command**: `pip install -r backend/requirements.txt`.
4.  **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`.
5.  **Environment Variables**:
    -   `PYTHON_VERSION`: `3.12.5` *(Required for compatibility)*
    -   `GEMINI_API_KEY`: Your Google AI Studio key.
    -   `TAVILY_API_KEY`: Your Tavily search key.
    -   `SUPABASE_URL` & `SUPABASE_KEY`: Your Supabase connection details.
    -   `GOOGLE_CLIENT_ID` & `GOOGLE_CLIENT_SECRET`: From Google Cloud Console.
    -   `FRONTEND_URL`: Your deployed Netlify URL.

### Frontend (Netlify)
1.  **Source**: Connect your GitHub repository.
2.  **Base Directory**: `frontend`.
3.  **Build Command**: `npm run build`.
4.  **Publish Directory**: `frontend/dist`.
5.  **Environment Variables**:
    -   `VITE_API_URL`: Your deployed Render backend URL.

---

## ⚠️ Troubleshooting: Render Build Failure

If you encounter an error like `Failed to build asyncpg` or `Failed building wheel for asyncpg` on Render:

1.  **Why it happens**: Render defaults to a developmental version of Python (3.14+) which is incompatible with many database libraries.
2.  **The Fix**: 
    -   Ensure `runtime.txt` exists in your project containing `python-3.12.5`.
    -   Set the `PYTHON_VERSION` environment variable to `3.12.5` in the Render dashboard.

---

## 🛠️ Local Development

1.  **Clone the Repo**: `git clone https://github.com/your-repo/MarketScout.git`
2.  **Backend Setup**:
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
3.  **Frontend Setup**:
    ```bash
    cd frontend
    npm install
    npm run dev
    ```
