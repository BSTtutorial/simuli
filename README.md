# SageMath Web Calculator (Lightweight)

A lightweight web-based calculator powered by SageMath that can perform complex mathematical computations. This version uses the **SageMathCell API** instead of hosting SageMath locally, making it perfect for free hosting platforms.

## ✨ Features

- 🔢 Full SageMath functionality via API
- 📊 Matrix operations, calculus, algebra, number theory
- 🎯 Equation solving, limits, derivatives, integration
- 🌐 Clean, modern web interface
- 🚀 **Super lightweight** (~50MB vs 4GB!)
- ⚡ **Fast deployment** (~1-2 minutes vs 15+ minutes)
- 💰 **Works on ANY free tier**

## 🚀 Quick Deploy

### Option 1: Railway.app (Recommended - Best Free Tier)

1. Sign up at [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your GitHub repository
4. Railway auto-detects the Dockerfile
5. Deploy! (Takes ~1-2 minutes)

**Why Railway?**
- ✅ $5 free credit monthly
- ✅ No credit card required initially
- ✅ Doesn't sleep aggressively
- ✅ Great for Docker apps

### Option 2: Render.com

1. Push code to GitHub
2. Go to [render.com](https://render.com/dashboard)
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Select **Docker** environment
6. Click "Create Web Service"

**Settings:**
- Environment: **Docker**
- Region: Choose closest to you
- Plan: Free

### Option 3: Fly.io

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Login
flyctl auth login

# Deploy
flyctl launch
flyctl deploy
```

### Option 4: Google Cloud Run

1. Install gcloud CLI
2. Build and deploy:
```bash
gcloud builds submit --tag gcr.io/YOUR-PROJECT/sagemath-calc
gcloud run deploy --image gcr.io/YOUR-PROJECT/sagemath-calc --platform managed
```

## 📁 Project Structure

```
sagemath-webapp-lite/
├── app.py                  # Flask app using SageMathCell API
├── templates/
│   └── index.html         # Frontend interface
├── requirements.txt       # Python dependencies (only 3!)
├── Dockerfile            # Docker configuration
├── render.yaml           # Render deployment config
└── README.md             # This file
```

## 🔧 Local Development

### Using Docker (Recommended)

```bash
docker build -t sagemath-lite .
docker run -p 10000:10000 sagemath-lite
```

Open http://localhost:10000

### Using Python directly

```bash
pip install -r requirements.txt
python app.py
```

## 💡 How It Works

Instead of installing the massive SageMath package (~4GB), this app:

1. Takes user input from the web interface
2. Sends it to SageMathCell's free public API
3. Returns the calculated result
4. Displays it in the browser

**Benefits:**
- ⚡ 50x smaller Docker image
- 🚀 10x faster deployment
- 💰 Works on smallest free tiers
- 🔄 Same SageMath functionality

## 📊 Usage Examples

**Factorization:**
```python
factor(2024)
```

**Derivatives:**
```python
derivative(x^3 + 2*x^2 - 5*x + 1, x)
```

**Integration:**
```python
integral(sin(x)*cos(x), x)
```

**Solve Equations:**
```python
solve([x + y == 6, x - y == 4], x, y)
```

**Matrix Operations:**
```python
matrix([[1,2],[3,4]]).determinant()
```

**Limits:**
```python
limit((sin(x)/x), x=0)
```

## 🆚 Lightweight vs Full Version

| Feature | Lightweight | Full Version |
|---------|-------------|--------------|
| Docker Image Size | ~150MB | ~4GB |
| Build Time | 1-2 min | 10-20 min |
| Memory Usage | ~50MB | ~500MB |
| Works on Free Tier? | ✅ All platforms | ⚠️ Limited |
| SageMath Features | ✅ Full | ✅ Full |
| Speed | ⚡ Fast | ⚡ Fast |
| Dependency | SageMathCell API | Self-hosted |

## ⚙️ Environment Variables

Only one required:
- **PORT**: Port number (default: 10000)

Auto-configured in `render.yaml` and Dockerfile.

## 🌐 API Dependency

This app uses the free **SageMathCell** public API:
- URL: https://sagecell.sagemath.org/service
- Rate limits: Reasonable for personal use
- Uptime: Very reliable (hosted by SageMath project)

If SageMathCell is down, calculations won't work. For production use requiring 100% uptime, consider the full self-hosted version.

## 🐛 Troubleshooting

**"SageMath service unavailable"**
- The SageMathCell API might be temporarily down
- Wait a few minutes and try again

**Timeout errors**
- Very complex calculations may timeout (30s limit)
- Try simplifying the calculation

**Build fails on Render**
- Make sure you selected **Docker** environment
- Not "Python" or "Node"

## 📝 License

MIT License - Free to use and modify

## 🙏 Credits

- Built with Flask
- Powered by [SageMathCell](https://sagecell.sagemath.org/)
- SageMath by the SageMath Development Team

## 💬 Support

For questions:
- SageMath syntax: [SageMath Docs](https://doc.sagemath.org/)
- Deployment issues: Check your platform's documentation
- This app: Open an issue in your repo
