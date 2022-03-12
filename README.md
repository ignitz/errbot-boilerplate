# ErrBot Boilerplate

> Yuri Niitsuma ignitzhjfk@gmail.com

Boilerplate for Errbot plugins.

```shell
python3 -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt
```

Add Slackv3 in errbot backend:

```shell
git clone https://github.com/errbotio/err-backend-slackv3 && \
mv err-backend-slackv3 venv/lib/python3.9/site-packages/errbot/backends/
# Attention: Change python3.9 to your Python version that are you using.
```

## Usage

First import environment variables:

```
source .env
```

Run:

```shell
# Run in console
errbot -T

# Run in Slack
errbot
```
