# Project Name

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

A Telegram bot generating image

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

Step 1: Clone the Repository
    First, clone the repository to your local machine using Git:

    git clone https://github.com/piumalSahashraka/freepik-image-generation-telegram-bot.git
    cd freepik-image-generation-telegram-bot

Step 2: Set Up a Virtual Environment (Optional but Recommended)
    It's a good practice to use a virtual environment to manage your project's dependencies:


    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Step 3: Install Dependencies
    With the virtual environment activated, install the required Python packages:

    pip install -r requirements.txt

Step 4: Configure Environment Variables
    Create a .env file in the root directory of the project to store environment variables like your Telegram bot token and API keys:


    touch .env
    Add the necessary variables to the .env file:

    TOKEN=your_bot_token #Get it by contacting to BotFather
    FREEPIK_API_KEY=your_freepik_api_id #Get it by creating api_id on https://www.freepik.com/api

Step 5: Run the Bot
    After setting up the environment, you can start the bot:

    python main.py

## Usage

To start the bot, use the command /start.

## Features

Support for various image styles.
Utilizes asynchronous programming for efficient performance.

## TO DO

Handle more exceptions.
Add image size
Add image colors

## Contributing

We welcome contributions to this project! Whether you're fixing a bug, adding a new feature, or improving documentation, your help is appreciated.

## Getting Help

If you have any questions or need assistance, feel free to open an issue or reach out to the maintainers.

## License

Copyright (c) 2024 Piumal Gunarathne
This project is licensed under the [MIT License](LICENSE).
