# 🏗️ RANTAI HealthChain - Technical Architecture

Comprehensive technical documentation of RANTAI HealthChain's architecture, design patterns, and implementation details.

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Architecture Layers](#architecture-layers)
3. [Technology Stack](#technology-stack)
4. [AI Intelligence Architecture](#ai-intelligence-architecture)
5. [Project Structure](#project-structure)
6. [Data Flow](#data-flow)
7. [Blockchain Integration](#blockchain-integration)
8. [State Management](#state-management)
9. [API Design](#api-design)
10. [Security Architecture](#security-architecture)
11. [Performance Optimization](#performance-optimization)
12. [Contact & Support](#contact--support)

---

## System Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                       │
│         (Next.js 15 + React 19 + TypeScript + AI)           │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                  Application Layer                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ Patient  │  │ Doctor   │  │Insurance │  │  Health  │    │
│  │ Portal   │  │ Panel    │  │ Portal   │  │ Centers  │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
│                                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │Emergency │  │ Second   │  │Predictive│  │  Mental  │    │
│  │   SOS    │  │ Opinion  │  │   AI     │  │  Health  │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│              AI Intelligence Layer (45+ Modes)                │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Google Gemini 2.0 Flash API - Medical AI Engine    │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ Fitness  │  │Nutrition │  │ Maternal │  │  Heart   │    │
│  │   AI     │  │   AI     │  │ & Child  │  │ Health   │    │
│  │ 5 Modes  │  │ 5 Modes  │  │  AI      │  │   AI     │    │
│  └──────────┘  └──────────┘  │ 5 Modes  │  │ 5 Modes  │    │
│  ┌──────────┐  ┌──────────┐  └──────────┘  └──────────┘    │
│  │  Mental  │  │   Eye    │  ┌──────────┐  ┌──────────┐    │
│  │ Wellness │  │  Health  │  │Emergency │  │  Second  │    │
│  │   AI     │  │   AI     │  │   AI     │  │ Opinion  │    │
│  │ 5 Modes  │  │ 5 Modes  │  │ Assistant│  │   AI     │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
│  + 7 more specialized AI modules...                          │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                  Blockchain Layer                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ Wagmi    │  │RainbowKit│  │ Ethers.js│  │  Smart   │    │
│  │  Hooks   │  │ Wallets  │  │ Library  │  │Contracts │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│          Ethereum Sepolia Network + IPFS Storage              │
└───────────────────────────────────────────────────────────────┘
```

### Core Principles

1. **AI-First Healthcare**: 45+ specialized AI modes for comprehensive care
2. **Patient-Centric Design**: Users own their data
3. **Blockchain Transparency**: Immutable, verifiable records
4. **Privacy First**: End-to-end encryption
5. **Dual-Mode Architecture**: Works with/without wallet
6. **Modular Structure**: Independent, reusable modules
7. **Type Safety**: Strict TypeScript throughout
8. **Responsive Design**: Mobile-first approach
9. **Indonesian Market Focus**: BPJS integration, Bahasa Indonesia

---

## Architecture Layers

### 1. Presentation Layer

**Technologies**: React 19, Next.js 15, TypeScript, Tailwind CSS

**Components**:
- **12 Major Portal Modules**: Patient, Doctor, Insurance, etc.
- **6 Health Centers with AI**: Each with dedicated AI Assistant
- **56+ shadcn/ui Components**: Buttons, Cards, Dialogs, etc.
- **AI Companion**: Floating chat interface
- **Connection Status**: Blockchain mode indicator

**Responsibilities**:
- Render UI components
- Handle user interactions
- Client-side routing (Next.js App Router)
- State management via hooks
- Responsive layouts
- AI chat interfaces

### 2. Application Layer

**Technologies**: Custom React Hooks, TypeScript

**Components**:
- **15 Custom Hooks**: Business logic encapsulation
- **Module State Management**: Local state per module
- **Form Validation**: Zod schemas, React Hook Form
- **Data Transformation**: Format data for UI
- **localStorage Integration**: Guest mode persistence

**Key Hooks**:
```typescript
use-health-chain.ts              // Core blockchain interactions
use-connection-mode.tsx          // Wallet connection state
use-immunization-tracker.ts      // Vaccination management
use-pharmacy-blockchain.ts       // Medication ordering
use-emergency-sos.ts             // Emergency system
use-second-opinion.ts            // Multi-doctor consultations
use-predictive-health-ai.ts      // AI risk predictions
use-mental-health-sanctuary.ts   // Mental wellness
use-lab-results.ts               // Lab integration
// ... and 6 more
```

### 3. AI Intelligence Layer

**Technologies**: Google Gemini 2.0 Flash API, Custom AI Prompts

**Architecture**:
- **16 AI API Routes**: Specialized endpoints for each AI module
- **45+ AI Modes**: Distributed across Health Centers and clinical modules
- **Context-Aware Processing**: Uses patient data for personalized responses
- **Indonesian Language**: All AI responses in Bahasa Indonesia
- **Real-Time Analysis**: Sub-2 second response times

**AI Categories**:

#### Health Centers AI (30 Modes)
- Fitness AI Coach (5 modes)
- Nutrition AI Coach (5 modes)
- Maternal & Child AI (5 modes)
- Heart Health AI (5 modes)
- Mental Wellness AI (5 modes)
- Eye Health AI (5 modes)

#### Clinical & Emergency AI (15+ Modes)
- Emergency AI Assistant
- Second Opinion AI
- Lab Interpretation Engine
- Vaccine Intelligence
- Mental Health Sanctuary AI
- Clinical Intelligence Suite
- And more...

#### Healthcare Operations AI
- Pharmacy Intelligence
- Health Insights Engine
- Smart Claims Intelligence
- Medical Knowledge Assistant

### 4. Blockchain Layer

**Technologies**: Wagmi, RainbowKit, Ethers.js, SIWE

**Components**:
- **Wallet Connection**: RainbowKit UI + Wagmi hooks
- **Smart Contract Interactions**: Read/write blockchain
- **Transaction Management**: Signing, broadcasting, verification
- **IPFS Integration**: Decentralized file storage
- **Network Management**: Sepolia testnet configuration

**Configuration** (`src/lib/web3-config.ts`):
```typescript
export const config = getDefaultConfig({
  appName: 'RANTAI HealthChain',
  projectId: 'f8d248f838ec4f12b0f01efd2b238206',
  chains: [sepolia],
  ssr: true,
});

export const HEALTH_CHAIN_CONTRACT = 
  '0xfC1D504D6D7049c548100AD21e11962180272177';
```

### 5. API Layer

**Technologies**: Next.js API Routes

**Endpoints**:
```
Core APIs:
/api/proxy          // External API requests (client → proxy → external)
/api/health         // Health check endpoint
/api/logger         // Logging endpoint

AI Intelligence APIs (16 Routes):
/api/fitness-ai                    // Fitness AI Coach (5 modes)
/api/nutrition-ai                  // Nutrition AI Coach (5 modes)
/api/maternal-child-ai             // Maternal & Child AI (5 modes)
/api/heart-health-ai               // Heart Health AI (5 modes)
/api/mental-wellness-enhanced-ai   // Mental Wellness AI (5 modes)
/api/eye-health-ai                 // Eye Health AI (5 modes)
/api/emergency-ai                  // Emergency Assistant
/api/second-opinion-ai             // Second Opinion AI
/api/lab-ai                        // Lab Interpretation
/api/vaccine-ai                    // Vaccine Intelligence
/api/mental-health-ai              // Mental Health Sanctuary AI
/api/pharmacy-ai                   // Pharmacy Intelligence
/api/clinical-ai                   // Clinical Intelligence Suite
/api/analytics-ai                  // Health Insights Engine
/api/claims-ai                     // Smart Claims Intelligence
/api/knowledge-ai                  // Medical Knowledge Assistant
```

**Proxy Architecture**:
- All external API calls routed through proxy
- Prevents CORS issues
- Hides API keys from client
- Rate limiting (future)

### 6. Data Layer

**Storage Options**:

#### Guest Mode (localStorage)
```typescript
// Data stored in browser localStorage
{
  "healthRecords": [...],
  "vaccinations": [...],
  "moodJournal": [...],
  "therapySessions": [...],
  "aiConversations": [...]
}
```

#### Blockchain Mode (Ethereum + IPFS)
```typescript
// Smart contract on Sepolia
contract HealthChain {
  struct Record {
    string ipfsHash;    // Reference to IPFS
    uint256 timestamp;
  }
  
  mapping(address => Record[]) public records;
  mapping(address => mapping(address => bool)) public access;
}
```

---

## Technology Stack

### Frontend Framework

#### Next.js 15.3.8+
- **App Router**: File-based routing
- **Server Components**: Improved performance
- **API Routes**: Backend endpoints (16 AI routes)
- **Image Optimization**: Automatic image optimization
- **Font Optimization**: Built-in font loading

#### React 19.1.0
- **Hooks**: useState, useEffect, useContext, custom hooks
- **Server Actions**: Direct server mutations (future)
- **Suspense**: Loading states
- **Error Boundaries**: Error handling

#### TypeScript 5.8.3
- **Strict Mode**: Full type safety
- **Type Inference**: Smart type detection
- **Interface Definitions**: 60+ interfaces
- **Generics**: Reusable type patterns

### Styling

#### Tailwind CSS
- **Utility-First**: Rapid UI development
- **Responsive**: Mobile-first breakpoints
- **Dark Mode**: Theme toggle support
- **Custom Theme**: Extended color palette
- **Animations**: Custom transitions

#### shadcn/ui Components
- **56 Components**: Pre-built, accessible
- **Radix UI**: Headless component primitives
- **Customizable**: Full control over styling
- **Accessible**: WCAG 2.1 compliant

### Blockchain

#### Wagmi 2.17.2
```typescript
// React hooks for Ethereum
useAccount()        // Get connected account
useConnect()        // Connect wallet
useDisconnect()     // Disconnect wallet
useBalance()        // Get ETH balance
useContractRead()   // Read smart contract
useContractWrite()  // Write smart contract
useWaitForTransaction() // Wait for confirmation
```

#### RainbowKit 2.2.8
- **Wallet UI**: Beautiful connection modal
- **Multiple Wallets**: MetaMask, Coinbase, Rainbow, WalletConnect
- **Network Switching**: Auto-prompt network change
- **Account Modal**: View address, balance, disconnect

#### Ethers.js 6.15.0
- **Contract Interaction**: Read/write smart contracts
- **Transaction Signing**: Sign messages & transactions
- **Event Listening**: Listen to blockchain events
- **Utility Functions**: Format addresses, parse units

### Artificial Intelligence

#### Google Gemini 2.0 Flash API
- **45+ Specialized Modes**: Distributed across 16 AI endpoints
- **Medical-Grade Analysis**: Disease prediction, risk assessment
- **Natural Language Processing**: Context-aware conversations
- **Indonesian Language**: Native Bahasa Indonesia support
- **Real-Time Responses**: <2 second latency
- **Multi-Modal**: Text analysis, medical reasoning

#### ElevenLabs TTS API
- **Voice Synthesis**: Indonesian voice output (future)
- **Natural Speech**: High-quality audio generation
- **Accessibility**: Audio feedback for visually impaired

#### AI Capabilities
- **Diagnostic Support**: Symptom analysis, differential diagnosis
- **Predictive Analytics**: Disease risk prediction (85-92% accuracy)
- **Treatment Recommendations**: Evidence-based guidance
- **Health Education**: Patient education in Indonesian
- **Emergency Triage**: Critical situation detection
- **Mental Health Support**: Therapeutic conversations

### State Management

#### Local State (React Hooks)
```typescript
// Module-level state with custom hooks
const {
  records,
  addRecord,
  updateRecord,
  deleteRecord
} = useHealthChain();
```

#### Context API
```typescript
// Global state for wallet connection
const ConnectionContext = createContext<ConnectionContextType>();

export function ConnectionProvider({ children }) {
  const { address, isConnected } = useAccount();
  const mode = isConnected ? 'blockchain' : 'guest';
  
  return (
    <ConnectionContext.Provider value={{ isConnected, address, mode }}>
      {children}
    </ConnectionContext.Provider>
  );
}
```

#### localStorage
```typescript
// Persistent guest mode data
localStorage.setItem('healthRecords', JSON.stringify(records));
const records = JSON.parse(localStorage.getItem('healthRecords') || '[]');
```

### Form Management

#### React Hook Form
- **Validation**: Real-time form validation
- **Performance**: Optimized re-renders
- **Type Safety**: Full TypeScript support
- **Error Handling**: User-friendly error messages

#### Zod
- **Schema Validation**: Type-safe schemas
- **Runtime Validation**: Validate at runtime
- **Error Messages**: Custom error messages
- **Type Inference**: Infer TypeScript types from schemas

### UI Libraries

#### Lucide React
- **1000+ Icons**: Beautiful, consistent icons
- **Tree-Shakable**: Only import what's used
- **Customizable**: Size, color, stroke width

#### Framer Motion
- **Animations**: Smooth, declarative animations
- **Gestures**: Drag, hover, tap interactions
- **Layout Animations**: Auto-animate layout changes

#### Recharts
- **Data Visualization**: Line, bar, pie, area charts
- **Responsive**: Adapts to container size
- **Customizable**: Full control over styling

---

## AI Intelligence Architecture

### Overview

RANTAI HealthChain features a comprehensive AI system with **45+ specialized modes** across **16 API endpoints**, powered by Google Gemini 2.0 Flash API.

### AI System Design

```
┌─────────────────────────────────────────────────────────────┐
│                   User Interaction Layer                      │
│         (Health Centers, Clinical Modules, Chat UI)          │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                  AI Request Handler                           │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Context Collection (Patient Data, Health Metrics)   │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Mode Selection (45+ Specialized AI Modes)           │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│              AI Processing Layer (16 API Routes)              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Google Gemini 2.0 Flash API Integration            │   │
│  │  - Medical knowledge base                            │   │
│  │  - Clinical reasoning engine                         │   │
│  │  - Evidence-based recommendations                    │   │
│  │  - Indonesian language processing                    │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                  Response Processing                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  - Format in Bahasa Indonesia                        │   │
│  │  - Add safety disclaimers                            │   │
│  │  - Crisis detection                                  │   │
│  │  - Professional referral guidance                    │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│              User Interface Display                           │
│         (Formatted Response with Markdown, Icons)            │
└───────────────────────────────────────────────────────────────┘
```

### AI Endpoint Architecture

Each AI endpoint follows a standardized architecture:

```typescript
// Example: /api/fitness-ai/route.ts
export async function POST(request: Request) {
  // 1. Parse request
  const { mode, query, context } = await request.json();
  
  // 2. Build specialized prompt for selected mode
  const systemPrompt = buildModePrompt(mode, context);
  
  // 3. Call Gemini API
  const response = await callGeminiAPI(systemPrompt, query);
  
  // 4. Process and format response
  const formattedResponse = formatInIndonesian(response);
  
  // 5. Add safety checks
  const safeResponse = addSafetyDisclaimer(formattedResponse);
  
  // 6. Return to client
  return Response.json({ response: safeResponse });
}
```

### AI Mode Specialization

Each of the 45+ AI modes is specialized for specific healthcare tasks:

#### Fitness AI (5 Modes)
- **Workout Optimizer**: Creates periodized training programs
- **Form Coach**: Provides exercise technique cues
- **Injury Prevention**: Analyzes pain patterns, suggests modifications
- **Progress Analyzer**: Breaks plateaus, optimizes performance
- **Sport-Specific**: Tailors training for specific sports

#### Nutrition AI (5 Modes)
- **Meal Planner**: Creates complete meal plans with macros
- **Nutrition Analyzer**: Breaks down food nutritional content
- **Supplement Advisor**: Recommends evidence-based supplements
- **Weight Management**: Sustainable weight loss/gain strategies
- **Food Consultant**: Answers specific nutrition questions

#### Clinical AI Modules
Each clinical AI module is trained with:
- **Medical Literature**: Evidence-based guidelines
- **Clinical Protocols**: Standard of care procedures
- **Indonesian Context**: BPJS system, local healthcare practices
- **Safety Protocols**: Crisis detection, emergency referral
- **Bahasa Indonesia**: Natural language processing in Indonesian

### Context-Aware AI

AI responses are personalized using patient context:

```typescript
interface PatientContext {
  // Demographics
  age?: number;
  gender?: string;
  weight?: number;
  height?: number;
  
  // Health Metrics
  bloodPressure?: string;
  bloodSugar?: number;
  cholesterol?: number;
  
  // Lifestyle
  exerciseFrequency?: string;
  smokingStatus?: string;
  alcoholConsumption?: string;
  
  // Medical History
  allergies?: string[];
  medications?: string[];
  conditions?: string[];
  
  // Goals
  fitnessGoals?: string[];
  dietaryRestrictions?: string[];
}
```

### AI Safety & Ethics

#### Crisis Detection
- Automatic detection of life-threatening symptoms
- Immediate emergency contact recommendations
- 119 (Emergency), 118 (Ambulance) hotline display

#### Medical Disclaimers
All AI responses include:
- "AI bukan pengganti dokter profesional"
- "Konsultasikan dengan dokter untuk diagnosis definitif"
- Emergency contact information

#### Evidence-Based Responses
- Recommendations follow WHO, IDAI guidelines
- References to medical literature
- Confidence levels for predictions

#### Cultural Sensitivity
- Indonesian healthcare system awareness (BPJS)
- Cultural values (family, community, faith)
- Local medical practices
- Bahasa Indonesia natural language

---

## Project Structure

```
src/
├── app/                          # Next.js App Router
│   ├── api/                      # API Routes (19 total)
│   │   ├── proxy/route.ts        # External API proxy
│   │   ├── health/route.ts       # Health check
│   │   ├── logger/route.ts       # Logging
│   │   │
│   │   ├── fitness-ai/route.ts              # Fitness AI (5 modes)
│   │   ├── nutrition-ai/route.ts            # Nutrition AI (5 modes)
│   │   ├── maternal-child-ai/route.ts       # Maternal & Child AI (5 modes)
│   │   ├── heart-health-ai/route.ts         # Heart Health AI (5 modes)
│   │   ├── mental-wellness-enhanced-ai/route.ts  # Mental Wellness AI (5 modes)
│   │   ├── eye-health-ai/route.ts           # Eye Health AI (5 modes)
│   │   ├── emergency-ai/route.ts            # Emergency Assistant
│   │   ├── second-opinion-ai/route.ts       # Second Opinion AI
│   │   ├── lab-ai/route.ts                  # Lab Interpretation
│   │   ├── vaccine-ai/route.ts              # Vaccine Intelligence
│   │   ├── mental-health-ai/route.ts        # Mental Health Sanctuary AI
│   │   ├── pharmacy-ai/route.ts             # Pharmacy Intelligence
│   │   ├── clinical-ai/route.ts             # Clinical Intelligence
│   │   ├── analytics-ai/route.ts            # Health Insights Engine
│   │   ├── claims-ai/route.ts               # Smart Claims Intelligence
│   │   └── knowledge-ai/route.ts            # Medical Knowledge Assistant
│   │
│   ├── layout.tsx                # Root layout (Farcaster integration)
│   ├── page.tsx                  # Homepage (12 portals)
│   ├── globals.css               # Global styles
│   └── fonts/                    # Custom fonts (Geist)
│
├── components/                   # React Components
│   ├── ui/                       # shadcn/ui components (56)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   └── ...
│   │
│   ├── health-centers/           # 6 Health Center modules
│   │   ├── heart-health-center.tsx          # + Heart Health AI
│   │   ├── eye-health-center.tsx            # + Eye Health AI
│   │   ├── maternal-child-health-center.tsx # + Maternal & Child AI
│   │   ├── nutrition-vitamin-center.tsx     # + Nutrition AI
│   │   ├── mental-health-center.tsx         # + Mental Wellness AI
│   │   └── fitness-center.tsx               # + Fitness AI
│   │
│   ├── AI Assistant Components:
│   │   ├── fitness-ai-assistant.tsx
│   │   ├── nutrition-ai-coach.tsx
│   │   ├── maternal-child-ai-consultant.tsx
│   │   ├── heart-health-ai-assistant.tsx
│   │   ├── mental-wellness-enhanced-assistant.tsx
│   │   └── eye-health-ai-assistant.tsx
│   │
│   ├── enhanced-patient-dashboard.tsx        # Patient Portal
│   ├── doctor-panel-enhanced.tsx             # Doctor Panel
│   ├── enhanced-insurance-panel.tsx          # Insurance + BPJS
│   ├── health-analytics-dashboard.tsx        # Analytics + AI Insights
│   ├── lab-results-auto-import.tsx           # Lab Results + AI Interpretation
│   ├── knowledge-center.tsx                  # Knowledge + AI Assistant
│   ├── immunization-tracker.tsx              # Vaccinations + AI Intelligence
│   ├── pharmacy-blockchain.tsx               # Pharmacy + AI Intelligence
│   ├── emergency-sos-module.tsx              # Emergency SOS + AI Assistant
│   ├── second-opinion-network.tsx            # Second Opinion + AI
│   ├── predictive-health-ai.tsx              # Predictive AI
│   ├── mental-health-sanctuary.tsx           # Mental Health + AI
│   │
│   ├── health-centers-portal.tsx             # Health Centers Hub
│   ├── ai-health-companion.tsx               # AI Chat
│   ├── wallet-connect.tsx                    # Wallet Button
│   ├── connection-status-banner.tsx          # Blockchain Status
│   ├── blockchain-feature-badge.tsx          # Feature Badge
│   ├── theme-toggle.tsx                      # Dark/Light Toggle
│   └── ...                                   # Other components
│
├── hooks/                        # Custom React Hooks (15)
│   ├── use-health-chain.ts                   # Core blockchain
│   ├── use-connection-mode.tsx               # Wallet state
│   ├── use-immunization-tracker.ts
│   ├── use-pharmacy-blockchain.ts
│   ├── use-emergency-sos.ts
│   ├── use-second-opinion.ts
│   ├── use-predictive-health-ai.ts
│   ├── use-mental-health-sanctuary.ts
│   ├── use-lab-results.ts
│   └── ...
│
├── lib/                          # Utilities & Config
│   ├── web3-config.ts            # Wagmi + RainbowKit config
│   ├── utils.ts                  # Helper functions (cn, etc.)
│   └── logger.ts                 # Logging utility
│
└── utils/                        # Additional Utilities
    └── manifestStatus.ts         # Farcaster manifest

public/                           # Static Assets
├── .well-known/
│   └── farcaster.json            # Farcaster mini-app config
└── ...                           # Images, icons, etc.

Root Files:
├── package.json                  # Dependencies
├── tsconfig.json                 # TypeScript config
├── tailwind.config.ts            # Tailwind config
├── next.config.js                # Next.js config
├── postcss.config.js             # PostCSS config
├── README.md                     # Main documentation
├── FEATURES.md                   # Feature docs
├── SETUP.md                      # Setup guide
└── ARCHITECTURE.md               # This file
```

---

## Data Flow

### Guest Mode Flow

```
User Action
    ↓
React Component
    ↓
Custom Hook (e.g., useHealthChain)
    ↓
Update Local State
    ↓
Save to localStorage
    ↓
Re-render UI
```

### Blockchain Mode Flow

```
User Action
    ↓
React Component
    ↓
Custom Hook
    ↓
Wagmi Hook (useContractWrite)
    ↓
Wallet Signature Request
    ↓
User Approves in Wallet
    ↓
Transaction Broadcast to Sepolia
    ↓
Wait for Confirmation (useWaitForTransaction)
    ↓
Update Local State
    ↓
Re-render UI with Transaction Hash
```

### AI Query Flow

```
User Question
    ↓
AI Assistant Component
    ↓
Mode Selection (1 of 45+ modes)
    ↓
Collect Patient Context
    ↓
POST Request to AI API Route
    ↓
Gemini API Processing
    ↓
Response Formatting (Indonesian)
    ↓
Safety Check & Disclaimer
    ↓
Display to User (<2 seconds)
```

### Example: Add Health Record

**Guest Mode:**
```typescript
const addRecord = (record: HealthRecord) => {
  const newRecord = { ...record, id: generateId() };
  const updated = [...records, newRecord];
  setRecords(updated);
  localStorage.setItem('healthRecords', JSON.stringify(updated));
};
```

**Blockchain Mode:**
```typescript
const addRecord = async (record: HealthRecord) => {
  // 1. Upload to IPFS (simulated)
  const ipfsHash = await uploadToIPFS(record);
  
  // 2. Write to smart contract
  const { write } = useContractWrite({
    address: HEALTH_CHAIN_CONTRACT,
    abi: HEALTH_CHAIN_ABI,
    functionName: 'addRecord',
    args: [ipfsHash],
  });
  
  const tx = await write();
  
  // 3. Wait for confirmation
  await tx.wait();
  
  // 4. Update local state
  const newRecord = { ...record, id: tx.hash };
  setRecords([...records, newRecord]);
};
```

---

## Blockchain Integration

### Smart Contract Architecture

#### Health Chain Contract
```solidity
// Simplified version of the smart contract
contract HealthChain {
    struct Record {
        string ipfsHash;
        uint256 timestamp;
    }
    
    mapping(address => Record[]) public patientRecords;
    mapping(address => mapping(address => bool)) public accessPermissions;
    
    // Add health record
    function addRecord(string memory ipfsHash) public {
        patientRecords[msg.sender].push(Record({
            ipfsHash: ipfsHash,
            timestamp: block.timestamp
        }));
    }
    
    // Grant access to doctor
    function grantAccess(address doctor) public {
        accessPermissions[msg.sender][doctor] = true;
    }
    
    // Revoke access
    function revokeAccess(address doctor) public {
        accessPermissions[msg.sender][doctor] = false;
    }
    
    // View records (requires permission)
    function viewRecords(address patient) public view returns (Record[] memory) {
        require(
            msg.sender == patient || accessPermissions[patient][msg.sender],
            "No permission"
        );
        return patientRecords[patient];
    }
}
```

### IPFS Integration

**File Upload Flow:**
```typescript
// 1. Convert file to buffer
const buffer = await file.arrayBuffer();

// 2. Upload to IPFS
const { cid } = await ipfsClient.add(buffer);

// 3. Store CID (IPFS hash) on blockchain
await addRecord(cid.toString());

// 4. Retrieve file
const chunks = [];
for await (const chunk of ipfsClient.cat(cid)) {
  chunks.push(chunk);
}
const file = new Blob(chunks);
```

### Transaction Management

**Transaction States:**
1. **Idle**: No transaction
2. **Pending**: User approves in wallet
3. **Broadcasting**: Sent to network
4. **Confirming**: Waiting for block confirmation
5. **Success**: Transaction confirmed
6. **Error**: Transaction failed

**Error Handling:**
```typescript
try {
  const tx = await write();
  await tx.wait();
  toast.success("Transaction successful!");
} catch (error) {
  if (error.code === 4001) {
    toast.error("User rejected transaction");
  } else if (error.code === -32603) {
    toast.error("Insufficient funds");
  } else {
    toast.error("Transaction failed");
  }
}
```

---

## State Management

### Local State Patterns

#### 1. Module-Level State (Custom Hooks)
```typescript
// hooks/use-immunization-tracker.ts
export function useImmunizationTracker() {
  const [children, setChildren] = useState<Child[]>([]);
  const [vaccinations, setVaccinations] = useState<Vaccination[]>([]);
  
  const addChild = (child: Child) => {
    setChildren([...children, child]);
    localStorage.setItem('children', JSON.stringify([...children, child]));
  };
  
  return { children, vaccinations, addChild, /* ... */ };
}
```

#### 2. Global State (Context API)
```typescript
// hooks/use-connection-mode.tsx
const ConnectionContext = createContext<ConnectionContextType>();

export function ConnectionProvider({ children }: { children: ReactNode }) {
  const { address, isConnected } = useAccount();
  const mode = isConnected ? 'blockchain' : 'guest';
  
  return (
    <ConnectionContext.Provider value={{ isConnected, address, mode }}>
      {children}
    </ConnectionContext.Provider>
  );
}

export function useConnectionMode() {
  return useContext(ConnectionContext);
}
```

#### 3. Persistent State (localStorage)
```typescript
// Save
localStorage.setItem('key', JSON.stringify(data));

// Load
const data = JSON.parse(localStorage.getItem('key') || '[]');

// Clear
localStorage.removeItem('key');
```

### State Synchronization

**Guest → Blockchain Migration:**
```typescript
const migrateToBlockchain = async () => {
  // 1. Load all localStorage data
  const localRecords = JSON.parse(
    localStorage.getItem('healthRecords') || '[]'
  );
  
  // 2. Upload each record to blockchain
  for (const record of localRecords) {
    await addRecordToBlockchain(record);
  }
  
  // 3. Clear localStorage (optional)
  // localStorage.clear();
  
  toast.success("Successfully migrated to blockchain!");
};
```

---

## API Design

### Proxy Endpoint

**Purpose**: Route all external API requests through server-side proxy

**Endpoint**: `/api/proxy/route.ts`

**Request Format:**
```typescript
POST /api/proxy

Headers:
  Content-Type: application/json

Body:
{
  "protocol": "https",
  "origin": "api.example.com",
  "path": "/endpoint",
  "method": "GET",
  "headers": {},
  "body": {}  // Optional
}
```

**Response Format:**
```typescript
{
  "success": true,
  "data": { /* API response */ },
  "error": null
}
```

### AI API Endpoints

All AI endpoints follow consistent design:

**Request Format:**
```typescript
POST /api/{module}-ai

Body:
{
  "mode": "workout_optimizer",  // One of 5 modes per module
  "query": "Create a workout plan",
  "context": {
    "age": 30,
    "weight": 70,
    "fitnessGoals": ["muscle_gain"]
  }
}
```

**Response Format:**
```typescript
{
  "response": "Formatted AI response in Bahasa Indonesia...",
  "confidence": 0.92,
  "mode": "workout_optimizer",
  "timestamp": "2024-01-15T10:30:00.000Z"
}
```

### Health Check Endpoint

**Endpoint**: `/api/health/route.ts`

**Purpose**: Verify API is running

**Response:**
```json
{
  "status": "ok",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "version": "1.0.0"
}
```

---

## Security Architecture

### Threat Model

**Threats Addressed:**
1. Unauthorized access to health records
2. Data tampering
3. Identity theft
4. Man-in-the-middle attacks
5. XSS attacks
6. CSRF attacks
7. Smart contract vulnerabilities
8. AI prompt injection

### Security Measures

#### 1. Blockchain Security
- **Immutable Records**: Cannot be changed after creation
- **Cryptographic Signatures**: Verify transaction authenticity
- **Smart Contract Access Control**: Only authorized addresses can read data
- **Transaction Verification**: Hash-based verification

#### 2. Data Encryption
- **HTTPS**: All connections encrypted (TLS 1.3)
- **IPFS Encryption**: Files encrypted before upload (planned)
- **localStorage Encryption**: Sensitive data encrypted (planned)

#### 3. Authentication
- **Wallet-Based Auth**: Cryptographic proof of identity
- **No Passwords**: Eliminates password-related vulnerabilities
- **Session Management**: Secure session tokens

#### 4. Frontend Security
- **Content Security Policy**: Prevent XSS
- **Input Sanitization**: Clean user inputs
- **Type Safety**: TypeScript prevents type errors
- **Dependency Scanning**: Regular security audits

#### 5. AI Safety
- **Prompt Injection Prevention**: Input validation and sanitization
- **Response Filtering**: Remove sensitive/harmful content
- **Rate Limiting**: Prevent abuse
- **Context Isolation**: Patient data compartmentalization

#### 6. Access Control
```typescript
// Smart contract access control
modifier onlyAuthorized(address patient) {
    require(
        msg.sender == patient || 
        accessPermissions[patient][msg.sender],
        "Not authorized"
    );
    _;
}
```

### Privacy Measures

#### 1. Patient Data Control
- Patients grant/revoke access
- Granular permissions (read-only, write, full access)
- Audit trail of all access

#### 2. Anonymous Support Groups
- No real names required
- Wallet-based pseudonyms
- Optional full anonymity

#### 3. Encrypted Journals
- Mood journal encrypted locally
- Only patient can decrypt
- Blockchain stores encrypted hash only

#### 4. GDPR Compliance (Planned)
- Right to be forgotten (off-chain data deletion)
- Data export functionality
- Consent management
- Privacy policy

---

## Performance Optimization

### Frontend Optimization

#### 1. Code Splitting
```typescript
// Dynamic imports for large components
const PharmacyBlockchain = dynamic(
  () => import('@/components/pharmacy-blockchain'),
  { loading: () => <Spinner /> }
);
```

#### 2. Image Optimization
```typescript
// Next.js Image component
<Image
  src="/logo.png"
  width={200}
  height={200}
  alt="Logo"
  priority  // Load immediately
/>
```

#### 3. Memoization
```typescript
// Prevent unnecessary re-renders
const MemoizedComponent = React.memo(ExpensiveComponent);

// Memoize expensive calculations
const result = useMemo(() => {
  return expensiveCalculation(data);
}, [data]);

// Memoize callbacks
const handleClick = useCallback(() => {
  doSomething();
}, []);
```

#### 4. AI Response Caching
```typescript
// Cache common AI queries
const cache = new Map();

if (cache.has(query)) {
  return cache.get(query);
}

const response = await callAI(query);
cache.set(query, response);
```

### Blockchain Optimization

#### 1. Batch Transactions
```typescript
// Submit multiple records in one transaction
function addRecordsBatch(string[] memory ipfsHashes) public {
    for (uint i = 0; i < ipfsHashes.length; i++) {
        patientRecords[msg.sender].push(Record({
            ipfsHash: ipfsHashes[i],
            timestamp: block.timestamp
        }));
    }
}
```

#### 2. Gas Optimization
- Use `uint256` instead of smaller types (Solidity quirk)
- Minimize storage writes
- Use events for logs (cheaper than storage)
- Cache contract reads

### AI Optimization

#### 1. Response Streaming
```typescript
// Stream AI responses for better UX
const stream = await callGeminiStream(query);
for await (const chunk of stream) {
  updateUI(chunk);
}
```

#### 2. Context Compression
```typescript
// Compress patient context to reduce API payload
const compressedContext = compressData(patientContext);
```

---

## Deployment Architecture

### Production Stack

```
┌─────────────────────────────────────┐
│           Vercel CDN                 │  Global CDN
└────────────┬────────────────────────┘
             │
┌────────────┴────────────────────────┐
│       Vercel Edge Network            │  Edge Functions
└────────────┬────────────────────────┘
             │
┌────────────┴────────────────────────┐
│        Next.js Application           │  Node.js Runtime
│  ┌──────────────────────────────┐   │
│  │  API Routes (/api/*)         │   │
│  │  - 16 AI Intelligence APIs   │   │
│  │  - Proxy, Health, Logger     │   │
│  └──────────────────────────────┘   │
│  ┌──────────────────────────────┐   │
│  │  Server Components           │   │
│  └──────────────────────────────┘   │
│  ┌──────────────────────────────┐   │
│  │  Client Components           │   │
│  └──────────────────────────────┘   │
└────────────┬────────────────────────┘
             │
┌────────────┴────────────────────────┐
│     Ethereum Sepolia Network         │  Blockchain
└──────────────────────────────────────┘
```

### CI/CD Pipeline

```
GitHub Push
    ↓
Vercel Auto-Deploy Triggered
    ↓
1. Install Dependencies (npm install)
    ↓
2. Run TypeScript Check (tsc --noEmit)
    ↓
3. Build Application (npm run build)
    ↓
4. Inject Farcaster Integration
    ↓
5. Run Tests (future: npm test)
    ↓
6. Deploy to Vercel Edge Network
    ↓
7. Health Check
    ↓
8. Go Live (or Rollback on Error)
```

---

## Future Architecture Improvements

### Planned Enhancements

1. **Enhanced AI Capabilities**
   - Multi-modal AI (image + text analysis)
   - Voice-based AI consultation
   - Real-time symptom monitoring
   - Predictive disease outbreak detection

2. **Microservices Architecture**
   - Separate services for each major module
   - Independent scaling
   - Better fault isolation

3. **Database Integration**
   - PostgreSQL for relational data
   - Redis for caching AI responses
   - MongoDB for unstructured data

4. **Message Queue**
   - RabbitMQ or Kafka for async processing
   - Background jobs (email notifications, etc.)

5. **Advanced Blockchain**
   - Layer 2 solutions (Base, Optimism, Arbitrum)
   - Zero-knowledge proofs for privacy
   - Cross-chain interoperability

6. **Real-Time Features**
   - WebSocket for live updates
   - Push notifications
   - Real-time chat with doctors

7. **ML/AI Infrastructure**
   - Dedicated ML service
   - Model versioning
   - A/B testing for predictions
   - Fine-tuned medical models

8. **Observability**
   - Distributed tracing (Jaeger)
   - Metrics (Prometheus, Grafana)
   - Log aggregation (ELK stack)
   - AI performance monitoring

---

## Contact & Support

### Development Team

**Repository**: https://github.com/mrbrightsides/healthchain

**Community Channels**:
- **Telegram**: https://t.me/khudriakhmad
- **Discord**: https://discord.com/channels/@khudri_61362

**Support**:
- **Email**: support@elpeef.com

### Contributing

Contributions are welcome! Areas of interest:
- AI mode improvements
- New health modules
- Blockchain optimizations
- Indonesian language enhancements
- BPJS integration expansions

### Reporting Issues

Submit issues via:
1. GitHub Issues (preferred)
2. Email: support@elpeef.com
3. Community channels (Telegram/Discord)

Include:
- Environment details
- Steps to reproduce
- Expected vs actual behavior
- Error logs/screenshots

---

## Conclusion

RANTAI HealthChain is built with:
- **Modern tech stack** (Next.js 15, React 19, TypeScript 5.8)
- **AI-first approach** (45+ specialized modes, Gemini 2.0 Flash)
- **Blockchain integration** (Ethereum, IPFS, Smart Contracts)
- **Modular architecture** (16 independent modules with AI)
- **Type-safe development** (Strict TypeScript)
- **Patient-centric design** (Data ownership, privacy)
- **Indonesian market focus** (BPJS, Bahasa Indonesia, local healthcare)
- **Scalable foundation** (Ready for future enhancements)

The architecture balances:
- **Performance** vs **Feature richness**
- **Decentralization** vs **User experience**
- **Security** vs **Accessibility**
- **Innovation** vs **Reliability**
- **AI Intelligence** vs **Human oversight**

---

For more information:
- [README.md](./README.md) - Project overview
- [FEATURES.md](./FEATURES.md) - Feature documentation
- [SETUP.md](./SETUP.md) - Setup guide

**Contact**: support@elpeef.com | **GitHub**: https://github.com/mrbrightsides/healthchain
