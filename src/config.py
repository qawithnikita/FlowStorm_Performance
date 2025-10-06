import os
from datetime import datetime

class BaseConfig:
      
      REPORT_FOLDER = os.path.join("reports", datetime.now().strftime("%m_%d_%Y__%H_%M"))
      os.makedirs(REPORT_FOLDER, exist_ok=True) 

      HOST = os.getenv("LOCUST_HOST", "http://localhost:8000")
      USERS = int(os.getenv("LOCUST_USERS", 10)) 
      SPAWN_RATE = int(os.getenv("LOCUST_SPAWN_RATE", 2))
      RUN_TIME = os.getenv("LOCUST_RUN_TIME", "1m")
      MIN_WAIT = int(os.getenv("LOCUST_MIN_WAIT", 1))
      MAX_WAIT = int(os.getenv("LOCUST_MAX_WAIT", 3))
      HTML_REPORT = os.getenv("LOCUST_HTML_REPORT", "report.html")
      CSV_REPORT = os.getenv("LOCUST_CSV_REPORT", "report")
      LOG_LEVEL = os.getenv("LOCUST_LOG_LEVEL", "INFO")
      HEADLESS = os.getenv("LOCUST_HEADLESS", "true").lower() == "true"

