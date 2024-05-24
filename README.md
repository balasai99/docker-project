# docker-project
A Docker container to generate periodic reports of the top 10 downloaded models from Hugging Face Model Hub.

# Hugging Face Model Hub Report Generator

This project provides a Docker container that periodically generates reports by fetching data from the Hugging Face Model Hub and compiling a list of the top 10 downloaded models.

## Features

- Periodically generates reports from Hugging Face Model Hub data.
- Compiles a list of the top 10 downloaded models.
- Easy setup and usage with Docker.

## Usage

### Prerequisites

- Docker installed on your linux system.

### Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/balasai99/docker-project.git

2. Navigate to the project directory:

   '''bash
   cd docker-project.git

3. Build the Docker image:

   '''bash
   docker build -t docker-project .

5. Run the Docker container:

   '''bash
   docker run --rm -v /path/to/reports:/reports docker-project

   This command runs the container, which executes the Python script, generates the report, saves it in the reports directory on your host machine, and then stops.

   Replace /path/to/reports with the path on your host machine where you want the report to be saved.


### Scheduling with Cron

To schedule the container to run periodically, use cron

1. Edit your crontab:

   '''bash
   crontab -e

2. Add a cron job to run the Docker container periodically:

   '''bash
   0 0 * * * docker run --rm -v /path/to/reports:/reports docker-project

   Replace /path/to/reports with the actual path where you want the reports to be saved.

### Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or features you'd like to see.

   



  

   

