import json
from flask import Flask
from fake_web_events import Simulation
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    simulation = Simulation(user_pool_size=1, sessions_per_day=100)
    events = simulation.run(duration_seconds=0.5)

    df = pd.DataFrame()
    for event in events:
        dfx = pd.DataFrame(event, index=[0])
        df = pd.concat([df, dfx], ignore_index=True)
    print(df.columns)
    return json.dumps(df.to_json(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8081', debug=True)