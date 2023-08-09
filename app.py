from pathlib import Path
import streamlit as st
from PIL import Image

#--path settings
current_dir=Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file=current_dir/"main.css"
resume_file=current_dir/"cv.pdf"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Tanushree Pandey"
PAGE_ICON = ":wave:"
NAME = "Tanushree Pandey"
DESCRIPTION = """
Aspiring Software Developer
"""
EMAIL = "tanupandey1616@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn":"https://linkedin.com/in/tanushreepandey1616",
    "GitHub": "https://github.com/Tanu1616",

}
PROJECTS = {
    "🏆 Cyber-Store-It is an Gadgets Ecommerce website .":"https://github.com/Tanu1616/Cyber-Store",
    "🏆 Chit-Chat-Store-It is an chatting App .":"https://github.com/Tanu1616/Chit-Chat",
    "🏆 Voice Assistant- It is a desktop application bascially works on voice command.":"https://github.com/Tanu1616/Voice_assistant",
    "🏆 Heath Insurance- It is an backend application works to predict the price of health insurance.":"https://github.com/Tanu1616/Health_Insurance",
    "🏆 Handwritten digit Recognition-It predict whatever number we write in alphabates.":"https://github.com/Tanu1616/handwritten_digitrecognition",
    

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")


with col1:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: C,Java,Python (Basic)
- 📊 Frontend- HTML,CSS
- 📊 Backend - MySQL
- 📚 Data Visulization: Plotly
- 📚 Machine Learning -Classification,Clustering
- 🗄️ Data Science - numpy,pandas,matplotlib,
"""
)

# --- Educations ---
st.write('\n')
st.subheader("Education")

st.write(
    """
- 🎓 Birla Institute Of Technology,Mesra, Ranchi                                  
       2021-23 | M.C.A. - Computer Applications | CGPA: 8.31 / 10.00
- 🎓 156-GOVT. P.G. College,Pipariya 
       2017-20 | B.C.A. - Computer Applications | Percentage : 71.20 / 100.00
- 🎓 BEERSHEBA INT.SCHOOL,PIPARIA,HOSHANGABAD,M.P, Pipariya
       2017 | 12th| CBSE | Percentage: 58.20 / 100.00
- 🎓 BEERSHEBA INT. SCHOOL,PIPARIYA,HOSHANGABAD,M.P, Pipariya 
       2015  | 10th| CBSE | Percentage: 72.20 / 100.00 
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- Internship
st.write("🚧", "**Machine Learning Trainee | Skill Vertex**")
st.write("05 Jul, 2022 - 05 Aug, 2022")
st.write(
    """
- ► Learns different Libraries of python
- ► Made projects using these libraries
"""
)
st.write('\n')
st.subheader("Qualities")
st.write(
    """
- ✔️ Class Representative Of BIT Mesra MCA Batch 2021-23
- ✔️ Organizing Events in College.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")











