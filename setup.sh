#!/bin/bash

sudo apt -y install dos2unix
dos2unix *.py
sudo chmod +x *.py