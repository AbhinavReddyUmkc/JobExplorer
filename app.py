from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the data
file_path = 'final_data.xlsx'
data = pd.read_excel(file_path)

@app.route('/')
def index():
    # Extract unique designations for the dropdown
    designations = data['Designation'].unique()
    return render_template('index.html', designations=designations)

@app.route('/filter', methods=['POST'])
def filter_data():
    # Get the selected designation
    selected_designation = request.form['designation']
    # Filter data based on the selection
    filtered_data = data[data['Designation'] == selected_designation]
    return render_template('table.html', tables=filtered_data.to_html(classes='table', index=False))

if __name__ == "_main_":
    app.run(host='0.0.0.0', port=5000, debug=True)