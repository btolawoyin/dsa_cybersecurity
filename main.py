import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta

# Load datasets
calls = pd.read_csv("data/CallLog.csv", parse_dates=['timestamp_start', 'timestamp_end'])
sms = pd.read_csv("data/SMS_Messages.csv", parse_dates=['timestamp'])
apps = pd.read_csv("data/AppUsage.csv", parse_dates=['timestamp'])

# Combine all logs for timeline
sms['event'] = 'SMS'
calls['event'] = 'Call'
apps['event'] = 'App'
apps = apps.rename(columns={'timestamp_start': 'timestamp'})  # Unify timestamp columns

timeline = pd.concat([calls, sms, apps], ignore_index=True)

# Plot
sns.scatterplot(data=timeline, x='timestamp', y='event', hue='event')
plt.xticks(rotation=45)
plt.tight_layout()
plt.title("Forensic Timeline: Call, SMS, App Usage")
plt.show()
