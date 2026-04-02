import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# --- подключение один раз (это важно) ---
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "telegram-bot-project-490909-bc267e80303d.json",
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1bsfp5uKYmuG0S-yDRb-tkKgmcc2h5qgDbjPbA994wbw"
).sheet1


def save_to_sheets(data: dict):
    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        data.get("name"),
        data.get("phone"),
        data.get("comment")
    ]

    try:
        sheet.append_row(row)
        print("WRITTEN TO GOOGLE SHEETS")
    except Exception as e:
        print("ERROR GOOGLE SHEETS:", e)