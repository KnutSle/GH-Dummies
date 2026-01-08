# Contributing Guide

This repository is for learning GitHub basics. Here's how to practice:

## Basic Git Commands

### 1. Clone the repository
```bash
git clone https://github.com/KnutSle/GH-Dummies.git
cd GH-Dummies
```

### 2. Check status
```bash
git status
```

### 3. Create a new branch
```bash
git checkout -b my-feature-branch
```

### 4. Make changes
Edit any file, for example `hello.py`

### 5. See your changes
```bash
git diff
```

### 6. Stage your changes
```bash
git add hello.py
# or add all changes:
git add .
```

### 7. Commit your changes
```bash
git commit -m "Description of your changes"
```

### 8. Push your branch
```bash
git push origin my-feature-branch
```

### 9. Create a Pull Request
Go to GitHub and create a pull request from your branch

## GitHub Workflow Practice

1. **Issues**: Create an issue to describe what you want to work on
2. **Branches**: Create a branch for your changes
3. **Commits**: Make small, focused commits with clear messages
4. **Pull Requests**: Open a PR when your changes are ready for review
5. **Review**: Ask for feedback on your PR
6. **Merge**: Merge your PR when approved

## Tips

- Write clear commit messages
- Keep commits small and focused
- Pull the latest changes regularly: `git pull origin main`
- Use descriptive branch names
- Test your changes before committing
