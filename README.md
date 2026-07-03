# FinRelief AI – AI Powered Debt Relief & Financial Recovery Platform

## Project Overview

FinRelief AI is an AI-powered debt relief and financial recovery platform that helps borrowers manage loans, analyze financial health, predict settlement opportunities, generate negotiation letters, and understand borrower rights through an interactive web application.

The project is developed using React.js, Vite, FastAPI, Python, and modern frontend technologies.

---

# Technology Stack

### Frontend
- React.js
- Vite
- JavaScript
- HTML5
- CSS3
- React Router DOM
- Axios

### Backend
- FastAPI
- Python

### Database
- SQLite (Development)
- MySQL (Future Integration)

### AI
- Google Gemini API (Future Integration)

---

# Epic 1 – Project Initialization

## Story 1 – Project Setup

### Description

Initialized the FinRelief AI project using React.js and Vite. Created the basic folder structure and configured the development environment.

### Features

- React + Vite Project
- Folder Structure
- Package Installation
- Git Repository
- Development Environment Setup

---

## Story 2 – Backend Setup

### Description

Configured FastAPI backend for API development.

### Features

- FastAPI Installation
- Python Virtual Environment
- API Structure
- Backend Server

---

## Story 3 – Version Control

### Description

Configured GitHub repository and project version control.

### Features

- Git Initialization
- GitHub Repository
- Initial Commit
- Branch Management

---

# Epic 2 – User Authentication

## Story 1 – Login Interface

### Description

Developed a modern login page with a professional dark-themed design.

### Features

- Login Form
- Email Field
- Password Field
- Responsive Design
- Dark Theme

---

## Story 2 – Registration Interface

### Description

Created borrower registration page.

### Features

- User Registration
- Input Validation
- Responsive Form
- Clean UI

---

## Story 3 – Authentication

### Description

Implemented authentication flow between frontend and backend.

### Features

- API Communication
- Authentication Requests
- Login Validation
- Error Handling

---

# Epic 3 – Financial Management

## Story 1 – Borrower Financial Profile

### Description

Developed borrower financial profile management.

### Features

- Monthly Income
- Monthly Expenses
- Loan Details
- Lump Sum Amount

---

## Story 2 – Loan Management

### Description

Implemented loan management interface.

### Features

- Add Loan
- Edit Loan
- Delete Loan
- Loan Table

---

## Story 3 – Financial Calculations

### Description

Implemented financial calculations.

### Features

- Monthly Surplus
- EMI Calculation
- Debt Ratio
- Financial Metrics

---

# Epic 4 – Frontend Development

## Story 1 – User Interface Development

### Description

Developed the frontend using React.js and Vite with a professional dark-themed interface.

### Features

- Login Page
- Dashboard
- Settlement Predictor
- Negotiation Email
- Know Your Rights
- History Module

---

## Story 2 – Backend Integration

### Description

Integrated the React frontend with the FastAPI backend using Axios.

### Features

- Axios Configuration
- FastAPI API Communication
- Backend Connectivity
- JWT Ready Architecture
- API Integration
- Real-time Data Communication

---

## Story 3 – Financial Dashboard Interface

### Description

Developed an interactive dashboard displaying borrower financial information.

### Features

- Dashboard Overview
- Monthly Income
- Monthly Expenses
- Monthly Surplus
- Total EMI
- Debt Ratio
- Stress Level
- Settlement Prediction
- Financial Profile
- Active Loan Table
- Responsive Dashboard

---

## Story 4 – UI Enhancement Module

### Description

Enhanced the user interface with modern styling and responsive layouts.

### Features

- Professional Dark Theme
- CSS Variables
- Responsive Layout
- Sidebar Navigation
- Dashboard Cards
- Financial Profile Cards
- Active Loan Table
- Navbar
- Flexbox Layout
- CSS Grid
- Hover Effects
- Mobile Responsive Design
- Improved Accessibility
- Consistent Theme Across Pages

---

# Project Structure

```text
frontend/
│
├── src/
│   ├── components/
│   │   ├── Sidebar.jsx
│   │   ├── Navbar.jsx
│   │   ├── StatsCard.jsx
│   │   ├── LoanTable.jsx
│   │
│   ├── pages/
│   │   ├── Dashboard.jsx
│   │   ├── FinancialHealth.jsx
│   │   ├── SettlementPredictor.jsx
│   │   ├── NegotiationEmail.jsx
│   │   ├── KnowYourRights.jsx
│   │   └── History.jsx
│   │
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
│
├── package.json
└── README.md

backend/
│
├── app.py
├── requirements.txt
└── venv/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/FinRelief-AI.git
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

## Backend

```bash
cd backend
uvicorn app:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Frontend URL

```
http://localhost:5173
```

---

# Future Enhancements

- Google Gemini AI Integration
- JWT Authentication
- MySQL Database
- PDF Report Generation
- AI Settlement Prediction
- Negotiation Letter Generator
- Email Integration
- Cloud Deployment

---

# Author

**Syed Zainul Abdin**

B.Tech – Artificial Intelligence & Data Science

Annamacharya Institute of Technology & Sciences, Kadapa

---

# License

This project is developed for academic purposes as part of the AI-Powered Debt Relief & Financial Recovery Platform.
