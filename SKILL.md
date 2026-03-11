---
name: transcript-to-content
description: Transform training transcripts into GOAL-branded learning materials. Use when the user provides training transcripts, meeting notes, or onboarding session recordings and requests structured training content such as SOPs, presentations, slide decks, learning modules, or training documentation. Specializes in extracting procedural knowledge from unstructured verbal data and formatting it into professional, branded deliverables.
---

# Transcript to Content

Transform raw training transcripts into professional, GOAL-branded learning materials including SOPs, presentations, and structured training modules.

## When to Use This Skill

Use this skill when:
- User provides training transcripts, meeting notes, or session recordings
- User requests creation of SOPs, presentations, or training materials from transcripts
- User asks to "extract training content" or "create learning materials" from verbal data
- User mentions creating GOAL-branded training documentation

## Core Workflow

### Step 1: Understand the Request

Identify what type of content the user needs:
- **Master Knowledge Source:** Structured learning module (metadata, terminology, SOPs, nuances, assessments)
- **Presentation/Slide Deck:** Visual training presentation with GOAL branding
- **SOP Document:** Step-by-step procedural documentation
- **Training Overview:** High-level summary of a specific topic

### Step 2: Locate and Analyze Transcripts

**If transcripts are in project directory:**
```bash
ls -lah /home/ubuntu/projects/[project-name]/
```

**Search for relevant content:**
```bash
grep -ri "keyword" /home/ubuntu/projects/[project-name]/*.md
```

Read relevant transcript files and identify:
- Main topics and concepts
- Step-by-step procedures
- Critical warnings or nuances
- Terminology and definitions
- Real examples or scenarios

### Step 3: Extract Structured Content

Apply **Chain of Thought processing:**
1. Read entire transcript(s) for macro-context
2. Isolate distinct topics
3. Extract facts, steps, and definitions
4. Remove conversational filler ("um," "uh," "I think")
5. Convert to imperative, authoritative language

**For Master Knowledge Source format:**
Read `/home/ubuntu/skills/transcript-to-content/references/master-knowledge-source-format.md` for complete schema and examples.

Key sections to extract:
- **Module Metadata:** Topic and learning objective
- **Key Terminology:** Definitions of jargon, acronyms, tools
- **Standard Operating Procedures:** Numbered steps in "Action > Result" format
- **Critical Nuances:** Warnings, consequences, best practices
- **Assessment Data:** 3-5 multiple-choice questions based on content

**Important:** Flag incomplete information with `[MISSING INFO]` rather than fabricating details.

### Step 4: Apply GOAL Branding

Read `/home/ubuntu/skills/transcript-to-content/references/goal-brand-guidelines.md` for complete brand standards.

**Key brand elements:**
- **Primary Color:** `#077BE5` (GOAL Blue)
- **Logo:** `goal-logo-light.png` (in `templates/` directory)
- **Typography:** Inter font (weights 400, 600, 700, 900)
- **Style:** Swiss International Style (clean grids, bold typography, minimal decoration)

**Logo usage:**
- Copy logo to working directory before use
- Use absolute paths in HTML: `<img src="/path/to/goal-logo-light.png">`
- Presentations: Top-right corner (140px width) on content slides

### Step 5: Create Deliverables

#### For Presentations

Read `/home/ubuntu/skills/transcript-to-content/references/presentation-guidelines.md` for detailed guidelines.

**Workflow:**
1. Initialize presentation using `slide_initialize` tool
2. Create outline (max 12 slides by default unless user specifies)
3. Copy logo to project directory:
   ```bash
   cp /home/ubuntu/skills/transcript-to-content/templates/goal-logo-light.png [project-dir]/
   ```
4. Edit slides one by one using `slide_edit` tool
5. Present using `slide_present` tool
6. Export to PDF if requested:
   ```bash
   manus-export-slides manus-slides://[version-id] pdf
   ```

**Standard presentation structure:**
1. Title slide
2. Definition/overview
3. Step-by-step content (4-6 steps)
4. Critical success factors
5. Common pitfalls
6. Key takeaways
7. Closing slide

**Design requirements:**
- Use GOAL Blue (`#077BE5`) for accents
- Include logo on every slide
- Maintain 720px height limit
- Use clean, grid-based layouts
- No rounded corners, shadows, or animations

#### For SOP Documents

Create Markdown documents with:
- Clear hierarchical structure (H1, H2, H3)
- Numbered procedures with imperative language
- Warning/caution callouts in blockquotes
- Tables for reference data
- Inline citations where applicable

#### For Master Knowledge Source

Follow the schema in `references/master-knowledge-source-format.md` exactly:
- Output ONLY the structured content (no preamble or postscript)
- Use strict Markdown formatting
- Convert all conversational language to authoritative instructions
- Flag unknowns with `[MISSING INFO]`

## Quality Standards

**Content Accuracy:**
- Base all content strictly on transcript material
- Never fabricate steps, data, or information
- Flag incomplete procedures clearly
- Verify terminology definitions

**Brand Consistency:**
- Use GOAL Blue (`#077BE5`) as primary accent color
- Include logo on all branded materials
- Apply Swiss International Style principles
- Use Inter font family

**Formatting:**
- Remove all conversational filler
- Use imperative voice for instructions
- Maintain clear visual hierarchy
- Ensure readability and scannability

## Common Patterns

### Pattern 1: Single Topic Presentation
User provides transcript(s) on one topic → Extract key content → Create 8-12 slide presentation

### Pattern 2: Multiple Topics to Learning Modules
User provides multiple transcripts → Extract each as separate module → Deliver as structured documents

### Pattern 3: Quick Reference SOP
User needs specific procedure → Extract relevant steps → Create concise SOP document

### Pattern 4: Training Overview
User requests summary of topic → Search transcripts → Extract and synthesize key points → Deliver as Markdown document

## Troubleshooting

**Issue:** Slide appears empty in PDF
**Solution:** Check padding values. Reduce padding, adjust spacing, ensure content fits within 720px height.

**Issue:** Logo not displaying
**Solution:** Verify logo was copied to project directory. Use absolute path in HTML.

**Issue:** Content seems incomplete
**Solution:** Flag with `[MISSING INFO]` rather than guessing. Ask user for clarification if critical.

**Issue:** Presentation exceeds height limit
**Solution:** Reduce font sizes, decrease spacing, condense content, or split into additional slides.

## Resources

- **Brand Guidelines:** `references/goal-brand-guidelines.md`
- **Master Knowledge Source Format:** `references/master-knowledge-source-format.md`
- **Presentation Guidelines:** `references/presentation-guidelines.md`
- **GOAL Logo:** `templates/goal-logo-light.png`
