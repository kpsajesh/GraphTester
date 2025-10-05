# This is runner file to orchestrate the test case generator nodes > state > graph > app

"""
Driver for Test Case Generator Pipeline
-----------------------------------------------
This script runs the LangGraph pipeline we built.

Usage:
  python -m src.graph.drivers.run_test_case_pipeline
"""

import logging
from pprint import pprint

from src.graph.test_case_generator.tc_graph import build_graph
from src.graph.test_case_generator.tc_state import TestCaseState

# Configure logger for consistent output
logging.basicConfig(level=logging.INFO, format="🔹 %(message)s")
logger = logging.getLogger(__name__)
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        help="Path to a requirement .txt file (default: first in data/requirements/)",
        default=None,
    )
    args = parser.parse_args()

    logger.info("🚀 Starting Test Case Generator pipeline...")

    # Build pipeline graph
    app = build_graph()

    # Initialize empty state (requirements will be filled by first node)
    init_state: TestCaseState = {}

    # Run pipeline
    final_state = app.invoke(init_state)

    # Pretty print results for teaching clarity
    logger.info("✅ Pipeline finished. Final state below:")
    
    # Printing the final state with all variables should not needed in the final version, just to see the output
    pprint(final_state) 


if __name__ == "__main__":
    main()
