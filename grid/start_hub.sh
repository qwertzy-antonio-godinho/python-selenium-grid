#! /bin/bash

printf "Init HUB:\n"
java -jar selenium-server-4.3.0.jar hub --config ./config/hub.toml
