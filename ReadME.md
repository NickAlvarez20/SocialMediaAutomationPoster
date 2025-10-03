# Social Media Automation Poster Project
## Table of Contents
- [Project Name](#project-name)
- [About](#about)
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Getting Started & Installation](#getting-started--installation)
- [Usage](#usage)
- [Learning Outcomes](#learning-outcomes)
- [Contributing](#contributing)
- [License](#license)
- [Credits & Acknowledgements](#credits--acknowledgements)
- [Contact](#contact)
## Project Name
Social Media Automation Poster
## About
Social Media Automation Poster is a Python-based tool designed to automate posting on the X platform, enabling users to maintain a consistent social media presence without manual intervention. The project allows users to schedule posts or post immediately using a JSON-based content database organized by categories (e.g., cooking, travel, photography, gardening, music). This automation helps busy individuals stay in a focused "flow state" by reducing the need for manual social media management. The repository includes the core automation script (autopost.py) and a sample content.json file. 
## Prerequisites
To run this project, you need Python 3 installed on your system.

Additional libraries are required:

-tweepy for interacting with the X API

-python-dotenv for loading environment variables

-schedule for scheduling posts Install these dependencies using:

`pip install tweepy python-dotenv schedule`

-You also need a valid .env file in the project root with your X API credentials (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET).


## Features
This Social Media Automation Poster includes these features:

-Automates posting to the X platform using the tweepy library.

-Supports immediate posting from a specified category or random selection within a category.

-Enables scheduled posting at user-defined times (default: 09:00, 12:00, 15:00, 18:00).

-Uses a JSON-based content database to organize posts by categories like cooking, travel, photography, gardening, and music.

-Includes a dry-run mode to simulate posts without publishing.

Rotates through categories for scheduled posts to ensure variety.
## Getting Started & Installation

Clone the repository to your local machine:
`git clone https://github.com/NickAlvarez20/SocialMediaAutomationPoster.git`

Install the required Python libraries:
`pip install tweepy python-dotenv schedule`

Create a .env file in the project root with your X API credentials:

-CONSUMER_KEY=your_consumer_key:

-CONSUMER_SECRET=your_consumer_secret:

-ACCESS_TOKEN=your_access_token:

-ACCESS_TOKEN_SECRET=your_access_token_secret:

Ensure a content.json file exists with your post content, following the structure in the provided sample.

## Usage
Run the Python script (autopost.py) from the command line with one of the following modes:

-Immediate Posting: Post a specific or random post from a category.
`python autopost.py --category cooking`

-Use --index to select a specific post or --dry-run to simulate without posting:
`python autopost.py --category cooking --index 0 --dry-run`

-Scheduled Posting: Run posts on a schedule with default or custom times.
`python autopost.py --run-schedule`

-Customize posting times:
`python autopost.py --run-schedule --schedule-times "08:00,12:30,17:00"`

-Ensure content.json is updated with your desired posts and categories.

## Learning Outcomes
This project helped me:

-Learn Python scripting for automation, including argparse for command-line interfaces and schedule for timed tasks.

-Integrate with external APIs, specifically the X API via tweepy, handling authentication and error cases.

-Work with JSON files for structured data storage and retrieval in a content database.

-Implement robust error handling and user feedback for file and input validation.

-Understand environment variable management using python-dotenv for secure API credential storage.

## Contributing
This is primarily a personal learning / portfolio repository, so formal contributions aren’t required. However, if you spot bugs, have project ideas, or want to add improvements, feel free to:
1. Fork the repo
2. Create a feature branch
3. Submit a pull request Please include clear explanations of your changes and test any new code.
## License
This repository is open and free for educational use.
*(If you decide on a specific license later, insert it here — e.g. MIT, Apache 2.0, etc.)*
## Credits & Acknowledgements
This project was created by NickAlvarez20 as part of my journey to learn Python programming. Check out my other repositories to see more of my work!
## Contact
You can find more of my work at [NickAlvarez20 on GitHub](https://github.com/NickAlvarez20).
