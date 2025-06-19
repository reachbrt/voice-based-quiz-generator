# 🏗️ Voice-Based Quiz Generator - Architecture Diagrams

## 📋 Table of Contents
1. [System Architecture Overview](#system-architecture-overview)
2. [Component Interaction Diagram](#component-interaction-diagram)
3. [Data Flow Diagrams](#data-flow-diagrams)
4. [Sequence Diagrams](#sequence-diagrams)
5. [Deployment Architecture](#deployment-architecture)

## 🏛️ System Architecture Overview

```mermaid
graph TB
    subgraph "Presentation Layer"
        UI[Streamlit Web Interface]
        VUI[Voice User Interface]
        API[REST API Endpoints]
    end
    
    subgraph "Business Logic Layer"
        AM[App Manager]
        QM[Quiz Manager]
        SM[Session Manager]
        PM[Performance Manager]
    end
    
    subgraph "Service Layer"
        DP[Document Processor]
        QG[Question Generator]
        VH[Voice Handler]
        PA[Performance Analyzer]
        EX[Export Service]
    end
    
    subgraph "Integration Layer"
        OPENAI[OpenAI GPT API]
        GSR[Google Speech Recognition]
        TTS[Text-to-Speech Service]
        FS[File System]
    end
    
    subgraph "Data Layer"
        SS[Session State]
        TF[Temporary Files]
        CF[Configuration Files]
        LF[Log Files]
    end
    
    UI --> AM
    VUI --> VH
    API --> AM
    AM --> QM
    AM --> SM
    QM --> QG
    QM --> PA
    SM --> PM
    DP --> FS
    QG --> OPENAI
    VH --> GSR
    VH --> TTS
    PA --> EX
    QM --> SS
    DP --> TF
    AM --> CF
    PM --> LF
    
    style UI fill:#e3f2fd
    style VUI fill:#e8f5e8
    style OPENAI fill:#fff3e0
    style GSR fill:#fff3e0
    style TTS fill:#fff3e0
    style SS fill:#f3e5f5
```

## 🔄 Component Interaction Diagram

```mermaid
graph LR
    subgraph "Frontend Components"
        UI[Streamlit UI]
        VUI[Voice Interface]
        UX[User Experience]
    end
    
    subgraph "Core Components"
        AM[App Manager]
        QM[Quiz Manager]
        DP[Document Processor]
        QG[Question Generator]
        VH[Voice Handler]
    end
    
    subgraph "External Services"
        OPENAI[OpenAI API]
        SPEECH[Speech Services]
        FILES[File System]
    end
    
    UI <--> AM
    VUI <--> VH
    UX <--> UI
    
    AM <--> QM
    AM <--> DP
    QM <--> QG
    QM <--> VH
    
    DP <--> FILES
    QG <--> OPENAI
    VH <--> SPEECH
    
    style UI fill:#bbdefb
    style OPENAI fill:#ffcc80
    style SPEECH fill:#ffcc80
```

## 📊 Data Flow Diagrams

### 1. Document Processing Flow

```mermaid
flowchart TD
    A[User Uploads Document] --> B{File Type?}
    B -->|PDF| C[PyPDF2 Extraction]
    B -->|DOCX| D[python-docx Extraction]
    B -->|TXT| E[Direct Text Reading]
    
    C --> F[Text Cleaning]
    D --> F
    E --> F
    
    F --> G[Content Preprocessing]
    G --> H[Text Chunking]
    H --> I[Ready for Question Generation]
    
    style A fill:#e1f5fe
    style I fill:#e8f5e8
```

### 2. Question Generation Flow

```mermaid
flowchart TD
    A[Processed Content] --> B[Create AI Prompt]
    B --> C[Send to OpenAI API]
    C --> D{API Response OK?}
    
    D -->|Yes| E[Parse JSON Response]
    D -->|No| F[Use Sample Questions]
    
    E --> G{Valid JSON?}
    G -->|Yes| H[Validate Questions]
    G -->|No| I[Try Alternative Parsing]
    
    H --> J{Questions Valid?}
    J -->|Yes| K[Questions Ready]
    J -->|No| L[Filter Valid Questions]
    
    I --> M{Parsing Success?}
    M -->|Yes| H
    M -->|No| F
    
    F --> K
    L --> K
    K --> N[Initialize Quiz Session]
    
    style A fill:#e1f5fe
    style K fill:#e8f5e8
    style F fill:#fff3e0
```

### 3. Voice Processing Flow

```mermaid
flowchart TD
    A[User Speaks] --> B[Audio Capture]
    B --> C[Audio Processing]
    C --> D[Send to Speech Recognition]
    D --> E{Recognition Success?}
    
    E -->|Yes| F[Parse Answer]
    E -->|No| G[Request Retry]
    
    F --> H{Valid Answer?}
    H -->|Yes| I[Submit Answer]
    H -->|No| J[Ask for Clarification]
    
    I --> K[Generate Feedback]
    K --> L[Text-to-Speech]
    L --> M[Play Audio Feedback]
    
    G --> A
    J --> A
    
    style A fill:#e1f5fe
    style I fill:#e8f5e8
    style M fill:#f3e5f5
```

## 🔄 Sequence Diagrams

### 1. Complete Quiz Session Sequence

```mermaid
sequenceDiagram
    participant U as User
    participant UI as Streamlit UI
    participant AM as App Manager
    participant DP as Document Processor
    participant QG as Question Generator
    participant AI as OpenAI API
    participant QM as Quiz Manager
    participant VH as Voice Handler
    participant SR as Speech Recognition
    
    Note over U,SR: Document Upload & Processing
    U->>UI: Upload Document
    UI->>AM: Process Upload Request
    AM->>DP: Extract Document Content
    DP->>DP: Clean & Preprocess Text
    DP->>AM: Return Processed Content
    
    Note over U,SR: Question Generation
    AM->>QG: Generate Questions Request
    QG->>AI: Send Content + Prompt
    AI->>QG: Return Generated Questions
    QG->>QG: Parse & Validate JSON
    QG->>AM: Return Valid Questions
    
    Note over U,SR: Quiz Session Initialization
    AM->>QM: Initialize Quiz Session
    QM->>QM: Setup Session State
    QM->>UI: Ready for Quiz
    
    Note over U,SR: Quiz Interaction Loop
    loop For Each Question
        QM->>UI: Display Current Question
        UI->>U: Show Question & Options
        
        alt Voice Mode Selected
            U->>VH: Speak Answer
            VH->>SR: Process Audio
            SR->>VH: Return Recognized Text
            VH->>VH: Parse Answer (A/B/C/D)
            VH->>QM: Submit Parsed Answer
        else Text Mode Selected
            U->>UI: Click Answer Option
            UI->>QM: Submit Selected Answer
        end
        
        QM->>QM: Evaluate Answer
        QM->>QM: Update Score & Progress
        QM->>UI: Show Feedback
        
        opt Voice Feedback Enabled
            QM->>VH: Generate Audio Feedback
            VH->>VH: Create TTS Audio
            VH->>UI: Play Audio Feedback
        end
        
        QM->>QM: Check Quiz Completion
    end
    
    Note over U,SR: Results & Analytics
    QM->>QM: Calculate Final Statistics
    QM->>UI: Display Results
    UI->>U: Show Performance Analytics
    
    opt Export Results
        U->>UI: Request Export
        UI->>QM: Generate Export Data
        QM->>U: Download Results File
    end
```

### 2. Error Handling Sequence

```mermaid
sequenceDiagram
    participant U as User
    participant UI as Streamlit UI
    participant QG as Question Generator
    participant AI as OpenAI API
    participant FB as Fallback System
    
    U->>UI: Request Question Generation
    UI->>QG: Generate Questions
    QG->>AI: API Request
    
    alt API Success
        AI->>QG: Valid Response
        QG->>QG: Parse JSON
        QG->>UI: Return Questions
    else API Error
        AI->>QG: Error Response
        QG->>FB: Trigger Fallback
        FB->>QG: Sample Questions
        QG->>UI: Return Fallback Questions
        UI->>U: Show Warning Message
    else JSON Parse Error
        AI->>QG: Invalid JSON
        QG->>QG: Try Alternative Parsing
        alt Alternative Success
            QG->>UI: Return Parsed Questions
        else Alternative Fails
            QG->>FB: Trigger Fallback
            FB->>QG: Sample Questions
            QG->>UI: Return Fallback Questions
        end
    end
```

## 🚀 Deployment Architecture

### 1. Local Development Architecture

```mermaid
graph TB
    subgraph "Developer Machine"
        subgraph "Development Environment"
            IDE[VS Code / IDE]
            TERM[Terminal]
            BROWSER[Web Browser]
        end
        
        subgraph "Python Environment"
            VENV[Virtual Environment]
            DEPS[Dependencies]
            APP[Streamlit App]
        end
        
        subgraph "Local Services"
            FS[File System]
            LOGS[Log Files]
            TEMP[Temp Files]
        end
    end
    
    subgraph "External Services"
        OPENAI[OpenAI API]
        GOOGLE[Google Services]
        GITHUB[GitHub Repository]
    end
    
    IDE --> APP
    TERM --> APP
    BROWSER --> APP
    APP --> VENV
    VENV --> DEPS
    APP --> FS
    APP --> LOGS
    APP --> TEMP
    APP --> OPENAI
    APP --> GOOGLE
    IDE --> GITHUB
    
    style APP fill:#e3f2fd
    style OPENAI fill:#fff3e0
    style GOOGLE fill:#fff3e0
```

### 2. Production Deployment Architecture

```mermaid
graph TB
    subgraph "Cloud Infrastructure"
        subgraph "Load Balancer"
            LB[Application Load Balancer]
        end
        
        subgraph "Application Tier"
            APP1[App Instance 1]
            APP2[App Instance 2]
            APP3[App Instance 3]
        end
        
        subgraph "Storage Tier"
            FS[Shared File System]
            LOGS[Centralized Logging]
            CACHE[Redis Cache]
        end
        
        subgraph "Monitoring"
            MON[Application Monitoring]
            ALERT[Alerting System]
            METRICS[Metrics Collection]
        end
    end
    
    subgraph "External Services"
        OPENAI[OpenAI API]
        GOOGLE[Google Cloud Services]
        CDN[Content Delivery Network]
    end
    
    subgraph "Users"
        WEB[Web Users]
        MOBILE[Mobile Users]
        API_USERS[API Users]
    end
    
    WEB --> CDN
    MOBILE --> CDN
    API_USERS --> LB
    CDN --> LB
    LB --> APP1
    LB --> APP2
    LB --> APP3
    
    APP1 --> FS
    APP2 --> FS
    APP3 --> FS
    
    APP1 --> CACHE
    APP2 --> CACHE
    APP3 --> CACHE
    
    APP1 --> LOGS
    APP2 --> LOGS
    APP3 --> LOGS
    
    APP1 --> OPENAI
    APP2 --> OPENAI
    APP3 --> OPENAI
    
    APP1 --> GOOGLE
    APP2 --> GOOGLE
    APP3 --> GOOGLE
    
    MON --> APP1
    MON --> APP2
    MON --> APP3
    MON --> ALERT
    MON --> METRICS
    
    style LB fill:#e3f2fd
    style APP1 fill:#e8f5e8
    style APP2 fill:#e8f5e8
    style APP3 fill:#e8f5e8
    style OPENAI fill:#fff3e0
    style GOOGLE fill:#fff3e0
```

### 3. Container Deployment Architecture

```mermaid
graph TB
    subgraph "Container Orchestration"
        subgraph "Kubernetes Cluster"
            subgraph "Namespace: quiz-app"
                POD1[App Pod 1]
                POD2[App Pod 2]
                POD3[App Pod 3]
                SVC[Service]
                ING[Ingress]
            end
            
            subgraph "Namespace: monitoring"
                PROM[Prometheus]
                GRAF[Grafana]
                ALERT[AlertManager]
            end
            
            subgraph "Namespace: logging"
                ELK[ELK Stack]
                FLUENTD[Fluentd]
            end
        end
        
        subgraph "Persistent Storage"
            PV[Persistent Volumes]
            SC[Storage Class]
        end
    end
    
    subgraph "External Dependencies"
        REGISTRY[Container Registry]
        OPENAI[OpenAI API]
        GOOGLE[Google Services]
    end
    
    ING --> SVC
    SVC --> POD1
    SVC --> POD2
    SVC --> POD3
    
    POD1 --> PV
    POD2 --> PV
    POD3 --> PV
    
    POD1 --> OPENAI
    POD2 --> OPENAI
    POD3 --> OPENAI
    
    POD1 --> GOOGLE
    POD2 --> GOOGLE
    POD3 --> GOOGLE
    
    PROM --> POD1
    PROM --> POD2
    PROM --> POD3
    
    FLUENTD --> POD1
    FLUENTD --> POD2
    FLUENTD --> POD3
    FLUENTD --> ELK
    
    REGISTRY --> POD1
    REGISTRY --> POD2
    REGISTRY --> POD3
    
    style POD1 fill:#e8f5e8
    style POD2 fill:#e8f5e8
    style POD3 fill:#e8f5e8
    style OPENAI fill:#fff3e0
    style GOOGLE fill:#fff3e0
```

---

## 📝 Diagram Legend

### Color Coding
- 🔵 **Blue**: User Interface Components
- 🟢 **Green**: Application Logic Components
- 🟠 **Orange**: External Services/APIs
- 🟣 **Purple**: Data Storage Components
- 🟡 **Yellow**: Infrastructure Components

### Component Types
- **Rectangles**: Services/Components
- **Diamonds**: Decision Points
- **Circles**: Start/End Points
- **Arrows**: Data Flow Direction
- **Dotted Lines**: Optional/Conditional Flow

This comprehensive architecture documentation provides a clear understanding of how the Voice-Based Quiz Generator system is structured, how components interact, and how data flows through the system.
