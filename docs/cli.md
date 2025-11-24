# 🖥️ Command Line Interface (CLI)

The Polygon Area Calculator includes a simple command-line interface for quickly computing properties of rectangles and squares without writing Python scripts.

---

## ▶️ Running the CLI

After installing the project (`pip install .`), run:

```bash
polygon-calculator --help
```

---

# 📐 Rectangle Mode

Compute properties of a rectangle:

```bash
polygon-calculator --rectangle 10 5
```

Output:

```
Rectangle(width=10, height=5)
Area: 50
Perimeter: 30
Diagonal: 11.18
Picture:
**********
**********
**********
**********
**********
```

---

# 🟥 Square Mode

Compute properties of a square:

```bash
polygon-calculator --square 7
```

Output:

```
Square(side=7)
Area: 49
Perimeter: 28
Diagonal: 9.89
Picture:
*******
*******
*******
*******
*******
*******
*******
```

---

## 📄 Notes

- All numeric inputs are automatically converted to floats  
- ASCII art drawing is limited to shapes ≤ 50×50  
- If no arguments are provided, help text is shown  

---

Happy computing! 🚀
