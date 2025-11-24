# Contributing to Polygon Area Calculator

Thank you for your interest in contributing!  
This project welcomes improvements, bug fixes, documentation updates, feature additions, and test enhancements.

Below are the guidelines and workflow to help you contribute effectively.

---

## 🧱 How to Contribute

### 1. Fork the Repository
Click **Fork** in the upper-right corner of the repository page on GitHub.

### 2. Clone Your Fork
```bash
git clone https://github.github.com/<your-username>/Polygon-Area-Calculator.git
cd Polygon-Area-Calculator
```

### 3. Create a Feature Branch
Follow this pattern:
```bash
git checkout -b feature/my-new-feature
```

### 4. Install the Project in Editable Mode
This lets Python import your live code changes:
```bash
pip install -e .
```

### 5. Install Dev Dependencies (Optional but Recommended)
If you want linting or formatting:
```bash
pip install black flake8 pytest
```

### 6. Run the Test Suite
Always run tests before submitting a PR.
```bash
pytest -q
```

### 7. Make Your Changes
Follow best practices:

- Maintain clear and descriptive naming
- Use consistent indentation and formatting
- Ensure Square still behaves as a proper subclass of Rectangle
- Keep public method behavior stable unless intentional change
- Write clear docstrings where needed

### 8. Commit Your Work
Write meaningful commit messages:
```bash
git commit -m "Fix: Improved get_amount_inside calculation"
git commit -m "Add: New tests for diagonal computation"
```

### 9. Push and Open a Pull Request
```bash
git push origin feature/my-new-feature
```

Then open a **Pull Request** on GitHub.

Describe:

- What you changed  
- Why you changed it  
- Any tests added or updated  
- Any breaking changes (if applicable)

---

## 🔍 Code Style

This project uses:

- **Black** → automatic code formatting  
- **Flake8** → linting for code quality  
- **Pytest** → testing framework  

Lint and test workflows run automatically on GitHub Actions for every pull request.

You can run them locally:

```bash
black .
flake8 .
pytest -q
```

---

## 🧪 Testing Guidelines

If you add new features, ensure:

- Your tests cover success + edge cases  
- Rectangle and Square still pass expected OOP relationships  
- get_picture() respects the 50x50 limit  
- get_amount_inside() handles non-fitting shapes gracefully  

Place all tests under:

```
tests/
```

---

## 💡 Suggestions and Feature Requests

Open an Issue if:

- You want to discuss a new feature  
- You have questions about design decisions  
- You found a bug  
- You want clarification about expected behavior  

Issues are appreciated as much as pull requests!

---

## 💬 Questions?

If you’re unsure about anything, feel free to open an issue.  
We’re friendly — ask anything! 😊

---

## 🙏 Thank You!

Your contributions make this project better for everyone.  
Happy coding! 🚀
