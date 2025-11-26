# VLArm
## HackClub X AMD Blueprint Build 2025

**Goal:** Replicating Google DeepMind's VLA model (Vision-Language-Action model) to create a robotic arm that can be used in industry settings.

**The twist:** This project will take an existing robot (HuggingFace's SO-101) and give it the capability to make decisions 'for itself' with the power of a locally-running MCP and LLM (from Ollama). Essentially, the robot will take actions based on language commands, controlled with a locally-running Large Language Model. 

**Future steps:** After I have the language commands set up, I will add Vision and Listening capabilities that let the model hear someone's commands and also see what it is doing live.

## How I'll build it

I'm hoping to get funding through HackClub's Blueprint program to get for the hardware to build this project. I will 3D print the parts without HackClub's funding.

# Structure

This repository contains the following files and directories:
* `BOM.csv`: Parts needed to build the arm.
* `3D`: 3D models and Ultimaker Cura files for 3D printing the casing for the arm.
* `mcp`: A folder with the files for setting up a MCP server that can be used to control the arm via an LLM.

# Setting up MCP for Ollama

The `mcp` folder in the main directory contains the files for running an MCP with Anthropic's open-source protocol. Anthropic's protocol can be used with Ollama through ollmcp, which is an open-source MCP client for Ollama. This folder contains files that can be configured with ollmcp to have a locally-running LLM through Ollama make tool calls to move the arm.

## Instructions

Set up the Prerequisites: 
* Ollama (https://ollama.com/): Make sure to run `ollama run qwen2.5` to get a LLM with tool-use running locally after Ollama is installed.
* Python

Then:
1. Run `pip install ollmcp`.
2. Assuming you've cloned this repository, go to the `mcp` directory.
3. Run `ollmcp --mcp-server server.py --model qwen2.5`.

## Credits
This project is based on the HuggingFace/TheRobotStudio SO-100 tutorial, Phosphobot API, and LeRobot library:

* https://huggingface.co/docs/lerobot/en/so100
* https://github.com/TheRobotStudio/SO-ARM100
* https://docs.phospho.ai/installation
* https://github.com/huggingface/lerobot
