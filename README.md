# Simple End-To-End Machine Learning Project on TelCo Churn Dataset using Random Forest Classification Model

The End-to-End Machine Learning Project was made for the reason of expanding my knowledge regarding Machine Learning and it's full process in real life work scenario. I was inspired to do this project after my mentor asked 'Do you know End-to-End Machine Learning preprocessing', I didn't know anything regarding that topic that time and i decide to learn about it and do a project about it.

## Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

Clone this repository by using this command on your Terminal

```bash
git clone https://github.com/VinV7/End-To-End-Machine-Learning-Project.git
```

Afterwards to install the required packages, you first need to create a Virtual Environment inside the cloned folder with this command inside your terminal

Windows
```bash
python -m venv YOUR_VENV_NAME
YOUR_VENV_NAME\Scripts\activate
```

Linux & MacOS
```bash
python3 -m venv YOUR_VENV_NAME
source YOUR_VENV_NAME/bin/activate
```

After creating a Virtual Environment, proceed to the requirement packages installation using the setup.py by inputing this command inside the terminal.

```bash
python setup.py install # Use Python3 if your system doesn't recognise regular Python
```

## Usage

In order to be able to use and experiment predicting whether the customer will churn or not, first change to the app directory and proceed to start the api.py manually or by using this command

```bash
cd app # If you're already on the end-to-end machine learning project directory
python api.py
```

Afterwards do a POST request on [Postman](https://www.postman.com) then use http://127.0.0.1:5000/predict as the address and input your data in Json Format, if you find any other method feel free to do it. But for this, I'll use [Postman API Platform](https://www.postman.com). 

```bash
# Json Data Format (Example)

{
    "Age": [25],
    "Number of Dependents": [1],
    "Zip Code": [12345],
    "Number of Referrals": [2],
    "Tenure in Months": [12],
    "Avg Monthly Long Distance Charges": [15.0],
    "Avg Monthly GB Download": [45.0],
    "Monthly Charge": [70.0],
    "Total Charges": [840.0],
    "Total Refunds": [0.0],
    "Total Extra Data Charges": [0.0],
    "Total Long Distance Charges": [180.0],
    "Total Revenue": [1020.0],
    "Satisfaction Score": [4],
    "Churn Score": [50],
    "CLTV": [1500],
    "Gender": ["Male"],
    "Under 30": ["Yes"],
    "Senior Citizen": ["No"],
    "Married": ["Yes"],
    "Dependents": ["No"],
    "City": ["Springfield"],
    "Phone Service": ["Yes"],
    "Multiple Lines": ["No"],
    "Internet Service": ["DSL"],
    "Online Security": ["Yes"],
    "Online Backup": ["No"],
    "Device Protection Plan": ["Yes"],
    "Premium Tech Support": ["No"],
    "Streaming TV": ["No"],
    "Streaming Movies": ["Yes"],
    "Streaming Music": ["No"],
    "Unlimited Data": ["Yes"],
    "Contract": ["Month-to-Month"]
}
```

If you have successfuly do the post request, the end result generated in the Postman API Platform would look like this 

```bash
{
    "prediction": [
        "No"
    ]
}
```

## Contributing

Pull requests are welcome. For major changes and improvements

## References 

### External Libraries

- [Pandas](https://pandas.pydata.org/): Used for data manipulation and analysis.
- [NumPy](https://numpy.org/): Fundamental package for scientific computing with Python.
- [Matplotlib](https://matplotlib.org/): Plotting library for creating visualizations in Python.
- [Scikit-learn](https://scikit-learn.org/): Machine learning library for Python.

### Online Resources

- [ChatGPT](https://chatgpt.com): Helping as a guide in this project.
- [StackOverFlow](https://stackoverflow.com): As a guide in solving problems in this project.

