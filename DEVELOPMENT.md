# Development Setup Guide

This guide is for **developers and contributors** working on the RAG package itself.

## 🚀 Quick Development Setup

### 1. **Clone and Setup Virtual Environment**

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd lawfirm-rag-package

# 2. Create virtual environment (Python 3.11+ required)
python3.11 -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install package in editable mode with dev dependencies
pip install -e ".[dev,web,gui,all]"

# 5. Verify installation
rag --help
```

### 2. **Task Master Project Management**

This project uses **Task Master** for development workflow management:

```bash
# View current development tasks
task-master list

# Get the next task to work on
task-master next

# View specific task details
task-master show <task-id>

# Mark task as complete
task-master set-status --id=<task-id> --status=done

# Add new development tasks
task-master add-task --prompt="Implement new feature X"
```

## 🛠️ Development Workflow

### **Standard Development Process:**

1. **Check current tasks:**
   ```bash
   task-master list --status=pending
   ```

2. **Get next task:**
   ```bash
   task-master next
   ```

3. **Work on the task** (following the task details)

4. **Test your changes:**
   ```bash
   # Run tests
   pytest tests/
   
   # Test CLI
   rag serve --reload
   
   # Test package build
   pip install -e .
   ```

5. **Mark task complete:**
   ```bash
   task-master set-status --id=<task-id> --status=done
   ```

6. **Commit changes:**
   ```bash
   git add .
   git commit -m "feat: implement task <task-id> - <description>"
   ```

## 📋 Development Environment Features

### **Virtual Environment Benefits:**
- ✅ **Isolation** - Won't conflict with other Python projects
- ✅ **Exact Dependencies** - Uses pinned versions from pyproject.toml
- ✅ **Editable Install** - Changes to code immediately available
- ✅ **Dev Tools** - Includes pytest, black, mypy, etc.

### **Task Master Benefits:**
- ✅ **Organized Workflow** - Clear task prioritization and dependencies
- ✅ **Progress Tracking** - See what's done and what's next
- ✅ **Task Details** - Implementation guidance for each task
- ✅ **Team Coordination** - Shared task visibility

## 🧪 Testing

### **Run Tests:**
```bash
# All tests
pytest

# With coverage
pytest --cov=lawfirm_rag

# Specific test file
pytest tests/test_document_processor.py

# Watch mode (reruns on changes)
pytest-watch
```

### **Code Quality:**
```bash
# Format code
black lawfirm_rag/

# Check imports
isort lawfirm_rag/

# Type checking
mypy lawfirm_rag/

# Linting
flake8 lawfirm_rag/
```

## 📦 Package Development

### **Build and Test Package:**
```bash
# Build package
python -m build

# Install locally from build
pip install dist/rag-package-*.whl

# Test installed package
rag serve
```

### **Development Server:**
```bash
# Run with auto-reload for development
rag serve --reload --verbose
```

## 🔧 Configuration

### **Development Configuration:**
Create a `config.dev.yaml` for development settings:

```yaml
# config.dev.yaml
api:
  host: "127.0.0.1"
  port: 8000
  cors: true

logging:
  level: DEBUG
  
llm:
  backend: ollama
  models:
    development: llama3.2
```

## 🚀 Deployment Testing

### **Test Production-like Install:**
```bash
# Create clean test environment
python3.11 -m venv test_env
test_env/Scripts/activate  # Windows
# or
source test_env/bin/activate  # Mac/Linux

# Install as end user would
pip install .

# Test end-user experience
rag serve
```

## 📁 Project Structure

```
lawfirm-rag-package/
├── venv/                    # Development virtual environment
├── tasks/                   # Task Master tasks
├── scripts/                 # Task Master scripts
├── lawfirm_rag/            # Main package code
├── tests/                   # Test suite
├── pyproject.toml          # Package configuration
├── requirements.txt        # Pinned dependencies
├── DEVELOPMENT.md          # This file
└── README.md              # User documentation
```

## 🤝 Contributing

1. **Setup development environment** (steps above)
2. **Check tasks:** `task-master list`
3. **Work on a task:** `task-master next`
4. **Create feature branch:** `git checkout -b feature/task-<id>-description`
5. **Make changes and test**
6. **Update tasks:** `task-master set-status --id=<id> --status=done`
7. **Commit:** `git commit -m "feat: implement task <id>"`
8. **Push and create PR**

---

## 💡 Pro Tips

- **Always activate venv** before development work
- **Use Task Master** to track progress and get organized workflow
- **Test both development and production installs** 
- **Run tests before committing**
- **Use `rag serve --reload`** for fast development iteration 