from langchain.llms import OpenAI

llm = OpenAI()

def generate_incident_report(alerts, sensor_data):
    prompt = f"""
    Generate an industrial incident report.

    Alerts:
    {alerts}

    Sensor Data:
    {sensor_data}

    Include:
    - Root cause
    - Risk level
    - Recommended actions
    """
    return llm(prompt)
