# DS5111 VM Setup

This repository contains setup scripts and instructions for recreating a working Python development environment on a new VM.

## Starting Point

This guide assumes:

- You have a new VM running Ubuntu.
- You have an SSH key configured for GitHub.
- You have already cloned this repository onto the VM.

## Step 1: Run the VM initialization script

From the root of the repository, run:

```bash
bash scripts/init.sh
# DS5111 VM Setup

This repository contains scripts and configuration files used to recreate a Python development environment on a new Ubuntu VM.

## Starting Point

Before beginning, make sure:

- You have a running Ubuntu VM
- You have an SSH key configured for GitHub access
- Git is already installed on the machine

## Step 1: Clone the Repository

Clone the repository onto the VM using SSH:

git clone git@github.com:YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git

Move into the repository:

cd YOUR_REPO_NAME

--------------------------------------------------

## Step 2: Run the VM Initialization Script

The initialization script updates the VM and installs required packages.

Run:

bash scripts/init.sh

This script installs:

- make
- python3.14-venv
- tree

Verify the script worked:

tree

If the command displays the project file structure, the installation worked correctly.

--------------------------------------------------

## Step 3: Configure Git Credentials

Run the Git credential setup script:

bash scripts/init_git_creds.sh

This script sets the global Git username and email.

Verify Git configuration:

git config --global --list

You should see:

user.email=your_email
user.name=your_username

--------------------------------------------------

## Step 4: Create the Python Virtual Environment

This project uses a makefile to automate environment creation and package installation.

Run:

make update

This command will:

1. Create a Python virtual environment named env
2. Upgrade pip
3. Install packages from requirements.txt

--------------------------------------------------

## Step 5: Activate the Virtual Environment

Activate the environment with:

. env/bin/activate

You should now see:

(env)

at the beginning of the terminal prompt.

--------------------------------------------------

## Step 6: Verify Installed Packages

Run:

pip list

You should see packages including:

- pandas
- numpy

--------------------------------------------------

## Repository Structure

DS5111/
├── makefile
├── requirements.txt
├── README.md
├── env/
└── scripts/
    ├── init.sh
    └── init_git_creds.sh

--------------------------------------------------

## Summary

This repository provides a repeatable process for rebuilding a Python development environment on a new VM. The setup scripts automate package installation, Git configuration, and virtual environment creation to make recovery and onboarding faster.
