@echo off

@REM variables
set venv_path=.\venv-popcat\Scripts\activate.bat
set commandScheduler=python popcat-automated.py

@REM activate virtual environment
call %venv_path%

@REM run the program
call %commandScheduler%

@REM exit program
exit