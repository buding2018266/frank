import warnings
import streamlit as st

warnings.simplefilter(action="ignore", category=FutureWarning)

# Must be the first Streamlit command
# 设置页面配置，使用自适应布局以适应不同设备
st.set_page_config(
    page_title="Frank's website",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': 'Personal website built with Streamlit'
    }
)

# Import pages from the new directory
#导入文件夹里的文件
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.resume import resume_page
from page_content.contact import contact_page

# Import components
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Load custom CSS
        load_css()

        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.radio(
            "Navigation", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")

        app["function"]()
        
        # Display footer at the bottom of each page
        display_footer()

# Initialize the app
app = MultiApp()

# Add pages to the app
app.add_app("Home Page", home_page)
app.add_app("Education Page", education_page)
app.add_app("Experience Page", experience_page)
app.add_app("Resume Page", resume_page)
app.add_app("Contact Page", contact_page)

# Run the app
app.run()
