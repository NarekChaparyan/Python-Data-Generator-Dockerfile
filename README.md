# Random Data Generator

This project generates a CSV file with random data using Python and Docker. The data includes ID, Name, Age, and Salary columns. The project is containerized with Docker, making it easy to run anywhere.

## Features

- Generates random data with specified columns.
- Saves the generated data to a CSV file (`random_data.csv`).
- Containerized using Docker for easy deployment.

## Requirements

- Docker installed on your machine.

## Getting Started

### Running Locally

1. Ensure you have Python 3 installed and create a virtual environment:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate
    ```

2. Install dependencies:

    ```bash
    pip install numpy pandas
    ```

3. Run the script:

    ```bash
    python generate_data.py
    ```

    This will generate the `random_data.csv` file in the current directory.

### Running with Docker

1. Build the Docker image:

    ```bash
    docker build -t narek07/random-data-generator .
    ```

2. Run the Docker container:

    ```bash
    docker run --rm narek07/random-data-generator
    ```

    This will generate the `random_data.csv` file inside the container.

### Pulling from Docker Hub

You can also pull and run the Docker image directly from Docker Hub:

```bash
docker run --rm narek07/random-data-generator
