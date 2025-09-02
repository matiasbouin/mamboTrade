# Automated Trading System – From PoC to Scalable Fintech Product

## 📌 Project Overview
This project starts as a **Proof of Concept (PoC)** for an automated trading system and evolves toward a **scalable, commercial fintech platform**.  
The system consists of three core microservices:

- **Data Collector**
- **Signal Service**
- **Execution Service**

---

## 💡 General Idea: Automated Trading System with Proof-of-Stake (PoS) Integration

### Core Concept
An algorithmic trading platform that:
- Executes trades based on AI-driven signals (technical indicators, sentiment analysis).
- Integrates with **Proof-of-Stake (PoS)** cryptocurrencies for **staking rewards**.  
- Includes **backtesting modules**, **risk management tools**, and **compliance features** for future regulatory readiness.

### Tech Stack (Planned - could change uppon implementation)
- **Backend**: Python/Go for trading engines; integration with Binance/Coinbase APIs.  
- **Data Pipeline**: Apache Kafka for real-time streams; ML models (TensorFlow/PyTorch) for predictive analytics.  
- **Infrastructure**: Kubernetes for scalability, Terraform for IaC, Prometheus/Grafana for monitoring.  
- **Blockchain**: PoS protocols (Ethereum 2.0, Cardano, Solana) for staking-as-a-service.  
- **Frontend / UX**: React dashboard with real-time charts, portfolio view, and alerts.  
- **Monetization**:  
  - Commissions on executed trades  
  - Revenue from staking services  
  - Premium subscription for advanced algorithms  
  - SaaS-style API access for hedge funds or prop traders  

### Why It Fits
- Combines **trading automation**, **crypto-native staking**, and **scalable DevOps practices**.  
- Positioned as a **fintech SaaS platform** with potential for **B2B (hedge funds, trading desks)** and **B2C (retail investors)** markets.  

---

## 🛤️ Development Path

### Phase 0: Foundation & Design (Week 1-2)
- Define **Minimal Viable PoC (MVPoC)**: goal is a working pipeline, not profitability.  
- Pick a single, liquid crypto pair (e.g., BTC/USDT).  
- Choose exchange with a stable API (Binance or Coinbase Prime).  
- Implement a **basic SMA crossover strategy (50 vs 200)**.  
- Bot places **mock (paper) trades**.  
- Architecture: Microservices (Data Collector, Signal Service, Execution Service).  
- (Optional) Add PostgreSQL/TimescaleDB for price/signals storage.  
- Language: Python (initial) → Go/Rust (future high-frequency).  
- Infrastructure: Pick a cloud provider (AWS/GCP/Azure).  

---

### Phase 1: Building the Core PoC (Week 3-6)

1. **Development Environment**
   - New GitHub/GitLab repository  
   - Python virtual environment  
   - `requirements.txt`: ccxt, pandas, fastapi, uvicorn, python-dotenv  

2. **Data Collector Service**
   - Fetch historical OHLCV data with `ccxt`.  
   - Store data in CSV/SQLite (later migrate to DB).  

3. **Signal Service**
   - Reads data, calculates 50/200 SMA crossover.  
   - Exposes REST endpoint via FastAPI.  

4. **Execution Service**
   - Polls Signal Service.  
   - On signal change, places **mock trade** (`BUY`/`SELL`) on Binance Testnet.  

5. **Basic Orchestration**
   - Docker Compose to run all three services.  

---

### Phase 2: DevOps & Infrastructure (Week 7-8)

1. **Containerization**
   - Dockerfiles for each service.  
   - `docker-compose.yml` including DB, networking.  

2. **Infrastructure as Code (IaC)**
   - Terraform for cloud infra (EKS/ECS, managed DB).  

3. **CI/CD Pipeline**
   - GitHub Actions/GitLab CI: lint → test → build → push → deploy.  

---

### Phase 3: Testing, Monitoring & Iteration (Ongoing)

1. **Testing**
   - Unit tests for strategies.  
   - Integration tests for inter-service communication.  

2. **Monitoring**
   - Health check endpoints (FastAPI).  
   - Prometheus/Grafana for metrics and alerting.  

3. **Feedback Loop**
   - Backtesting engine with pandas.  
   - Structured logging (json-logger).  

---

## 🚀 Growth Path (Scaling Toward Commercialization)

- **Expand Data Sources**  
  Add sentiment feeds (Twitter, Reddit, news APIs) and traditional market data.  

- **AI/ML Integration**  
  Use deep learning for predictive analytics (LSTMs, transformers for time series).  

- **Risk & Compliance Layer**  
  - Portfolio balancing  
  - Stop-loss / take-profit automation  
  - KYC/AML integration for B2C rollout  

- **Scalability**  
  - Kafka or RabbitMQ for streaming  
  - Redis for caching signals/orders  
  - Optimized DBs (ClickHouse, TimescaleDB)  

- **Commercialization Features**  
  - SaaS REST API for institutional clients  
  - Web dashboard (React/Next.js) for traders  
  - Tiered subscription model (Basic, Pro, Enterprise)  

