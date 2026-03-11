# GOAL-Branded Presentation Guidelines

## Overview

Create professional, Swiss International Style presentations with GOAL branding that communicate training content clearly and effectively.

## Presentation Structure

### Standard Slide Deck Structure (12 slides max by default)

1. **Title Slide** - Topic introduction with metadata
2. **Definition/Overview** - What is the concept?
3. **Step-by-Step Content** - Core instructional slides (typically 4-6 steps)
4. **Critical Success Factors** - Key principles for effectiveness
5. **Common Pitfalls** - Mistakes to avoid
6. **Key Takeaways** - Summary checklist
7. **Closing Slide** - Final thought and branding

## Design Standards

### Visual Style

**Swiss International Style:**
- Clean grid systems
- Bold typography
- Minimal decoration
- Ample white space
- Geometric accents (lines, circles) used sparingly

**Prohibited Elements:**
- Rounded corners
- Card components with border accents
- Shadowed boxes
- CSS animations or transitions
- Inline SVG code

### Color Application

**Primary Accent:** GOAL Blue (`#077BE5`)
- Header underlines
- Key metrics and highlights
- Chart elements
- Important callouts

**Supporting Colors:**
- Background: `#F2F2F2` (light grey)
- Text: `#1A1A1A` (near black)
- Secondary text: `#333333`, `#555555`, `#666666`
- Dark panels: `#1A1A1A` (for contrast sections)

**Color Usage Rules:**
- Use at most 2-3 colors per slide
- Ensure sufficient contrast for readability
- Apply colors consistently throughout presentation

### Typography

**Font:** Inter (Google Fonts)
- Weights: 400, 600, 700, 900

**Hierarchy:**
- Slide Headers: 48px, weight 900
- Body Text: 18-24px, weight 400-500
- Labels: 14-18px, weight 600-700
- Large Numbers: 240px, weight 900 (for step indicators)

### Logo Placement

**Content Slides:** Top-right corner, 140px width
**Title/Closing Slides:** Top-left or top-right, 180-200px width

Always use absolute path:
```html
<img src="goal-logo-light.png" alt="GOAL Logo" class="logo">
```

## Layout Patterns

### Title Slide Layout
- Large title (84-96px)
- Subtitle with accent border
- Metadata (module, focus area)
- Accent bar (40px width, full height)
- Logo placement
- Geometric accent element

### Content Slide Layouts

**Three-Column Grid:**
- Large step number (240px, outlined)
- Main content (instructions, metrics)
- Insight/example panel (dark background)

**Two-Column Split:**
- Left: Logic/formulas/steps
- Right: Examples/calculations (dark panel)

**Full-Width with Sections:**
- Header with underline accent
- Multiple content sections with clear hierarchy
- Visual dividers between sections

### Data Visualization

**Chart Guidelines:**
- Use Chart.js for standard charts (avoid inline SVG)
- Apply GOAL Blue (`#077BE5`) for primary data
- Use white or grey for secondary data
- Include clear labels and legends
- Wrap canvas elements in fixed-height divs

**Example:**
```html
<div style="height: 180px;">
    <canvas id="myChart"></canvas>
</div>
```

## Content Guidelines

### Writing Style

- **Imperative voice:** "Navigate to...", "Click...", "Set..."
- **Concise bullets:** Maximum 3-4 main points per slide
- **Clear hierarchy:** Use bold for emphasis, not decoration
- **Action-oriented:** Focus on what to do, not just what to know

### Information Density

- **Title slide:** Minimal text, strong visual presence
- **Content slides:** Balanced text and white space
- **Summary slides:** Checklist format with check marks (✓)

### Critical Elements to Include

1. **Step Numbers:** Large, prominent, consistent styling
2. **Action Items:** Clear, numbered lists with arrows (→) or bullets
3. **Warnings/Alerts:** Highlighted boxes with distinct styling
4. **Examples:** Real scenarios in contrasting panels
5. **Takeaways:** Summarized as actionable checklist items

## Technical Requirements

### HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Slide Title]</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        /* Styles here */
    </style>
</head>
<body>
    <div class="slide-container">
        <!-- Content here -->
    </div>
</body>
</html>
```

### Critical CSS Rules

**Slide Container:**
```css
.slide-container {
    width: 1280px;
    min-height: 720px;
    background-color: #F2F2F2;
    position: relative;
    overflow: hidden;
    padding: 80px 100px 60px;
    display: flex;
    flex-direction: column;
}
```

**Key Constraints:**
- Use `min-height` not `height` to prevent overflow
- Never use `padding-bottom` property
- Always use `padding-top` for vertical spacing
- No CSS on body tag
- No `position: absolute` for main containers

## Workflow

1. **Initialize presentation** using `slide_initialize` tool
2. **Create outline** with all slide IDs and summaries
3. **Edit slides one by one** using `slide_edit` tool (never batch edit)
4. **Copy logo** to project directory before editing slides
5. **Present** using `slide_present` tool when complete
6. **Export to PDF** using `manus-export-slides` utility if requested

## Quality Checklist

Before presenting, verify:
- [ ] Logo appears on all slides
- [ ] GOAL Blue (`#077BE5`) used consistently
- [ ] All slides fit within 720px height
- [ ] Typography hierarchy is clear
- [ ] No prohibited design elements used
- [ ] Content is factual and based on source material
- [ ] Charts and visualizations are properly labeled
