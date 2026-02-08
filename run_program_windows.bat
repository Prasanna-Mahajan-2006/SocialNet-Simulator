@echo off

set SOURCE_FILE=LONG_ASSIGNMENT_MAJOR.cpp
set EXECUTABLE_NAME=social_network_app.exe

echo Compiling %SOURCE_FILE%...

:: Compilation Step (using g++).
g++ -std=c++17 -Wall %SOURCE_FILE% -o %EXECUTABLE_NAME%

:: Check the error level of the previous command (g++)
if %errorlevel% neq 0 (
    echo.
    echo Compilation failed. Check your C++ code and ensure g++ is in your PATH.
    goto :end
)

echo.
echo Compilation successful. Executable created: %EXECUTABLE_NAME%
echo ------------------------------------------------------
echo Running the program. Enter commands (e.g., addUser, addPostHelper)...
echo Type in QUIT and then Enter to quit the program.

:: Execution Step
:: This runs the executable and waits for commands via the terminal (stdin).
%EXECUTABLE_NAME%

echo ------------------------------------------------------
echo Program finished.

:end
pause