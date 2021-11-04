#!/bin/bash
echo Running the stop ELN script

ps -ef | grep puma | awk '{print $2}' | xargs kill