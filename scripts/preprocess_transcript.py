#!/usr/bin/env python3
"""
Transcript Preprocessor for Meeting Insights Analyzer

This script preprocesses meeting transcripts to clean and standardize them
before analysis. It handles common transcript formats from Zoom, Google Meet,
Microsoft Teams, and Otter.ai.

Usage:
    python3 preprocess_transcript.py <input_file> [output_file]

If no output file is specified, creates a cleaned version with _cleaned suffix.
"""

import sys
import re
from pathlib import Path
from datetime import datetime


def detect_format(content: str) -> str:
    """Detect the transcript format based on content patterns."""
    if "WEBVTT" in content[:100]:
        return "vtt"
    if re.search(r'^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}', content, re.MULTILINE):
        return "vtt"
    if re.search(r'^\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', content, re.MULTILINE):
        return "srt"
    if re.search(r'\[\d{2}:\d{2}:\d{2}\]', content):
        return "timestamp_bracket"
    if re.search(r'^\d{1,2}:\d{2}(:\d{2})?\s', content, re.MULTILINE):
        return "simple_timestamp"
    if re.search(r'^[A-Za-z\s]+:\s', content, re.MULTILINE):
        return "speaker_colon"
    return "plain"


def clean_vtt(content: str) -> str:
    """Clean WebVTT format transcripts."""
    lines = content.split('\n')
    cleaned = []
    current_speaker = ""
    current_text = []
    
    for line in lines:
        line = line.strip()
        # Skip WEBVTT header and timing lines
        if line == "WEBVTT" or re.match(r'\d{2}:\d{2}:\d{2}\.\d{3} -->', line):
            continue
        # Skip sequence numbers
        if re.match(r'^\d+$', line):
            continue
        # Skip empty lines
        if not line:
            if current_text:
                cleaned.append(f"{current_speaker}: {' '.join(current_text)}" if current_speaker else ' '.join(current_text))
                current_text = []
            continue
        
        # Check for speaker tag
        speaker_match = re.match(r'<v ([^>]+)>', line)
        if speaker_match:
            if current_text and current_speaker:
                cleaned.append(f"{current_speaker}: {' '.join(current_text)}")
                current_text = []
            current_speaker = speaker_match.group(1)
            line = re.sub(r'<v [^>]+>', '', line).strip()
        
        # Remove other VTT tags
        line = re.sub(r'<[^>]+>', '', line)
        if line:
            current_text.append(line)
    
    if current_text:
        cleaned.append(f"{current_speaker}: {' '.join(current_text)}" if current_speaker else ' '.join(current_text))
    
    return '\n'.join(cleaned)


def clean_srt(content: str) -> str:
    """Clean SRT format transcripts."""
    lines = content.split('\n')
    cleaned = []
    current_text = []
    
    for line in lines:
        line = line.strip()
        # Skip sequence numbers
        if re.match(r'^\d+$', line):
            continue
        # Skip timing lines
        if re.match(r'\d{2}:\d{2}:\d{2},\d{3} -->', line):
            continue
        # Empty lines indicate end of subtitle block
        if not line:
            if current_text:
                cleaned.append(' '.join(current_text))
                current_text = []
            continue
        current_text.append(line)
    
    if current_text:
        cleaned.append(' '.join(current_text))
    
    return '\n'.join(cleaned)


def clean_timestamp_bracket(content: str) -> str:
    """Clean transcripts with [HH:MM:SS] timestamps."""
    # Remove timestamps but keep speaker and text
    cleaned = re.sub(r'\[\d{2}:\d{2}:\d{2}\]\s*', '', content)
    return cleaned.strip()


def clean_simple_timestamp(content: str) -> str:
    """Clean transcripts with simple timestamps at line start."""
    lines = content.split('\n')
    cleaned = []
    
    for line in lines:
        # Remove leading timestamps
        line = re.sub(r'^\d{1,2}:\d{2}(:\d{2})?\s*', '', line)
        if line.strip():
            cleaned.append(line.strip())
    
    return '\n'.join(cleaned)


def standardize_speakers(content: str) -> str:
    """Standardize speaker labels and merge consecutive same-speaker lines."""
    lines = content.split('\n')
    cleaned = []
    current_speaker = None
    current_text = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check for speaker pattern
        speaker_match = re.match(r'^([A-Za-z\s\.\-\']+):\s*(.*)$', line)
        if speaker_match:
            speaker = speaker_match.group(1).strip()
            text = speaker_match.group(2).strip()
            
            if speaker == current_speaker:
                # Same speaker, append text
                if text:
                    current_text.append(text)
            else:
                # New speaker, save previous and start new
                if current_speaker and current_text:
                    cleaned.append(f"{current_speaker}: {' '.join(current_text)}")
                current_speaker = speaker
                current_text = [text] if text else []
        else:
            # No speaker label, append to current
            if current_speaker:
                current_text.append(line)
            else:
                cleaned.append(line)
    
    # Don't forget the last speaker
    if current_speaker and current_text:
        cleaned.append(f"{current_speaker}: {' '.join(current_text)}")
    
    return '\n\n'.join(cleaned)


def extract_metadata(content: str) -> dict:
    """Extract meeting metadata from transcript."""
    metadata = {
        'speakers': set(),
        'duration_estimate': None,
        'detected_format': None
    }
    
    # Find all speaker names
    speakers = re.findall(r'^([A-Za-z\s\.\-\']+):', content, re.MULTILINE)
    metadata['speakers'] = sorted(set(s.strip() for s in speakers))
    
    return metadata


def preprocess_transcript(input_path: str, output_path: str = None) -> str:
    """
    Main preprocessing function.
    
    Args:
        input_path: Path to input transcript file
        output_path: Optional path for output file
        
    Returns:
        Cleaned transcript content
    """
    input_file = Path(input_path)
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    content = input_file.read_text(encoding='utf-8')
    
    # Detect and clean based on format
    format_type = detect_format(content)
    print(f"Detected format: {format_type}")
    
    if format_type == "vtt":
        cleaned = clean_vtt(content)
    elif format_type == "srt":
        cleaned = clean_srt(content)
    elif format_type == "timestamp_bracket":
        cleaned = clean_timestamp_bracket(content)
    elif format_type == "simple_timestamp":
        cleaned = clean_simple_timestamp(content)
    else:
        cleaned = content
    
    # Standardize speakers and merge consecutive lines
    cleaned = standardize_speakers(cleaned)
    
    # Extract metadata
    metadata = extract_metadata(cleaned)
    
    # Create header
    header = f"""# Meeting Transcript
## Preprocessed: {datetime.now().strftime('%Y-%m-%d %H:%M')}
## Original Format: {format_type}
## Speakers Identified: {', '.join(metadata['speakers']) if metadata['speakers'] else 'Unknown'}

---

"""
    
    final_content = header + cleaned
    
    # Write output if path provided
    if output_path:
        output_file = Path(output_path)
    else:
        output_file = input_file.parent / f"{input_file.stem}_cleaned{input_file.suffix}"
    
    output_file.write_text(final_content, encoding='utf-8')
    print(f"Cleaned transcript saved to: {output_file}")
    print(f"Speakers found: {', '.join(metadata['speakers']) if metadata['speakers'] else 'None identified'}")
    
    return final_content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 preprocess_transcript.py <input_file> [output_file]")
        print("\nSupported formats:")
        print("  - WebVTT (.vtt)")
        print("  - SRT (.srt)")
        print("  - Timestamped text ([HH:MM:SS] format)")
        print("  - Speaker-labeled text (Speaker: text)")
        print("  - Plain text")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        preprocess_transcript(input_path, output_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
