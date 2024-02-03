import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests

def convert_markdown_to_pdf(markdown_content, Resume_file="Resume.pdf", engine="weasyprint"):
    # Define CSS styles for the PDF
    cssfile = """
                body{
                    padding: 0px;
                    margin:0px;
                }
                h1 {
                color: MidnightBlue;
                margin:0px;
                padding:0px;
                    
                }
                h3{
                    color: MidnightBlue;
                    padding-bottom:0px; 
                    margin-bottom:0px; 
                }
                li{
                    margin-top:5px;
                }
                
                """
    # API endpoint for converting Markdown to PDF
    url = "https://md-to-pdf.fly.dev"

    # Data to be sent in the POST request
    data = {
        'markdown': markdown_content,
        'css': cssfile,
        'engine': engine
    }

    # Send a POST request to the API
    response = requests.post(url, data=data)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Save the generated PDF to a file
        with open(Resume_file, 'wb') as f:
            f.write(response.content)
        print(f"PDF saved to {Resume_file}")
    else:
        print(f"Error {response.status_code}: {response.text}")


class Resume:
    def __init__(self, name, email, mobile, education, skills, experience, projects, achievements, activities):
        # Initialize the Resume object with user information
        self.name = name
        self.email = email
        self.mobile = mobile
        self.education = education
        self.skills = skills
        self.experience = experience
        self.projects = projects
        self.achievements = achievements
        self.activities = activities

    def generate_markdown(self):
        # Generate Markdown content for the resume
        markdown_text = f"<h1 style=\"text-align:center;\">{self.name}</h1>\n<p style=\"text-align:center;\">Email: {self.email} | Mobile: {self.mobile} </p>\n\n"
        markdown_text += "### Education\n\n---\n\n"
        # Add education details to the Markdown content
        for edu in self.education:
            markdown_text += f"- {edu['level']}: {edu['institution']} | {edu['field']} | Score: {edu['score']} | {edu['duration']}." + "\n\n"

        markdown_text += "### Skills\n\n---\n\n"
        # Add skills to the Markdown content
        markdown_text += f"{self.skills} \n\n"

        markdown_text += "### Experience\n\n---\n\n"
        # Add work experience details to the Markdown content
        for exp in self.experience:
            markdown_text += f"- **{exp['job_role']}({exp['company_name']})**: {exp['description']}\n"

        markdown_text += "\n### Projects\n\n---\n\n"
        # Add project details to the Markdown content
        for proj in self.projects:
            markdown_text += f"- **{proj['name']}**: {proj['description']}\n"

        markdown_text += "\n### Achievements\n\n---\n\n"
        # Add achievement details to the Markdown content
        for ach in self.achievements:
            markdown_text += f"- {ach}\n"

        markdown_text += "\n### Other Activities\n\n---\n\n"
        # Add other activities to the Markdown content
        markdown_text += self.activities + '\n'

        return markdown_text

 

class ResumeGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Generator")
        self.root.geometry("400x400")

        # User details
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.mobile_var = tk.StringVar()

        # Education details
        self.education_entries = []

        # Skills
        self.skills_var = tk.StringVar()

        # Experience details
        self.experience_entries = []

        # Projects details
        self.projects_entries = []

        # Achievements
        self.achievements_var = tk.StringVar()

        # Activities
        self.activities_var = tk.StringVar()

        # Create UI
        self.create_user_interface()

    def create_user_interface(self):
        # User Details
        user_label = ttk.Label(self.root, text="User Details", font=("Helvetica", 16))
        user_label.grid(row=0, column=0, columnspan=2, pady=10)

        name_label = ttk.Label(self.root, text="Name:")
        name_label.grid(row=1, column=0, sticky="e")
        name_entry = ttk.Entry(self.root, textvariable=self.name_var)
        name_entry.grid(row=1, column=1, pady=5)

        email_label = ttk.Label(self.root, text="Email:")
        email_label.grid(row=2, column=0, sticky="e")
        email_entry = ttk.Entry(self.root, textvariable=self.email_var)
        email_entry.grid(row=2, column=1, pady=5)

        mobile_label = ttk.Label(self.root, text="Mobile:")
        mobile_label.grid(row=3, column=0, sticky="e")
        mobile_entry = ttk.Entry(self.root, textvariable=self.mobile_var)
        mobile_entry.grid(row=3, column=1, pady=5)

        # Education Details
        education_label = ttk.Label(self.root, text="Education Details", font=("Helvetica", 16))
        education_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Add education entry button
        add_education_button = ttk.Button(self.root, text="Add Education", command=self.add_education_entry)
        add_education_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Skills
        skills_label = ttk.Label(self.root, text="Skills:")
        skills_label.grid(row=6, column=0, sticky="e")
        skills_entry = ttk.Entry(self.root, textvariable=self.skills_var)
        skills_entry.grid(row=6, column=1, pady=5)

        # Experience Details
        experience_label = ttk.Label(self.root, text="Experience Details", font=("Helvetica", 16))
        experience_label.grid(row=7, column=0, columnspan=2, pady=10)

        # Add experience entry button
        add_experience_button = ttk.Button(self.root, text="Add Experience", command=self.add_experience_entry)
        add_experience_button.grid(row=8, column=0, columnspan=2, pady=5)

        # Projects Details
        projects_label = ttk.Label(self.root, text="Projects Details", font=("Helvetica", 16))
        projects_label.grid(row=9, column=0, columnspan=2, pady=10)

        # Add projects entry button
        add_projects_button = ttk.Button(self.root, text="Add Projects", command=self.add_projects_entry)
        add_projects_button.grid(row=10, column=0, columnspan=2, pady=5)

        # Achievements
        achievements_label = ttk.Label(self.root, text="Achievements:")
        achievements_label.grid(row=11, column=0, sticky="e")
        achievements_entry = ttk.Entry(self.root, textvariable=self.achievements_var)
        achievements_entry.grid(row=11, column=1, pady=5)

        # Activities
        activities_label = ttk.Label(self.root, text="Activities:")
        activities_label.grid(row=12, column=0, sticky="e")
        activities_entry = ttk.Entry(self.root, textvariable=self.activities_var)
        activities_entry.grid(row=12, column=1, pady=5)

        # Generate Resume Button
        generate_button = ttk.Button(self.root, text="Generate Resume", command=self.generate_resume)
        generate_button.grid(row=13, column=0, columnspan=2, pady=10)

    def add_education_entry(self):
        # Add entry for education details
        education_frame = ttk.Frame(self.root)
        education_frame.grid(row=len(self.education_entries) + 6, column=0, columnspan=2, pady=5)

        level_label = ttk.Label(education_frame, text="Level:")
        level_label.grid(row=0, column=0, sticky="e")
        level_entry = ttk.Entry(education_frame)
        level_entry.grid(row=0, column=1, pady=5)

        institution_label = ttk.Label(education_frame, text="Institution:")
        institution_label.grid(row=1, column=0, sticky="e")
        institution_entry = ttk.Entry(education_frame)
        institution_entry.grid(row=1, column=1, pady=5)

        field_label = ttk.Label(education_frame, text="Field:")
        field_label.grid(row=2, column=0, sticky="e")
        field_entry = ttk.Entry(education_frame)
        field_entry.grid(row=2, column=1, pady=5)

        duration_label = ttk.Label(education_frame, text="Duration:")
        duration_label.grid(row=3, column=0, sticky="e")
        duration_entry = ttk.Entry(education_frame)
        duration_entry.grid(row=3, column=1, pady=5)

        score_label = ttk.Label(education_frame, text="Score:")
        score_label.grid(row=4, column=0, sticky="e")
        score_entry = ttk.Entry(education_frame)
        score_entry.grid(row=4, column=1, pady=5)

        entry = {"level": level_entry, "institution": institution_entry, "field": field_entry,
                 "duration": duration_entry, "score": score_entry}
        self.education_entries.append(entry)

    def add_experience_entry(self):
        # Add entry for experience details
        experience_frame = ttk.Frame(self.root)
        experience_frame.grid(row=len(self.experience_entries) + 8, column=0, columnspan=2, pady=5)

        job_role_label = ttk.Label(experience_frame, text="Job Role:")
        job_role_label.grid(row=0, column=0, sticky="e")
        job_role_entry = ttk.Entry(experience_frame)
        job_role_entry.grid(row=0, column=1, pady=5)

        company_name_label = ttk.Label(experience_frame, text="Company Name:")
        company_name_label.grid(row=1, column=0, sticky="e")
        company_name_entry = ttk.Entry(experience_frame)
        company_name_entry.grid(row=1, column=1, pady=5)

        description_label = ttk.Label(experience_frame, text="Description:")
        description_label.grid(row=2, column=0, sticky="e")
        description_entry = ttk.Entry(experience_frame)
        description_entry.grid(row=2, column=1, pady=5)

        entry = {"job_role": job_role_entry, "company_name": company_name_entry, "description": description_entry}
        self.experience_entries.append(entry)

    def add_projects_entry(self):
        # Add entry for projects details
        projects_frame = ttk.Frame(self.root)
        projects_frame.grid(row=len(self.projects_entries) + 10, column=0, columnspan=2, pady=5)

        name_label = ttk.Label(projects_frame, text="Name:")
        name_label.grid(row=0, column=0, sticky="e")
        name_entry = ttk.Entry(projects_frame)
        name_entry.grid(row=0, column=1, pady=5)

        description_label = ttk.Label(projects_frame, text="Description:")
        description_label.grid(row=1, column=0, sticky="e")
        description_entry = ttk.Entry(projects_frame)
        description_entry.grid(row=1, column=1, pady=5)

        entry = {"name": name_entry, "description": description_entry}
        self.projects_entries.append(entry)

    def get_user_input(self):
        # Collect user input from the UI
        user_details = {
            "name": self.name_var.get(),
            "email": self.email_var.get(),
            "mobile": self.mobile_var.get(),
            "education": [],
            "skills": self.skills_var.get(),
            "experience": [],
            "projects": [],
            "achievements": self.achievements_var.get(),
            "activities": self.activities_var.get()
        }

        # Collect education details
        for entry in self.education_entries:
            user_details["education"].append({
                "level": entry["level"].get(),
                "institution": entry["institution"].get(),
                "field": entry["field"].get(),
                "duration": entry["duration"].get(),
                "score": entry["score"].get()
            })

        # Collect experience details
        for entry in self.experience_entries:
            user_details["experience"].append({
                "job_role": entry["job_role"].get(),
                "company_name": entry["company_name"].get(),
                "description": entry["description"].get()
            })

        # Collect projects details
        for entry in self.projects_entries:
            user_details["projects"].append({
                "name": entry["name"].get(),
                "description": entry["description"].get()
            })

        return user_details

    def generate_resume(self):
        # Generate the resume and save as PDF
        user_details = self.get_user_input()
        resume = Resume(**user_details)
        markdown_text = resume.generate_markdown()

        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            convert_markdown_to_pdf(markdown_text, Resume_file=file_path)
            messagebox.showinfo("Resume Generated", f"Resume saved at: {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeGeneratorGUI(root)
    root.mainloop()
