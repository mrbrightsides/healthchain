# Third-Party APIs & SDKs

This document provides comprehensive information about all external APIs, SDKs, and services integrated into **RANTAI HealthChain**. These third-party services enable advanced features like AI-powered diagnostics, blockchain storage, voice assistance, and decentralized medical imaging.

---

## 📊 Overview

| Service | Purpose | Pricing | API Key Required |
|---------|---------|---------|------------------|
| **Google Gemini API** | AI-powered medical diagnostics & health predictions | Free tier + Pay-as-you-go | ✅ Yes |
| **ElevenLabs API** | Voice synthesis for health assistant | Free tier + Paid plans | ✅ Yes |
| **Ethereum & Base** | Blockchain storage for health records | Gas fees apply | ❌ No (wallet-based) |
| **Pinata & IPFS** | Decentralized medical imaging storage | Free tier + Paid plans | ✅ Yes |
| **RainbowKit & Wagmi** | Web3 wallet integration | Free | ❌ No |
| **jsPDF** | PDF generation for medical records | Free (MIT) | ❌ No |
| **Lucide React** | Icon library | Free (ISC) | ❌ No |

---

## 🤖 1. Google Gemini API

### Purpose
Google Gemini 2.0 Flash API powers the entire AI intelligence system in RANTAI HealthChain, providing **45+ specialized AI modes** across 16 healthcare modules.

### Key Features Used
- **Medical Diagnostics** - Symptom analysis, differential diagnosis, risk assessment
- **Health Predictions** - Disease risk modeling, progression forecasting
- **Clinical Decision Support** - Treatment recommendations, lab interpretation
- **Health Education** - Medical knowledge, wellness guidance
- **Emergency Triage** - Severity assessment, crisis detection
- **Vision AI** - Medical image analysis (X-ray, CT, MRI interpretation)

### API Endpoints in RANTAI
1. `/api/gemini` - General AI health assistance
2. `/api/gemini-vision` - Medical image analysis
3. `/api/fitness-ai` - Fitness coaching (5 modes)
4. `/api/nutrition-ai` - Nutrition guidance (5 modes)
5. `/api/maternal-child-ai` - Maternal & child health (5 modes)
6. `/api/heart-health-ai` - Cardiovascular health (5 modes)
7. `/api/mental-wellness-enhanced-ai` - Mental health support (5 modes)
8. `/api/eye-health-ai` - Eye health consultation (5 modes)
9. `/api/emergency-ai` - Emergency assessment (5 modes)
10. `/api/second-opinion-ai` - Second opinion analysis (6 modes)
11. `/api/medical-knowledge` - Health education AI
12. `/api/vaccine-intelligence` - Immunization guidance
13. `/api/lab-interpretation` - Lab results analysis
14. `/api/pharmacy-intelligence` - Medication guidance
15. `/api/clinical-intelligence` - Clinical notes AI
16. `/api/claims-intelligence` - Insurance claims AI
17. `/api/health-insights` - Analytics AI

### Rate Limits & Quotas
- **Free Tier**: 15 requests per minute (RPM), 1,500 requests per day (RPD)
- **Pay-as-you-go**: 1,000 RPM, 5M RPD
- **Model**: gemini-2.0-flash-exp (latest experimental)

### Pricing
- **Free Tier**: $0 (suitable for development and small-scale testing)
- **Paid Tier**: $0.075 per 1M input tokens, $0.30 per 1M output tokens
- **Estimated Cost**: ~$50-200/month for 10K active users

### API Key Required
✅ Yes - `GEMINI_API_KEY` environment variable

