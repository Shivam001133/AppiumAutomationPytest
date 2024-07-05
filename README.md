# Pytest Appium with LambdaTest

This project demonstrates how to use pytest for running Appium-based tests on devices with LambdaTest.

## Prerequisites

1. Python 3.10 installed on your machine.
2. Pip (Python package installer).
3. Appium server.
4. LambdaTest account (required if using LambdaTest devices).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Shivam001133/AppiumAutomationPytest.git
    cd AppiumAutomationPytest
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root directory and add your LambdaTest credentials:

    ```
    LAMBDATEST_USERNAME="your_username"
    LAMBDATEST_ACCESS_KEY="your_access_key"
    ```

2. Project Structure:
    - `/src/`:
        - `/constants/`: Contains constants used in test cases.
        - `/utilities/`: Utility functions for tests.
    - `/test/`:
        - `/fixtures/`: Pytest fixtures organized by category for easy management.
        - `/pages/`: Page objects for UI test cases.
        - `/test_cases/`: Test cases written using pytest.
    - `/docs/`: Documentation folder containing Appium tutorials and documentation.
    - `/data/env/`: Environment-specific configuration files (`stg`, `dev`, `qa`, `prod`).

3. Additional Configuration:
    - Two `conftest.py` files are used, one in the root directory and another in the `test` folder.
    - `pytest.ini` contains all pytest configurations for the project.

## License

This project is licensed under the MIT License. See the <a href="[https://www.w3schools.com](https://github.com/Shivam001133/AppiumAutomationPytest/blob/main/LICENSE)">LICENSE</a> file for details.