- **Security**  
  - Encrypted API key storage (Vault, KMS)  
  - Role-based access control (RBAC)  
  - Audit logs for trades  

- **Long-Term Vision**  
  - Launch as a **fintech SaaS** platform  
  - Integrate staking-as-a-service (ETH, ADA, SOL)  
  - API marketplace for custom trading strategies  

---

## 📊 Positioning as a Fintech Product
By Phase 3, the project moves from PoC to:  

- **B2C product**: retail traders use a web dashboard with signals, bots, and staking.  
- **B2B product**: institutional clients consume signals and execution API at scale.  
- **Revenue model**: subscriptions, trade commissions, staking fees.  
- **Market readiness**: modular microservice design + Kubernetes ensures **scalability & reliability**.  

---

## ⚠️ Important Notes
- Early phases are **educational and experimental**.  
- Real money trading requires **rigorous testing**, **risk management**, and **compliance**.  
- This system **must not** be deployed with live funds until fully validated.  

---

---

# Automated Trading System - Docker Setup Guide

## Prerequisites
- Docker Desktop installed on macOS
- Binance Testnet API keys (for execution service)

---

## 🚀 Quick Start

### Clone the repository
```bash
git clone <your-repo-url>
cd mamboTrade
```

### Set up environment variables
```bash
cp .env.example .env
```
Edit `.env` with your Binance Testnet API keys.

### Build and run the application
```bash
docker compose up --build
```

---

## 🛠️ Detailed Steps - First-Time Setup

### Clone the project
```bash
git clone <your-repo-url>
cd mamboTrade
```

### Create environment file from template
```bash
cp .env.example .env
nano .env   # or use your preferred editor
```

Configure environment variables with your Binance Testnet credentials:
```env
BINANCE_TESTNET_API_KEY=your_api_key_here
BINANCE_TESTNET_SECRET_KEY=your_secret_key_here
```

🔗 To get Binance Testnet API keys: [Binance Testnet](https://testnet.binance.vision/)

---

## ▶️ Running the Application

### Start all services in foreground (see logs)
```bash
docker compose up --build
```

### Start in background (detached mode)
```bash
docker compose up --build -d
```

### Stop all services
```bash
docker compose down
```

### Stop and remove volumes (clean slate)
```bash
docker compose down -v
```

---

## 🧪 Testing the Services

### Test the Signal Service API
```bash
curl http://localhost:8000/signal
```
**Expected response:**
```json
{"signal":"BUY|SELL","sma50":12345.67,"sma200":12345.67,"timestamp":"2025-09-01 10:00:00"}
```

### Check Service Status
```bash
# View running containers
docker compose ps

# View logs for a specific service
docker compose logs signal-service
docker compose logs execution-service

# Follow logs in real-time
docker compose logs -f execution-service
```

### Verify Data Collection
```bash
# Check if data files were created
docker compose exec signal-service ls -la /app/shared_data
```

---

## 💻 Development Workflow

```bash
# Rebuild after code changes
docker compose up --build

# Run a specific service
docker compose up signal-service

# Access a container shell for debugging
docker compose exec signal-service bash
docker compose exec execution-service bash

# Test API from within the network
docker compose exec execution-service python -c "import requests; print(requests.get('http://signal-service:8000/signal').json())"
```

---

## 📂 Project Structure

```text
mamboTrade/
├── docker-compose.yml          # Container orchestration
├── .env                        # Environment variables (ignored by git)
├── requirements.txt            # Python dependencies
├── data_collector/             # Data fetching service
│   ├── data_collector.py
│   └── Dockerfile
├── signal_service/             # Trading signal API
│   ├── signal_service.py
│   └── Dockerfile
└── execution_service/          # Trade execution service
    ├── execution_service.py
    └── Dockerfile
```

---

## 🐞 Troubleshooting

### Common Issues

**Port already in use**
```bash
# Check if port 8000 is being used
lsof -i :8000
# Kill the process or change the port in docker-compose.yml
```

**Permission errors**
```bash
# Reset Docker permissions (if needed)
sudo chown -R $USER:$USER .
```

**Container networking issues**
```bash
# Reset Docker network
docker network prune
```

**Build cache issues**
```bash
# Rebuild without cache
docker compose build --no-cache
docker compose up
```

### Debugging Tips

Check container logs:
```bash
docker compose logs
docker compose logs service_name
```

Inspect container status:
```bash
docker ps -a
docker inspect container_name
```

Test service connectivity:
```bash
# From your host
curl http://localhost:8000/signal

# From within the container network
docker compose exec execution-service python -c "import requests; print(requests.get('http://signal-service:8000/signal').status_code)"
```

---

## 📈 Next Steps

- Modify the trading strategy in `signal_service.py`
- Add more indicators or data sources
- Implement real order placement (uncomment code in `execution_service.py`)
- Set up monitoring with Prometheus/Grafana
- Add a frontend dashboard to visualize signals and performance

---

## ⚠️ Important Notes

- This is a proof-of-concept system for educational purposes  
- **Never use real API keys or funds with this system initially**  
- All trading involves risk — test thoroughly before considering real money  
- The system uses historical data — past performance doesn't guarantee future results  