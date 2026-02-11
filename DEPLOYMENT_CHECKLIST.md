# ✅ Render Deployment Checklist

Follow these steps exactly and you'll be live in 5 minutes!

## Before You Start

- [ ] Have a GitHub account
- [ ] Have a Render account (free signup at render.com)
- [ ] Have a CoCalc account (free signup at cocalc.com)

## Step-by-Step Deployment

### 1️⃣ Get CoCalc API Key (2 minutes)

- [ ] Go to https://cocalc.com
- [ ] Sign up or log in
- [ ] Click settings gear ⚙️ (top right)
- [ ] Scroll to "API Keys" section
- [ ] Click "Create API Key"
- [ ] Copy the key (starts with `sk_`)
- [ ] **Save it somewhere** - you won't see it again!

### 2️⃣ Upload to GitHub (2 minutes)

- [ ] Create new repository on GitHub
- [ ] Name it whatever you want (e.g., `sagemath-calculator`)
- [ ] Make it Public or Private (your choice)
- [ ] Upload all files from this folder
- [ ] Commit the files

### 3️⃣ Deploy on Render (1 minute)

- [ ] Go to https://render.com/dashboard
- [ ] Click "New +" button
- [ ] Select "Web Service"
- [ ] Connect your GitHub account (if first time)
- [ ] Select your repository
- [ ] **IMPORTANT**: Set Environment to **Docker**
- [ ] Choose Free plan
- [ ] Scroll to "Environment Variables"
- [ ] Add variable:
  - Key: `COCALC_API_KEY`
  - Value: `sk_your_actual_key_here`
- [ ] Click "Create Web Service"

### 4️⃣ Wait for Build (1-2 minutes)

- [ ] Watch the build logs
- [ ] Wait for "Your service is live 🎉"
- [ ] Click the URL Render provides

### 5️⃣ Test It! (30 seconds)

- [ ] Open your app URL
- [ ] Try: `factor(2024)`
- [ ] Click "Calculate"
- [ ] See result: `2^3 * 11 * 23`
- [ ] 🎉 Success!

## Common Mistakes to Avoid

❌ **Selecting "Python" instead of "Docker"** → Won't work  
✅ Select "Docker" environment

❌ **Forgetting to add COCALC_API_KEY** → App will crash  
✅ Add it in Environment Variables section

❌ **API key has spaces or quotes** → Will fail  
✅ Copy just the key: `sk_abc123...`

❌ **Committing .env file with real API key** → Security risk  
✅ Only commit .env.example, add real key in Render dashboard

## Verification Steps

After deployment, check:

- [ ] App URL loads the calculator interface
- [ ] Can enter code in the text box
- [ ] "Calculate" button works
- [ ] Results appear below
- [ ] Try a few examples from the README

## If Something Goes Wrong

1. **Check Render Logs**: Dashboard → Logs tab
2. **Verify API Key**: Environment tab → Check `COCALC_API_KEY` is set
3. **Rebuild**: Manual Deploy → "Clear build cache & deploy"

## Environment Settings Summary

| Setting | Value |
|---------|-------|
| Environment | **Docker** |
| Plan | Free |
| Branch | main |
| Docker Command | Auto-detected |
| Health Check Path | /health |

## Your App is Live! 🎉

**Next Steps:**
- Share your calculator URL with friends
- Try more complex calculations
- Customize the UI in `templates/index.html`
- Add more features to `app.py`

**Need Help?**
- Check README.md for full documentation
- Review Render logs for errors
- Verify API key is correct

---

**Total Time: ~5 minutes**  
**Total Cost: $0**  
**Difficulty: Easy** ⭐⭐☆☆☆
