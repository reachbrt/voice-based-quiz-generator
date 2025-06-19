# 📁 Voice-Based Quiz Generator - Project Structure

## 🏗️ Directory Organization

This document provides a comprehensive overview of the project structure and organization.

### 📂 Root Directory Structure

```
voice-based-quiz-generator/
├── 📄 Core Application Files
├── 📚 Documentation (docs/)
├── 🧪 Tests (tests/)
├── 📜 Scripts (scripts/)
├── 💡 Examples (examples/)
├── 🎨 Assets (assets/)
├── ⚙️ Configuration Files
└── 🔧 Development Tools
```

## 📄 Core Application Files

### Main Application Components
```
├── app.py                    # Main Streamlit application entry point
├── config.py                 # Configuration management and settings
├── document_processor.py     # Document parsing (PDF, DOCX, TXT)
├── question_generator.py     # AI-powered question generation using OpenAI
├── quiz_manager.py          # Quiz session management and analytics
└── voice_handler.py         # Speech recognition and text-to-speech
```

#### File Descriptions

**`app.py`**
- Main Streamlit application
- User interface and navigation
- Component orchestration
- Session state management

**`config.py`**
- Environment variable management
- API key configuration
- Application settings
- Default values and constants

**`document_processor.py`**
- Multi-format document parsing
- Text extraction and cleaning
- Content preprocessing
- File validation

**`question_generator.py`**
- OpenAI GPT integration
- Question generation logic
- JSON parsing and validation
- Fallback question systems

**`quiz_manager.py`**
- Quiz session lifecycle
- Performance tracking
- Analytics and scoring
- Data export functionality

**`voice_handler.py`**
- Speech recognition integration
- Text-to-speech synthesis
- Audio file management
- Voice command processing

## 📚 Documentation (docs/)

### Documentation Structure
```
docs/
├── TECHNICAL_DOCUMENTATION.md    # Detailed technical architecture
├── ARCHITECTURE_DIAGRAMS.md      # Visual system design diagrams
├── SYSTEM_OVERVIEW.md             # High-level project overview
├── CONTRIBUTING.md                # Contribution guidelines
├── INSTALL.md                     # Installation instructions
├── SETUP_INSTRUCTIONS.md          # Detailed setup guide
└── PROJECT_STRUCTURE.md           # This file
```

#### Documentation Categories

**Technical Documentation**
- System architecture details
- Component interactions
- API integrations
- Database schemas

**User Guides**
- Installation instructions
- Setup procedures
- Usage examples
- Troubleshooting guides

**Developer Resources**
- Contributing guidelines
- Code standards
- Development workflow
- Testing procedures

## 🧪 Tests (tests/)

### Test Organization
```
tests/
├── test_installation.py          # Installation verification
├── test_session_state.py         # Streamlit session state testing
├── test_openai_fix.py            # OpenAI integration tests
├── test_json_parsing.py          # JSON parsing validation
├── test_final_fix.py             # Comprehensive system tests
├── verify_setup.py               # Setup verification
├── quick_test.py                 # Quick functionality tests
├── check_status.py               # System status checks
└── debug_openai.py               # OpenAI debugging utilities
```

#### Test Categories

**Installation Tests**
- Dependency verification
- Environment setup validation
- Configuration checks

**Unit Tests**
- Individual component testing
- Function-level validation
- Error handling verification

**Integration Tests**
- Component interaction testing
- API integration validation
- End-to-end workflows

**System Tests**
- Full application testing
- Performance validation
- User workflow testing

## 📜 Scripts (scripts/)

### Automation Scripts
```
scripts/
├── setup.py                      # Project setup automation
├── deploy_and_run.sh             # Deployment automation
├── github_setup.sh               # GitHub repository setup
├── github_setup.bat              # Windows GitHub setup
└── create_github_repo.sh         # Repository creation
```

#### Script Categories

**Setup Scripts**
- Environment preparation
- Dependency installation
- Configuration setup

**Deployment Scripts**
- Application deployment
- Server configuration
- Production setup

**Development Scripts**
- Development environment setup
- Code quality tools
- Testing automation

## 💡 Examples (examples/)

### Example Applications
```
examples/
├── demo.py                       # Demonstration application
├── sample_documents/             # Sample files for testing
├── usage_examples/               # Code usage examples
└── tutorials/                    # Step-by-step tutorials
```

#### Example Categories

**Demonstrations**
- Basic usage examples
- Feature showcases
- Integration examples

**Tutorials**
- Getting started guides
- Advanced usage patterns
- Best practices

**Sample Data**
- Test documents
- Sample configurations
- Example outputs

## 🎨 Assets (assets/)

### Asset Organization
```
assets/
├── images/                       # Project images and screenshots
├── audio/                        # Sample audio files
├── documents/                    # Sample documents
└── icons/                        # Application icons
```

## ⚙️ Configuration Files

### Configuration Structure
```
├── requirements.txt              # Python dependencies
├── .env.example                 # Environment variables template
├── .env                         # Environment variables (local)
├── Makefile                     # Build automation
├── .gitignore                   # Git ignore patterns
└── LICENSE                      # MIT License
```

#### Configuration Categories

**Dependencies**
- Python package requirements
- Version specifications
- Optional dependencies

**Environment**
- API keys and secrets
- Configuration variables
- Runtime settings

**Build Tools**
- Make targets
- Automation scripts
- Development helpers

## 🔧 Development Tools

### Development Structure
```
├── .github/                     # GitHub workflows and templates
├── __pycache__/                 # Python bytecode cache
├── venv/                        # Virtual environment
└── .git/                        # Git repository data
```

## 📋 File Naming Conventions

### Python Files
- **snake_case**: All Python files use snake_case naming
- **Descriptive names**: Clear, descriptive file names
- **Component grouping**: Related functionality grouped together

### Documentation
- **UPPERCASE**: Major documentation files in UPPERCASE
- **Descriptive**: Clear indication of content
- **Markdown**: All documentation in Markdown format

### Tests
- **test_prefix**: All test files start with `test_`
- **Component matching**: Test files match component names
- **Descriptive**: Clear indication of what is being tested

## 🎯 Best Practices

### File Organization
1. **Logical grouping**: Related files in appropriate directories
2. **Clear naming**: Descriptive and consistent naming
3. **Separation of concerns**: Different types of files in different directories
4. **Documentation**: Each directory has clear purpose

### Development Workflow
1. **Core files**: Main application logic in root directory
2. **Supporting files**: Documentation, tests, scripts in subdirectories
3. **Clean separation**: Clear boundaries between different types of content
4. **Easy navigation**: Intuitive structure for new contributors

### Maintenance
1. **Regular cleanup**: Remove unused files and directories
2. **Documentation updates**: Keep structure documentation current
3. **Consistent organization**: Maintain established patterns
4. **Version control**: Track structural changes in git

## 🚀 Getting Started

### For New Contributors
1. **Read documentation**: Start with README.md and this file
2. **Explore structure**: Familiarize yourself with directory organization
3. **Run tests**: Execute tests to understand functionality
4. **Check examples**: Review examples for usage patterns

### For Users
1. **Main application**: Start with app.py
2. **Configuration**: Set up .env file
3. **Documentation**: Read installation and setup guides
4. **Examples**: Try demo.py for quick start

This organized structure ensures maintainability, scalability, and ease of contribution for the Voice-Based Quiz Generator project.
