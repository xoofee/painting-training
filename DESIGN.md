# Painting Enlightenment PDF Design

## Goal

Create a child-facing, print-ready A4 PDF for a four-year-old beginner who likes drawing and can already make simple strokes, rockets, flowers, and basic coloring.

The PDF should feel like playful guided practice, not a formal art class or parent instruction manual.

## Output

- Files:
  - `painting_enlightenment_10_pages.pdf`: current full-color version
  - `painting_enlightenment_10_pages_ink_save.pdf`: no-color, ink-save version
- Format: PDF only
- Page size: A4 portrait
- Page count: 10 pages
- Artwork style: vector shapes for clean printing
- Text level: almost none

The ink-save version should preserve the same 10-page structure, activities, tracing guides, and practice areas as the full-color version. It should use strokes only, with no colored fills and no large gray filled areas.

## Audience

Primary user: a four-year-old child.

Secondary user: an adult who may print the PDF and sit nearby, but the pages should not depend on written adult instructions.

## Design Principles

- Use large, friendly shapes with thick outlines.
- Keep each page simple and uncluttered.
- Provide one activity per page.
- Show a simple finished example.
- Include pale dotted guide strokes for tracing.
- Leave generous blank space for free practice.
- Use simple color swatches where helpful.
- Avoid tiny details, dense patterns, long text, or complicated instructions.
- Keep the PDF usable in black-and-white printing, while still nicer in color.

## Page Structure

Each page should generally include:

1. A simple completed example near the top.
2. A dotted or pale tracing version in the middle.
3. A blank practice area near the bottom.
4. Optional color swatches in the corner.
5. A tiny page number only if needed.

The page should be understandable visually without text.

## Page Plan

1. Lines and curves warm-up
2. Rocket
3. Flower
4. Sun and clouds
5. Fish
6. House
7. Tree
8. Car
9. Animal face
10. Rainbow and free drawing

## Difficulty Progression

The activities should move from simple motor practice to simple recognizable drawings:

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
- Practice area: very pale gray rounded rectangle with dashed border
- Stroke weight: thick enough for preschool tracing
- Color palette: red, orange, yellow, green, blue, purple, pink, brown

Ink-save mode:

- Page border: black or dark-gray outline only
- Main outline: black or dark gray
- Guide outline: pale gray dotted lines
- Practice area: outline only, with no filled background
- Shapes: white or no-fill interiors only
- Color swatches: omit them, or render as outline-only circles if needed
- Stroke weight: still thick enough for preschool tracing

These tokens should stay consistent unless the whole visual style is intentionally changed.

## Future Refactor Notes

Good future improvements:

- Move page definitions into structured data instead of hard-coded page calls.
- Add optional localized parent notes as a separate companion page, not inside child worksheets.
- Add a command-line option for output filename.
- Add a black-and-white variant.
- Add a second set with animals, food, or nature themes.
- Add render-based visual regression checks if a reliable PDF renderer is available.

Avoid future changes that:

- Add lots of text to the child pages.
- Make the drawings too detailed for a four-year-old.
- Reduce the blank practice space.
- Depend on paid fonts or external image assets.
- Make the PDF hard to print on ordinary home printers.

## Acceptance Checklist

- The PDF has exactly 10 A4 portrait pages.
- Each page has one clear activity.
- All artwork fits inside the printable area.
- Dotted guide lines are visible but not visually dominant.
- Practice areas are large enough for a young child.
- The pages are usable without reading instructions.
- Both PDFs can be regenerated from `create_painting_pdf.py`.
- The ink-save PDF is visibly lower-ink than the full-color PDF.
