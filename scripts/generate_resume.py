#!/usr/bin/env python3
"""Generate Mathias Fonseca's resume PDF.

Single source of truth for the downloadable resume linked from the site's
CTAs (public/Mathias-Fonseca-Resume.pdf). Edit the CONTENT block below and
re-run:

    python3 scripts/generate_resume.py

Requires: reportlab. Design mirrors the site (dark header band, forest-green
accents, zebra skills table).
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

# ---------------------------------------------------------------- palette ---
HEADER_BG = (0x11 / 255, 0x1c / 255, 0x17 / 255)   # dark teal band
ACCENT = (0x2d / 255, 0x6a / 255, 0x4f / 255)      # forest green
SAGE = (0xb7 / 255, 0xd5 / 255, 0xc8 / 255)        # light sage (subtitle)
PILL_BG = (0x1f / 255, 0x39 / 255, 0x2e / 255)
WHITE = (1, 1, 1)
INK = (0.11, 0.12, 0.13)                           # body text
MUTED = (0.42, 0.45, 0.44)                         # locations / dates
ZEBRA = (0.949, 0.968, 0.960)                      # skills table stripe
RULE = (0.80, 0.83, 0.82)

# ------------------------------------------------------------------ fonts ---
F = "Helvetica"
FB = "Helvetica-Bold"

# ------------------------------------------------------------ CONTENT ------
NAME = "Mathias Fonseca"
TITLE = "Senior Staff Engineer, Fintech · Solutions Architect"
CONTACT = "Berlin, Germany  |  mathifonseca@gmail.com  |  linkedin.com/in/mathifonseca  |  mathifonseca.me"
PILLS = ["15+ Years Experience", "50+ PSP Integrations", "$40B GMV Scale",
         "100+ People Led", "20+ Teams Built"]

SUMMARY = (
    "Senior Staff Engineer in Fintech at Wolt — part of DoorDash's global Money organisation "
    "spanning Wolt, Deliveroo, and DoorDash. 15+ years building payment systems at scale across "
    "Latin America, Europe, the Middle East, and Asia: founding engineer at Payrails, and earlier "
    "scaled Delivery Hero's Global Fintech team from 3 to 100+ people powering $40B annual GMV. "
    "Alongside the payments work, I drive how the engineering org adopts AI — raising developer "
    "velocity and pushing toward genuinely AI-native engineering. 7 years a Software Architecture "
    "professor; conference speaker."
)

# Each job: (company, location, [ (role, dates, [bullets]) ... ])
EXPERIENCE = [
    ("Wolt + DoorDash", "Berlin, Germany", [
        ("Senior Staff Engineer, Fintech", "May 2026 – Present", [
            "Technical direction for the international Money platform — payments, payouts, lending, card "
            "issuing, and gift cards spanning Wolt, Deliveroo, and DoorDash across Europe, the Middle East, "
            "Asia, and the Americas",
            "Helping bring the three companies' financial solutions onto common ground as they consolidate — "
            "the same work I did building Delivery Hero's global fintech and helping merchants consolidate at Payrails",
            "Driving AI adoption and developer velocity across the org; AI Ambassador moving teams from "
            "AI-assisted to genuinely AI-native ways of working, and defining how we evaluate AI-built systems",
            "Shaping long-term technical direction across teams through architecture docs, prototypes, and RFCs",
        ]),
    ]),
    ("Payrails", "Berlin, Germany", [
        ("Founding Engineer · Solutions Architect & Principal Engineer", "Dec 2021 – Dec 2025", [
            "First employee — designed and built the company's core technical architecture from scratch, "
            "now powering enterprise merchants' entire payment stack",
            "Grew the company to 100+ people across 9 teams (Berlin & Cairo); collaborated across product, "
            "tech, GTM, sales, and customer success",
            "Drove merchant success from zero to first 15 enterprise clients: onboarding, critical issue "
            "resolution, and process improvement",
            "Supported sales pipeline with technical demos, RFPs, and solution design for enterprise prospects",
            "Maintained the core architecture blueprint and led key technical decisions via RFC-driven processes",
        ]),
    ]),
    ("Delivery Hero", "Berlin, Germany", [
        ("Global Fintech Principal Engineer", "Oct 2020 – Dec 2021", [
            "Helped grow Global Fintech from 3 to 100+ people across 8 specialised teams (Payments, Risk, "
            "Compliance, Wallet, Payouts, Integrations, Analytics, Business)",
            "Provided architectural guidance across 50+ countries powering $40B in annual GMV",
            "Cross-functional consultant: payments and fraud system design across Delivery Hero's global footprint",
            "Bridged engineering, product, and compliance to ensure consistency, scalability, and regulatory alignment",
        ]),
        ("Global Payments Senior Engineering Manager", "May 2019 – Oct 2020", [
            "Built the Global Fintech team from scratch at Delivery Hero HQ",
            "Designed scalable payment solutions across diverse market requirements; expanded to new payment methods",
            "Led cross-functional teams on fraud prevention, compliance, and checkout optimisation",
        ]),
    ]),
    ("PedidosYa", "Montevideo, Uruguay", [
        ("Shopping Tribe Technical Leader", "Jan 2019 – Apr 2019", [
            "Led 5 teams (~30 engineers) across Ordering, Checkout, Payments, and Fraud for Latin America's "
            "#1 food delivery platform — 15 countries, $2.5B+ GMV",
            "Ensured architectural consistency across platforms and markets; aligned with Product and stakeholders",
        ]),
        ("Payments & Fraud Prevention Engineering Manager", "Sep 2016 – Apr 2019", [
            "Led the Payments and Fraud Prevention Squad — set OKRs, planned projects, negotiated with PSPs, "
            "balanced stakeholder interests",
            "Continued as full-stack engineer and API designer across payment integration and fraud prevention systems",
        ]),
        ("Senior Full Stack Engineer", "Oct 2013 – Sep 2016", [
            "One of the first engineers — built the platform from scratch, expanding across 12+ countries",
            "Developed deep expertise in payment systems and fraud prevention in one of the world's highest-fraud markets",
        ]),
    ]),
    ("Universidad ORT Uruguay", "Montevideo, Uruguay", [
        ("Software Architecture Professor", "Aug 2012 – Apr 2019", [
            "7 years teaching Software Architecture for BSc Software Engineering and Computer Science; "
            "Architectural Patterns, Quality Attributes, Tactics with Java EE",
        ]),
        ("Software Engineering in the Cloud Professor", "Jul 2014 – Sep 2015", [
            "Advanced course on cloud architecture, Web APIs, and deployment strategies",
        ]),
    ]),
]

EARLIER = [
    ("Softruck", "CTO", "Belo Horizonte, Brazil", "Sep–Dec 2015"),
    ("MercadoLibre", "Software Engineer", "Montevideo, Uruguay", "May–Oct 2013"),
    ("Tata Consultancy Services", "Business Analyst & .NET Developer", "Montevideo, Uruguay", "2010–2013"),
    ("TECHO", "IT Manager / Volunteer (anti-poverty NGO)", "Montevideo, Uruguay", "2008–2011"),
]

SKILLS = [
    ("Languages", "Java · Kotlin · Go · Groovy · Python · TypeScript · React"),
    ("Infrastructure", "AWS · Docker · Kubernetes · Terraform"),
    ("Data", "PostgreSQL · Redis · Kafka · BigQuery"),
    ("Payments Domain", "50+ PSP integrations · Orchestration · Fraud prevention · Chargebacks · Payouts"),
    ("Compliance", "PCI-DSS · GDPR · SCA / PSD2 / Open Banking · AML/KYC · ISO 27001"),
    ("Architecture", "Domain-Driven Design · Event-driven architecture · RFC-driven decisions · Distributed systems"),
    ("AI & Dev Productivity", "AI-native engineering · Developer velocity · Applied LLMs · Agentic workflows · AI adoption"),
    ("Leadership", "Cross-functional team leadership · OKRs · Technical strategy · Mentorship · Solutions architecture"),
    ("Human Languages", "Spanish (Native) · English (Fluent) · Portuguese (Professional) · German (B1) · Italian (Elementary)"),
]

EDUCATION = [
    ("Big Data & Machine Learning Specialization", "Universidad ORT Uruguay · 2018–2020"),
    ("BSc in Information Technology", "Universidad ORT Uruguay · 2008–2012"),
]

TALKS = [
    ("[Conference Talk]", "Payments Engineering and Stoicism", "QuantumTech 2021"),
    ("[Conference Panel]", "Payments in the Sharing Economy", "PAYMENTSfn 2019"),
    ("[Article]", "Mastering PSP Integrations", "mathifonseca.me"),
    ("[Article]", "A Survival Guide for Payments", "mathifonseca.me"),
    ("[Case Study]", "PedidosYa Payment Infrastructure", "Spreedly"),
    ("[Podcast]", "Payments and Delivery in Latin America", "LATAM payments series"),
]

# ------------------------------------------------------------- geometry ----
PW, PH = A4
LM = 18 * mm          # left margin
RM = PW - 18 * mm     # right edge
CW = RM - LM          # content width


class Doc:
    def __init__(self, path):
        self.c = canvas.Canvas(path, pagesize=A4)
        self.y = PH
        self.page = 1

    # -- primitives --------------------------------------------------------
    def text(self, x, y, s, font=F, size=9.5, color=INK):
        self.c.setFillColorRGB(*color)
        self.c.setFont(font, size)
        self.c.drawString(x, y, s)

    def rtext(self, x, y, s, font=F, size=9.5, color=MUTED):
        self.c.setFillColorRGB(*color)
        self.c.setFont(font, size)
        self.c.drawRightString(x, y, s)

    def link(self, x, y, s, font=F, size=9.3, color=ACCENT):
        """Green underlined link-style text; returns advance width."""
        self.text(x, y, s, font, size, color)
        w = stringWidth(s, font, size)
        self.c.setStrokeColorRGB(*color)
        self.c.setLineWidth(0.5)
        self.c.line(x, y - 1.5, x + w, y - 1.5)
        return w

    def wrap(self, s, font, size, width):
        words = s.split()
        lines, cur = [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if stringWidth(t, font, size) <= width:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def footer(self):
        self.c.setFillColorRGB(*MUTED)
        self.c.setFont(F, 8)
        self.c.drawString(LM, 12 * mm, "mathifonseca.me")
        self.c.drawRightString(RM, 12 * mm, f"Page {self.page}")

    def need(self, h):
        if self.y - h < 20 * mm:
            self.footer()
            self.c.showPage()
            self.page += 1
            self.y = PH - 20 * mm

    def section(self, label):
        self.need(16 * mm)
        self.y -= 6
        self.text(LM, self.y, label.upper(), FB, 10.5, ACCENT)
        self.y -= 4
        self.c.setStrokeColorRGB(*RULE)
        self.c.setLineWidth(0.6)
        self.c.line(LM, self.y, RM, self.y)
        self.y -= 12

    # -- header band -------------------------------------------------------
    def header(self):
        bh = 46 * mm
        self.c.setFillColorRGB(*HEADER_BG)
        self.c.rect(0, PH - bh, PW, bh, fill=1, stroke=0)
        self.text(LM, PH - 17 * mm, NAME, FB, 26, WHITE)
        self.text(LM, PH - 24 * mm, TITLE, F, 12, SAGE)
        self.text(LM, PH - 30 * mm, CONTACT, F, 8.4, (0.72, 0.80, 0.76))
        # pills
        x = LM
        py = PH - 40 * mm
        self.c.setFont(F, 8)
        for p in PILLS:
            tw = stringWidth(p, F, 8)
            pw = tw + 12
            self.c.setFillColorRGB(*PILL_BG)
            self.c.roundRect(x, py - 3, pw, 13, 3, fill=1, stroke=0)
            self.c.setFillColorRGB(*SAGE)
            self.c.drawString(x + 6, py + 1, p)
            x += pw + 6
        self.y = PH - bh - 8 * mm

    # -- experience --------------------------------------------------------
    def job(self, company, location, roles):
        # keep the company header + first role's first line together
        self.need(22 * mm)
        self.text(LM, self.y, company, FB, 11.5, ACCENT)
        self.rtext(RM, self.y, location, F, 9, MUTED)
        self.y -= 13
        for ri, (role, dates, bullets) in enumerate(roles):
            if ri > 0:
                self.need(16 * mm)
            self.text(LM, self.y, role, FB, 10, INK)
            self.rtext(RM, self.y, dates, F, 9, MUTED)
            self.y -= 12
            for b in bullets:
                self.bullet(b)
            self.y -= 3
        self.y -= 6

    def bullet(self, s):
        bx = LM + 4
        tx = LM + 12
        lines = self.wrap(s, F, 9.3, CW - 12)
        self.need(len(lines) * 11 + 2)
        # bullet dot
        self.c.setFillColorRGB(*ACCENT)
        self.c.setFont(F, 9.3)
        self.c.drawString(bx, self.y, "•")
        for i, ln in enumerate(lines):
            self.text(tx, self.y, ln, F, 9.3, INK)
            self.y -= 11

    # -- earlier experience table -----------------------------------------
    def earlier(self):
        for comp, role, loc, dates in EARLIER:
            self.need(12 * mm)
            label = f"{comp} — {role}"
            lines = self.wrap(label, F, 9.3, CW * 0.52)
            # company portion in accent, rest ink — approximate by drawing company then role
            cw = self.link(LM, self.y, comp, FB, 9.3)
            self.text(LM + cw, self.y, " — " + role, F, 9.3, INK)
            self.rtext(RM - 30 * mm, self.y, loc, F, 9, MUTED)
            self.rtext(RM, self.y, dates, F, 9, MUTED)
            self.y -= 13
        self.y -= 2

    # -- skills zebra table ------------------------------------------------
    def skills(self):
        label_w = 42 * mm
        for i, (k, v) in enumerate(SKILLS):
            lines = self.wrap(v, F, 9, CW - label_w - 6)
            rh = max(13, len(lines) * 11 + 2)
            self.need(rh + 2)
            if i % 2 == 0:
                self.c.setFillColorRGB(*ZEBRA)
                self.c.rect(LM - 3, self.y - rh + 9, CW + 6, rh, fill=1, stroke=0)
            self.text(LM, self.y, k, FB, 9, INK)
            for j, ln in enumerate(lines):
                self.text(LM + label_w, self.y - j * 11, ln, F, 9, INK)
            self.y -= rh
        self.y -= 4

    def two_col(self, rows, left_font=F, left_color=INK, right_color=MUTED, right_accent=False):
        for left, right in rows:
            self.need(12 * mm)
            self.text(LM, self.y, left, left_font, 9.5, left_color)
            self.rtext(RM, self.y, right, F, 9.3, ACCENT if right_accent else right_color)
            self.y -= 13
        self.y -= 2

    def talks(self):
        for tag, title, venue in TALKS:
            self.need(12 * mm)
            tw = stringWidth(tag + " ", F, 9.3)
            self.text(LM, self.y, tag + " ", F, 9.3, MUTED)
            self.link(LM + tw, self.y, title, F, 9.3)
            self.rtext(RM, self.y, venue, F, 9, MUTED)
            self.y -= 13

    def build(self):
        self.header()
        self.section("Summary")
        for ln in self.wrap(SUMMARY, F, 9.5, CW):
            self.need(12)
            self.text(LM, self.y, ln, F, 9.5, INK)
            self.y -= 12
        self.section("Experience")
        for comp, loc, roles in EXPERIENCE:
            self.job(comp, loc, roles)
        self.section("Earlier Experience")
        self.earlier()
        self.section("Skills & Domain Expertise")
        self.skills()
        self.section("Education")
        self.two_col(EDUCATION, right_accent=True)
        self.section("Selected Talks & Publications")
        self.talks()
        self.footer()
        self.c.setTitle("Mathi Fonseca — Resume")
        self.c.setAuthor("Mathi Fonseca")
        self.c.save()


if __name__ == "__main__":
    import os
    out = os.environ.get("RESUME_OUT") or os.path.join(
        os.path.dirname(__file__), "..", "public", "Mathias-Fonseca-Resume.pdf")
    Doc(os.path.abspath(out)).build()
    print("wrote", os.path.abspath(out))
