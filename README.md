# Workflow Engine

## Overview

Workflow Engine executes configurable workflows defined in JSON files.

---

## Features

- JSON-based workflows
- Dynamic execution
- Step-by-step processing
- Extensible architecture

---

## Files

- workflow_parser.py
- workflow_runner.py

---

## Usage

```bash
python workflow_runner.py
```

---

## Example

Workflow File:

resume_workflow.json

```json
{
    "name": "Resume Processing",
    "steps": [
        {"action": "Extract Text"},
        {"action": "Find Skills"},
        {"action": "Generate Report"},
        {"action": "Save Output"}
    ]
}
```

Output:

```text
WORKFLOW ENGINE

Workflow: Resume Processing

▶ Executing: Extract Text
✓ Completed: Extract Text

▶ Executing: Find Skills
✓ Completed: Find Skills

▶ Executing: Generate Report
✓ Completed: Generate Report

▶ Executing: Save Output
✓ Completed: Save Output

🚀 Workflow Finished
```

---

## Future Improvements

- Plugin System
- Custom Actions
- Conditional Steps
- Parallel Execution
- API Integration
- File Processing
- Database Actions