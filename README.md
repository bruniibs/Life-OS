<div align="center">

# ✦ Life OS

**A personal organization system, built one module at a time.**

A Python-based project designed to bring everyday planning, productivity, and personal management into one modular workspace.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Work%20in%20Progress-93A9CB?style=flat-square)
![Interface](https://img.shields.io/badge/Interface-CLI-64748B?style=flat-square)

</div>

---

## ✨ Overview

**Life OS** is a personal project exploring how to build an integrated, customizable system for organizing daily life.

Rather than starting with a large application, the project is being developed incrementally. Its first working module is a **command-line task planner**, with the long-term goal of connecting planning, routines, meals, fitness, and other aspects of personal organization in one interface.

> **Current stage:** Python CLI prototype. A graphical interface and additional modules are planned, not yet implemented.

## ✅ Current features

The task planner currently supports:

- **Task creation** with an automatically assigned ID
- **Task listing** with visual completion indicators
- **Task completion** by ID
- **Task removal** by ID
- **Local JSON persistence** to keep tasks between sessions
- **Modular organization**, separating task operations, data storage, and the CLI
- **Basic input validation** for menu actions and task IDs

### In progress

- [ ] Save and use task priorities (`low`, `medium`, `high`) consistently
- [ ] Improve task validation and error handling
- [ ] Add automated tests
- [ ] Refine the command-line experience

**Note:** The CLI already asks for a priority, but the latest reviewed version does not yet pass that value into the task-creation function. Priority support is therefore listed as *in progress*.

## 🧩 Planned modules

| Module | Vision | Status |
| --- | --- | --- |
| **Planner** | Tasks, priorities, schedules, and daily planning | 🛠️ CLI prototype |
| **Meals** | Recipes, meal plans, and grocery lists | 📋 Planned |
| **Fitness** | Workouts and activity tracking | 📋 Planned |
| **Habits & routines** | Recurring activities and progress tracking | 📋 Planned |
| **Personal dashboard** | A unified visual interface for all modules | 📋 Planned |

These are development goals, not currently available features.

## 🛠️ Tech stack

- **Python** — application logic and CLI
- **JSON** — local task data persistence
- **`pathlib`** — filesystem paths
- **Git & GitHub** — version control and project development

No external Python packages are required for the currently reviewed CLI implementation.

## 🚀 Getting started

### Requirements

- Python 3 installed
- Git (optional, for cloning)

### Run locally

1. Clone your Life OS repository, or download its source files.
2. Open a terminal in the repository folder.
3. Run the file containing the application's CLI entry point:

```bash
python main.py
```

If `main.py` is inside a `src/` directory, run:

```bash
python src/main.py
```

> The exact command depends on your repository's folder layout. Keep `planner.py` and `storage.py` importable by `main.py`.

The application displays an interactive menu:

```text
LIFE OS
Planner

Menu:
1. Ver tarefas
2. Adicionar tarefa
3. Concluir tarefa
4. remover tarefa
5. Sair
```

The current CLI prompts are in Portuguese.

## 📂 Project organization

The prototype separates responsibilities into three Python modules:

```text
LifeOS/
├── main.py       # CLI and user interaction
├── planner.py    # Task operations
├── storage.py    # Loading and saving task data
└── data/
    └── tasks.json  # Local persistent data (created/used by storage)
```

*Illustrative layout: your repository may place Python files inside another directory.*

### How it works

1. **`main.py`** receives a command from the user.
2. **`planner.py`** handles the requested task operation.
3. **`storage.py`** reads or writes the task collection in JSON.
4. The CLI displays the result and continues until the user exits.

A typical task record contains:

```json
{
  "id": 1,
  "title": "Study Python",
  "completed": false
}
```

Task IDs and the task collection are persisted locally, allowing data to be loaded across sessions.

## 🗺️ Roadmap

- [x] Build the first CLI task planner
- [x] Implement task creation, listing, completion, and removal
- [x] Add JSON-based persistence
- [x] Separate CLI, planner logic, and storage
- [ ] Complete task priority integration
- [ ] Add automated tests and more robust validation
- [ ] Extend tasks with scheduling and categories
- [ ] Design and build the graphical interface
- [ ] Introduce new personal-organization modules
- [ ] Integrate modules into a unified Life OS

## 🎯 Why I'm building this

Life OS is both a practical personal organization project and a way to improve my software development skills through **modular architecture, data persistence, clean code, and iterative development**.

The goal is to build something useful, understandable, and extensible—starting small and improving it with each milestone.

## 👩‍💻 Author

Developed by **[Bruna Sant'Ana](https://github.com/bruniibs)**.

---

<div align="center">
  <sub>Made with Python · Growing one feature at a time ✦</sub>
</div>
