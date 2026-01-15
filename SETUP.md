# 🔧 RANTAI HealthChain - Development Setup Guide

Complete guide for setting up RANTAI HealthChain for local development.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [AI Features Setup](#ai-features-setup)
6. [Building for Production](#building-for-production)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Troubleshooting](#troubleshooting)
10. [Support & Contact](#support--contact)

---

## Prerequisites

### Required Software

#### Node.js & npm
- **Node.js**: 18.x or higher
- **npm**: 9.x or higher (comes with Node.js)

Check versions:
```bash
node --version  # Should be v18.0.0 or higher
npm --version   # Should be 9.0.0 or higher
```

Install Node.js from: https://nodejs.org/

#### Git
- **Git**: Latest version

Check version:
```bash
git --version
```

Install Git from: https://git-scm.com/

### Recommended Software

- **VS Code**: https://code.visualstudio.com/
- **VS Code Extensions**:
  - ESLint
  - Prettier
  - Tailwind CSS IntelliSense
  - TypeScript and JavaScript Language Features

### Blockchain Requirements

#### Web3 Wallet
- **MetaMask**: https://metamask.io/
- **Coinbase Wallet**: https://www.coinbase.com/wallet
- **Rainbow Wallet**: https://rainbow.me/

#### Test ETH (Sepolia)
- Get free Sepolia ETH from faucets:
  - https://sepoliafaucet.com/
  - https://www.alchemy.com/faucets/ethereum-sepolia
  - https://faucet.quicknode.com/ethereum/sepolia

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mrbrightsides/healthchain.git
cd healthchain
```

### 2. Install Dependencies

Using npm:
```bash
npm install
```

Using yarn:
```bash
yarn install
```

Using pnpm:
```bash
pnpm install
```

This will install all dependencies listed in `package.json`:
- **Next.js 15.3.8+** - React framework
- **React 19.1.0** - UI library
- **TypeScript 5.8.3** - Type safety
- **Wagmi 2.17.2** - Ethereum React hooks
- **RainbowKit 2.2.8** - Wallet UI
- **Ethers.js 6.15.0** - Ethereum library
- **Tailwind CSS** - Styling
- **shadcn/ui** - Component library
- **Google Gemini API** - AI intelligence (45+ modes)
- **ElevenLabs** - Voice synthesis
- And 60+ other dependencies

### 3. Verify Installation

Check that all dependencies installed correctly:
```bash
npm list --depth=0
```

---

## Configuration

### 1. Environment Variables

The app doesn't require a `.env` file for basic functionality. All configuration is in the code.

**Key Configuration Files:**

#### `src/lib/web3-config.ts`
```typescript
// RainbowKit WalletConnect Project ID
const projectId = 'f8d248f838ec4f12b0f01efd2b238206';

// Ethereum Network (Sepolia testnet)
chains: [sepolia]

// Smart Contract Address
HEALTH_CHAIN_CONTRACT = '0xfC1D504D6D7049c548100AD21e11962180272177'
```

#### AI Configuration
AI features are configured with the following API keys hardcoded in route files:
- **Google Gemini 2.0 Flash API** - Powers 45+ specialized AI modes
- **ElevenLabs API** - Indonesian voice synthesis
- All keys are configured in respective `/api/*-ai/route.ts` files

#### `next.config.js`
```javascript
// Next.js configuration
// Optimized for production deployment
```

### 2. TypeScript Configuration

The project uses strict TypeScript settings. See `tsconfig.json`:
```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    // ... other strict settings
  }
}
```

### 3. Tailwind CSS

Tailwind is pre-configured. See `tailwind.config.ts` for theme customization.

---

## Running the Application

### Development Mode

Start the development server:
```bash
npm run dev
```

The app will be available at:
- **Local**: http://localhost:3000
- **Network**: http://[your-ip]:3000

Features in development mode:
- Hot module replacement (HMR)
- Fast refresh
- Error overlay
- Source maps
- TypeScript type checking

### Connect Wallet

1. Open http://localhost:3000
2. Click "Connect Wallet" button
3. Select wallet (MetaMask, Coinbase, Rainbow)
4. Approve connection
5. Switch to Sepolia network if prompted
6. Start using the app!

### Explore Features

**Without Wallet (Guest Mode):**
- All features work with localStorage
- No blockchain transactions
- Data persists locally
- AI features fully functional

**With Wallet (Blockchain Mode):**
- Connect wallet first
- All actions recorded on blockchain
- Full healthcare sovereignty
- Transaction verification

---

## AI Features Setup

### Overview

RANTAI HealthChain includes **45+ specialized AI modes** powered by Google Gemini 2.0 Flash API across 16 modules.

### AI Modules Included

#### 🏥 Health Centers AI (30 Modes)
1. **Fitness AI Coach** (5 modes) - `/api/fitness-ai`
   - Workout Optimizer, Form Coach, Injury Prevention, Progress Analyzer, Sport-Specific Training

2. **Nutrition AI Coach** (5 modes) - `/api/nutrition-ai`
   - Meal Planner, Nutrition Analyzer, Supplement Advisor, Weight Management, Food Consultant

3. **Maternal & Child AI** (5 modes) - `/api/maternal-child-ai`
   - Pregnancy Advisor, Child Development, Feeding Consultant, Growth Interpreter, Vaccination Guide

4. **Heart Health AI** (5 modes) - `/api/heart-health-ai`
   - Risk Analysis, Symptom Checker, Lifestyle Guidance, Trend Analysis, Emergency Assessment

5. **Mental Wellness AI** (5 modes) - `/api/mental-wellness-enhanced-ai`
   - Mental Health Companion, Anxiety Management, Sleep Coach, Grief Support, Mindfulness Guide

6. **Eye Health AI** (5 modes) - `/api/eye-health-ai`
   - Vision Analysis, Screen Strain Consultant, Eyewear Guidance, Vision Improvement, Symptom Interpreter

#### 🚨 Clinical & Emergency AI (15+ Modes)
7. **Emergency AI Assistant** - `/api/emergency-ai`
8. **Second Opinion AI** - `/api/second-opinion-ai`
9. **Lab Interpretation Engine** - `/api/lab-ai`
10. **Vaccine Intelligence** - `/api/vaccine-ai`
11. **Mental Health Sanctuary AI** - `/api/mental-health-ai`

#### 💼 Healthcare Operations AI
12. **Pharmacy Intelligence** - `/api/pharmacy-ai`
13. **Clinical Intelligence Suite** - `/api/clinical-ai`
14. **Health Insights Engine** - `/api/analytics-ai`
15. **Smart Claims Intelligence** - `/api/claims-ai`
16. **Medical Knowledge Assistant** - `/api/knowledge-ai`

### AI Configuration

All AI endpoints are pre-configured. No additional setup required for:
- Google Gemini API integration
- Context-aware responses
- Indonesian language support
- Real-time medical analysis

### Testing AI Features

1. Run the development server
2. Navigate to any Health Center
3. Click "AI Assistant" tab (default first tab)
4. Select an AI mode
5. Use quick query buttons or type custom questions
6. View real-time AI responses in Bahasa Indonesia

---

## Building for Production

### 1. Build the Application

Create optimized production build:
```bash
npm run build
```

This will:
- Compile TypeScript to JavaScript
- Bundle all code (including 16 AI API routes)
- Optimize assets
- Generate static pages
- Minify JavaScript & CSS
- Inject Farcaster mini-app integration
- Create production-ready `.next` folder

### 2. Test Production Build Locally

Run the production build locally:
```bash
npm start
```

Access at http://localhost:3000

### 3. Analyze Bundle Size

Check bundle size and composition:
```bash
npm run build -- --analyze
```

---

## Testing

### Manual Testing Checklist

#### Homepage
- [ ] Load homepage successfully
- [ ] See 12 portal buttons
- [ ] Theme toggle works (light/dark)
- [ ] Responsive on mobile/tablet/desktop
- [ ] AI Companion button visible (bottom-right)

#### Wallet Connection
- [ ] Connect wallet button visible
- [ ] RainbowKit modal opens
- [ ] Can connect MetaMask
- [ ] Can connect Coinbase Wallet
- [ ] Can connect Rainbow
- [ ] Wallet address displayed
- [ ] Network shows Sepolia
- [ ] Can disconnect wallet

#### Patient Portal
- [ ] Access patient portal
- [ ] Add health record
- [ ] Upload document
- [ ] View records list
- [ ] Grant access to doctor
- [ ] Revoke access
- [ ] All saved to blockchain (if connected)

#### Doctor Panel
- [ ] Access doctor panel
- [ ] View patient list
- [ ] Add observation
- [ ] Write prescription
- [ ] Record diagnosis

#### Insurance Portal
- [ ] Submit insurance claim
- [ ] Auto-approval works
- [ ] View claim history
- [ ] Verify BPJS card
- [ ] Submit BPJS claim
- [ ] AI fraud detection active

#### Lab Results
- [ ] Auto-import from lab
- [ ] View results
- [ ] Abnormal alerts work
- [ ] Manual upload
- [ ] AI Lab Interpretation available

#### Immunization Tracker
- [ ] Add child profile
- [ ] View vaccination schedule
- [ ] Record vaccination
- [ ] Mint NFT certificate
- [ ] AI Vaccine Intelligence working

#### Pharmacy
- [ ] Browse medications
- [ ] Add to cart
- [ ] Compare prices
- [ ] Submit order
- [ ] AI Pharmacy Intelligence functional

#### Emergency SOS
- [ ] Fill Medical ID
- [ ] Add emergency contacts
- [ ] View nearby hospitals
- [ ] Tap SOS button (test mode)
- [ ] AI Emergency Assistant available

#### Second Opinion Network
- [ ] Submit medical case
- [ ] View doctor network
- [ ] Doctors submit opinions
- [ ] Consensus detection
- [ ] AI Second Opinion Assistant working

#### Predictive AI
- [ ] Enter health metrics
- [ ] View risk assessments
- [ ] Get prevention plans
- [ ] AI insights displayed

#### Mental Health Sanctuary
- [ ] Mood journaling
- [ ] Book therapy session
- [ ] Join support group
- [ ] Meditation exercises
- [ ] Mental health assessments
- [ ] View crisis resources
- [ ] AI Mental Wellness Assistant functional

#### Health Centers (All 6)
- [ ] Access all 6 centers
- [ ] Use interactive tools
- [ ] Save results
- [ ] **AI Assistant tab available in each center**
- [ ] Test all 30 AI modes across centers

#### AI Health Companion
- [ ] Chat button visible
- [ ] Open chat interface
- [ ] Ask health question
- [ ] Get AI response
- [ ] Use quick actions

### AI-Specific Testing

#### Fitness AI Coach
- [ ] Workout Optimizer generates personalized plans
- [ ] Form Coach provides technique guidance
- [ ] Injury Prevention analyzes pain
- [ ] Progress Analyzer breaks plateaus
- [ ] Sport-Specific Training customizes programs

#### Nutrition AI Coach
- [ ] Meal Planner creates complete meal plans
- [ ] Nutrition Analyzer breaks down food
- [ ] Supplement Advisor recommends vitamins
- [ ] Weight Management provides strategies
- [ ] Food Consultant answers nutrition questions

#### Maternal & Child AI
- [ ] Pregnancy Advisor gives week-by-week guidance
- [ ] Child Development interprets milestones
- [ ] Feeding Consultant helps with nutrition
- [ ] Growth Interpreter analyzes percentiles
- [ ] Vaccination Guide optimizes schedules

#### Heart Health AI
- [ ] Risk Analysis assesses cardiovascular health
- [ ] Symptom Checker triages cardiac symptoms
- [ ] Lifestyle Guidance provides heart-healthy tips
- [ ] Trend Analysis interprets BP/HR patterns
- [ ] Emergency Assessment identifies critical situations

#### Mental Wellness AI
- [ ] Mental Health Companion provides empathetic support
- [ ] Anxiety Management teaches CBT techniques
- [ ] Sleep Coach optimizes sleep hygiene
- [ ] Grief Support helps process loss
- [ ] Mindfulness Guide teaches meditation

#### Eye Health AI
- [ ] Vision Analysis interprets test results
- [ ] Screen Strain Consultant addresses CVS
- [ ] Eyewear Guidance interprets prescriptions
- [ ] Vision Improvement suggests exercises
- [ ] Symptom Interpreter triages eye conditions

### Automated Testing (Coming Soon)

```bash
# Unit tests
npm run test

# E2E tests
npm run test:e2e

# Coverage report
npm run test:coverage
```

---

## Deployment

### Vercel (Recommended)

#### Option 1: Deploy via GitHub

1. Push code to GitHub
2. Go to https://vercel.com
3. Click "New Project"
4. Import GitHub repository
5. Vercel auto-detects Next.js
6. Click "Deploy"
7. Done! The app is live with all AI features

#### Option 2: Deploy via CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Deploy to production
vercel --prod
```

**Vercel Configuration:**
- Framework: Next.js
- Build Command: `npm run build`
- Output Directory: `.next`
- Install Command: `npm install`

### Netlify

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
netlify deploy --prod
```

**Netlify Configuration:**
```toml
# netlify.toml
[build]
  command = "npm run build"
  publish = ".next"

[[plugins]]
  package = "@netlify/plugin-nextjs"
```

### Custom Server

#### Using PM2

```bash
# Install PM2
npm install -g pm2

# Build
npm run build

# Start with PM2
pm2 start npm --name "rantai-healthchain" -- start

# Save PM2 configuration
pm2 save

# Setup startup script
pm2 startup
```

#### Using Docker

```dockerfile
# Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```

Build and run:
```bash
docker build -t rantai-healthchain .
docker run -p 3000:3000 rantai-healthchain
```

---

## Troubleshooting

### Common Issues

#### Issue: `npm install` fails

**Solution:**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

#### Issue: Port 3000 already in use

**Solution:**
```bash
# Find process using port 3000
lsof -i :3000

# Kill the process
kill -9 [PID]

# Or use different port
PORT=3001 npm run dev
```

#### Issue: TypeScript errors

**Solution:**
```bash
# Delete .next folder
rm -rf .next

# Rebuild
npm run build
```

#### Issue: Wallet not connecting

**Possible causes:**
- Wrong network (switch to Sepolia)
- No wallet installed
- Popup blocked
- Wallet locked

**Solutions:**
- Install MetaMask
- Switch to Sepolia network
- Allow popups
- Unlock wallet
- Refresh page

#### Issue: AI responses not working

**Possible causes:**
- API rate limits
- Network connectivity
- Missing dependencies

**Solutions:**
- Wait a few minutes (rate limit reset)
- Check internet connection
- Verify all dependencies installed
- Check browser console for errors
- Contact support (see below)

#### Issue: Build fails with "Module not found"

**Solution:**
```bash
# Reinstall dependencies
rm -rf node_modules
npm install

# Clear Next.js cache
rm -rf .next
```

#### Issue: Slow build times

**Solutions:**
- Enable SWC compiler (default in Next.js 15)
- Increase Node.js memory:
  ```bash
  NODE_OPTIONS=--max_old_space_size=4096 npm run build
  ```
- Disable unused features
- Use incremental builds

#### Issue: Styles not loading

**Solution:**
```bash
# Rebuild Tailwind
npx tailwindcss -i ./src/app/globals.css -o ./dist/output.css

# Clear Next.js cache
rm -rf .next

# Restart dev server
npm run dev
```

#### Issue: Farcaster integration issues

**Solution:**
- Farcaster metadata is auto-injected during build
- Check `public/.well-known/farcaster.json` exists
- Verify `src/app/layout.tsx` has FarcasterWrapper
- Clear `.next` folder and rebuild

---

## Support & Contact

### Getting Help

If issues are encountered that aren't covered in this guide:

#### 1. Documentation
- **README.md** - Project overview and features
- **ARCHITECTURE.md** - Technical architecture details
- **FEATURES.md** - Complete feature documentation

#### 2. GitHub
- **Repository**: https://github.com/mrbrightsides/healthchain
- **Issues**: Create a new issue with error logs and steps to reproduce
- **Discussions**: Ask questions and share ideas

#### 3. Community
- **Telegram**: https://t.me/khudriakhmad
- **Discord**: https://discord.com/channels/@khudri_61362

#### 4. Direct Support
- **Email**: support@elpeef.com
- Include error logs, screenshots, and detailed description

### Reporting Bugs

When reporting bugs, include:
1. **Environment**: OS, Node.js version, browser
2. **Steps to reproduce**: Detailed step-by-step
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Error messages**: Console logs, screenshots
6. **AI Module (if applicable)**: Which AI feature is affected

### Feature Requests

Feature requests are welcome! Submit via:
- GitHub Issues (tagged as "enhancement")
- Telegram community discussion
- Email to support@elpeef.com

---

## Development Tips

### VS Code Setup

**Recommended settings.json:**
```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "typescript.tsdk": "node_modules/typescript/lib"
}
```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/my-feature

# Make changes and commit
git add .
git commit -m "Add my feature"

# Push to GitHub
git push origin feature/my-feature

# Create Pull Request on GitHub
```

### Code Quality

```bash
# Run linter
npm run lint

# Fix linting issues
npm run lint -- --fix

# Type check
npx tsc --noEmit
```

### Performance Monitoring

```bash
# Analyze bundle
npm run build -- --analyze

# Check bundle size
du -sh .next

# Lighthouse audit
npx lighthouse http://localhost:3000
```

---

## Additional Resources

### Documentation
- **Next.js**: https://nextjs.org/docs
- **React**: https://react.dev/
- **TypeScript**: https://www.typescriptlang.org/docs/
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Wagmi**: https://wagmi.sh/
- **RainbowKit**: https://www.rainbowkit.com/docs
- **Ethers.js**: https://docs.ethers.org/
- **Google Gemini API**: https://ai.google.dev/

### Blockchain Resources
- **Ethereum**: https://ethereum.org/developers
- **Sepolia Testnet**: https://sepolia.dev/
- **IPFS**: https://docs.ipfs.tech/

### Community
- **GitHub**: https://github.com/mrbrightsides/healthchain
- **Telegram**: https://t.me/khudriakhmad
- **Discord**: https://discord.com/channels/@khudri_61362
- **Email**: support@elpeef.com

---

## Next Steps

After setup:
1. ✅ Explore all 12 portal modules
2. ✅ Connect wallet and try blockchain features
3. ✅ Test all 6 Health Centers with AI Assistants
4. ✅ Try all 45+ AI modes across modules
5. ✅ Chat with AI Companion
6. ✅ Read [FEATURES.md](./FEATURES.md) for detailed docs
7. ✅ Check [ARCHITECTURE.md](./ARCHITECTURE.md) for technical overview
8. ✅ Join community on Telegram/Discord
9. ✅ Start building and contributing!

---

**Build the future of healthcare with AI + Blockchain! 🚀**

**Contact:** support@elpeef.com | **GitHub:** https://github.com/mrbrightsides/healthchain
