def create_reserve_table_message(user_data: dict):
    message = f"""
Table Reservation Details:
----------------------------
Client Name: {user_data.get("name")}
Client Email: {user_data.get("email")}
Number of People: {user_data.get("person")}
Arrival Time: {user_data.get("timing")}
Arrival Date: {user_data.get("date")}
"""
    if phone := user_data.get("phone"):
        message += "Client Phone Number: " + phone
    return message
