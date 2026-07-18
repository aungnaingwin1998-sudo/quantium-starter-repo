#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run test suite
pytest

# Store test result
TEST_RESULT=$?

# Return exit code
if [ $TEST_RESULT -eq 0 ]; then
    echo "All tests passed"
    exit 0
else
    echo "Tests failed"
    exit 1
fi