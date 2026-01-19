# House Price Prediction Project

This project is a **full-stack Machine Learning application** that predicts housing prices based on California housing data. It consists of a **FastAPI backend API** and a **Streamlit frontend UI**, both Dockerized for easy deployment.

---

## **📁 Project Structure**

ML_Project/
│
├── app/                   # FastAPI ML API
│   ├── main.py            # FastAPI routes
│   ├── model.py           # ML model + preprocessing
│   └── schema.py          # Pydantic request/response schemas
│
├── ui/                    # Streamlit UI
│   └── ui_app.py          # User interface
│
├── model.pkl              # Trained ML pipeline (preprocessing + model)
├── requirements.txt       # Python dependencies for API + UI
├── Dockerfile             # Dockerfile for FastAPI API
├── Dockerfile.ui          # Dockerfile for Streamlit UI
├── docker-compose.yml     # Optional: run API + UI together locally
└── README.md              # Project description & instructions

---

## **🚀 Features**

- Predict house prices using an **XGBoost + preprocessing pipeline**  
- FastAPI backend with `/predict` endpoint  
- Streamlit UI for interactive input  
- Dockerized for **consistent local and cloud deployment**  
- Ready to deploy on **Render, AWS, or other cloud services**  

---

## **🛠 Installation & Setup**

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd ML_Project
2️⃣ Create virtual environment & install dependencies
bash
Copy code
python -m venv .venv
source .venv/Scripts/activate     # Windows
pip install --upgrade pip
pip install -r requirements.txt
3️⃣ Run FastAPI API locally
bash
Copy code
uvicorn app.main:app --reload
API will run on http://localhost:8000

Test endpoint /predict using Postman or Python requests.

4️⃣ Run Streamlit UI locally
bash
Copy code
streamlit run ui/ui_app.py
UI will run on http://localhost:8501

Make sure the API is running, otherwise prediction will fail.

🐳 Docker Instructions
1️⃣ Build Docker images
bash
Copy code
docker build -t ml-api:latest -f Dockerfile .
docker build -t ml-ui:latest -f Dockerfile.ui .
2️⃣ Run locally using Docker Compose (optional)
bash
Copy code
docker-compose up --build
API → http://localhost:8000/predict

Streamlit UI → http://localhost:8501

3️⃣ Push images to Docker Hub
bash
Copy code
docker tag ml-api:latest iamchandannnn/ml-api:latest
docker push iamchandannnn/ml-api:latest

docker tag ml-ui:latest iamchandannnn/ml-ui:latest
docker push iamchandannnn/ml-ui:latest
☁️ Deployment on Render
API Service: Create new Web Service on Render → choose Docker → use iamchandannnn/ml-api:latest

UI Service: Create new Web Service on Render → choose Docker → use iamchandannnn/ml-ui:latest

Update API_URL in Streamlit to the public URL of your deployed API:

python
Copy code
API_URL = "https://<your-api-service>.onrender.com/predict"
Deploy UI → your app is now live online.

💡 Notes
The ML model is saved as a pipeline (preprocessing + XGBoost) in model.pkl.

Optional inputs (e.g., latitude/longitude) can be skipped in the UI.

Docker ensures consistency across environments.

Can be extended to version models, add authentication, or use cloud storage.

👨‍💻 Technologies Used
Python 3.11

FastAPI → Backend API

Streamlit → Frontend UI

XGBoost / Scikit-learn / Pandas → ML model & preprocessing

Docker → Containerization

Render.com → Cloud deployment