# Contributing to Voice-Based Quiz Generator

Thank you for your interest in contributing to the Voice-Based Quiz Generator! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature or bug fix
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request

## Development Setup

### Prerequisites
- Python 3.8+
- Git
- OpenAI API key (for testing)

### Setup Development Environment
```bash
# Clone your fork
git clone https://github.com/yourusername/voice-based-quiz-generator.git
cd voice-based-quiz-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies including dev tools
make dev-install
# Or manually:
pip install -r requirements.txt
pip install black flake8 pytest
```

## Code Style

We use Black for code formatting and Flake8 for linting.

```bash
# Format code
make format
# Or: black *.py

# Lint code
make lint
# Or: flake8 *.py --max-line-length=88 --ignore=E203,W503
```

## Testing

### Running Tests
```bash
# Test installation
python test_installation.py

# Run demo
python demo.py

# Test the full application (requires API key)
streamlit run app.py
```

### Adding Tests
- Add unit tests for new functionality
- Test both success and error cases
- Include tests for voice and non-voice modes
- Test with different document types

## Contribution Guidelines

### Bug Reports
When reporting bugs, please include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages or logs
- Screenshots if applicable

### Feature Requests
For new features, please:
- Check existing issues first
- Describe the use case
- Explain the expected behavior
- Consider backward compatibility

### Pull Requests
- Create a descriptive title
- Reference related issues
- Include tests for new functionality
- Update documentation as needed
- Ensure all tests pass
- Follow the existing code style

## Areas for Contribution

### High Priority
- [ ] Improved error handling and user feedback
- [ ] Additional document format support (PowerPoint, etc.)
- [ ] Better voice recognition accuracy
- [ ] Mobile-responsive design improvements
- [ ] Performance optimizations

### Medium Priority
- [ ] Multiple language support
- [ ] Custom question templates
- [ ] Integration with learning management systems
- [ ] Advanced analytics and reporting
- [ ] Offline mode capabilities

### Low Priority
- [ ] Gamification features
- [ ] Social sharing capabilities
- [ ] Custom themes and styling
- [ ] Plugin architecture
- [ ] API for external integrations

## Code Organization

### File Structure
```
├── app.py                    # Main Streamlit application
├── config.py                 # Configuration management
├── document_processor.py     # Document processing logic
├── question_generator.py     # AI question generation
├── voice_handler.py          # Voice processing
├── quiz_manager.py           # Quiz session management
├── requirements.txt          # Dependencies
├── tests/                    # Test files (to be added)
└── docs/                     # Documentation (to be added)
```

### Adding New Features

1. **Document Processors**: Add new format support in `document_processor.py`
2. **Question Types**: Extend `question_generator.py` for new question formats
3. **Voice Features**: Enhance `voice_handler.py` for new audio capabilities
4. **UI Components**: Add new Streamlit components in `app.py`
5. **Analytics**: Extend `quiz_manager.py` for new tracking features

## Documentation

- Update README.md for user-facing changes
- Update INSTALL.md for setup changes
- Add docstrings to new functions and classes
- Include inline comments for complex logic
- Update this CONTRIBUTING.md for process changes

## Release Process

1. Update version numbers
2. Update CHANGELOG.md
3. Test thoroughly
4. Create release notes
5. Tag the release
6. Update documentation

## Getting Help

- Check existing issues and documentation
- Ask questions in GitHub Discussions
- Join our community chat (if available)
- Contact maintainers directly for sensitive issues

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow GitHub's community guidelines

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

Thank you for contributing to make this project better!
