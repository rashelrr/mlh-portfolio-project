#!/bin/bash

tmux kill-server
cd ~/mlh-portfolio-project
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s portfolio_session 'flask run --host=0.0.0.0'
