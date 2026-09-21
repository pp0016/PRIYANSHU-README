# 🖨️ Micro Print Page Order Guide

## Problem Kya Hai?

Aapke paas ek PDF hai (8, 16, 24... pages). Jab aap **micro print** (4-up) karte ho toh ek A4 sheet pe 4 chhote pages aate hain. Aap chahte ho ki **dono side** (duplex) use ho — aur jab aap sheet cut karo toh har piece ke **aage-peeche sahi consecutive pages** aayein.

## Layout Samjho

A4 Portrait sheet pe 4 micro pages aise aate hain:

```
┌──────────┬──────────┐
│ Top-Left │Top-Right │
│   (TL)   │  (TR)    │
├──────────┼──────────┤
│Bottom-Left│Bottom-Right│
│   (BL)   │  (BR)    │
└──────────┴──────────┘
```

## Flip Physics (Long-Edge Duplex)

Jab printer duplex print karta hai portrait mein (long-edge flip = book ki tarah paltna), toh **left-right mirror** hota hai:

| Front Position | ↔ | Back Position |
|---|---|---|
| TL | ↔ | TR |
| TR | ↔ | TL |
| BL | ↔ | BR |
| BR | ↔ | BL |

## ✅ 8 Pages Ka Final Order

### Goal: Cut karne pe yeh pairs chahiye
| Cut Position | Front | Back |
|---|---|---|
| Top-Left | Page 1 | Page 2 |
| Top-Right | Page 3 | Page 4 |
| Bottom-Left | Page 5 | Page 6 |
| Bottom-Right | Page 7 | Page 8 |

### FRONT Side (Sheet 1 ka page 1):
```
┌──────────┬──────────┐
│  Page 1   │  Page 3  │
│   (TL)    │   (TR)   │
├──────────┼──────────┤
│  Page 5   │  Page 7  │
│   (BL)    │   (BR)   │
└──────────┴──────────┘
```

### BACK Side (Sheet 1 ka page 2):
```
┌──────────┬──────────┐
│  Page 4   │  Page 2  │
│   (TL)    │   (TR)   │
├──────────┼──────────┤
│  Page 8   │  Page 6  │
│   (BL)    │   (BR)   │
└──────────┴──────────┘
```

> [!IMPORTANT]
> Back side mein pages **mirror** mein hain! Page 4 left pe hai aur Page 2 right pe — kyunki flip karne pe TL↔TR swap hota hai.

## 📊 Quick Reference Table

### 8 Pages → 1 Sheet
| | TL | TR | BL | BR |
|---|---|---|---|---|
| **FRONT** | 1 | 3 | 5 | 7 |
| **BACK** | 4 | 2 | 8 | 6 |

### 16 Pages → 2 Sheets
**Sheet 1:**
| | TL | TR | BL | BR |
|---|---|---|---|---|
| **FRONT** | 1 | 3 | 5 | 7 |
| **BACK** | 4 | 2 | 8 | 6 |

**Sheet 2:**
| | TL | TR | BL | BR |
|---|---|---|---|---|
| **FRONT** | 9 | 11 | 13 | 15 |
| **BACK** | 12 | 10 | 16 | 14 |

### 24 Pages → 3 Sheets
**Sheet 3:**
| | TL | TR | BL | BR |
|---|---|---|---|---|
| **FRONT** | 17 | 19 | 21 | 23 |
| **BACK** | 20 | 18 | 24 | 22 |

### General Formula (Har 8 pages ke group ke liye):
Pages `N` to `N+7`:
| | TL | TR | BL | BR |
|---|---|---|---|---|
| **FRONT** | N | N+2 | N+4 | N+6 |
| **BACK** | N+3 | N+1 | N+7 | N+5 |

## 🔧 PDF Mein Page Order

Agar aap manually PDF arrange kar rahe ho (Adobe Acrobat, PDF arranger, etc.):

**8 pages ka naya PDF order:**
```
Page 1, Page 3, Page 5, Page 7,    ← Front side ke 4 pages (TL, TR, BL, BR)
Page 4, Page 2, Page 8, Page 6     ← Back side ke 4 pages (TL, TR, BL, BR)
```

**16 pages ka naya PDF order:**
```
Page 1, Page 3, Page 5, Page 7,    ← Sheet 1 Front
Page 4, Page 2, Page 8, Page 6,    ← Sheet 1 Back
Page 9, Page 11, Page 13, Page 15, ← Sheet 2 Front
Page 12, Page 10, Page 16, Page 14 ← Sheet 2 Back
```

## 🖨️ Printing Instructions

1. **PDF arrange karo** (manually ya script se)
2. PDF open karo → Print
3. **Pages per sheet**: 4 (ya "Multiple" → 2×2)
4. **Page order**: Left to Right, Top to Bottom
5. **Duplex**: ON → **Long Edge Flip**
6. **Orientation**: Portrait
7. Print all pages
8. ✂️ Cut each sheet into 4 pieces
9. 🎉 Har piece ke aage-peeche sahi pages!

## 🐍 Python Script

Script location: `C:\Users\renu5\.gemini\antigravity\scratch\micro_print_arranger.py`

### Usage:
```bash
# Basic: input PDF → output PDF (auto-named)
python micro_print_arranger.py mybook.pdf

# Custom output name
python micro_print_arranger.py mybook.pdf arranged.pdf

# Short-edge flip (notepad style)
python micro_print_arranger.py mybook.pdf arranged.pdf --flip short

# Just see the order table (no PDF needed)
python micro_print_arranger.py --order-only 24
```

> [!TIP]
> Agar aapke pages odd number mein hain (jaise 11), toh script automatically blank pages add kar degi padding ke liye.

## ⚠️ Short-Edge Flip (Agar printer notepad style flip karta hai)

Agar aapka printer **short-edge** flip karta hai (upar-neeche paltna), toh order alag hoga:

### 8 Pages — Short Edge:
| | TL | TR | BL | BR |
|---|---|---|---|---|
| **FRONT** | 1 | 3 | 5 | 7 |
| **BACK** | 6 | 8 | 2 | 4 |

Script mein `--flip short` use karo.
