# Aegis Planner

**Aegis Planner** is a governed autonomous agentic AI system designed to manage the full lifecycle of human goals — from interpretation and planning to execution, evaluation, and adaptation — while remaining safe, transparent, and user-controlled.

Unlike traditional productivity tools or conversational AI assistants, Aegis Planner **assumes responsibility for planning and execution decisions** under explicit human-defined boundaries.

---

## Why Aegis Planner?

Most existing tools fail in one of two ways:

- **Productivity tools** organize tasks but require constant human decision-making.
- **AI assistants** can reason but do not own outcomes or adapt reliably over time.

Aegis Planner fills this gap by providing **cognitive offloading without loss of control**.

The system continuously plans, executes, evaluates, and replans in response to real-world feedback — without requiring micromanagement.

---

## Core Principles

- **Governed Autonomy**  
  Autonomy is explicit, bounded, adjustable, and always overridable by the user.

- **Separation of Intelligence and Authority**  
  Large Language Models (LLMs) are used strictly for reasoning and evaluation.  
  All execution authority lives in deterministic backend code.

- **Auditability by Design**  
  Every plan, execution, failure, and replan is logged and reconstructable.

- **Failure as a First-Class Signal**  
  Missed deadlines and execution failures trigger evaluation and replanning instead of system breakdown.

---

## System Overview

At a high level, Aegis Planner operates as a continuous control loop:

Goal → Plan → Execute → Observe → Evaluate → Replan

- Goals are provided in natural language.
- Plans are versioned and immutable.
- Executions are append-only factual records.
- Evaluations inform future decisions.
- Users retain visibility and override control at all times.

---

## Architecture Summary

- **Backend:** Python 3.11, FastAPI
- **Async Processing:** Celery + Redis
- **Agents:** LangGraph-based reasoning agents (no execution authority)
- **Database:** PostgreSQL (decision-history oriented)
- **Infra:** Docker & Docker Compose

### Authority Model

| Layer | Responsibility |
|-----|---------------|
| LLM Agents | Reasoning, evaluation, proposal generation |
| Backend Core | Decision-making, validation, execution |
| Execution Layer | Deterministic, allowlisted actions only |

LLMs **cannot**:
- execute tools
- modify system state
- call APIs directly
- bypass permission checks

---

## MVP Scope

The current focus is a **backend-first MVP** that validates:

- Autonomous planning and replanning
- Safe execution orchestration
- Auditability and explainability
- Bounded autonomy controls

### Explicitly Out of Scope (for MVP)

- UI / frontend
- Multi-user collaboration
- Financial or irreversible actions
- Advanced long-term learning optimization

---

## Repository Structure

aegis-planner/
├── app/
│ ├── api/ # FastAPI routes
│ ├── agents/ # Reasoning agents (LLM-based)
│ ├── core/ # Control loop, permissions, audit
│ ├── executor/ # Deterministic execution layer
│ ├── db/ # Database models & sessions
│ ├── schemas/ # Pydantic validation schemas
│ ├── workers/ # Async workers (Celery)
│ └── main.py # Application entry point
├── tests/
├── docker-compose.yml
├── Dockerfile
└── requirements.txt


---

## Safety & Security

Aegis Planner is designed to be **safe by architecture**, not by prompt engineering.

Key guarantees:
- LLM outputs are schema-validated
- Execution is fully deterministic
- Tools are allowlisted and permission-gated
- Audit logs are immutable
- Autonomy can be paused or overridden instantly

---

## Project Status

🚧 **Active development**  
Current focus: backend MVP with a single-user, single-goal autonomous loop.

---

## Philosophy

> *If a system cannot explain, constrain, and audit its own behavior, it should not be autonomous.*

Aegis Planner is an exploration of how autonomy can be built **responsibly**, without sacrificing human control or trust.

---

## License

MIT (subject to change)

---

## Contact

Built as a serious system design and engineering project exploring governed autonomy in agentic AI.
