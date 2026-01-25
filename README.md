# Network Security Project

## 📋 Project Overview

A comprehensive machine learning project for detecting phishing websites using network security data. This end-to-end ML pipeline includes data ingestion from MongoDB, data validation, transformation, model training with MLflow tracking, and deployment via FastAPI.

## 🎯 Problem Statement

Phishing attacks are a major cybersecurity threat where attackers create fake websites to steal sensitive information. This project builds a machine learning system to classify URLs as legitimate or phishing based on various features extracted from network traffic and URL characteristics.

## 🏗️ Project Architecture

The project follows a modular architecture with the following components:

```
Network Security Project
│
├── Data Ingestion        → Fetches data from MongoDB
├── Data Validation       → Validates schema and detects data drift
├── Data Transformation   → Preprocesses and transforms features
├── Model Training        → Trains ML models with hyperparameter tuning
└── Deployment            → FastAPI web service for predictions
```

## 🚀 Features

- **Automated ML Pipeline**: End-to-end pipeline from data ingestion to model deployment
- **MongoDB Integration**: Seamless data fetching from cloud database
- **Data Drift Detection**: Monitors data quality and distribution changes
- **MLflow Tracking**: Experiment tracking and model versioning with DagsHub integration
- **Multiple ML Models**: Supports various classifiers (Random Forest, Gradient Boosting, AdaBoost, Decision Tree, Logistic Regression)
- **RESTful API**: FastAPI-based web service for real-time predictions
- **Modular Codebase**: Clean, maintainable code following software engineering best practices

## 📊 Dataset

**Dataset Name**: Phishing Data (`phisingData.csv`)

**Features**: 31 features including:

- URL characteristics (IP Address, URL Length, Shortening Service)
- Security indicators (SSL State, HTTPS Token, DNS Record)
- Content features (Links in tags, Pop-up Window, IFrame)
- Domain features (Age of Domain, Domain Registration Length)
- Web traffic metrics (Page Rank, Google Index, Web Traffic)

**Target Variable**: `Result` (1 = Legitimate, -1 = Phishing)

## 🛠️ Tech Stack

### Core Technologies

- **Python 3.x**: Primary programming language
- **MongoDB**: Database for storing phishing data
- **FastAPI**: Web framework for API development
- **MLflow**: Experiment tracking and model registry
- **DagsHub**: MLOps platform for tracking experiments

### Machine Learning Libraries

- **scikit-learn**: ML algorithms and preprocessing
- **pandas**: Data manipulation
- **numpy**: Numerical computations
- **PyYAML**: Configuration management
- **dill**: Advanced object serialization

### Deployment & DevOps

- **Docker**: Containerization (configured)
- **Uvicorn**: ASGI server for FastAPI
- **python-dotenv**: Environment variable management

## 📁 Project Structure

```
Network Security Project/
│
├── networksecurity/              # Main package
│   ├── components/               # Pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/                 # Training pipeline
│   │   └── training_pipeline.py
│   ├── entity/                   # Data classes
│   │   ├── config_entity.py
│   │   └── artifact_entity.py
│   ├── constant/                 # Constants and configs
│   ├── exception/                # Custom exceptions
│   ├── logging/                  # Logging utilities
│   ├── utils/                    # Utility functions
│   │   ├── main_utils/
│   │   └── ml_utils/
│   └── cloud/                    # Cloud storage utilities
│
├── Artifacts/                    # Training artifacts (timestamped)
├── data_schema/                  # Data schema definitions
│   └── schema.yaml
├── final_model/                  # Production model
├── mlruns/                       # MLflow tracking
├── templates/                    # HTML templates
├── prediction_output/            # Prediction results
│
├── app.py                        # FastAPI application
├── main.py                       # Pipeline execution script
├── push_data.py                  # MongoDB data upload
├── requirements.txt              # Dependencies
├── setup.py                      # Package setup
├── Dockerfile                    # Docker configuration
└── README.md                     # This file
```

## 🔧 Installation

### Prerequisites

- Python 3.8+
- MongoDB Atlas account (or local MongoDB)
- Git

### Setup Steps

1. **Clone the repository**

