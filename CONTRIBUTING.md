# Contributing to RANTAI HealthChain

First off, thank you for considering contributing to RANTAI HealthChain! It's people like you who make HealthChain such a powerful tool for democratizing healthcare access across Indonesia.

## 🌟 Vision

RANTAI HealthChain is building the future of decentralized healthcare for Indonesia's 270+ million people. We're combining cutting-edge AI, blockchain technology, and deep cultural understanding to make quality healthcare accessible to everyone, regardless of location or economic status.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [Community](#community)

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive Behavior:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable Behavior:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at **support@elpeef.com**. All complaints will be reviewed and investigated promptly and fairly.

## 🚀 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include as many details as possible:

**Bug Report Template:**
```markdown
**Description:**
A clear and concise description of the bug.

**Steps to Reproduce:**
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

**Expected Behavior:**
What should happen.

**Actual Behavior:**
What actually happens.

**Environment:**
- OS: [e.g., Windows 11, macOS 14, Ubuntu 22.04]
- Browser: [e.g., Chrome 120, Safari 17]
- Node Version: [e.g., 18.17.0]
- Network: [e.g., localhost, testnet, mainnet]

**Screenshots:**
If applicable, add screenshots.

**Additional Context:**
Any other relevant information.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description** of the enhancement
- **Use case**: Why this enhancement would be useful
- **Implementation ideas**: If applicable, suggest how it could be implemented
- **Mockups/examples**: Visual aids help communicate ideas

### Contributing Code

We welcome code contributions! Here are areas where contributions are especially valuable:

**High-Priority Areas:**
- 🏥 **Healthcare Module Improvements**: Enhancing AI accuracy in specialized medical domains
- 🌐 **Localization**: Indonesian language improvements, regional dialect support
- 🔐 **Security Enhancements**: Smart contract audits, encryption improvements
- ♿ **Accessibility**: Making the platform more accessible to users with disabilities
- 📱 **Mobile Optimization**: Improving performance on low-end devices
- 🧪 **Testing**: Increasing test coverage, especially for critical healthcare features

**Good First Issues:**
- Documentation improvements
- UI/UX refinements
- Bug fixes in non-critical modules
- Adding unit tests
- Performance optimizations

## 💻 Development Setup

### Prerequisites

Ensure the following are installed:
- **Node.js**: v18.17.0 or higher
- **npm** or **pnpm**: Latest stable version
- **Git**: For version control
- **Ethereum Wallet**: MetaMask or similar (for blockchain features)

### Installation

```bash
# Clone the repository
git clone https://github.com/mrbrightsides/healthchain.git
cd healthchain

# Install dependencies
npm install
# or
pnpm install

# Set up environment variables
cp .env.example .env.local
# Edit .env.local with your API keys

# Run development server
npm run dev
# or
pnpm dev

# Open http://localhost:3000
```

### Required API Keys

To run the full platform locally, obtain the following API keys:

- **Google Gemini API**: For AI medical analysis
- **ElevenLabs API**: For voice synthesis
- **Pinata API**: For IPFS storage
- **Ethereum RPC**: For blockchain interactions

See `.env.example` for configuration details.

### Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Type checking
npm run type-check

# Linting
npm run lint
```

## 📁 Project Structure

```
healthchain/
├── src/
│   ├── app/                    # Next.js app directory
│   │   ├── api/               # API routes
│   │   ├── dashboard/         # Main dashboard
│   │   └── modules/           # Health modules
│   ├── components/            # React components
│   │   ├── ui/               # shadcn/ui components
│   │   ├── health/           # Health-specific components
│   │   └── blockchain/       # Web3 components
│   ├── hooks/                # Custom React hooks
│   ├── lib/                  # Utility libraries
│   │   ├── ai/              # AI integration
│   │   ├── blockchain/      # Web3 utilities
│   │   └── healthcare/      # Healthcare logic
│   ├── types/               # TypeScript definitions
│   └── styles/              # Global styles
├── public/                   # Static assets
├── docs/                     # Documentation
└── tests/                    # Test files
```

## 📐 Coding Standards

### TypeScript Guidelines

**Strict Typing:**
```typescript
// ✅ Good: Explicit types
interface PatientRecord {
  id: string;
  name: string;
  age: number;
  conditions: MedicalCondition[];
}

function analyzePatient(record: PatientRecord): DiagnosisResult {
  // Implementation
}

// ❌ Bad: Implicit any
function analyzePatient(record) {
  // Implementation
}
```

**No Implicit Any:**
```typescript
// ✅ Good: Proper typing for dynamic access
type ConfigKey = 'api' | 'timeout';
const config: Record<ConfigKey, string | number> = {
  api: 'https://api.example.com',
  timeout: 5000
};

// ❌ Bad: Untyped dynamic access
const value = config[userInput]; // Error!
```

**Type Imports:**
```typescript
// ✅ Good: Type-only imports
import type { PatientRecord } from '@/types/healthcare';

// ❌ Bad: Runtime imports for types
import { PatientRecord } from '@/types/healthcare';
```

### React Best Practices

**Component Structure:**
```typescript
// ✅ Good: Proper component structure
'use client';

import type { FC } from 'react';
import { useState, useEffect } from 'react';

interface HealthModuleProps {
  patientId: string;
  moduleType: string;
}

export const HealthModule: FC<HealthModuleProps> = ({ patientId, moduleType }) => {
  const [data, setData] = useState<PatientData | null>(null);
  
  useEffect(() => {
    // Fetch data
  }, [patientId]);

  return (
    <div className="p-4">
      {/* Component content */}
    </div>
  );
};
```

**Hooks Usage:**
```typescript
// ✅ Good: Custom hooks for complex logic
function usePatientData(patientId: string) {
  const [data, setData] = useState<PatientData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    // Fetch logic
  }, [patientId]);

  return { data, loading, error };
}
```

### Naming Conventions

- **Components**: PascalCase (`PatientDashboard.tsx`)
- **Hooks**: camelCase with 'use' prefix (`useHealthData.ts`)
- **Utilities**: camelCase (`formatDiagnosis.ts`)
- **Types/Interfaces**: PascalCase (`PatientRecord`, `DiagnosisResult`)
- **Constants**: UPPER_SNAKE_CASE (`MAX_RETRY_ATTEMPTS`)

### File Organization

- **One component per file**: Each component should have its own file
- **Co-locate related files**: Keep components, styles, and tests together
- **Index files**: Use for clean imports, but don't overuse

### Comments & Documentation

```typescript
/**
 * Analyzes patient symptoms using Google Gemini AI
 * 
 * @param symptoms - Array of patient-reported symptoms
 * @param history - Patient medical history
 * @returns AI-generated preliminary diagnosis with confidence scores
 * 
 * @example
 * ```typescript
 * const diagnosis = await analyzeSymptoms(
 *   ['headache', 'fever', 'fatigue'],
 *   patientHistory
 * );
 * ```
 */
async function analyzeSymptoms(
  symptoms: string[],
  history: MedicalHistory
): Promise<DiagnosisResult> {
  // Implementation
}
```

### AI Integration Guidelines

When working with AI features:

1. **Always validate AI outputs** before displaying to users
2. **Include disclaimers** that AI suggestions require professional verification
3. **Implement rate limiting** to prevent API abuse
4. **Handle errors gracefully** with meaningful user feedback
5. **Log AI interactions** for quality improvement and debugging

### Blockchain Best Practices

1. **Gas optimization**: Minimize on-chain operations
2. **Error handling**: Always handle transaction failures
3. **User confirmation**: Require explicit user consent for blockchain actions
4. **Fallback mechanisms**: Provide non-blockchain alternatives when needed

### Security Guidelines

**Critical Rules:**
- ❌ **Never commit API keys** or secrets to version control
- ❌ **Never store sensitive health data** in localStorage
- ✅ **Always encrypt** patient data before storage
- ✅ **Always validate** user inputs on both client and server
- ✅ **Use prepared statements** for database queries
- ✅ **Implement rate limiting** on API endpoints

## 🔄 Pull Request Process

### Before Submitting

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/add-mental-health-module
   ```

2. **Make commits with clear messages**:
   ```bash
   git commit -m "feat(mental-health): add anxiety assessment tool"
   ```

3. **Follow commit convention**:
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `style:` Code style changes (formatting)
   - `refactor:` Code refactoring
   - `test:` Adding or updating tests
   - `chore:` Maintenance tasks

4. **Update documentation** if needed

5. **Add tests** for new features

6. **Ensure all tests pass**:
   ```bash
   npm run test
   npm run type-check
   npm run lint
   ```

### Submitting Pull Request

1. **Push branch to GitHub**:
   ```bash
   git push origin feature/add-mental-health-module
   ```

2. **Open Pull Request** with detailed description:

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issue
Closes #123

## Testing
Describe testing performed.

## Screenshots
If applicable, add screenshots.

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
- [ ] All tests passing
```

3. **Respond to review feedback** promptly

4. **Update branch** if requested:
   ```bash
   git rebase main
   git push --force-with-lease
   ```

### Review Process

- Maintainers will review PRs within **48-72 hours**
- At least **one approval** required for merge
- CI/CD checks must **pass**
- Conflicts must be **resolved**

## 🌐 Community

### Getting Help

**GitHub Issues**: For bug reports and feature requests  
**Telegram**: [@khudriakhmad](https://t.me/khudriakhmad) - For real-time discussions  
**Discord**: [Join our Discord](https://discord.com/channels/@khudri_61362) - For community chat  
**Email**: [support@elpeef.com](mailto:support@elpeef.com) - For private inquiries

### Communication Channels

- **GitHub Discussions**: For general questions and ideas
- **Telegram Group**: For quick questions and community support
- **Discord Server**: For development discussions and collaboration
- **Email**: For security issues and private matters

### Recognition

Contributors will be recognized in:
- Project README.md
- Release notes
- Special mentions for significant contributions

### Financial Contributions

We're exploring ways to reward significant contributors through:
- Blockchain-based bounties
- Revenue sharing for commercial partnerships
- Token allocations (when available)

## 🎯 Priority Areas for Contribution

### Current Focus

1. **Hospital Integration Testing**: Help test with real Indonesian healthcare facilities
2. **Indonesian Language Refinement**: Improve medical terminology and cultural context
3. **Mobile Performance**: Optimize for low-end Android devices
4. **Accessibility Compliance**: WCAG 2.1 AA compliance
5. **Security Audits**: Smart contract and API security reviews

### Future Roadmap

- Multi-chain support (Polygon, Base)
- Traditional medicine (Jamu) integration
- Wearable device connectivity
- Regional expansion (SEA markets)

## 📜 License

By contributing to RANTAI HealthChain, contributors agree that their contributions will be licensed under the project's license (see LICENSE file).

## 🙏 Acknowledgments

Thank you to all contributors who have helped make HealthChain a reality. Together, we're building a healthier Indonesia!

---

**Questions?** Reach out via [Telegram](https://t.me/khudriakhmad) or [email](mailto:support@elpeef.com).

**Ready to contribute?** Check out our [good first issues](https://github.com/mrbrightsides/healthchain/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)!
