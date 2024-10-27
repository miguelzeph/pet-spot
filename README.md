# Pet-Spot: Animal Classification with Machine Learning

**Pet-Spot** is a web application designed to classify animals using a pre-trained machine learning model. Users can upload an image of their pet, and the application predicts the type of animal using probability scores. This project integrates several tools and technologies, including Flask, Chart.js, and a TensorFlow model.

## Overview
Pet-Spot leverages a pre-trained TensorFlow model to identify different types of animals from an uploaded image. The application:
- Accepts an image file from the user.
- Passes the image to the backend for classification.
- Displays the predicted probabilities of each animal class in an interactive bar chart created with Chart.js.


## Technologies Used

### Flask
- **Flask** is a Python web framework used to build the backend server of Pet-Spot. It handles routing, file uploads, and model inference requests.
  
### TensorFlow
- **TensorFlow** powers the pre-trained model that classifies animal images. This model is loaded on the Flask server and used to process uploaded images, returning probabilities for each possible animal class.

### Chart.js
- **Chart.js** is a JavaScript library used to create dynamic and interactive charts on the frontend. In this project, it generates a bar chart displaying the probability scores for each animal category.


## Project Setup
This project runs on **Python 3.7**. You can use [pyenv](https://github.com/pyenv/pyenv) to manage multiple Python versions and switch between them. For more details, see the [official pyenv documentation](https://github.com/pyenv/pyenv#installation).


### Prerequisites
- Python 3.7+
- Flask
- TensorFlow
- JavaScript (for Chart.js integration)


1. **Create a Virtual Environment**

   Use `virtualenv` to create a virtual environment with Python 3.7:

   ```bash
   virtualenv --python=/path/to/your/python3.7 <your_env_name>

Replace /path/to/your/python3.7 with the path to your Python 3.7 executable, and <your_env_name> with a name for your environment.

2. Activate the Virtual Environment

Activate your virtual environment using:

```bash
source your_env_name/bin/activate
```

3. Install the rest of dependencies:

```bash
pip install -r requirements.txt
```


## How to Execute


1. Move to folder src
```bash
cd src
```
2. Export **Config.yml**
```bash
export KLEIN_CONFIG=config_example.yml
```

3. Execute Flask
```bash
flask --app main.py run
```

4. Access the Application

- Navigate to **http://localhost:5000** in your web browser.