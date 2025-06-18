import streamlit as st
from PIL import Image
import webbrowser

logo_im = Image.open("./logo.png")

# ------------------ SETTINGS ------------------ #
st.set_page_config(layout="wide", page_title="Zuka Analytics", page_icon=logo_im)

profile_im = Image.open("./profile.jpg")

# ------------------ SIDEBAR ------------------ #
st.sidebar.image(profile_im, width=150)
st.sidebar.markdown("""
<style>
.sidebar-title {
    font-size: 24px;
    font-weight: bold;
    color: #4CAF50;
    margin-bottom: 10px;
}
.sidebar-subtitle {
    font-size: 16px;
    color: #333;
    margin-bottom: 10px;
}
.sidebar-links a {
    display: block;
    margin: 6px 0;
    color: #333;
    font-weight: 500;
    text-decoration: none;
}
.sidebar-links a:hover {
    color: #4CAF50;
}
</style>
<div class="sidebar-title">👩‍💻 Jesyldah W</div>
<div class="sidebar-subtitle">Data Scientist | Developer | Business Analyst</div>
<div class="sidebar-subtitle"><em>\"Turning data into decisions, and code into solutions.\"</em></div>
<div class="sidebar-links">
    <!--a href="My_CV_Amanda_Joy.pdf">📄 Download CV</a-->
    <!--a href="mailto:amanda@example.com">📧 Email</a-->
    <!--a href="https://www.linkedin.com/in/jesyldah-w-67657a72/">💼 LinkedIn</a-->
    <!--a href="https://github.com/Jesyldah">🐙 GitHub</a-->
    <!--a href="https://wa.me/2547xxxxxxx">💬 WhatsApp</a-->
</div>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&style=flat)](https://www.linkedin.com/in/jesyldah-w-67657a72/)
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github&style=flat)](https://github.com/Jesyldah)
<!--[![WhatsApp](https://img.shields.io/badge/Chat-25D366?logo=whatsapp&style=flat)](https://wa.me/2547xxxxxxx)
[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&style=flat)](mailto:amanda@example.com)-->

**🔧 Core Tools:**
Python | SQL | Streamlit | Power BI

**🔗 Quick Links**
- [🌟 Featured Projects](#featured-projects)
- [🛠️ All Projects](#all-projects)
- [🧠 Skills](#skills)
- [📄 About Me](#about-me)
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------ #
st.title("👋 Hi! I'm Jesyldah")
st.subheader("Data Scientist | Developer | Business Analyst")
st.markdown("""
Welcome to my portfolio! Here you'll find a showcase of the applications and analytics tools I've built using Streamlit, Python, and other technologies. 
Feel free to explore and reach out if you'd like to collaborate!
""")

# ------------------ FEATURED PROJECTS ------------------ #
st.markdown('<a name="featured-projects"></a>', unsafe_allow_html=True)
st.markdown("## 🌟 Featured Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(Image.open("./cashmirror.png"))
    st.markdown("**📊 M-PESA Reconciliation Tool**")
    st.caption("Automates parsing and analysis of M-Pesa PDF statements")
    if st.button("View App", key="proj1"):
        webbrowser.open_new_tab("https://cashmirror.streamlit.app//")

# with col2:
#     st.image("https://via.placeholder.com/300x180.png?text=Project+2")
#     st.markdown("**🛍️ Price Comparison App**")
#     st.caption("Compares household item prices across supermarkets")
#     if st.button("View App", key="proj2"):
#         webbrowser.open_new_tab("https://your-streamlit-app-url-2")

with col2:
    st.image(Image.open("./openaccess.png"))
    st.markdown("**🏗️ Housing Development Cost Benchmarking**")
    st.caption("Compare and benchmark housing development costs across projects and regions")
    if st.button("Explore Tool", key="proj6"):
        webbrowser.open_new_tab("https://kobov0.streamlit.app//")

with col3:
    st.image(Image.open("./nut world logo.png"))
    st.markdown("**🥜 NutsWorld Website**")
    st.caption("E-commerce site for premium cashew nuts and healthy snacks")
    if st.button("Visit Site", key="proj5"):
        webbrowser.open_new_tab("https://nutsworld.co.ke/")

# with col3:
#     st.image("https://via.placeholder.com/300x180.png?text=Project+3")
#     st.markdown("**🗜️ Poverty Prediction Map**")
#     st.caption("Visualizes poverty levels across Kenya using satellite and census data")
#     if st.button("View App", key="proj3"):
#         webbrowser.open_new_tab("https://your-streamlit-app-url-3")

# col4, col5 = st.columns(2)

# ------------------ ALL PROJECTS ------------------ #
st.markdown('<a name="all-projects"></a>', unsafe_allow_html=True)
st.markdown("## 🛠️ All Projects")

projects = [
    {"title": "M-Pesa Reconciliation Tool", "desc": "Automates parsing and analysis of M-Pesa PDF statements.", "url": "https://cashmirror.streamlit.app//"},
    {"title": "Housing Development Cost Benchmarking", "desc": "Compare and benchmark housing development costs across projects.", "url": "https://kobov0.streamlit.app/"},
    {"title": "NutsWorld Website", "desc": "E-commerce site for premium cashew nuts and healthy snacks.", "url": "https://nutsworld.co.ke/"},
    {"title": "Poverty Prediction Map", "desc": "Visualizes poverty levels across Kenya using satellite and census data.", "url": "https://zuka-analytics.streamlit.app/"},
    # {"title": "NutsWorld Website", "desc": "E-commerce platform for healthy nut-based snacks.", "url": "https://nutsworld.co.ke/"},
    # {"title": "Housing Development Cost Benchmarking", "desc": "Compare construction costs by region and building type.", "url": "https://your-housing-cost-app-url"}
]

for proj in projects:
    with st.expander(proj["title"]):
        st.write(proj["desc"])
        st.markdown(f"[View App]({proj['url']})")

# ------------------ SKILLS ------------------ #
st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
st.markdown("## 🧠 Skills & Tools")
skills = ["Python", "Streamlit", "Pandas", "SQL", "Power BI", "Excel", "Regex", "scikit-learn", "Git"]
st.write(", ".join(skills))

# ------------------ ABOUT ME ------------------ #
st.markdown('<a name="about-me"></a>', unsafe_allow_html=True)
st.markdown("## 📄 About Me")
st.write("I'm passionate about building tools that solve real-world problems using data and automation. I love working at the intersection of technology and business insight.")
