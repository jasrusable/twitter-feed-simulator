# A twitter feed app

## Quickstart

### Requirements
- Git
- Python 3.6

### Clone the repo

```git clone https://github.com/jasrusable/twitter-feed-simulator.git```

### Install dependancies

```pip install -r requirements.txt```

### Run the app
From the parent directory, run the following command to display the help text & usage:

```python cli.py```

### Simple example

```python cli.py --tweets-file ./sample_data/tweets.txt --follow-events-file ./sample_data/follow_events.txt print-users-feeds```

## Tests

Tests are run using `pytest`

### Run tests once off

From the root directory, run:

```pytest```

### Run tests continually

From the root directory, run:

```ptw```