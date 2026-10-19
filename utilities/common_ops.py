import os
import xml.etree.ElementTree as ET


def get_data(node_name):
    # TIBA_BEARER_TOKEN - For security reasons, the token is stored in environment variables.
    if node_name == "Bearer_token":
        token = os.environ.get("TIBA_BEARER_TOKEN")
        if not token:
            raise Exception("Environment variable TIBA_BEARER_TOKEN is not set. "
                            "Set it with: setx TIBA_BEARER_TOKEN \"<your token>\" and restart PyCharm.")
        return token

    # TIBA_PARK_CLOUD_ID - For security reasons, the park cloud ID is stored in environment variables.
    if node_name == "Park_Cloud_ID":
        park_cloud_id = os.environ.get("TIBA_PARK_CLOUD_ID")
        if not park_cloud_id:
            raise Exception("Environment variable TIBA_PARK_CLOUD_ID is not set. "
                            "Set it with: setx TIBA_PARK_CLOUD_ID \"<your park cloud id>\" and restart PyCharm.")
        return park_cloud_id

    # The UI username and password are also stored in environment variables for security reasons.
    if node_name == "UI_Username":
        username = os.environ.get("TIBA_UI_USERNAME")
        if not username:
            raise Exception("Environment variable TIBA_UI_USERNAME is not set. "
                            "Set it in Windows environment variables and restart PyCharm.")
        return username

    # The UI password is also stored in environment variables for security reasons.
    if node_name == "UI_Password":
        password = os.environ.get("TIBA_UI_PASSWORD")
        if not password:
            raise Exception("Environment variable TIBA_UI_PASSWORD is not set. "
                            "Set it in Windows environment variables and restart PyCharm.")
        return password

    root = ET.parse("C:/Automation/Learning_Automation/configuration/data.xml").getroot()
    return root.find(".//" + node_name).text

