#!/bin/bash

# Input: Write a bash script that tests the endpoints using curl
# Create a random timeline post using POST endpoint
# and check the GET endpoint to make sure it was added. 

RAND=$((1 + $RANDOM % 100))

curl -X POST http://127.0.0.1:5000/api/timeline_post -d "name=Jane$RAND&email=jane$RAND@example.com&content=Testing post endpoint $RAND" 

# Check for successful POST by doing GET
RESULT=$(curl -s http://127.0.0.1:5000/api/timeline_post | jq -r ".timeline_posts | .[] | select(.name == \"Jane$RAND\") | select(.email == \"jane$RAND@example.com\") | select(.content == \"Testing post endpoint $RAND\")")

# Return success if above command returned a non-empty result
# non-empty result means it found matching command
if [[ -z $RESULT ]]
then
    echo "Fail."
else
    echo "Success."
fi

