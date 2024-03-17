# WPCLI-YML-Updater #
wpcli-yml-updater is an open-source Python script written by Sam Bunker. This script accepts a specially formatted wp-cli.yml document that is created when building a WordPress website.

## How to use ##
Copy the text in your wp-cli.yml file found in your wordpress folder. Paste it into the txts/yml-paste.txt. Run main.py (don't forget to download the dependencies below). The output can be found in txts/export.txt.

## Why this script? ##
In the summer of 2023, I obtained an internship for a company as an interactive developer (web developer). In this role, I was tasked with various roles, one of which was performing WordPress maintenance on our clients's websites. This work was grueling due to the repetitive nature of checking each WordPress official plugin and our internal plugins. I enjoyed performing maintenance on client websites, but the task itself was inherently annoying.
So, I built a script to automate the entire process. This helped me knock out what would take around thirty minutes of constant copying and pasting and querying each plugin down to just a couple seconds. The script utilizes BeautifulSoup for webscrapping WordPress's websites for the latest plugin versions, as well as our company's internal website, where we house our plugins.
Our company's website has been redacted, which affects the current code. If you are only using WordPress's official plugins for updates, I will be releasing a more public version to remedy this.

## Future Goals ##
I plan on attaching this script to the company I'm interning for's pipeline to automate our wp-cli.yml maintenance. (We still check our development environments to ensure no bugs from updated cores, plugins, or themes.)

## Python Versions Tested ##
3.10

## Python Dependencies ##
BeautifulSoup, Requests, Re
