# [Tell Us a Climate Story!](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/tell-us-a-climate-story/?tab=details)

## **About the Challenge**

- **Over the last several decades, a huge amount of climate data from numerous sources has been collected. This data is freely available to the public, but making sense of this vast amount of data is not easy! Your challenge is to use the open-source data on the U.S. Greenhouse Gas Center website to tell a compelling story about climate change.**


<font color='red'>**(Under development)**</font>
# Our Solution 💡

>The **Climate Story Project** is an interactive web application that provides visual data insights on climate change. This project aims to educate and engage users by presenting CO₂ concentration data, climate change impacts, and potential solutions in a clear and accessible way. The platform allows users to explore historical data, understand climate trends, and interact with visual representations of the data through charts and tables.

# Goals 🎯

- **Democratize access to information on climate change through an accessible**, intuitive and visually appealing platform.
- Transform complex data into simple and understandable information, helping to combat **misinformation and fake news**, promoting greater environmental awareness.
- Increase the **autonomy of the population** in understanding the impact of climate change, contributing to collective action.

## Table of Contents 📑

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview 🖥️

Climate change is one of the most pressing issues of our time, and data is a critical tool in understanding its scope. Our project addresses the challenge of communicating complex climate data in an easy-to-understand format for the general public. The **Climate Story Project** focuses on the growing concentration of CO₂ in the atmosphere and its impact on global warming.

By providing real-time data, historical comparisons, and visual charts, we aim to raise awareness and inspire action toward mitigating climate change.

## Features 🪧

- **CO₂ Concentration Data**: Displays CO₂ levels from various years, allowing users to track changes over time.
- **Interactive Charts**: Users can view charts that illustrate emissions data using Chart.js.
- **Climate Impact Section**: Presents information on the impacts of rising CO₂ levels and offers insights into potential solutions.
- **API Integration**: Real-time data retrieval from the back-end to display on the front-end in a user-friendly format.

## Installation ⚙️

To run the Climate Story Project locally, follow these steps:

### Prerequisites 📍

Make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [Git](https://git-scm.com/)

### Steps

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/AngelOttoni/climate-story-project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd climate-story-project
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   flask run
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000` to view the app.

## Usage

Once the application is running, you can explore the following sections:

- **Overview**: Learn about the project and its importance.
- **CO₂ Concentration Data**: See historical CO₂ data displayed in a table format.
- **Interactive Charts**: Visualize emissions data using interactive charts.
- **Climate Impacts**: Learn about the effects of climate change and potential solutions.

The back-end Flask server serves API data to the front-end, which dynamically updates the charts and tables as new data becomes available.

## Project Structure 🗂️

```plaintext
climate-story-website/
│
├── app/                     # Application folder
│   ├── __init__.py           # Initializes Flask app
│   ├── routes.py             # Defines routes and API endpoints
│   └── static/               # Static files (CSS, JavaScript)
│       ├── styles.css        # Styles for the front-end
│       └── scripts.js        # JavaScript logic for data handling
│   └── templates/            # HTML templates
│       └── index.html        # Main webpage template
├── requirements.txt          # List of Python dependencies
├── README.md                 # Project documentation
└── run.py                    # Runs the Flask application
```

## API Endpoints 🔗

The Climate Story Project uses a simple API to deliver CO₂ data to the front-end.

- **`GET /api/co2data`**: Retrieves CO₂ concentration data for the front-end to display.

Example Response:

```json
{
  "data": [
    {"year": 2018, "concentration": 409.8},
    {"year": 2019, "concentration": 410.5},
    {"year": 2020, "concentration": 414.1},
    {"year": 2021, "concentration": 415.7},
    {"year": 2022, "concentration": 420.0}
  ]
}
```

## Technologies Used 🌐

- **Python**: Programming language used for back-end development.
- **Flask**: Micro-framework for web development.
- **JavaScript**: For handling front-end interactivity.
- **Chart.js**: For creating interactive charts to visualize data.
- **HTML/CSS**: For structuring and styling the web pages.

## Contributing 👥

We welcome contributions from the community! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m "Description of feature"`.
4. Push to your branch: `git push origin feature-name`.
5. Submit a pull request for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<font color='#f0962a'>*Thank you for checking out the Climate Story Project! We hope this tool will help raise awareness and inspire action to combat climate change.*</font>

<div align="center">
  <h3 style="color:#349193;">By: Solaris Team 🚀⚝🌍☀️</h3>
</div>

<div align="center">
    <a href="https://www.linkedin.com/in/angelica-lima-75204a224/" target="_blank">👩🏽‍🚀 Angélica Lima</a>&nbsp;&nbsp;
    <a href="https://www.linkedin.com/in/angelina-meiras-ottoni/" target="_blank">👩🏻‍🚀 Angelina Meiras</a>&nbsp;&nbsp;
    <a href="https://www.linkedin.com/in/d%C3%A9bora-campos-34515a1b9/" target="_blank">👩🏽‍🚀 Débora Campos</a>&nbsp;&nbsp;
    <a href="https://www.linkedin.com/in/maryllian-vieira-dev/" target="_blank">👩🏽‍🚀 Maryllian Vieira</a>&nbsp;&nbsp;
    <a href="https://www.linkedin.com/in/nicolydrummond/" target="_blank">👩🏻‍🚀 Nicoly Drummond</a>&nbsp;&nbsp;
    <a href="https://www.linkedin.com/in/patriciaalcantara2/" target="_blank">👩🏽‍🚀 Patrícia Alcântara</a><br><br>  
</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/AngelOttoni/climate-story-project/main/app/static/img/solaris-team.jpeg" alt="Solaris Team" width="300">
</p>
