[Leggi in Italiano](README.it.md)

# Credit Card Approval Prediction System

This project implements a machine learning system to predict the approval of credit card applications. The application uses a neural network built with TensorFlow and Keras, is written in Python with an Object-Oriented Programming (OOP) approach, and can be run both locally and through a Docker container.

## Table of Contents

- [Project Goal](#project-goal)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Execution Guide](#setup-and-execution-guide)
  - [Prerequisites](#prerequisites)
  - [Option 1: Run with Docker (Recommended)](#option-1-run-with-docker-recommended)
  - [Option 2: Run Locally](#option-2-run-locally)
- [Implementation Details](#implementation-details)
  - [Dataset](#dataset)
  - [Data Preprocessing](#data-preprocessing)
  - [Neural Network Model](#neural-network-model)
- [Author](#author)

## Project Goal

Banks receive numerous credit card applications, and他们的 manual evaluation is a slow and error-prone process. This project automates the approval process by building a predictive model that analyzes applicant data to determine the likelihood of approval.

## Technologies Used

- **Language**: Python 3.11
- **Machine Learning**: TensorFlow, Keras
- **Data Manipulation**: Pandas, NumPy
- **Preprocessing**: Scikit-learn
- **Containerization**: Docker

## Project Structure

```
credit-approval-system/
├── .venv/                # Local virtual environment (ignored by Git and Docker)
├── app.py                # Main script with the application logic
├── crx.data              # The raw dataset
├── requirements.txt      # List of Python dependencies
├── Dockerfile            # Instructions to build the Docker image
├── .dockerignore         # Files and folders to exclude from the Docker build
└── README.md             # This file (English)
└── README.it.md          # Italian version of the README
```

## Setup and Execution Guide

### Prerequisites

- [Git](https://git-scm.com/)
- [Python 3.11](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (for the Docker option)

### Option 1: Run with Docker (Recommended)

This is the easiest and fastest way to run the application, as it does not require any manual setup of the Python environment.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/aciluca/credit-approval-system.git
    cd credit-approval-system
    ```

2.  **Build the Docker image:**
    The `docker build` command reads the `Dockerfile` and creates an image containing the application and all its dependencies.
    ```bash
    docker build -t credit-approver-app .
    ```

3.  **Run the container:**
    Launch the application inside the container. The `--rm` flag ensures the container is removed after execution.
    ```bash
    docker run --rm credit-approver-app
    ```
    You will see the output of the training and evaluation process printed directly to your terminal.

### Option 2: Run Locally

Follow these steps to set up the environment and run the script on your computer.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/aciluca/credit-approval-system.git
    cd credit-approval-system
    ```

2.  **Download the dataset:**
    The original dataset comes from the UCI Machine Learning Repository. You can download it with `curl` (on macOS/Linux) or `wget`.
    ```bash
    # On Linux/macOS
    curl -o crx.data http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data

    # On Windows (using PowerShell)
    Invoke-WebRequest -Uri http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data -OutFile crx.data
    ```

3.  **Create and activate a virtual environment:**
    It's a best practice to isolate project dependencies.
    ```bash
    # Create the virtual environment
    python -m venv .venv

    # Activate the environment
    # On Windows
    .\.venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate
    ```

4.  **Install dependencies:**
    The `requirements.txt` file contains all the necessary libraries.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Python script:**
    Now that the environment is set up, you can launch the application.
    ```bash
    python app.py
    ```

## Implementation Details

### Dataset

The project uses the [Credit Approval Data Set](http://archive.ics.uci.edu/ml/datasets/Credit+Approval) from the UCI Repository. To protect privacy, feature names and values have been anonymized.

### Data Preprocessing

The `app.py` script performs the following preprocessing steps:
1.  **Handling Missing Values**: Missing values (indicated by `?`) are imputed using the mean for numerical columns and the mode for categorical ones.
2.  **Encoding Categorical Variables**: Categorical features are converted to numerical ones using One-Hot Encoding.
3.  **Scaling**: All features are standardized (mean 0, variance 1) using `StandardScaler` to optimize model performance.

### Neural Network Model

A sequential neural network was implemented with Keras, consisting of:
-   An input layer
-   Two hidden layers (`Dense`) with `ReLU` activation.
-   An output layer with `Sigmoid` activation, ideal for binary classification problems.

The model is compiled with the `Adam` optimizer and the `binary_crossentropy` loss function.

## Author

- **Luca Acerbi** - [aciluca](https://github.com/aciluca)
