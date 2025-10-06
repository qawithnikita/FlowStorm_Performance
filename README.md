# FlowStorm Performance

**FlowStorm Performance** is a Python-based load testing project using **Locust**. It simulates multiple user flows to measure the performance of APIs and services. The project is designed for testing, benchmarking, and generating performance reports in HTML and CSV formats.

## Features

- Simulates multiple types of user flows:
  - **BasicFlowUser**: Standard sequence of API calls
  - **LongConversationUser**: Extended interaction flow
  - **PartialFlowUser**: Partial flow for idle or interrupted sessions
- Generates **HTML and CSV reports** for performance metrics
- Configurable via environment variables:
  - Users count, spawn rate, run time, host, log level, etc.
- Organized modular structure for easy extension and customization

## Installation

1. Clone the repository:
   git clone https://github.com/qawithnikita/FlowStorm_Performance.git
   cd FlowStorm_Performance
   
Install dependencies:
pip install -r requirements.txt

## Usage

Run the load test using the custom script:

python run_locust_file.py

Reports will be saved automatically in the reports/ folder with timestamped subfolders.
