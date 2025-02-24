# SP25_DS5111_nnx3ue

## VM Setup
After logging onto a new VM the user should do the following:
- Run the following from the command line manually: sudo apt update
- Set up git credentials and create an ssh key by following the steps outlined in: 00_00_setup_script_for_git_github.md
- Clone this repo
- Run the following from the command line to run the init script: ./init.sh

## Project Specific Setup
After following the steps outlined in the VM Setup section, the user should do the following:
- Run the following from the command line to install chrome headless browser: ./install_chrome_headless.sh
- Note: The requirements.txt file contains the packages required for this pipeline to work
- Run the following from the command line to continue setting up the virtual environment and installing dependencies: make update
- Run the following from the command line to run a job in the makefile to test the headless browser: make ygainers.csv

## Repository Structure

SP25_DS5111_nnx3ue
├── 00_00_setup_script_for_git_github.md
├── 00_01_setup_git_global_creds.md
├── init.sh
├── install_chrome.sh
├── makefile
├── README.md
└──requirements.txt

![Feature Validation](https://github.com/samajohnson/SP25_DS5111_nnx3ue/actions/workflows/validations.yml/badge.svg)


