"""Print today's local date as YYYY-MM-DD. Standard library only; reads nothing, writes nothing, no network."""
import datetime

print(datetime.date.today().isoformat())
