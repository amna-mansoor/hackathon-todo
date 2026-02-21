# Hackathon II: The Evolution of Todo 🚀

[cite_start]This repository contains the implementation for **Hackathon II: Spec-Driven Development & Cloud Native AI**[cite: 3]. [cite_start]It showcases the evolution of a simple Todo application from a CLI tool into a modern, Full-Stack Web Application built entirely using AI-assisted Spec-Driven Development[cite: 95, 133].

## 🏗️ Architecture & Tech Stack

[cite_start]This project uses a monorepo structure to house both the frontend and backend [cite: 181, 207-212]. 

**Frontend:**
* [cite_start]**Framework:** Next.js 16+ (App Router) [cite: 143]
* [cite_start]**Language:** TypeScript [cite: 273]
* [cite_start]**Styling:** Tailwind CSS [cite: 274]
* [cite_start]**Authentication:** Better Auth (JWT) [cite: 143, 154]

**Backend:**
* [cite_start]**Framework:** Python FastAPI [cite: 143]
* [cite_start]**ORM:** SQLModel [cite: 143]
* [cite_start]**Database:** Neon Serverless PostgreSQL [cite: 140, 143]
* [cite_start]**Package Manager:** UV [cite: 103]

**AI & Workflow:**
* [cite_start]**Methodology:** Spec-Driven Development (SDD) [cite: 98]
* [cite_start]**Tools:** Spec-Kit Plus, Gemini/Claude Code, and `AGENTS.md` guidelines[cite: 105, 106, 948].

---

## ✨ Features Implemented (Phases I & II)

* [cite_start]**User Authentication:** Secure signup and login flow using Better Auth and JWT tokens[cite: 141, 154].
* [cite_start]**Task Management:** Full CRUD operations[cite: 137, 330]:
  * [cite_start]Add new tasks[cite: 39].
  * [cite_start]View a list of user-specific tasks[cite: 42, 350].
  * [cite_start]Update task titles and descriptions[cite: 41].
  * [cite_start]Mark tasks as complete/pending[cite: 43].
  * [cite_start]Delete tasks[cite: 40].
* [cite_start]**Data Isolation:** All REST API endpoints (`/api/{user_id}/tasks`) are secured so users can only access their own data[cite: 145, 171].

---

## 📁 Project Structure

```text
hackathon-todo/
├── AGENTS.md                 # Master constitution for AI agent behavior
├── CLAUDE.md                 # Root instructions linking to AGENTS.md
├── spec-kit/                 # Source of truth for all application specifications
│   ├── config.yaml           # Spec-Kit configuration
│   └── specs/                # AI-generated specifications (Features, API, DB)
├── frontend/                 # Next.js Application
│   ├── CLAUDE.md             # Frontend-specific AI guidelines
│   └── .env.local            # Frontend secrets (Better Auth)
└── backend/                  # FastAPI Application
    ├── CLAUDE.md             # Backend-specific AI guidelines
    ├── main.py               # API Entrypoint
    └── .env                  # Backend secrets (Neon DB, Better Auth)
