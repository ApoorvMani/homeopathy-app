import streamlit as st
import json
import os

st.set_page_config(
    page_title="Homeopathy AI",
    page_icon="🌿",
    layout="centered",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Crimson+Pro:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --forest:       #162d20;
    --forest-mid:   #2a5239;
    --sage:         #3d7a52;
    --sage-light:   #5fa070;
    --mint:         #9dd4af;
    --cream:        #f6f1e8;
    --cream-dark:   #ede7da;
    --parchment:    #cfc5aa;
    --text-dark:    #19271e;
    --text-mid:     #3b5446;
    --text-light:   #6a8878;
    --gold:         #c8a44a;
    --gold-light:   #e6c87a;
    --red-soft:     #b83232;
    --card-bg:      #ffffff;
    --card-border:  #ddd6c8;
    --progress-bg:  #deeae2;
}

/* ── Base ─────────────────────────────────────────────────────────────────── */
.stApp {
    background-color: var(--cream);
    font-family: 'Crimson Pro', Georgia, serif;
}
.main .block-container {
    max-width: 780px;
    padding-top: 2.2rem;
    padding-bottom: 4rem;
    padding-left: 2rem;
    padding-right: 2rem;
}
h1, h2, h3 {
    font-family: 'Playfair Display', Georgia, serif;
    color: var(--forest);
}

/* ── Sidebar ─────────────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: var(--forest) !important;
}
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stMarkdown div,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] small {
    color: var(--cream) !important;
}
[data-testid="stSidebar"] .stTextInput > div > div > input {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid var(--sage) !important;
    color: var(--cream) !important;
    border-radius: 6px !important;
}
[data-testid="stSidebar"] .stTextInput > div > div > input::placeholder {
    color: rgba(168, 213, 181, 0.5) !important;
}
[data-testid="stSidebar"] .stTextInput > label {
    color: var(--mint) !important;
    font-family: 'Crimson Pro', serif !important;
    font-size: 0.9rem !important;
}

/* ── Page header ─────────────────────────────────────────────────────────── */
.app-header {
    margin-bottom: 1.6rem;
}
.app-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.1rem;
    font-weight: 700;
    color: var(--forest);
    letter-spacing: -0.5px;
    line-height: 1.2;
    margin: 0 0 0.25rem 0;
}
.app-subtitle {
    font-family: 'Crimson Pro', serif;
    font-size: 1.05rem;
    color: var(--text-light);
    font-style: italic;
    margin: 0;
}
.botanical-divider {
    border: none;
    height: 2px;
    background: linear-gradient(
        to right,
        transparent 0%,
        var(--parchment) 15%,
        var(--sage)     45%,
        var(--gold)     50%,
        var(--sage)     55%,
        var(--parchment) 85%,
        transparent 100%
    );
    margin: 1.4rem 0;
}

/* ── Input area ──────────────────────────────────────────────────────────── */
.stTextArea > label { display: none !important; }
.stTextArea > div > div > textarea {
    font-family: 'Crimson Pro', serif !important;
    font-size: 1.05rem !important;
    background: white !important;
    border: 2px solid var(--cream-dark) !important;
    border-radius: 10px !important;
    color: var(--text-dark) !important;
    padding: 1rem 1.1rem !important;
    line-height: 1.6 !important;
    transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
    resize: vertical !important;
}
.stTextArea > div > div > textarea:focus {
    border-color: var(--sage) !important;
    box-shadow: 0 0 0 3px rgba(61, 122, 82, 0.12) !important;
    outline: none !important;
}

/* ── Button ──────────────────────────────────────────────────────────────── */
.stButton > button {
    background: var(--forest-mid) !important;
    color: var(--cream) !important;
    font-family: 'Crimson Pro', serif !important;
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.4px !important;
    border: none !important;
    border-radius: 7px !important;
    padding: 0.55rem 1.8rem !important;
    transition: background 0.2s ease, transform 0.15s ease, box-shadow 0.2s ease !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    background: var(--forest) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 5px 14px rgba(22, 45, 32, 0.28) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── Symptom chips ───────────────────────────────────────────────────────── */
.chips-section-label {
    font-family: 'Playfair Display', serif;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: var(--text-light);
    margin: 1.2rem 0 0.6rem 0;
}
.symptom-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-bottom: 0.5rem;
}
.chip {
    background: var(--forest-mid);
    color: #d4eed9;
    font-family: 'Crimson Pro', serif;
    font-size: 0.85rem;
    font-weight: 500;
    padding: 0.28rem 0.85rem;
    border-radius: 20px;
    display: inline-block;
    letter-spacing: 0.2px;
}

