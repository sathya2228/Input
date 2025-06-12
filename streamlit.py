
import streamlit as st
import requests
import datetime

# --- UI Setup ---
st.set_page_config(page_title="Leave Request Form", layout="centered")

st.title("📝 Employee Leave Request")
st.markdown("Fill out the form below to submit your leave request.")

# --- Input Fields ---
name = st.text_input("Employee Name")
email = st.text_input("Official Email")
leave_type = st.selectbox("Leave Type", ["Casual Leave", "Sick Leave", "Earned Leave", "Maternity Leave", "Other"])
start_date = st.date_input("Leave Start Date", min_value=datetime.date.today())
end_date = st.date_input("Leave End Date", min_value=start_date)
reason = st.text_area("Reason for Leave")

# --- Submit Button ---
if st.button("Submit Leave Request"):
    if name and email and leave_type and start_date and end_date:
        data = {
            "name": name,
            "email": email,
            "leave_type": leave_type,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "reason": reason
        }
        
        # Replace this with your actual n8n webhook URL
        webhook_url = "https://sathyaaaa.app.n8n.cloud/webhook-test/78925f62-f134-4c48-9755-9b7ffafbe36e"

        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 200:
                st.success("✅ Leave request submitted successfully!")
            else:
                st.error(f"❌ Failed to submit. Error code: {response.status_code}")
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
    else:
        st.warning("⚠️ Please fill in all required fields.")
