# python-selenium-grid
A playground repository with an example test framework written in Python using Selenium Grid.
This repo was setup for me to catchup with latest developments in Selenium using Python as the programming laguage, the last time I used it was in mid 2018 with Java bindings. This is still pretty much a work in progress and currently has Driver factory, Page Object Model and the ability to run in a distributed way (through the Selenium grid). As a test playground I'm using a website who publishes news about technology and operating system to write and run browser tests against.

TODO:
- Rework POM
- Implement test suites 
- Implement concurrent execution
- Use Ghrekin (BDD)
- Rework precommit hooks
- Possibly more...

## Software
- Java JRE (Headless)
- Firefox and Chrome browsers installed
- Python

## Notes
```grid``` directory contains scripts to start the grid instance:
- ```start-hub.sh``` configuration file in ```config/hub.toml```
- ```start-node.sh``` configuration file in ```config/node.toml```, for Firefox and Chrome (drivers are included)

Create a virtual environment ```python -m venv .venv``` and activate it (```source .venv/bin/activate```), then install from requirements.txt file ```pip install -r requirements.txt```. 

Run ```pytest``` to run the tests.
