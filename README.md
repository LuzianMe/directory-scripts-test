# directory-scripts-test

A minimal Claude Code plugin made to learn one thing: how Anthropic's plugin directory treats a skill that runs a script from its own `scripts/` folder when the plugin comes from an individual account, not a verified organization.

It contains one skill, `date-check`, and one script, `skills/date-check/scripts/today.py`, which prints today's date in ISO format. The script uses only the Python standard library, reads no files, writes no files and makes no network requests.

This repository is temporary. It will be withdrawn from the directory and deleted once the question is answered.

License: MIT.