```bash
git clone <repository-url>
cd "Network Security Project"
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the project root:

```env
MONGODB_URL_KEY=your_mongodb_connection_string
MONGO_DB_URL=your_mongodb_connection_string
```

5. **Install package in development mode**

```bash
pip install -e .
```

## 💻 Usage

### 1. Push Data to MongoDB (First Time Setup)

```bash
python push_data.py
```

### 2. Train the Model

```bash
python main.py
```

Or use the training pipeline:

```python
from networksecurity.pipeline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run_pipeline()
```

### 3. Run the FastAPI Application

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### 4. Access the API

- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### 5. Make Predictions

**Using the Web Interface**:

1. Navigate to http://localhost:8000/docs
2. Use the `/predict` endpoint
3. Upload a CSV file with the same features as training data
4. Get predictions in HTML table format

**Using cURL**:

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test.csv"
```

## 🔬 ML Pipeline Details

### 1. Data Ingestion

- Connects to MongoDB Atlas
- Exports data as Pandas DataFrame
- Splits data into train/test sets (80:20)
- Stores in feature store

### 2. Data Validation

- Validates schema against `schema.yaml`
- Checks column names and data types
- Detects data drift using statistical tests
- Generates drift reports

### 3. Data Transformation

- Handles missing values
- Feature engineering
- Applies preprocessing pipelines
- Saves preprocessor object

### 4. Model Training

- **Models Evaluated**:
  - Random Forest Classifier
  - Gradient Boosting Classifier
  - AdaBoost Classifier
  - Decision Tree Classifier
  - Logistic Regression

- **Evaluation Metrics**:
  - F1 Score
  - Precision
  - Recall

- **MLflow Integration**:
  - Logs parameters, metrics, and models
  - Tracks experiments in DagsHub
  - Model versioning and registry

### 5. Model Selection

- Selects best model based on F1 score
- Saves final model to `final_model/`
- Implements custom `NetworkModel` wrapper

## 📈 MLflow Tracking

The project uses MLflow with DagsHub for experiment tracking:

- **Repository**: https://dagshub.com/raunaqmittal/network-security
- **Tracked Metrics**: F1 Score, Precision, Recall
- **Tracked Parameters**: Model hyperparameters
- **Artifacts**: Trained models, preprocessors

## 🌐 API Endpoints

### GET `/`

- Redirects to API documentation

### GET `/train`

- Triggers the complete training pipeline
- Returns: Training status message

### POST `/predict`

- **Input**: CSV file with features
- **Output**: HTML table with predictions
- Saves predictions to `prediction_output/output.csv`

## 🔐 Security & Best Practices

- Environment variables for sensitive data
- Custom exception handling
- Comprehensive logging system
- Modular and testable code structure
- Type hints for better code quality

## 📝 Configuration

### Schema Configuration (`data_schema/schema.yaml`)

Defines:

- Column names and data types
- Numerical columns
- Feature validation rules

### Training Pipeline Constants

Located in `networksecurity/constant/training_pipeline/__init__.py`:

- Pipeline names and directories
- Train/test split ratios
- File naming conventions

## 🐛 Error Handling

The project implements custom exception handling:

```python
from networksecurity.exception.exception import NetworkSecurityException
```

All exceptions are logged with detailed traceback information.

## 📊 Logging

Comprehensive logging system located in `networksecurity/logging/`:

- Logs stored in `networksecurity/logs/`
- Timestamped log files
- Multiple log levels (INFO, DEBUG, ERROR)

## 🚢 Deployment

### Docker Deployment (To be configured)

```bash
docker build -t network-security .
docker run -p 8000:8000 network-security
```

### Cloud Deployment Options

- AWS EC2 / ECS
- Google Cloud Run
- Azure Container Instances
- Heroku

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Author

**Raunaq Mittal**

- Email: raunaqmittal2004@gmail.com
- GitHub: [@raunaqmittal](https://github.com/raunaqmittal)

## 🙏 Acknowledgments

- Course: Udemy - Krish Naik's ML Project Series
- Dataset: Phishing Website Detection Dataset
- MLOps Platform: DagsHub

## 📞 Support

For issues or questions:

1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Contact via email

---

**Project Status**: ✅ Active Development

**Last Updated**: January 2026
