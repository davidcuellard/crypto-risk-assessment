# Machine Learning Models

## Component Description

This directory contains scripts and resources for training and evaluating the machine learning models used in the cryptocurrency risk assessment.

## Data Preparation

- The models use data from the `/data/processed/` directory.
- Ensure that the dataset is prepared and preprocessed before training.

## Training

### 1. Navigate to the ML Models Directory

```bash
cd ml_models
```

2. Create and Activate a Virtual Environment

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies

```bash
Copy code
pip install -r requirements.txt
```

4. Run the Training Script

```bash
Copy code
python train_model.py
```

- This will train the model and save it as `risk_assessment_model.pkl`.

## Evaluation
- After training, evaluate the model's performance using the provided evaluation scripts.
- Adjust hyperparameters and features as necessary to improve performance.


## Usage
- The trained model file `risk_assessment_model.pkl` is used by the backend API.
- Ensure the model file is moved or copied to the `/backend/` directory after training.

## Notes
- Keep track of model versions and parameters used during training.
- Document any changes or experiments for reproducibility.
