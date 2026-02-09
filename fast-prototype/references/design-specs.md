# Interface Design Specifications

Quick reference for design system and component specifications.

---

## Color System

### Primary Colors

```yaml
Primary: "#409EFF"     # Main actions, links, highlights
Success: "#67C23A"     # Success states, confirm
Warning: "#E6A23C"     # Warnings, attention
Danger: "#F56C6C"      # Delete actions, errors
Info: "#909399"        # Info, secondary text
```

### Neutral Colors

```yaml
Text Primary: "#303133"    # Main text
Text Secondary: "#606266"  # Secondary text
Text Placeholder: "#C0C4CC" # Placeholder

Border Base: "#DCDFE6"     # Base borders
Border Light: "#E4E7ED"    # Light borders

Bg Base: "#FFFFFF"         # Base background
Bg Light: "#F5F7FA"        # Light background
```

---

## Typography

### Font Family

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
             "Helvetica Neue", Arial, sans-serif;
```

### Font Sizes

| Usage | Size | Line Height | Weight |
|-------|------|-------------|--------|
| H1 - Large Title | 24px | 32px | 600 |
| H2 - Medium Title | 20px | 28px | 600 |
| H3 - Small Title | 16px | 24px | 600 |
| Body | 14px | 22px | 400 |
| Small | 12px | 20px | 400 |
| Caption | 12px | 18px | 400 |

---

## Spacing

### Base Unit: 4px

```yaml
xs: 4px    (0.25rem)
sm: 8px    (0.5rem)
md: 16px   (1rem)
lg: 24px   (1.5rem)
xl: 32px   (2rem)
2xl: 48px  (3rem)
```

### Usage

```yaml
Component padding: sm (8px) - md (16px)
Component margin: md (16px) - lg (24px)
Page padding: md (16px) - lg (24px)
```

---

## Border Radius

```yaml
Small: 2px   # Tags, badges
Base: 4px    # Inputs, buttons
Large: 8px   # Cards, dialogs
```

---

## Shadow

```yaml
Light: "0 1px 2px rgba(0, 0, 0, 0.05)"
Base: "0 2px 8px rgba(0, 0, 0, 0.1)"
Large: "0 4px 16px rgba(0, 0, 0, 0.15)"
```

---

## Component Specifications

### Button

**Primary Button**
- Background: Primary (#409EFF)
- Text: White
- Height: 32px / 40px
- Padding: 0 16px
- Radius: 4px

**States**: Hover (+10% dark), Active (+20% dark), Disabled (#C0C4CC)

### Input

**Default**
- Height: 32px / 40px
- Padding: 0 12px
- Border: 1px solid #DCDFE6
- Radius: 4px

**States**: Focus (Primary color border), Error (Red border), Disabled (Light gray bg)

### Table

**Structure**
- Border: 1px solid #EBEEF5
- Header bg: #F5F7FA
- Row height: 48px
- Cell padding: 12px

**Typography**: Header 14px/600, Body 14px/400

**States**: Hover row (#F5F7FA), Selected row (#ECF5FF)

### Card

**Default**
- Background: White
- Radius: 8px
- Shadow: Base
- Padding: 20px

**Header**
- Border bottom: 1px solid #EBEEF5
- Padding: 20px 20px 12px
- Font: 16px/600

---

## Layout

### Breakpoints

```yaml
xs: 0px      # Mobile
sm: 640px    # Mobile landscape
md: 768px    # Tablet
lg: 1024px   # Desktop
xl: 1280px   # Large desktop
2xl: 1536px  # Extra large
```

### Container

```yaml
Max width:
  Mobile: 100%
  Tablet: 720px
  Desktop: 960px
  Large: 1140px
```

### Admin Layout

```yaml
Sidebar width: 200px / 240px
Header height: 60px
Content padding: 24px
```

---

## Responsive

**Mobile First**: Start with mobile, enhance for larger screens

**Touch Targets**: Minimum 44px × 44px

**Hidden/Show**
```html
<div class="hidden md:block">Hide on mobile</div>
<div class="block md:hidden">Show on mobile only</div>
```

---

## Accessibility

### Color Contrast

- **AA**: Normal text 4.5:1, Large text 3:1
- **AAA**: Normal text 7:1, Large text 4.5:1

### Focus States

- Clear focus indicator
- Keyboard navigable
- Focus follows tab order

---

## Icon Sizes

```yaml
Small: 14px × 14px   # Table actions
Base: 16px × 16px    # Default
Medium: 20px × 20px  # Navigation
Large: 24px × 24px   # Status icons
```
