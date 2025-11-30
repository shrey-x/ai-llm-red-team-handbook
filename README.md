# AI / LLM Red Team Field Manual & Consultant's Handbook

![Repository Banner](assets/banner.svg)

![License](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)
![Last Updated](https://img.shields.io/badge/Last%20Updated-November%202025-orange.svg)

A complete operational toolkit for conducting **AI/LLM red team assessments** on Large Language Models, AI agents, RAG pipelines, and AI-enabled applications.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/shiva108/ai-llm-red-team-handbook.git
cd ai-llm-red-team-handbook

# Manual testing: Open docs/AI_LLM Red Team Field Manual.md

# Automated testing:
cd scripts
pip install -r requirements.txt
python runner.py --config config.py
```

📖 **Detailed setup:** See [Configuration Guide](docs/Configuration.md)

---

## Repository Contents

| Resource | Description |
|----------|-------------|
| **[Field Manual](docs/AI_LLM%20Red%20Team%20Field%20Manual.md)** | Compact operational reference with attack prompts, tooling, OWASP/MITRE mappings |
| **[Handbook](docs/AI%20LLM%20Red%20Team%20Hand%20book.md)** | Full consultancy guide with methodology, threat modeling, RoE/SOW templates |
| **[Building AI Red Teams](docs/Building%20a%20World-Class%20AI%20Red%20Team.md)** | Strategic guide for building security teams |
| **[Report Template](docs/Full_LLM_RedTeam_Report_Template.docx)** | Client-ready assessment report template |
| **[Python Framework](scripts/)** | Automated testing suite for prompt injection, jailbreaks, data leakage, tool misuse |

---

## Prerequisites

**Manual Testing:** Any text editor + target LLM access

**Automated Testing:**
- Python 3.8+
- Dependencies: `requests`, `pytest`, `pydantic`, `python-dotenv`
- API credentials for target LLM

---

## Python Testing Framework

### Test Suites

- `test_prompt_injection.py` - Automated prompt injection attacks
- `test_safety_bypass.py` - Jailbreak and guardrail bypass tests
- `test_data_exposure.py` - Data leakage and PII extraction
- `test_tool_misuse.py` - Function-calling and plugin abuse
- `test_fuzzing.py` - Adversarial input fuzzing
- `test_integrity.py` - Model integrity and consistency

### Configuration

Create `scripts/.env`:
```bash
API_ENDPOINT=https://api.example.com/v1/chat/completions
API_KEY=your-secret-api-key
MODEL_NAME=gpt-4
```

Run tests:
```bash
python runner.py                           # All tests
python runner.py --test prompt_injection   # Specific test
python runner.py --verbose                 # Verbose output
```

📖 **Full configuration options:** [Configuration Guide](docs/Configuration.md)

---

## Use Cases

**Red Team Engagements:** Use Field Manual attack prompts and Python framework for assessments

**Training:** Leverage Handbook for onboarding and team development

**Client Work:** Export PDFs for proposals and methodology documents

---

## Roadmap

**Planned:**
- Sample RAG and LLM test environments
- Additional attack case studies
- Extended multimodal AI coverage

**Contributions welcome** via issues and PRs.

---

## License

Licensed under **CC BY-SA 4.0**. See [LICENSE](LICENSE) for details.

---

## Disclaimer

⚠️ **For authorized security testing only.**

Ensure:
- Written authorization (SOW/RoE) is in place
- Compliance with applicable laws and regulations
- No unauthorized testing on production systems

The authors accept no liability for unauthorized use.
