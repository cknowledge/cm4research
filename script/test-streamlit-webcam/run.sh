#!/bin/bash

echo "========================================================"

streamlit run ${CM_TMP_CURRENT_SCRIPT_PATH}/src/app.py
test $? -eq 0 || exit 1

echo ========================================================
