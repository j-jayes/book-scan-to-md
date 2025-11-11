# Contributing to Book Scan to Markdown

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in the [Issues](https://github.com/j-jayes/book-scan-to-md/issues) tab
2. If not, create a new issue with:
   - Clear title describing the problem
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)
   - Example PDF or screenshots (if relevant)

### Suggesting Enhancements

We welcome suggestions for new features! Please:

1. Check existing issues and pull requests first
2. Create an issue describing:
   - The problem you're trying to solve
   - Your proposed solution
   - Why this would be useful to others
   - Any implementation ideas

### Code Contributions

#### Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/book-scan-to-md.git
   cd book-scan-to-md
   ```

3. Set up development environment:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -e ".[dev]"
   ```

4. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Making Changes

1. **Write Clean Code**:
   - Follow PEP 8 style guidelines
   - Use type hints where appropriate
   - Add docstrings to functions and classes
   - Keep functions focused and small

2. **Format Your Code**:
   ```bash
   make format  # Runs black
   make lint    # Runs ruff
   ```

3. **Test Your Changes**:
   - Test manually with sample PDFs
   - Ensure existing functionality still works
   - Add tests if you're adding new features

4. **Document Your Changes**:
   - Update README.md if adding features
   - Add examples to docs/EXAMPLES.md
   - Update docs/DOCUMENTATION.md for architecture changes

#### Commit Guidelines

Write clear, descriptive commit messages:

```bash
# Good
git commit -m "Add support for JPEG image input"
git commit -m "Fix page number removal for bottom-centered numbers"
git commit -m "Improve error handling for corrupted PDFs"

# Bad
git commit -m "fix bug"
git commit -m "updates"
git commit -m "wip"
```

#### Submitting Pull Requests

1. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Create a Pull Request on GitHub:
   - Use a clear, descriptive title
   - Reference any related issues (#123)
   - Describe what changes you made and why
   - Include screenshots/examples if relevant
   - List any breaking changes

3. Wait for review:
   - Respond to feedback promptly
   - Make requested changes
   - Be patient - reviews may take time

## Development Guidelines

### Code Style

- Use Black for formatting (line length: 100)
- Use Ruff for linting
- Follow PEP 8 conventions
- Use type hints for function parameters and returns

### Project Structure

```
book-scan-to-md/
├── scripts/          # Python scripts
├── data/            # Data directories
├── docs/            # Documentation
├── pyproject.toml   # Project configuration
└── tests/           # Tests (if added)
```

### Adding New Features

When adding new features:

1. Consider backwards compatibility
2. Update documentation
3. Add usage examples
4. Consider performance implications
5. Think about error handling

### Improving Documentation

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add more examples
- Improve setup instructions
- Translate documentation (if multilingual support is added)

## Areas for Contribution

Here are some areas where contributions would be especially valuable:

### High Priority
- [ ] Add comprehensive test suite
- [ ] Improve error handling and recovery
- [ ] Add progress saving for large documents
- [ ] Support for direct image input (not just PDF)

### Medium Priority
- [ ] Web interface for easier use
- [ ] Docker containerization
- [ ] Batch processing optimizations
- [ ] Multi-language support

### Nice to Have
- [ ] OCR confidence scoring
- [ ] Automatic image preprocessing
- [ ] Custom prompt templates
- [ ] Output format options (HTML, DOCX, etc.)

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other contributors

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal attacks
- Publishing others' private information

## Questions?

If you have questions about contributing:

- Check existing documentation
- Look through closed issues and PRs
- Open a new issue with your question
- Reach out to maintainers

## Recognition

Contributors will be recognized in:
- The project README
- Release notes for their contributions
- GitHub contributors page

Thank you for contributing to make this project better! 🎉
