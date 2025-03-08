# Flask Travel Website (FTW)

## Overview
This project is an educational website built using the **Flask framework**, designed to simulate a travel company's platform. The site provides various functionalities to assist users in planning their trips, including tour search, AI-based travel recommendations, currency exchange rates, and contact information. The website is fully responsive and optimized for mobile and tablet devices, utilizing the **Bootstrap framework** for styling and layout.

Below is a video demonstration showcasing the functionality and design of the site:

[**Video Demonstration**](https://github.com/samedimanche/FlaskSiteFTW/assets/152053503/37c2b054-3a3e-44bf-95d3-c432da172a68)

---

## Features

### 1. **Main Page**
   - Serves as the homepage with navigation links to other sections of the website.

### 2. **Tour Search**
   - Allows users to search for tours based on the following parameters:
     - Price range (from and to).
     - Preferred departure city.
     - Resort country.
     - Preferred departure date.
   - Displays the top 3 results from the **Tour API**, including:
     - Hotel name.
     - Link to hotel descriptions.
     - City of the selected resort.
     - Price range.
     - Tour dates.

### 3. **Where to Go (AI-Based Recommendations)**
   - Utilizes the **Pandas library** (Python) to analyze user preferences and provide travel recommendations.
   - Users input:
     - Budget for travel.
     - Departure city.
     - Age.
     - Type of vacation.
     - Preferred transport.
     - Number of fellow travelers.
   - The system suggests a city based on a database of previous travelers' experiences.
   - The city name is clickable and redirects to a Google search for more information.

### 4. **Exchange Rate**
   - Displays the exchange rates for **9 major currencies**.
   - Includes a currency converter that allows users to:
     - Convert rubles to a selected currency.
     - Convert a selected currency to rubles.
   - Rates are based on the **Central Bank of the Russian Federation**.

### 5. **Contacts**
   - Provides the address and contact details of the travel company that owns the website.

---

## Technologies Used
- **Backend**: Python (Flask framework).
- **Frontend**: HTML, CSS, JavaScript, Bootstrap.
- **Data Analysis**: Pandas library (Python).
- **API Integration**: Tour API for tour search functionality.
- **Currency Data**: Central Bank of the Russian Federation exchange rates.
- **Responsive Design**: Bootstrap framework for mobile and tablet compatibility.

---

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- Pandas (for AI-based recommendations)

### Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/samedimanche/FlaskSiteFTW.git
   cd FlaskSiteFTW
   ```

2. **Set Up the Environment**:
   - Install the required dependencies:
     ```bash
     pip install flask pandas
     ```

3. **Run the Application**:
   - **Using an IDE**:
     Run the `python app.py` command directly from your IDE.
   - **Using Command Line or Terminal**:
     ```bash
     set FLASK_APP=app.py
     flask run --host=0.0.0.0
     ```

4. **Access the Website**:
   Open your browser and navigate to `http://localhost:5000` to view the website.

---

## Usage
The website is designed to assist users in planning their travels by providing tools for tour search, destination recommendations, and currency conversion. It is intuitive and user-friendly, with a responsive design that ensures a seamless experience across devices.

---

## Acknowledgments
- **Flask** community for backend support.
- **Bootstrap** for responsive design.
- **Pandas** for data analysis and AI-based recommendations.
- **Tour API** for tour search functionality.
- **Central Bank of the Russian Federation** for currency exchange rates.

---

For more details, visit the [GitHub repository](https://github.com/samedimanche/FlaskSiteFTW).
