echo ========================================================

streamlit run %CM_TMP_CURRENT_SCRIPT_PATH%\src\app.py
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

echo ========================================================
