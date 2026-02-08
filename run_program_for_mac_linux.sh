#!/bin/bash

# Define variables
SOURCE_FILE="LONG_ASSIGNMENT_MAJOR.cpp"
EXECUTABLE_NAME="social_network_app" # .exe extension is typically omitted on Unix

echo "Compiling $SOURCE_FILE..."


# Compilation Step (using g++).
g++ -std=c++17 -Wall "$SOURCE_FILE" -o "$EXECUTABLE_NAME"

# Check the exit status ($?) of the previous command (g++)
if [ $? -ne 0 ]; then
    echo ""
    echo "Compilation failed. Check your C++ code and ensure g++ is installed and in your PATH."
    exit 1 # Exit with a non-zero status to indicate an error
fi

echo ""
echo " Compilation successful. Executable created: $EXECUTABLE_NAME"
echo "------------------------------------------------------"
echo "Running the program. Enter commands (e.g., ADD_USER, ADD_POST)..."
echo "Type in QUIT and then Enter to quit the program."

# Execution Step
./"$EXECUTABLE_NAME"

echo "------------------------------------------------------"
echo "Program finished."

# The 'read -p' command is the common Unix equivalent for the 'pause' command in Windows
read -p "Press Enter to exit..."