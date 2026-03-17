# 🌿 Homeopathy AI Assistant

An AI-powered repertory tool for experienced homeopathy practitioners.
Cross-references symptoms against Kent's Repertory and Boericke's Materia Medica,
returning the top 3 ranked remedies with matching rubrics, contradictions, and
decisive modalities.

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Provide your Groq API key

**Option A – environment variable (recommended)**

```bash
# macOS / Linux
export GROQ_API_KEY="gsk_..."

# Windows PowerShell
$env:GROQ_API_KEY = "gsk_..."

# Windows Command Prompt
set GROQ_API_KEY=gsk_...
```

**Option B – Streamlit secrets**
Create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "gsk_..."
```

**Option C – sidebar input**
Paste the key directly into the sidebar at runtime (stored in session state only).

Get a free API key at [console.groq.com](https://console.groq.com).

### 3. Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## Usage

1. Type symptoms in natural language into the text box.
   Include chief complaint, location, sensation, modalities (worse/better), and onset.
2. Click **Find Remedies**.
3. The app extracts structured symptoms, displays them as chips, then shows
   the top 3 remedies with:
   - Match percentage (animated progress bar)
   - Matching rubrics / materia medica pointers
   - Contradictions (symptoms that don't fit)
   - Core character of each remedy
   - Decisive modalities and a confidence note

---

## Model

`llama-3.3-70b-versatile` via the Groq API.
Temperature is kept low (0.25) for consistent, repeatable analysis.

---

## Disclaimer

This tool supports practitioner decision-making.
Final judgement always rests with the practitioner.
