from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

def run_reporting_procedure():
    try:
        connection = psycopg2.connect(os.environ['DATABASE_URL'])
        cursor = connection.cursor()
        cursor.execute("SELECT run_reporting_procedures();")
        connection.commit()
        print("Reporting procedures executed successfully.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()


scheduler = BackgroundScheduler()
scheduler.add_job(func=run_reporting_procedure, trigger="interval", minutes=5)  # Run every 30 minutes
scheduler.start()

@app.route('/')
def index():
    return "The reporting scheduler is running."

@app.route('/run-report')
def run_report():
    run_reporting_procedure()
    return "Report procedure initiated."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3838, use_reloader=False)
