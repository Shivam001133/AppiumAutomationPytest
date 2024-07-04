import os
import logging
from dotenv import load_dotenv
from Project.src.constants import constants

# load dot .env file
load_dotenv()

logger = logging.getLogger(__name__)

# Environment variables in data.env folder
ENVIRONMENTS = {
    "QA": "data.env.qa_env",
    "STG": "data.env.staging_env",
    "DEV": "data.env.develop_env",
    "PROD": "data.env.production_env"
}

# Add command line options 
def pytest_addoption(parser):
    parser.adoption(
        "--env",
        action="store",
        dest="env",
        default="QA", # if not specified, default to QA
        help="Environment to run tests on",
        choices=("QA", "STG", "DEV", "PROD")
    )

# Manage environment variables
def env_manage(config, env_name):
    if env_name:
        constants.ENV = env_name
    logger.warning(f"Running tests on {env_name} environment")
    os.environ['SIMPLE_SETTINGS'] = ENVIRONMENTS[constants.ENV]
    if not config.getoption('r'):
        config.option.allure_report_dir = 'allure/allure-results'

# Configure pytest
def pytest_configure(config):
    constants.ENV = config.getoption('env')

    env_manage(config, constants.ENV)

    # Set max fail test cases his will exit the test run after the specified number of test failures
    # here is set to 5
    config.option.maxfail = 5
