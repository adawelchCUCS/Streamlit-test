import streamlit as st
import pandas as pd

# Import your report generation functions from other scripts
from reports.HOPWA.hopwa import generate_hopwa_report
#from reports.MCN_Report.MCN_Report import generate_mcn_report

# from other_reports import generate_mcn_report, generate_hospitalizations_report, generate_entitlements_report

# List of reports available
report_list = ['MCN Report', 'Hospitalizations Report', 'Entitlements Report', 'HOPWA Report']

# Initialize session state for the DataFrame if it doesn't already exist
if 'df' not in st.session_state:
    st.session_state['df'] = None

# Dropdown for selecting report
report_type = st.selectbox('Select a report to run', report_list)

# Step 1: File upload
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# Step 2: Handle file upload and store in session state
if uploaded_file is not None:
    try:
        st.session_state['df'] = pd.read_csv(uploaded_file)
        st.write("File uploaded successfully!")
        st.write(st.session_state['df'].head())  # Display a preview of the data
    except pd.errors.EmptyDataError:
        st.error("The uploaded file is empty. Please check the file.")
    except pd.errors.ParserError:
        st.error("Error parsing the CSV file. Please ensure it is properly formatted.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

# Dictionary mapping report types to their corresponding functions
report_functions = {
    'MCN Report': None, #generate_mcn_report,
    'Hospitalizations Report': None,  # generate_hospitalizations_report,  # Uncomment once implemented
    'Entitlements Report': None,  # generate_entitlements_report,  # Uncomment once implemented
    'HOPWA Report': generate_hopwa_report
}

# Step 3: When the user clicks 'Run Report', use the data stored in session state
if st.button('Run Report'):
    if st.session_state['df'] is not None:
        try:
            report_function = report_functions.get(report_type)
            if report_function:
                report_function(st.session_state['df'])  # Call the appropriate function
                st.success(f"{report_type} successfully generated.")
            else:
                st.error(f"No function is implemented for {report_type}.")
        except Exception as e:
            st.error(f"An error occurred while generating the report: {e}")
    else:
        st.warning("Please upload a CSV file to proceed.")

# Optional: Button to clear the uploaded file and session state
if st.button('Clear Uploaded File'):
    st.session_state['df'] = None
    st.write("File cleared. Please upload a new CSV file.")
