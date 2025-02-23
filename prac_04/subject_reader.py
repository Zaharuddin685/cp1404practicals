FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)  # Call the new function to display the subject details

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []  # Initialize an empty list to store the data
    with open(FILENAME) as input_file:  # Open the file using 'with' to automatically handle closing
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Convert the number of students to an integer
            data.append(parts)  # Append the list of parts to the data list
    return data  # Return the nested list

def display_subject_details(data):
    """Display the subject details in the format: subject code, lecturer, number of students."""
    for subject in data:
        subject_code, lecturer, num_students = subject
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")

main()
