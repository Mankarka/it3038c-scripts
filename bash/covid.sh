#!/bin/bash
# This Script download covid data and display it


DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative') 
DEATH=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
TODAY=$(date)


echo "On $TODAY, there were $POSITIVE positive, $NEGATIVE negative, $DEATH deaths, $HOSPITALIZED hospitalized"
