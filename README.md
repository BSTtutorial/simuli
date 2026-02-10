# SageMath Web Calculator

A web-based calculator powered by SageMath that can perform complex mathematical computations including calculus, algebra, linear algebra, and more.

## Features

- 🔢 Symbolic mathematics (calculus, algebra, number theory)
- 📊 Matrix operations
- 🎯 Equation solving
- 📈 Limits and derivatives
- ∫ Integration
- 🌐 Clean, modern web interface
- 🚀 Easy to deploy on Render

## Local Development

### Prerequisites

- Docker (recommended) OR
- SageMath installed locally
- Python 3.8+

### Running with Docker (Recommended)

```bash
docker build -t sagemath-webapp .
docker run -p 10000:10000 sagemath-webapp
```

Then open http://localhost:10000 in your browser.

### Running without Docker

If you have SageMath installed:

```bash
pip install Flask gunicorn
python app.py
```

## Deploying to Render

### Method 1: Using the Render Dashboard (Easiest)

1. Create a GitHub repository and push all these files to it
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Render will automatically detect the `render.yaml` file
6. Click "Apply" to deploy

### Method 2: Manual Setup

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: sagemath-calculator (or your preferred name)
   - **Environment**: Docker
   - **Region**: Choose your preferred region
   - **Branch**: main (or your default branch)
   - **Dockerfile Path**: ./Dockerfile
5. Click "Create Web Service"

### Method 3: Using Render Blueprint

If you have the `render.yaml` file in your repo:

```bash
# Push your code to GitHub first, then:
# Render will automatically detect and use the render.yaml configuration
```

## Configuration

The application uses the following environment variables:

- `PORT`: The port the application runs on (default: 10000)

These are automatically configured in the `render.yaml` file.

## Project Structure

```
sagemath-webapp/
├── app.py                  # Flask application backend
├── templates/
│   └── index.html         # Frontend interface
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── render.yaml           # Render deployment configuration
└── README.md             # This file
```

## Usage Examples

Once deployed, you can use the calculator with SageMath syntax:

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

## Troubleshooting

### Build takes too long on Render

The SageMath Docker image is large (~4GB). The first build may take 10-15 minutes. Subsequent builds will be faster due to caching.

### Application times out

For complex calculations, you may need to increase the timeout. This is already set to 120 seconds in the Dockerfile's gunicorn command.

### Memory issues

SageMath requires significant memory. On Render's free tier, you get 512MB RAM. For complex calculations, you may need to upgrade to a paid plan.

## Cost

- **Render Free Tier**: Good for testing and light use
  - 512 MB RAM
  - 0.1 CPU
  - Apps sleep after 15 minutes of inactivity
  
- **Render Starter ($7/month)**: Better for regular use
  - 512 MB RAM
  - 0.5 CPU
  - No sleep

## License

MIT License - Feel free to use and modify as needed.

## Support

For issues with:
- SageMath syntax: See [SageMath Documentation](https://doc.sagemath.org/)
- Deployment: Check [Render Documentation](https://render.com/docs)
- This app: Open an issue in your repository

## Notes

- The app uses Flask for the web framework
- Gunicorn serves the application in production
- SageMath provides all mathematical computation capabilities
- The Docker approach ensures consistent environment across local and production