### Documentation
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Pricing Calculator](https://ai.google.dev/pricing)

---

## 🎙️ 2. ElevenLabs API

### Purpose
Provides natural, human-like voice synthesis in **Indonesian language** for the Voice Health Assistant feature, enabling audio playback of medical knowledge articles.

### Key Features Used
- **Text-to-Speech (TTS)** - Convert medical articles to natural Indonesian speech
- **Voice Selection** - Multiple Indonesian voice options
- **Real-time Synthesis** - On-demand audio generation
- **Multilingual Support** - Indonesian primary, English secondary

### API Endpoint in RANTAI
- `/api/elevenlabs` - Voice synthesis endpoint for Health Knowledge module

### Integration Details
- **Voice Model**: Eleven Multilingual v2
- **Language**: Indonesian (id) primary
- **Output Format**: MP3 audio stream
- **Use Case**: "Read Aloud" feature in Health Knowledge Center

### Rate Limits & Quotas
- **Free Tier**: 10,000 characters/month
- **Starter Plan**: 30,000 characters/month
- **Creator Plan**: 100,000 characters/month
- **Pro Plan**: 500,000 characters/month

### Pricing
- **Free**: $0 (10K characters)
- **Starter**: $5/month (30K characters)
- **Creator**: $22/month (100K characters)
- **Pro**: $99/month (500K characters)
- **Overage**: $0.30 per 1,000 characters

### API Key Required
✅ Yes - `ELEVENLABS_API_KEY` environment variable

### Documentation
- [ElevenLabs Documentation](https://elevenlabs.io/docs)
- [API Reference](https://elevenlabs.io/docs/api-reference)
- [Pricing Plans](https://elevenlabs.io/pricing)

---

## 🔗 3. Ethereum & Base Network (Blockchain)

### Purpose
Provides blockchain infrastructure for decentralized health record storage, enabling users to control their medical data with cryptographic security and immutability.

### Networks Used
1. **Ethereum Mainnet** - Primary blockchain for production
2. **Base (Coinbase L2)** - Layer 2 solution for lower gas fees
3. **Ethereum Sepolia** - Testnet for development

### Key Features Used
- **Wallet Connection** - MetaMask, Coinbase Wallet, WalletConnect integration
- **Smart Contract Interaction** - Health record storage and retrieval
- **Transaction Signing** - Cryptographic proof of medical data ownership
- **Guest Mode** - Non-blockchain fallback for users without wallets
- **Multi-chain Support** - Seamless switching between networks

### Gas Fees
- **Ethereum Mainnet**: ~$2-20 per transaction (variable based on network congestion)
- **Base Network**: ~$0.01-0.50 per transaction (L2 efficiency)
- **Recommendation**: Use Base for cost-effective operations

### API Key Required
❌ No - Wallet-based authentication (user signs transactions)

### Documentation
- [Ethereum Developer Docs](https://ethereum.org/en/developers/docs/)
- [Base Network Documentation](https://docs.base.org/)
- [RainbowKit Docs](https://www.rainbowkit.com/docs/introduction)
- [Wagmi Documentation](https://wagmi.sh/)

---

## 💾 4. Pinata & IPFS (Decentralized Storage)

### Purpose
Provides decentralized, permanent, and tamper-proof storage for medical imaging files (X-rays, CT scans, MRI images) using the **InterPlanetary File System (IPFS)** with Pinata as the gateway service.

### Key Features Used
- **Medical Image Upload** - Upload diagnostic images to IPFS
- **Content Addressing** - Retrieve files via unique CID (Content Identifier)
- **Immutable Storage** - Files cannot be altered once stored
- **Metadata Storage** - Store patient info, imaging type, timestamps
- **AI Vision Integration** - Combine IPFS storage with Gemini Vision AI for analysis

### API Endpoint in RANTAI
- `/api/pinata` - Upload medical images to IPFS via Pinata

### Integration Details
- **File Types Supported**: PNG, JPG, JPEG, DICOM
- **Max File Size**: 100MB per image (configurable)
- **Storage**: IPFS distributed network
- **Gateway**: Pinata dedicated gateway for fast retrieval

### Rate Limits & Quotas
- **Free Tier**: 1GB storage, 100 pins
- **Picnic Plan**: $20/month (100GB storage, unlimited pins)
- **Submarine Plan**: $100/month (1TB storage, unlimited pins)

### Pricing
- **Free**: $0 (1GB, 100 pins)
- **Paid Plans**: Starting at $20/month
- **Bandwidth**: Free for uploads, gateway retrievals included

### API Key Required
✅ Yes - `PINATA_JWT` environment variable

### Documentation
- [Pinata Documentation](https://docs.pinata.cloud/)
- [IPFS Documentation](https://docs.ipfs.tech/)
- [Pinata Pricing](https://www.pinata.cloud/pricing)

---

## 🌐 5. RainbowKit & Wagmi (Web3 Integration)

### Purpose
Provides seamless Web3 wallet connection and blockchain interaction capabilities for RANTAI HealthChain's blockchain features.

### Key Features Used
- **RainbowKit** - Beautiful, responsive wallet connection modal
- **Wagmi** - React hooks for Ethereum interactions
- **Wallet Support** - MetaMask, Coinbase Wallet, WalletConnect, Rainbow, Trust Wallet
- **Multi-chain** - Ethereum, Base, Sepolia support
- **Transaction Handling** - Send/sign transactions, read contract data
- **Account Management** - ENS name resolution, balance checking

### Integration Details
- **Components Used**: `ConnectButton`, wallet modals
- **Hooks Used**: `useAccount`, `useConnect`, `useDisconnect`, `useBalance`, `useContractWrite`
- **Chains**: Ethereum Mainnet, Base, Sepolia testnet
- **Theme**: Custom RANTAI HealthChain branding

### Pricing
- **Free** - 100% open-source, no API keys required
- **No Rate Limits** - Client-side library

### API Key Required
❌ No - Pure frontend library (requires RPC endpoint for blockchain access)

### Documentation
- [RainbowKit Documentation](https://www.rainbowkit.com/)
- [Wagmi Documentation](https://wagmi.sh/)
- [GitHub - RainbowKit](https://github.com/rainbow-me/rainbowkit)
- [GitHub - Wagmi](https://github.com/wevm/wagmi)

---

## 📄 6. jsPDF (PDF Generation)

### Purpose
Client-side PDF generation for exporting medical records, lab results, prescriptions, and health reports.

### Key Features Used
- **Medical Records Export** - Generate PDF summaries of patient health data
- **Lab Reports** - Create printable lab result documents
- **Prescription Export** - Format medication prescriptions
- **Health Summaries** - Generate comprehensive health reports
- **Custom Styling** - Apply RANTAI HealthChain branding to PDFs

### Integration Details
- **Library**: jsPDF v4.0.0
- **Use Cases**:
  - Patient Dashboard - Export health records
  - Lab Results - Download lab reports
  - Immunization Tracker - Print vaccination records
  - Pharmacy - Export prescription history
  - Insurance - Generate claim documentation

### Pricing
- **Free** - MIT License, open-source

### API Key Required
❌ No - Pure JavaScript library

### Documentation
- [jsPDF Documentation](https://github.com/parallax/jsPDF)
- [jsPDF API Reference](https://rawgit.com/MrRio/jsPDF/master/docs/)

---

## 🎨 7. Lucide React (Icon Library)

### Purpose
Provides a comprehensive set of beautiful, consistent icons used throughout the RANTAI HealthChain user interface.

### Key Features Used
- **200+ Icons** - Medical, health, UI, and utility icons
- **Customizable** - Adjustable size, color, stroke width
- **Tree-shakable** - Only import icons you use (smaller bundle)
- **TypeScript Support** - Full type definitions
- **Consistent Design** - Matches RANTAI HealthChain aesthetic

### Icons Used (Examples)
- Medical: `Heart`, `Activity`, `Stethoscope`, `Pill`, `Syringe`
- Health: `Brain`, `Eye`, `Baby`, `Dumbbell`, `Apple`
- UI: `Menu`, `Settings`, `Bell`, `Search`, `ChevronRight`
- Emergency: `AlertTriangle`, `Phone`, `Ambulance`, `Shield`

### Pricing
- **Free** - ISC License, open-source

### API Key Required
❌ No - Pure React component library

### Documentation
- [Lucide Icons](https://lucide.dev/)
- [Lucide React Documentation](https://lucide.dev/guide/packages/lucide-react)
- [Icon Search](https://lucide.dev/icons/)

---

## 🔑 Environment Variables Configuration

To run RANTAI HealthChain locally or in production, configure the following environment variables:

```bash
# Google Gemini API (Required for AI features)
GEMINI_API_KEY=your_gemini_api_key_here

# ElevenLabs API (Required for Voice Assistant)
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

# Pinata IPFS (Required for Medical Imaging)
PINATA_JWT=your_pinata_jwt_token_here

# Optional: Custom RPC endpoints for blockchain
NEXT_PUBLIC_ALCHEMY_ID=your_alchemy_api_key_here
NEXT_PUBLIC_INFURA_ID=your_infura_api_key_here
```

### How to Obtain API Keys

1. **Google Gemini API**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Sign in with Google account
   - Click "Get API Key" → Create new key
   - Copy and add to `.env.local`

2. **ElevenLabs API**
   - Sign up at [ElevenLabs](https://elevenlabs.io/)
   - Navigate to Profile → API Keys
   - Generate new API key
   - Copy and add to `.env.local`

3. **Pinata JWT**
   - Create account at [Pinata](https://www.pinata.cloud/)
   - Go to API Keys section
   - Generate new JWT token with upload permissions
   - Copy and add to `.env.local`

---

## 📊 Rate Limits & Quotas Summary

| Service | Free Tier Limit | Paid Tier Limit | Recommended for |
|---------|----------------|----------------|-----------------|
| **Gemini API** | 15 RPM, 1,500 RPD | 1,000 RPM, 5M RPD | Free: Development<br>Paid: Production |
| **ElevenLabs** | 10,000 chars/month | 500,000 chars/month | Free: Testing<br>Paid: Production |
| **Pinata IPFS** | 1GB storage | 1TB+ storage | Free: MVP<br>Paid: Scale |
| **Ethereum** | N/A (gas fees) | N/A (gas fees) | Use Base L2 for lower fees |
| **RainbowKit/Wagmi** | No limits | No limits | All stages (free) |
| **jsPDF** | No limits | No limits | All stages (free) |
| **Lucide React** | No limits | No limits | All stages (free) |

---

## 💰 Cost Estimation (Monthly)

### Development Environment
- **Gemini API**: $0 (free tier sufficient)
- **ElevenLabs**: $0 (free tier sufficient)
- **Pinata**: $0 (free tier sufficient)
- **Blockchain**: $10-50 (Base testnet gas fees)
- **Total**: **$10-50/month**

### Small Scale (1,000 active users)
- **Gemini API**: $50-100 (paid tier)
- **ElevenLabs**: $22 (Creator plan)
- **Pinata**: $20 (Picnic plan)
- **Blockchain**: $50-100 (Base mainnet gas)
- **Total**: **~$150-250/month**

### Medium Scale (10,000 active users)
- **Gemini API**: $300-500
- **ElevenLabs**: $99 (Pro plan)
- **Pinata**: $100 (Submarine plan)
- **Blockchain**: $200-500
- **Total**: **~$700-1,200/month**

### Large Scale (100,000+ active users)
- **Gemini API**: $2,000-5,000
- **ElevenLabs**: $300+ (Enterprise)
- **Pinata**: $500+ (Custom)
- **Blockchain**: $1,000-3,000
- **Total**: **~$3,800-8,500/month**

---

## 🔒 API Security Best Practices

### 1. Environment Variables
- ✅ Store API keys in `.env.local` (never commit to Git)
- ✅ Use different keys for development/staging/production
- ✅ Rotate keys regularly (every 90 days recommended)
- ✅ Restrict API key permissions to minimum required

### 2. Server-Side API Calls
- ✅ All API calls are made from Next.js API routes (server-side)
- ✅ Never expose API keys to client-side JavaScript
- ✅ Use Next.js middleware for authentication checks
- ✅ Implement request validation and sanitization

### 3. Rate Limiting
- ✅ Implement rate limiting per user/IP address
- ✅ Use exponential backoff for retries
- ✅ Cache responses when appropriate
- ✅ Monitor API usage with logging

### 4. Error Handling
- ✅ Catch and log API errors properly
- ✅ Provide user-friendly error messages
- ✅ Implement fallbacks for API failures
- ✅ Set up alerts for critical API errors

---

## 🐛 Troubleshooting

### Gemini API Issues

**Problem**: "API key not valid" error
- **Solution**: Verify `GEMINI_API_KEY` is correctly set in `.env.local`
- **Check**: API key is enabled in Google AI Studio

**Problem**: Rate limit exceeded
- **Solution**: Implement request queuing or upgrade to paid tier
- **Check**: Monitor usage in Google AI Studio dashboard

### ElevenLabs Issues

**Problem**: Voice synthesis fails
- **Solution**: Verify `ELEVENLABS_API_KEY` is valid
- **Check**: Free tier character limit not exceeded

**Problem**: Audio quality poor
- **Solution**: Adjust voice model or stability/similarity settings
- **Check**: Network bandwidth for audio streaming

### Pinata IPFS Issues

**Problem**: Upload fails
- **Solution**: Check file size (max 100MB default)
- **Verify**: `PINATA_JWT` has upload permissions

**Problem**: Image retrieval slow
- **Solution**: Use Pinata dedicated gateway
- **Consider**: Pinata submarine (faster retrieval)

### Blockchain Issues

**Problem**: Wallet won't connect
- **Solution**: Ensure user has MetaMask or compatible wallet installed
- **Check**: Correct network selected (Ethereum/Base)

**Problem**: Transaction fails
- **Solution**: Check user has sufficient ETH for gas fees
- **Recommend**: Switch to Base network for lower fees

---

## 🚀 Future API Integrations

RANTAI HealthChain plans to integrate additional services:

### Telemedicine
- **Twilio Video API** - Video consultations with doctors
- **Agora.io** - Alternative video/audio solution

### Notifications
- **Twilio SMS** - Appointment reminders, health alerts
- **Firebase Cloud Messaging** - Push notifications for mobile app

### Payment Processing
- **Stripe** - International payment processing
- **Xendit** - Indonesian payment gateway (BPJS, bank transfers)

### Wearable Integration
- **Fitbit API** - Activity tracking, heart rate data
- **Apple HealthKit** - iOS health data integration
- **Google Fit** - Android health data integration

### Advanced AI
- **OpenAI GPT-4** - Enhanced conversational AI
- **Anthropic Claude** - Medical reasoning and analysis
- **Hugging Face Models** - Specialized medical NLP models

---

## 📞 Support & Contact

For questions about third-party API integration or issues with external services:

- **GitHub**: [github.com/mrbrightsides/healthchain](https://github.com/mrbrightsides/healthchain)
- **Email**: [support@elpeef.com](mailto:support@elpeef.com)
- **Telegram**: [@khudriakhmad](https://t.me/khudriakhmad)
- **Discord**: [@khudri_61362](https://discord.com/channels/@khudri_61362)

For API-specific support, please contact the respective service providers using their official documentation links provided above.

---

## 📚 Additional Resources

- [RANTAI HealthChain README](./README.md)
- [Setup Guide](./SETUP.md)
- [Architecture Documentation](./ARCHITECTURE.md)
- [Features Documentation](./FEATURES.md)

---

**Last Updated**: January 2025  
**RANTAI HealthChain Version**: 2.0  
**AI Intelligence System**: 45+ Specialized Modes Across 16 Modules
