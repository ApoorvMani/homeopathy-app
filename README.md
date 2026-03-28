# 🌿 Homeopathy AI Assistant

An AI-powered repertory tool for experienced homeopathy practitioners.
Cross-references symptoms against Kent's Repertory and Boericke's Materia Medica,
returning the top 3 ranked remedies with matching rubrics, contradictions, and
decisive modalities.

**Live demo →** [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://homeopathy-app.streamlit.app)

---

## Features

- **Natural language input** — describe symptoms, modalities, and onset in plain text
- **Structured symptom extraction** — displayed as chips before analysis
- **Top 3 remedies** ranked by match strength with animated progress bars
- **Kent's Repertory + Boericke's Materia Medica** cross-reference on every result
- **Contradictions shown honestly** — symptoms that don't fit each remedy
- **Decisive modalities panel** — the key differentiators between remedies
- **Confidence note** — practitioner-facing summary of analysis certainty

---

## Stack

| Layer | Technology |
|-------|-----------|
| UI | [Streamlit](https://streamlit.io) |
| LLM | `llama-3.3-70b-versatile` via [Groq](https://groq.com) |
| Styling | Custom CSS (Playfair Display + Crimson Pro) |

---

## Local Setup

### 1. Clone and install

```bash
git clone https://github.com/ApoorvMani/homeopathy-app.git
cd homeopathy-app
pip install -r requirements.txt
```

### 2. Provide your Groq API key

**Option A — environment variable (recommended)**

```bash
# macOS / Linux
export GROQ_API_KEY="gsk_..."

# Windows PowerShell
$env:GROQ_API_KEY = "gsk_..."

# Windows Command Prompt
set GROQ_API_KEY=gsk_...
```

**Option B — Streamlit secrets**

Create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "gsk_..."
```

**Option C — sidebar input**

Paste the key directly into the sidebar at runtime (stored in session state only).

Get a free API key at [console.groq.com](https://console.groq.com).

### 3. Run

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`.

---

## Deploy to Streamlit Community Cloud

1. Fork or push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select the repo, set **Main file path** to `app.py`
4. Add `GROQ_API_KEY` under **Advanced settings → Secrets**:
   ```toml
   GROQ_API_KEY = "gsk_..."
   ```
5. Click **Deploy**

---

## Usage

1. Enter symptoms in natural language — include chief complaint, location, sensation, modalities (worse/better), and onset
2. Click **Find Remedies**
3. The app extracts structured symptoms as chips, then shows the top 3 remedies with:
   - Match percentage with animated progress bar
   - Matching rubrics / materia medica pointers
   - Contradictions (symptoms that don't fit)
   - Core character of each remedy
   - Decisive modalities and a confidence note

---

## Model

`llama-3.3-70b-versatile` via the Groq API. Temperature 0.25 for consistent, repeatable analysis.

---

## Disclaimer

This tool supports practitioner decision-making.
Final judgement always rests with the practitioner.