/* ── Remedy card ─────────────────────────────────────────────────────────── */
.remedy-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-left: 5px solid var(--sage);
    border-radius: 12px;
    padding: 1.4rem 1.5rem 1.2rem 1.5rem;
    margin: 1.3rem 0 0 0;
    box-shadow: 0 2px 10px rgba(22, 45, 32, 0.07);
}
.remedy-card-header {
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
    margin-bottom: 0.2rem;
}
.rank-badge {
    flex-shrink: 0;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: var(--gold);
    color: white;
    font-family: 'Playfair Display', serif;
    font-size: 0.8rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 4px;
}
.remedy-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--forest);
    line-height: 1.2;
    margin: 0;
    flex: 1;
}
.core-character {
    font-family: 'Crimson Pro', serif;
    font-size: 0.98rem;
    color: var(--text-light);
    font-style: italic;
    margin: 0.35rem 0 1rem 2.3rem;
    line-height: 1.5;
}
.match-label-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.4rem;
}
.match-label {
    font-family: 'Crimson Pro', serif;
    font-size: 0.92rem;
    font-weight: 500;
    color: var(--text-mid);
}
.match-pct-badge {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--sage);
}
.progress-track {
    background: var(--progress-bg);
    border-radius: 6px;
    height: 9px;
    margin-bottom: 1.1rem;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    border-radius: 6px;
    background: linear-gradient(90deg, var(--sage) 0%, var(--forest-mid) 100%);
    transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}
.card-section-label {
    font-family: 'Playfair Display', serif;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 1.1px;
    text-transform: uppercase;
    color: var(--sage);
    margin: 0.9rem 0 0.45rem 0;
}
.card-section-label-contra {
    font-family: 'Playfair Display', serif;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 1.1px;
    text-transform: uppercase;
    color: var(--red-soft);
    margin: 0.9rem 0 0.45rem 0;
}
.match-item, .contra-item {
    font-family: 'Crimson Pro', serif;
    font-size: 0.97rem;
    color: var(--text-dark);
    padding: 0.2rem 0 0.2rem 1.3rem;
    position: relative;
    line-height: 1.5;
}
.match-item::before {
    content: '✓';
    color: var(--sage);
    position: absolute;
    left: 0;
    font-size: 0.82rem;
    top: 0.28rem;
    font-weight: 700;
}
.contra-item::before {
    content: '✗';
    color: var(--red-soft);
    position: absolute;
    left: 0;
    font-size: 0.82rem;
    top: 0.28rem;
    font-weight: 700;
}

/* ── Analysis box ────────────────────────────────────────────────────────── */
.analysis-box {
    background: var(--forest);
    border-radius: 10px;
    padding: 1.3rem 1.5rem;
    margin: 1.8rem 0 0.5rem 0;
}
.analysis-title {
    font-family: 'Playfair Display', serif;
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 0.8px;
    color: var(--mint);
    margin: 0 0 0.6rem 0;
    text-transform: uppercase;
}
.analysis-item {
    font-family: 'Crimson Pro', serif;
    font-size: 0.97rem;
    color: #cce8d4;
    padding: 0.18rem 0 0.18rem 1.2rem;
    position: relative;
    line-height: 1.5;
}
.analysis-item::before {
    content: '◆';
    color: var(--gold);
    position: absolute;
    left: 0;
    font-size: 0.55rem;
    top: 0.42rem;
}
.confidence-note {
    background: linear-gradient(135deg, rgba(42,82,57,0.9), rgba(61,122,82,0.8));
    border: 1px solid rgba(157, 212, 175, 0.2);
    border-radius: 7px;
    padding: 0.75rem 1.1rem;
    margin-top: 1.1rem;
    font-family: 'Crimson Pro', serif;
    font-size: 1rem;
    font-style: italic;
    color: #e0f0e6;
    line-height: 1.55;
}
.confidence-icon {
    margin-right: 0.4rem;
    font-style: normal;
}

/* ── Error / raw response ────────────────────────────────────────────────── */
.raw-response-box {
    background: #f2ede4;
    border: 1px solid var(--parchment);
    border-radius: 8px;
    padding: 1.1rem 1.3rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    white-space: pre-wrap;
    max-height: 420px;
    overflow-y: auto;
    color: var(--text-dark);
    line-height: 1.6;
    margin-top: 0.8rem;
}

/* ── Disclaimer ──────────────────────────────────────────────────────────── */
.disclaimer {
    font-family: 'Crimson Pro', serif;
    font-size: 0.88rem;
    color: var(--text-light);
    text-align: center;
    border-top: 1px solid var(--card-border);
    padding-top: 1.2rem;
    margin-top: 2.5rem;
    font-style: italic;
    line-height: 1.6;
}

