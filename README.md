# WatchPost
WatchPost is a LinkedIn post automation tool that leverages GitHub repository activity to generate daily content updates. It uses GitHub Actions to fetch the git diff of specified repositories, comparing the current state to that of 24 hours ago. This diff is then used as a prompt for GPT (Generative Pre-trained Transformer) to create engaging LinkedIn posts about the project's progress.

## Features
- **Automated Post Creation**: Utilizes OpenAI's GPT to generate LinkedIn posts based on recent changes in your GitHub repositories.
- **GitHub Integration**: Tracks changes across multiple repositories using GitHub Actions.
- **Customizable Templates**: Comes with predefined templates in config.py for the first post and subsequent updates, which you can customize as needed.
