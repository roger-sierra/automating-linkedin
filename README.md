# Automating LinkedIn

This Python project automates the process of logging into LinkedIn, searching for Python developer jobs, and saving jobs and following companies using Selenium.

## Features

- Logs into LinkedIn using provided credentials.
- Searches for Python developer jobs in Poland using the URL provided.
- Iterates through each job listing, saves the job, and follows the company.

## Installation

### Prerequisites

- Python 3.x
- [Google Chrome](https://www.google.com/chrome/)
- [Selenium](https://selenium.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/linkedin-job-saver-bot.git
   cd linkedin-job-saver-bot

2. **Install the required Python packages:**

   ```bash
   pip install selenium python-dotenv

3. **Set up environment variables:**

   Create a .env file in the project root directory and add your LinkedIn credentials:

   ```bash
   LINKEDIN_USERNAME=your_linkedin_username
   LINKEDIN_PASSWORD=your_linkedin_password

### Usage

1. ***Run the script**

   ```bash
   python automating_linkedin.py
