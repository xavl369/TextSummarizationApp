# Automatic Text Summarization Project

This project combines Angular for the frontend and Python Flask for the backend to perform automatic text summarization.

## Features

- **Frontend (Angular version 17.2):**
  - Allows users to input text and choose a summarization method.
  - Provides a user-friendly interface to summarize text.
  - Displays both the original and summarized text.
  
- **Backend (Python version 3.9.18) (Flask version 3.0.2):**
  - Receives text input and summarization method selection from the frontend.
  - Performs text summarization using various algorithms.
  - Returns the summarized text to the frontend for display.

## Supported Summarization Methods

The following summarization methods are supported in this project:

- **Bert**
- **Frequency Based**
- **Cosine Similarity**
- **GPT (Generative Pre-trained Transformer)**
- **LSTM (Long Short-Term Memory)**
- **Luhn**
- **Edmundson**
- **KL-Sum**
- **LexRank**
- **LSA (Latent Semantic Analysis)**
- **Sumy Luhn**


## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies for both the frontend and backend.
4. Run the backend server using Python Flask.
5. Run the Angular development server for the frontend.
6. Access the application through your web browser.

## Installation

### Backend Setup (Python Flask)

1. Ensure you have Python installed on your system.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

Or

1. Ensure you have Anaconda installed on your system.
2. Create an environment from an environment.yml file

```bash
conda env create -f environment.yml
```

3. Set the environment variable `SUMMARIZATION_API_KEY` with the APIKey Value for the app security.
4. Set the environment variable `OPENAI_API_KEY` obtained from OpenAI API subscription. 

### Frontend Setup (Angular)

1. Make sure you have Node.js and npm installed on your system.
2. Install Angular CLI globally:

```bash
npm install -g @angular/cli
```

3. Install the required dependencies:

```bash
npm install
```

## Running the Application

### Backend (Python Flask)

If using anaconda activate environment first with the command:

```bash
conda activate text-summarization
```

Run the following command to start the Flask server from the working directory:

```bash
python app.py
```

### Frontend (Angular)

Run the following command to start the Angular development server:

```bash
ng serve
```


## Images

Sample images related to the project:

![image](https://github.com/xavl369/TextSummarizationApp/assets/31866236/94e2028b-d783-44ca-840c-f0c60adaa020)

![image](https://github.com/xavl369/TextSummarizationApp/assets/31866236/1bd1e81b-6aa4-49a1-ba1f-e4e3a5d9f205)



## Contributors
- Abraham Saul Sandoval Meneses
