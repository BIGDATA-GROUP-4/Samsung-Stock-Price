@echo off
echo Running Samsung Electronics Interactive Visualization...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Please install Python first.
    pause
    exit /b 1
)

:: Install required packages
echo Installing required packages...
pip install -r requirements.txt

:: Run the visualization script
echo Starting visualization...
python samsung_interactive_visualization.py

:: Open the visualization in default browser
echo Opening visualization in browser...
start samsung_interactive_chart_standalone.html

echo Done!
pause 