/* ── Spinner text ────────────────────────────────────────────────────────── */
[data-testid="stSpinner"] p {
    font-family: 'Crimson Pro', serif !important;
    font-size: 1rem !important;
    color: var(--text-mid) !important;
}

/* ── Warning / error tweaks ──────────────────────────────────────────────── */
.stAlert {
    border-radius: 8px !important;
    font-family: 'Crimson Pro', serif !important;
    font-size: 0.97rem !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div style="padding:0.8rem 0 1rem 0;">
            <div style="font-family:'Playfair Display',serif;font-size:1.45rem;
                        font-weight:700;color:#9dd4af;line-height:1.2;margin-bottom:0.35rem;">
                🌿 Homeopathy AI
            </div>
            <div style="font-family:'Crimson Pro',serif;font-size:0.88rem;
                        color:#5fa070;font-style:italic;letter-spacing:0.3px;">
                Repertory Assistant &nbsp;·&nbsp; v1.0
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """<hr style="border:none;border-top:1px solid rgba(61,122,82,0.4);margin:0 0 1rem 0;">""",
        unsafe_allow_html=True,
    )

    api_key_input = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="gsk_…",
        help="Only needed if GROQ_API_KEY env variable is not set.",
    )
    if api_key_input:
        st.session_state["groq_api_key"] = api_key_input

    st.markdown(
        """
        <div style="margin-top:1.5rem;font-family:'Crimson Pro',serif;
                    font-size:0.82rem;color:#5fa070;line-height:1.6;">
            Uses Kent's Repertory &amp; Boericke's Materia Medica via<br>
            <strong style="color:#9dd4af;">llama-3.3-70b-versatile</strong> on Groq.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Helpers ────────────────────────────────────────────────────────────────────
def get_api_key() -> str | None:
    if st.session_state.get("groq_api_key"):
        return st.session_state["groq_api_key"]
    if "GROQ_API_KEY" in os.environ:
        return os.environ["GROQ_API_KEY"]
    try:
        return st.secrets["GROQ_API_KEY"]
    except Exception:
        return None


SYSTEM_PROMPT = """\
You are an expert homeopathic repertory assistant with complete knowledge of \
Kent's Repertory and Boericke's Materia Medica. \
The practitioner using this tool is experienced — do not explain basics. \
Be precise, cite specific rubrics and materia medica characteristics. \
Always show contradictions honestly.

Return your response as structured JSON with this EXACT schema (no markdown, \
no code fences, raw JSON only):

{
  "extracted_symptoms": ["symptom1", "symptom2"],
  "remedies": [
    {
      "name": "Remedy Name",
      "match_percent": 85,
      "matching_symptoms": ["reason1", "reason2"],
      "contradictions": ["contradiction1"],
      "core_character": "one line summary"
    }
  ],
  "decisive_modalities": ["modality1"],
  "confidence_note": "note here"
}

Return exactly 3 remedies ranked by match strength. \
Return ONLY valid JSON — absolutely no markdown formatting, no code blocks, \
no commentary outside the JSON object.\
"""


def query_groq(symptoms_text: str, api_key: str) -> str:
    from groq import Groq  # imported here so missing install gives a clear error

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Patient symptoms: {symptoms_text}\n\n"
                    "Analyse and return the top 3 remedies as JSON."
                ),
            },
        ],
        temperature=0.25,
        max_tokens=2048,
    )
    return response.choices[0].message.content


def parse_response(raw: str) -> tuple[dict | None, str | None]:
    """Strip optional markdown fences then parse JSON. Returns (data, error)."""
    text = raw.strip()
    # Remove ```json … ``` or ``` … ``` wrappers if present
    if text.startswith("```"):
        lines = text.splitlines()
        # drop first and last fence lines
        inner = lines[1:] if len(lines) > 1 else lines
        if inner and inner[-1].strip() == "```":
            inner = inner[:-1]
        text = "\n".join(inner).strip()
    try:
        return json.loads(text), None
    except json.JSONDecodeError as exc:
        return None, str(exc)


def build_remedy_card_html(rank: int, remedy: dict) -> str:
    name      = remedy.get("name", "Unknown")
    match_pct = max(0, min(100, int(remedy.get("match_percent", 0))))
    core_char = remedy.get("core_character", "")
    matching  = remedy.get("matching_symptoms", [])
    contras   = remedy.get("contradictions", [])

    # matching items
    match_html = ""
    if matching:
        match_html = '<div class="card-section-label">Matching Symptoms</div>'
        for m in matching:
            match_html += f'<div class="match-item">{m}</div>'

    # contradiction items
    contra_html = ""
    if contras:
        contra_html = '<div class="card-section-label-contra">Contradictions</div>'
        for c in contras:
            contra_html += f'<div class="contra-item">{c}</div>'

    return f"""
<div class="remedy-card">
  <div class="remedy-card-header">
    <div class="rank-badge">{rank}</div>
    <div class="remedy-name">{name}</div>
  </div>
  <div class="core-character">{core_char}</div>

  <div class="match-label-row">
    <span class="match-label">Symptom match</span>
    <span class="match-pct-badge">{match_pct}%</span>
  </div>
  <div class="progress-track">
    <div class="progress-fill" style="width:{match_pct}%;"></div>
  </div>

  {match_html}
  {contra_html}
</div>
"""


# ── Main UI ────────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="app-header">
  <p class="app-title">🌿 Homeopathy AI Assistant</p>
  <p class="app-subtitle">Expert repertory analysis &nbsp;·&nbsp; Kent &amp; Boericke cross-reference</p>
</div>
<hr class="botanical-divider">
""",
    unsafe_allow_html=True,
)

