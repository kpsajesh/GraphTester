# This is runner file to orchestrate the log analyser nodes > state > graph > app

# Use below code to run this file step by step:
# 1. create virtual environment - 
#  python -m venv .\venv
# 2. activate virtual environment
# .\venv\Scripts\Activate.ps1
# 3 If any error in activating virtual environment, run this command in PowerShell: 
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# 4. install dependencies one by one
# pip install langchain langchain-openai langchain-ollama python-dotenv langgraph rich loguru
# -here rich and loguru dependancies are to see logs in a better organised way
# 5. TO see the versions of installed packages
# pip show  langchain langchain-openai langchain-ollama python-dotenv langgraph rich loguru
# 6. set OPENAI_API_KEY in .env variable ( This may not be required for Ollama, but just in case you want to test OpenAI also)
#   $env:OPENAI_API_KEY="your_api_key_here" 
#   6.a Check the Open AI API is set correctly
#       echo $env:OPENAI_API_KEY  > would show the saved API key 
# 7 Now run the ollama.
# open powershell seperately from run window > – Windows +R > powershell
#   7.a Type ollama > run > shows the commands
#   7.b Type ollama run mistral:7b  (this will start the ollama server)
#   7.c Type a sample prompt like "What is machine learning?" to check whether it is working fine.
# 8. Now run the file (make sure ollama is running before the runnning this command)
# python -m src.graph.drivers.run_log_analyzer_pipeline

# The project contains a demo API services for Testrail, Jira and Slack
# GO to JiraTestrailSlackAPI-ToTest folder in this project> double click start-all.bat > will start all the API services, to see
#   Testrail UI, open browser and type http://localhost:4001/ui & API can be seen from http://localhost:4001/docs#
#   Jira UI, open browser and type http://localhost:4002/ui & API can be seen from http://localhost:4002/docs#
#   Slack UI, open browser and type http://localhost:4003/ui & API can be seen from http://localhost:4003/docs#



"""
- Driver for Log Analyzer Pipeline
----------------------------------------
This script runs the LangGraph Log Analyzer pipeline.

Usage:
  python -m src.graph.drivers.run_log_analyzer_pipeline --inputs data/logs/runtime_errors.log
  python -m src.graph.drivers.run_log_analyzer_pipeline --inputs data/logs/runtime_errors.log data/logs/app_startup.log
"""

import logging
import argparse
from pprint import pprint

from src.graph.log_analyzer.log_graph import build_graph
from src.graph.log_analyzer.log_state import LogAnalyzerState

# Configure logger
logging.basicConfig(level=logging.INFO, format="🔹 %(message)s")
logger = logging.getLogger(__name__)


def main():
    print('hi')
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inputs",
        nargs="+",
        help="One or more log file paths",
        default=None,
    )
    args = parser.parse_args()

    logger.info("🚀 Starting Log Analyzer pipeline...")

    # Build pipeline graph
    app = build_graph()

    # Initialize state
    init_state: LogAnalyzerState = {}
    if args.inputs:
        init_state["log_paths"] = args.inputs

    # Run pipeline
    final_state = app.invoke(init_state)

    # Summarize results
    issues = final_state.get("jira_issues", [])
    slack = final_state.get("slack_notifications", [])
    logger.info(
        f"✅ Finished: {len(final_state.get('groups', []))} groups analyzed, "
        f"{len(issues)} Jira issues created, Slack sent={bool(slack)}"
    )

    # Debugging/teaching: print full state
    pprint(final_state)


if __name__ == "__main__":
    main()
