# NOXARIA

**A modular, extensible personal AI assistant built with Python and Django.**

Noxaria aims to become a personal assistant that combines natural-language understanding, knowledge retrieval, desktop automation, and system monitoring through a unified interface.

The project prioritizes modularity, lightweight components, user control, and the ability to switch between local and cloud-based AI providers.

> **Development status:** Early development. The Django project and initial assistant interface are being built. Intent recognition, RAG, AI integrations, and desktop automation are planned components, not yet completed features.

---

## Table of Contents

- [Vision](#vision)
- [Core Principles](#core-principles)
- [Planned Features](#planned-features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development Roadmap](#development-roadmap)
- [Security](#security)
- [Design Philosophy](#design-philosophy)
- [Contributing](#contributing)
- [License](#license)

---

## Vision

Noxaria is designed to be more than a chatbot. Its long-term goal is to act as a practical assistant that understands user requests, retrieves relevant information, and performs approved tasks through controlled software modules.

The intended system will support both local and cloud-based intelligence, allowing users to balance privacy, performance, capability, and hardware limitations.

The long-term vision includes:

- Natural-language interaction.
- Intelligent application and file management.
- Local knowledge retrieval.
- Task and reminder management.
- System and application monitoring.
- Optional voice interaction.
- Configurable local and cloud AI backends.

---

## Core Principles

### 1. Modular architecture

Each major capability should be independently testable and replaceable.

The interface, intent classifier, retrieval system, AI provider, and action handlers should not be tightly coupled.

### 2. Lightweight intelligence

Noxaria will investigate compact embedding models such as Sentence-BERT (SBERT) for semantic intent recognition and search.

Large language models should be used where their capabilities justify the additional resource cost, rather than for every operation.

### 3. Local-first where practical

Local processing should be preferred when it provides adequate performance and capability.

Cloud APIs may be used as optional providers for tasks that benefit from stronger language understanding or generation.

### 4. Controlled automation

Recognizing a command is not the same as safely executing it.

Actions should pass through validation, permission checks, and explicit handlers before interacting with the operating system.

### 5. Incremental development

Noxaria will be built in small, testable stages. Features should be validated before additional complexity is introduced.

---

## Planned Features

| Component | Purpose | Status |
|---|---|---|
| Django web interface | Main dashboard and interaction interface | Initial development |
| Intent recognition | Identify the user's intended task | Planned |
| Entity extraction | Extract application names, paths, times, and other parameters | Planned |
| Action router | Dispatch recognized intents to approved handlers | Planned |
| SBERT embeddings | Semantic similarity and intent matching | Under consideration for implementation |
| RAG subsystem | Retrieve relevant information from indexed documents | Planned |
| AI provider adapter | Switch between supported local and cloud models | Planned |
| Application launcher | Open approved desktop applications | Planned |
| File management | Search and manage files through controlled operations | Planned |
| Reminders and tasks | Create and manage scheduled tasks | Planned |
| System monitoring | Collect relevant system and application metrics | Planned |
| Voice interface | Speech input and optional text-to-speech | Planned |
| Persistent storage | Save configuration, reminders, and other required state | Planned |

---

## Architecture

Noxaria is intended to use a modular architecture in which Django provides the web interface and request-handling layer, while the assistant's core capabilities live in separate Python modules.

### Request processing

The planned request flow is:

1. Receive a user message through the interface.
2. Normalize the input and classify the intent.
3. Extract required entities and parameters.
4. Route the request to an approved handler or retrieval subsystem.
5. Validate permissions and execute the requested operation when applicable.
6. Return the result to the interface.

### Intent recognition

The initial candidate is a pretrained SBERT sentence-embedding model, such as `all-MiniLM-L6-v2`.

The classifier will compare incoming messages with representative examples of supported intents. Unknown or ambiguous requests should be rejected or clarified rather than forced into an incorrect category.

Fine-tuning may be introduced if evaluation shows that the pretrained model does not meet the project's accuracy requirements.

### Retrieval-augmented generation

RAG will be an optional subsystem for requests that require information from project documentation, notes, or other indexed content.

The intended pipeline is:

1. Convert source documents into searchable passages.
2. Generate embeddings and build a local retrieval index.
3. Retrieve relevant passages for a user query.
4. Optionally pass the retrieved context to a language model.
5. Return an answer grounded in the retrieved material.

Direct actions, such as opening an approved application, should not require RAG.

### AI provider abstraction

Local and cloud models should be accessed through a common provider interface.

This will allow the project to switch providers without rewriting the intent router, interface, or action handlers.

### Separation of responsibilities

- **Django:** Web requests, routing, templates, and interface integration.
- **Intent module:** Intent classification and confidence evaluation.
- **Retrieval module:** Document indexing and semantic search.
- **AI provider module:** Optional language-model inference.
- **Action modules:** Approved system and application operations.
- **Storage module:** Persistent application state when required.

Django is the web framework, not the assistant's entire intelligence or automation engine.

---

## Technology Stack

| Technology | Intended role |
|---|---|
| Python | Primary programming language |
| Django 5.2 | Web framework |
| HTML and CSS | Interface and styling |
| JavaScript | Client-side interaction |
| Sentence Transformers | Sentence embeddings and semantic similarity |
| PyTorch | Model inference where required by the selected model |
| Local vector index | Semantic document retrieval |
| SQLite | Initial development database |
| Local or cloud LLM APIs | Optional natural-language generation |

The exact model, retrieval library, and storage backend will be selected through testing. Not every component needs to be installed at the beginning.

---

## Project Structure

The following is the intended direction for the codebase. Some modules are planned and may not exist yet.

```text
noxaria-diamond/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── templates/
│   │   └── core/
│   │       └── home.html
│   ├── static/
│   │   └── core/
│   │       └── style.css
│   ├── ai/
│   │   ├── intent_classifier.py
│   │   ├── entity_extractor.py
│   │   └── providers/
│   ├── retrieval/
│   │   ├── indexer.py
│   │   └── search.py
│   ├── actions/
│   │   ├── applications.py
│   │   └── files.py
│   ├── services/
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── manage.py
├── main.py
├── README.md
└── requirements.txt
```

The AI, retrieval, action, and service directories are proposed modules, not necessarily part of the current implementation. The structure will evolve as requirements become clearer.

---

## Getting Started

### Requirements

- Windows 11 or another supported operating system.
- Python 3.11 for the current development environment.
- Django 5.2.
- PyCharm or another Python-compatible editor.
- Git (recommended).

### 1. Clone the repository

If the project is hosted on Git:

```bash
git clone <repository-url>
cd noxaria-diamond
```

If you already have the project locally, open its existing directory instead.

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
py -3.11 -m venv .noxaria
```

Activate it:

```powershell
.\.noxaria\Scripts\Activate.ps1
```

If the environment already exists and is configured in PyCharm, activate that environment rather than creating another one.

### 3. Install dependencies

Upgrade pip and install Django:

```powershell
python -m pip install --upgrade pip
python -m pip install "Django>=5.2,<6.0"
```

Additional AI dependencies should be installed only when their corresponding modules are introduced.

### 4. Run database migrations

```powershell
python manage.py migrate
```

### 5. Start the development server

```powershell
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

The development server is intended for local development, not public production deployment.

---

## Development Roadmap

### Phase 1 — Foundation

- [x] Create the Django project.
- [x] Create and register the `core` app.
- [x] Configure the initial homepage route.
- [ ] Build the reusable dashboard interface.
- [ ] Separate templates, styling, and application logic.
- [ ] Establish basic tests and configuration practices.

### Phase 2 — Intent recognition

- [ ] Create an independent intent-classification module.
- [ ] Define the initial supported intent categories.
- [ ] Build a representative command dataset.
- [ ] Benchmark a pretrained SBERT model.
- [ ] Implement confidence thresholds and unknown-intent handling.
- [ ] Evaluate fine-tuning only if the baseline needs improvement.

### Phase 3 — Controlled action system

- [ ] Build a central intent router.
- [ ] Extract and validate command parameters.
- [ ] Add approved application-launching operations.
- [ ] Add safe file-search operations.
- [ ] Introduce permission checks, confirmations, and audit logging.

### Phase 4 — Knowledge retrieval

- [ ] Implement document ingestion.
- [ ] Split documents into searchable passages.
- [ ] Build a local semantic index.
- [ ] Evaluate retrieval quality.
- [ ] Add grounded answer generation through an optional LLM.

### Phase 5 — AI providers

- [ ] Define a common provider interface.
- [ ] Integrate a compatible local model.
- [ ] Add optional cloud providers.
- [ ] Implement provider selection and fallback behavior.
- [ ] Measure latency, memory usage, and answer quality.

### Phase 6 — Personal assistant capabilities

- [ ] Reminders and task management.
- [ ] Application and system monitoring.
- [ ] Voice input and text-to-speech.
- [ ] User preferences and persistent state.
- [ ] Additional desktop automation modules.

---

## Security

Noxaria is intended to interact with local files and applications, so security must be part of its architecture.

Planned safeguards include:

- Allowlisted actions rather than arbitrary command execution.
- Input validation and path restrictions.
- Confirmation for destructive or sensitive operations.
- Separation between model-generated text and executable instructions.
- Protection of API keys and other secrets through environment variables.
- Restricted access to files and system operations.
- Logging of important actions without unnecessarily storing private content.
- Authentication and appropriate deployment settings before any network exposure.

A language model or intent classifier must never be treated as a security boundary.

---

## Design Philosophy

The interface is intended to use a dark, cyberpunk-inspired visual style with clean layouts, restrained neon accents, and a command-center aesthetic.

The user experience should emphasize:

- Clarity over unnecessary animation.
- Fast access to common tasks.
- Visible system status.
- Transparent feedback when actions succeed or fail.
- Clear distinction between available features and features still under development.

---

## Contributing

Noxaria is under active development.

Before introducing a major dependency or architectural change:

1. Identify the problem it solves.
2. Measure whether a simpler solution is sufficient.
3. Keep modules independently testable.
4. Document security implications.
5. Evaluate performance on the target hardware.

Small, verified improvements are preferred over premature complexity.

---

## License

No license has been specified yet. Until one is selected, all rights remain with the applicable copyright holder. Add an explicit open-source license before distributing the project under open-source terms.

---

**NOXARIA — A personal assistant built around modular intelligence, controlled automation, and user choice.**