symptoms_input: str = st.text_area(
    label="Symptoms",
    placeholder="Describe symptoms, modalities, onset…\n\nExample: dry cough worse at night, better sitting up, started after getting wet, restless",
    height=148,
    label_visibility="collapsed",
)

col_btn, col_spacer = st.columns([1, 3])
with col_btn:
    find_pressed = st.button("Find Remedies", use_container_width=True)

# ── Processing ─────────────────────────────────────────────────────────────────
if find_pressed:
    if not symptoms_input.strip():
        st.warning("Please describe the symptoms before searching.")
    else:
        api_key = get_api_key()
        if not api_key:
            st.error(
                "No Groq API key found. Paste one in the sidebar "
                "or set the `GROQ_API_KEY` environment variable."
            )
        else:
            with st.spinner("Cross-referencing repertory…"):
                try:
                    raw_response = query_groq(symptoms_input.strip(), api_key)
                except Exception as exc:
                    st.error(f"Groq API error: {exc}")
                    st.stop()

            data, parse_error = parse_response(raw_response)

            if parse_error or data is None:
                st.warning(
                    "The model returned a response that could not be parsed as JSON. "
                    "Raw output is shown below."
                )
                st.markdown(
                    f'<div class="raw-response-box">{raw_response}</div>',
                    unsafe_allow_html=True,
                )
            else:
                # ── Extracted symptoms chips ───────────────────────────────
                extracted = data.get("extracted_symptoms", [])
                if extracted:
                    st.markdown(
                        '<div class="chips-section-label">Extracted Symptoms</div>',
                        unsafe_allow_html=True,
                    )
                    chips = "".join(
                        f'<span class="chip">{s}</span>' for s in extracted
                    )
                    st.markdown(
                        f'<div class="symptom-chips">{chips}</div>',
                        unsafe_allow_html=True,
                    )

                st.markdown(
                    '<hr class="botanical-divider" style="margin-top:1.2rem;">',
                    unsafe_allow_html=True,
                )

                # ── Remedy cards ───────────────────────────────────────────
                remedies = data.get("remedies", [])
                if not remedies:
                    st.info("No remedies were returned. Try rephrasing the symptoms.")
                else:
                    for idx, remedy in enumerate(remedies[:3]):
                        st.markdown(
                            build_remedy_card_html(idx + 1, remedy),
                            unsafe_allow_html=True,
                        )

                # ── Analysis panel ─────────────────────────────────────────
                decisive   = data.get("decisive_modalities", [])
                confidence = data.get("confidence_note", "")

                if decisive or confidence:
                    decisive_html = ""
                    if decisive:
                        decisive_html = '<div class="analysis-title">Decisive Modalities</div>'
                        decisive_html += "".join(
                            f'<div class="analysis-item">{d}</div>' for d in decisive
                        )

                    conf_html = ""
                    if confidence:
                        conf_html = (
                            f'<div class="confidence-note">'
                            f'<span class="confidence-icon">📋</span>{confidence}</div>'
                        )

                    st.markdown(
                        f'<div class="analysis-box">{decisive_html}{conf_html}</div>',
                        unsafe_allow_html=True,
                    )

# ── Disclaimer ─────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="disclaimer">
    This tool supports practitioner decision-making.<br>
    Final judgement always rests with the practitioner.
</div>
""",
    unsafe_allow_html=True,
)
