---
name: meeting-insights-analyzer
description: This skill transforms training and onboarding meeting transcripts into structured learning materials, documentation, and actionable review content. Use this skill when processing meeting transcripts from onboarding sessions, training meetings, or knowledge transfer conversations to extract key information and generate study guides, quick reference sheets, checklists, FAQ documents, action item lists, and training effectiveness assessments.
---

# Meeting Insights Analyzer: Onboarding Edition

## Overview

This skill processes training and onboarding meeting transcripts to extract key information and generate comprehensive learning materials. It identifies critical knowledge, creates multiple formats of review content, compiles actionable takeaways, and evaluates training communication effectiveness to help new employees succeed and improve future onboarding sessions.

## When to Use This Skill

Use this skill when:
- Processing transcripts from new employee onboarding sessions
- Creating learning materials from training meetings (Zoom, Google Meet, Teams recordings)
- Generating study guides and reference materials for new hires
- Extracting action items and onboarding milestones from training content
- Evaluating trainer communication effectiveness and identifying knowledge gaps
- Building a library of standardized onboarding documentation
- Preparing pre-boarding materials for incoming employees

## Core Capabilities

The skill performs four integrated functions:

### 1. Knowledge Extraction
Identify and organize key topics, concepts, tools, processes, and company information covered during training. Separate content into:
- **Critical Must-Know**: Information essential for day-one success
- **Important Context**: Background knowledge that supports understanding
- **Supplementary Reference**: Nice-to-know details for future reference

### 2. Learning Material Generation
Automatically create multiple formats of review materials:
- Study guides with structured topic breakdowns
- Quick reference sheets for daily use
- Checklists for onboarding completion tracking
- FAQ documents addressing common questions
- Glossary of company-specific terms and acronyms

### 3. Takeaway Compilation
Produce concise summaries including:
- Action items with clear ownership and deadlines
- First-day/week/month task lists
- Policy requirements and compliance items
- System access information and credentials needed
- Onboarding milestones and checkpoints

### 4. Training Communication Analysis
Evaluate onboarding effectiveness by measuring:
- Clarity of instruction delivery
- Pacing and information density
- Engagement level and interaction quality
- Knowledge gaps where jargon went unexplained
- Sections requiring follow-up or clarification

## Workflow

### Step 1: Transcript Input and Initial Scan

When processing a transcript, first perform a complete scan to identify:
1. Meeting participants and their roles (trainer, new hire, observer)
2. Overall meeting structure and topic flow
3. Duration and pacing of different sections
4. Types of content covered (policy, systems, culture, procedures)

### Step 2: Content Categorization

Organize extracted content into the following categories:

**Systems & Access**
- Platforms and software mentioned
- Account setup requirements
- Login credentials and access levels
- Permission structures

**Policies & Procedures**
- Company policies discussed
- Compliance requirements
- Standard operating procedures
- Escalation paths

**Team & Organization**
- Reporting structures
- Key contacts and their roles
- Team introductions
- Cross-functional relationships

**Role Expectations**
- Job responsibilities outlined
- Performance expectations
- Key deliverables mentioned
- Success metrics

**Tools & Software**
- Applications to learn
- Training resources mentioned
- Documentation locations
- Help desk procedures

**Culture & Values**
- Company culture elements
- Communication norms
- Behavioral expectations
- Unwritten rules mentioned

**Projects & Priorities**
- Current team projects
- Immediate priorities
- Context for ongoing work
- Background on recent decisions

**Emergency Contacts**
- IT support information
- HR contacts
- Manager availability
- Troubleshooting resources


### Step 3: Knowledge Gap Identification

Flag instances where:
- Jargon or acronyms used without explanation
- Concepts referenced without context
- Complex processes summarized too quickly
- New hire appeared confused (if transcript includes reactions)
- Topics mentioned but not fully explained
- Assumed prior knowledge that may not exist

### Step 4: Generate Output Documents

Based on the extracted content, generate the requested output formats. See the Output Templates section in references/output-templates.md for specific formatting guidelines.

## Processing Guidelines

### Handling Multiple Transcripts

When processing multiple transcripts from the same onboarding program:
1. Look for overlapping content to avoid duplication
2. Note inconsistencies between trainers for review
3. Build cumulative materials that reference all sessions
4. Track which topics were covered in which sessions

### Identifying Speaker Roles

When transcripts include speaker labels:
- **Trainer indicators**: Explains concepts, answers questions, guides discussion
- **New hire indicators**: Asks questions, confirms understanding, requests clarification
- **Observer indicators**: Minimal speaking, occasional clarifications

### Quality Markers to Extract

Look for and preserve:
- Analogies and examples that clarify concepts
- "Pro tips" or insider knowledge shared
- Common mistakes to avoid
- Historical context that explains current processes
- Rationale behind policies or procedures

### Handling Incomplete or Poor Quality Transcripts

When transcript quality is limited:
1. Note sections with unclear audio/transcription
2. Flag content that appears incomplete
3. Recommend follow-up questions for unclear sections
4. Provide partial outputs with clear caveats

## Example Usage

### Example 1: Processing a Single Onboarding Transcript

**User Request:** "Process this onboarding transcript and create a study guide and checklist for the new hire."

**Approach:**
1. Read the full transcript to understand scope
2. Categorize all content using the framework above
3. Extract key knowledge and action items
4. Generate study guide using template from references/output-templates.md
5. Generate checklist with prioritized tasks
6. Note any knowledge gaps for follow-up

### Example 2: Creating FAQ from Multiple Sessions

**User Request:** "Here are three onboarding transcripts. Create a comprehensive FAQ document."

**Approach:**
1. Process each transcript for question-answer pairs
2. Identify common questions across sessions
3. Consolidate answers, noting any variations
4. Organize by topic category
5. Add questions implied by knowledge gaps

### Example 3: Evaluating Trainer Effectiveness

**User Request:** "Analyze this training session for communication effectiveness."

**Approach:**
1. Evaluate pacing (concepts per minute, pauses for questions)
2. Assess clarity (definitions provided, examples given)
3. Identify engagement markers (questions asked, interactive elements)
4. Note knowledge gaps (undefined jargon, assumed knowledge)
5. Generate effectiveness report with recommendations

## Best Practices

### For Knowledge Extraction
- Prioritize accuracy over comprehensiveness
- When in doubt, categorize content as requiring follow-up
- Preserve trainer's phrasing for critical procedures
- Note confidence level for ambiguous content

### For Learning Material Generation
- Match output complexity to the topic
- Include practical examples whenever available
- Create logical flow from foundational to advanced concepts
- Ensure all generated materials reference source sessions

### For Takeaway Compilation
- Always assign clear ownership to action items
- Include realistic deadlines based on stated timelines
- Distinguish between hard deadlines and suggested timeframes
- Flag dependencies between tasks

### For Communication Analysis
- Be constructive, not critical, in feedback
- Focus on actionable improvements
- Acknowledge effective techniques
- Consider trainer experience level in recommendations

## Output File Naming Convention

When saving generated materials, use consistent naming:
- `[date]_[topic]_study-guide.md`
- `[date]_[topic]_quick-reference.md`
- `[date]_[topic]_checklist.md`
- `[date]_[topic]_action-items.md`
- `[date]_[topic]_faq.md`
- `[date]_[topic]_effectiveness-report.md`

## Resources

This skill includes reference documentation with detailed output templates. See:
- `references/output-templates.md` - Complete templates for all output document types
