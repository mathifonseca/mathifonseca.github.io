# scripts

## generate_resume.py

Single source of truth for the downloadable resume at
`public/Mathias-Fonseca-Resume.pdf` (linked from the site's CTAs).

Edit the `CONTENT` block in `generate_resume.py`, then regenerate:

```bash
python3 -m venv .venv && source .venv/bin/activate   # first time
pip install reportlab
python3 scripts/generate_resume.py                   # writes public/Mathias-Fonseca-Resume.pdf
```

Set `RESUME_OUT=/tmp/preview.pdf` to render elsewhere without touching the
live file. Keep the resume content in sync with `src/pages/work.astro` and
`src/pages/index.astro` when experience or positioning changes.
