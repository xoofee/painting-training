# Painting Enlightenment PDF Design

## Goal

Create a child-facing, print-ready A4 PDF for a four-year-old beginner who likes drawing and can already make simple strokes, rockets, flowers, and basic coloring.

The PDF should feel like playful guided practice, not a formal art class or parent instruction manual.

## Output

- Files:
  - `painting_enlightenment_50_pages.pdf`: full-color version
  - `painting_enlightenment_50_pages_ink_save.pdf`: no-color, ink-save version
- Format: PDF only
- Page size: A4 portrait
- Page count: 50 pages
- Artwork style: vector shapes for clean printing
- Text level: almost none

The ink-save version should preserve the same 50-page structure and activities as the full-color version. It should use dotted strokes only, with no colored fills and no large gray filled areas.

## Audience

Primary user: a four-year-old child.

Secondary user: an adult who may print the PDF and sit nearby, but the pages should not depend on written adult instructions.

## Design Principles

- Use large, friendly shapes with thick outlines.
- Keep each page moderately dense but still preschool-friendly.
- Provide one visual theme per page.
- Show several simple examples and tracing copies.
- Include pale dotted guide strokes for tracing in color mode.
- Use the full printable area; do not include a bottom gray self-exercise box.
- Use simple color swatches where helpful.
- Avoid tiny details, dense patterns, long text, or complicated instructions.
- Keep the PDF usable in black-and-white printing, while still nicer in color.

## Page Structure

Each page should generally include:

1. Three to six large child-friendly drawings.
2. A mix of completed examples and tracing copies.
3. Optional color swatches in the corner for color mode.
4. A tiny page number only if needed.

The page should be understandable visually without text.

## Page Plan

The 50 pages should be distinct, not simple repeats. They cover warm-up strokes, beginner objects, nature, vehicles, animals, food, weather, sky themes, simple scenes, and mixed shape-combination practice.

## Difficulty Progression

The activities should move from simple motor practice to simple recognizable drawings and mixed pages:

1. Straight lines, vertical lines, arcs, and waves
2. Simple object outlines
3. Repeated round shapes
4. Combining circles and short lines
5. Symmetric shapes and small details
6. Basic geometric drawing
7. Organic rounded forms
8. Rectangles, circles, and wheels
9. Facial placement and expression
10. Color bands and open-ended drawing

## Visual Tokens

The project should support two rendering modes.

Color mode:

- Page border: light gray rounded rectangle
- Main outline: dark gray
- Guide outline: pale gray dotted lines
- No bottom practice area
- Stroke weight: thick enough for preschool tracing
- Color palette: red, orange, yellow, green, blue, purple, pink, brown

Ink-save mode:

- Page border: dotted black or dark-gray outline only
- Main outline: dotted black or dark gray
- Guide outline: dotted pale gray
- No bottom practice area
- Shapes: no-fill interiors only
- Color swatches: omit them
- Stroke weight: still thick enough for preschool tracing

These tokens should stay consistent unless the whole visual style is intentionally changed.

## Future Refactor Notes

Good future improvements:

- Move page definitions into structured data instead of hard-coded page calls.
- Add optional localized parent notes as a separate companion page, not inside child worksheets.
- Add a command-line option for output filename.
- Add a black-and-white variant.
- Add render-based visual regression checks if a reliable PDF renderer is available.

Avoid future changes that:

- Add lots of text to the child pages.
- Make the drawings too detailed for a four-year-old.
- Bring back the bottom gray self-exercise box.
- Depend on paid fonts or external image assets.
- Make the PDF hard to print on ordinary home printers.

## Acceptance Checklist

- Each PDF has exactly 50 A4 portrait pages.
- Each page has one clear visual theme.
- All artwork fits inside the printable area.
- Dotted guide lines are visible but not visually dominant.
- Pages use the printable area without a bottom gray practice panel.
- The pages are usable without reading instructions.
- Both PDFs can be regenerated from `create_painting_pdf.py`.
- The ink-save PDF is visibly lower-ink than the full-color PDF and uses dotted outlines throughout the artwork.
