# 🔢 SageMath Web Calculator - Complete Render Deployment Package

A beautiful, lightweight web calculator powered by SageMath through CoCalc's API. Deploy to Render in under 5 minutes!

![](https://img.shields.io/badge/Python-3.11-blue)
![](https://img.shields.io/badge/Flask-3.0-green)
![](https://img.shields.io/badge/Docker-Ready-blue)
![](https://img.shields.io/badge/Deploy-Render-purple)

## ✨ Features

- 🔢 **Full SageMath Functionality**: Calculus, algebra, number theory, linear algebra
- 🎨 **Beautiful UI**: Modern, gradient design with responsive layout
- 🚀 **Lightweight**: ~150MB Docker image, deploys in 1-2 minutes
- 💰 **Free Tier Compatible**: Works perfectly on Render's free plan
- 🔐 **Secure**: API keys via environment variables
- ⚡ **Fast**: Powered by CoCalc's reliable infrastructure

## 📦 What's Included

```
sagemath-calculator/
├── app.py              # Flask backend with CoCalc API integration
├── templates/
│   └── index.html     # Beautiful frontend interface
├── requirements.txt   # Python dependencies (Flask, Gunicorn, Requests)
├── Dockerfile         # Container configuration
├── render.yaml        # Render deployment config
├── .gitignore         # Git ignore file
├── .env.example       # Environment variable template
└── README.md          # This file
```

## 🚀 Deploy to Render (Step-by-Step)

### Step 1: Get Your CoCalc API Key (FREE)

1. **Sign up at CoCalc**: Go to [https://cocalc.com](https://cocalc.com) and create a FREE account
2. **Access Settings**: Click the gear icon (⚙️) in the top right
3. **Navigate to API Keys**: Settings → Account Settings → scroll to "API Keys"
4. **Create API Key**: Click "Create API Key" button
5. **Copy Your Key**: Save it somewhere safe (looks like `sk_abc123...`)
   - ⚠️ You won't be able to see it again!

### Step 2: Push to GitHub

1. **Create a new GitHub repository** (public or private)
2. **Upload all files** from this folder to your repo
3. **Commit and push**

```bash
# Quick commands if using Git CLI:
git init
git add .
git commit -m "Initial commit - SageMath calculator"
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Render

1. **Go to Render**: Visit [https://render.com/dashboard](https://render.com/dashboard)
2. **Sign up/Login**: Create account or sign in (free)
3. **New Web Service**: Click "New +" → "Web Service"
4. **Connect GitHub**: 
   - Connect your GitHub account
   - Select your repository
5. **Configure Settings**:
   - **Name**: `sagemath-calculator` (or your preferred name)
   - **Environment**: **Docker** ⬅️ IMPORTANT!
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Plan**: **Free**
6. **Add Environment Variable**:
   - Click "Advanced" or scroll down to "Environment Variables"
   - Click "Add Environment Variable"
   - **Key**: `COCALC_API_KEY`
   - **Value**: `sk_your_actual_api_key_from_step1`
7. **Create Web Service**: Click the button!

### Step 4: Wait for Deployment

- First build takes ~1-2 minutes
- Watch the build logs
- When you see "Your service is live 🎉" you're done!

### Step 5: Use Your Calculator! 🎉

Click the URL Render provides (looks like `https://sagemath-calculator.onrender.com`)

## 📊 Usage Examples

Once deployed, try these calculations:

**Factorization:**
```python
factor(2024)
# Result: 2^3 * 11 * 23
```

**Derivatives:**
```python
derivative(x^3 + 2*x^2 - 5*x + 1, x)
# Result: 3*x^2 + 4*x - 5
```

**Integration:**
```python
integral(sin(x)*cos(x), x)
# Result: sin(x)^2/2
```

**Solve Equations:**
```python
solve([x + y == 6, x - y == 4], x, y)
# Result: [[x == 5, y == 1]]
```

**Matrix Determinant:**
```python
matrix([[1,2],[3,4]]).determinant()
# Result: -2
```

**Limits:**
```python
limit((sin(x)/x), x=0)
# Result: 1
```

## 🔧 Local Development (Optional)

### Using Docker

```bash
# Build
docker build -t sagemath-calc .

# Run (with API key)
docker run -p 10000:10000 \
  -e COCALC_API_KEY=sk_your_key_here \
  sagemath-calc
```

Open [http://localhost:10000](http://localhost:10000)

### Using Python

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export COCALC_API_KEY=sk_your_key_here  # Linux/Mac
# OR
set COCALC_API_KEY=sk_your_key_here     # Windows

# Run
python app.py
```

## ⚙️ Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `COCALC_API_KEY` | ✅ Yes | Your CoCalc API key from cocalc.com |
| `PORT` | ❌ No | Port number (default: 10000, auto-set by Render) |

## 🐛 Troubleshooting

### "CoCalc API key not configured"
**Problem**: Environment variable not set  
**Solution**: Add `COCALC_API_KEY` in Render dashboard → Environment tab

### "Invalid CoCalc API key"
**Problem**: Wrong API key or typo  
**Solution**: 
- Check for extra spaces
- Generate a new key at cocalc.com
- Update in Render dashboard

### Build Fails
**Problem**: Wrong environment selected  
**Solution**: Make sure you selected **Docker** (not Python or Node.js)

### App Crashes After Deployment
**Problem**: Missing API key  
**Solution**: Check Render logs, ensure `COCALC_API_KEY` is set

### Slow First Response
**Problem**: Render free tier apps sleep after inactivity  
**Solution**: Normal behavior, subsequent requests will be fast

## 💰 Costs

### Render Free Tier
- ✅ 750 hours/month
- ✅ Apps sleep after 15 min inactivity
- ✅ 512 MB RAM
- ✅ Perfect for this app!

### CoCalc Free Tier
- ✅ API access included
- ✅ Reasonable rate limits
- ✅ Full SageMath functionality
- ✅ No credit card required

**Total Cost: $0/month** 🎉

## 🔒 Security Best Practices

- ✅ Never commit `.env` files to Git (already in `.gitignore`)
- ✅ Never share your API key publicly
- ✅ Use environment variables for secrets
- ✅ Regenerate API key if exposed
- ✅ Review Render's environment variables periodically

## 📚 Resources

- [SageMath Documentation](https://doc.sagemath.org/)
- [CoCalc API Docs](https://doc.cocalc.com/api/)
- [Render Documentation](https://render.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)

## 🆘 Support

**Issues with:**
- **SageMath syntax**: Check [SageMath docs](https://doc.sagemath.org/)
- **CoCalc API**: Visit [CoCalc support](https://doc.cocalc.com/)
- **Render deployment**: Check [Render docs](https://render.com/docs)
- **This app**: Open an issue in your GitHub repo

## 📝 License

MIT License - Free to use, modify, and distribute!

## 🙏 Credits

- **Built with**: Flask, Gunicorn, Python
- **Powered by**: CoCalc API
- **Math Engine**: SageMath
- **Hosting**: Render.com

---

**Made with ❤️ for the math community**

🌟 Star this repo if you find it useful!
