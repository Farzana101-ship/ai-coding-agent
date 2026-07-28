# AI Coding Agent

## Overview

This project implements a lightweight AI Coding Agent in Python that analyzes an existing codebase, creates an execution plan, identifies the files that need to be updated, applies repository modifications, and summarizes the completed work.

The target application used for this assignment is the EasyNotes Node.js application:
https://github.com/callicoder/node-easy-notes-app

The product request given to the agent was:

> Improve the application so users can better organise and search their notes.

The agent analyzes the repository and determines that adding **tags** and **search functionality** is an appropriate solution while preserving the existing CRUD functionality.

---

# Architecture

The project is divided into small, modular components.

```
ai-coding-agent/
│
├── main.py
├── repository_explorer.py
├── planner.py
├── code_modifier.py
├── summarizer.py
├── requirements.txt
└── README.md
```

## Components

### main.py

Acts as the entry point of the application.

Responsibilities:

- Starts the workflow
- Explores the repository
- Generates the execution plan
- Calls the repository modifier
- Displays the final summary

---

### repository_explorer.py

Responsible for repository analysis.

Functions:

- Scan the target repository recursively
- Identify source files
- Read file contents
- Return project structure

---

### planner.py

Responsible for planning.

Functions:

- Understand the repository
- Identify relevant files
- Create an execution plan
- Return files that should be modified

---

### code_modifier.py

Responsible for repository modification.

Current implementation automatically updates selected files by applying deterministic code changes.

Implemented modifications include:

- Adding Tags support
- Updating controller logic
- Updating application routes

---

### summarizer.py

Responsible for displaying the final summary.

Outputs:

- Repository summary
- Features implemented
- Files modified

---

# Agent Workflow

```
Start
   │
   ▼
Explore Repository
   │
   ▼
Identify Important Files
   │
   ▼
Create Execution Plan
   │
   ▼
Modify Repository
   │
   ▼
Generate Summary
   │
   ▼
End
```

---

# Repository Exploration

The repository explorer scans the target project recursively.

For the EasyNotes repository, it identifies the following files as relevant:

- app/models/note.model.js
- app/controllers/note.controller.js
- app/routes/note.routes.js

These files contain the application's data model, business logic, and API definitions.

---

# Product Requirement

Input:

> Improve the application so users can better organise and search their notes.

The agent determines that the following enhancements satisfy the requirement:

- Tags for organising notes
- Search functionality for retrieving notes efficiently

---

# Features Implemented

## 1. Tags Support

Added a new field to the Note model:

```javascript
tags: [String]
```

This allows each note to contain multiple tags.

Example:

```json
{
  "title": "React Interview",
  "content": "Revise Hooks",
  "tags": ["react", "frontend"]
}
```

---

## 2. Search Support

Implemented a search endpoint that enables searching notes by:

- Title
- Content
- Tags

Example:

```
GET /notes?search=react
```

---

## 3. Existing CRUD Preserved

The existing APIs remain unchanged.

Supported operations:

- Create Note
- Retrieve Notes
- Retrieve Single Note
- Update Note
- Delete Note

---

# Files Modified

```
app/models/note.model.js
app/controllers/note.controller.js
app/routes/note.routes.js
```

---

# Assumptions

- The repository is already functional.
- Existing CRUD APIs should remain compatible.
- Tags provide a lightweight organisation mechanism.
- Search should be implemented without introducing additional external dependencies.

---

# Trade-offs

To keep the implementation focused within the assignment time limit:

- Search is implemented using simple matching instead of advanced indexing.
- Tags are stored as an array of strings.
- The implementation focuses on backend improvements only.

Future improvements could include:

- AI-generated code patches
- Automatic Git commits
- Test generation
- Semantic search
- Vector embeddings
- Multi-step planning with validation

---

# How to Run

## 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

---

## 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run the AI Agent

```bash
python main.py
```

---

# Example Output

```
Scanning repository...

Repository Summary
----------------------------------------
Node.js Express Notes CRUD application using MongoDB.

Execution Plan
----------------------------------------
• Explore repository structure
• Identify model, controller and route files
• Add tags support
• Implement search functionality
• Update CRUD operations while preserving existing behaviour
• Generate summary of changes

Files to Modify
----------------------------------------
note.model.js
note.controller.js
note.routes.js

Modifying repository...

✔ note.model.js already updated
✔ note.controller.js already updated
✔ note.routes.js already updated

Repository updated successfully.

Summary
----------------------------------------
✔ Added Tags support
✔ Added Search endpoint
✔ Existing CRUD APIs preserved
```

---

# Technologies Used

- Python 3.12
- Node.js
- Express.js
- MongoDB
- Mongoose
- Git
- GitHub

---

# Future Improvements

Potential enhancements include:

- Integrating an LLM to generate code patches dynamically.
- Automatic validation of modified code.
- Support for multiple programming languages.
- Automatic pull request generation.
- Test execution after modifications.
- Smarter repository understanding using embeddings.

---

# Author

**Farzana Kauser**