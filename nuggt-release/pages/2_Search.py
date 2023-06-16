from nuggt import *
import os
from helper.sidebar_functions import sidebar_logo

form_url = os.getenv("FORM_URL")
firstFieldKey = os.getenv("FIRST_FIELD_KEY")
secondFieldKey = os.getenv("SECOND_FIELD_KEY")
thirdFieldKey = os.getenv("THIRD_FIELD_KEY")
fourthFieldKey = os.getenv("FOURTH_FIELD_KEY")

sidebar_logo("assets/nuggt-logo.png")

print(form_url)
print(firstFieldKey)
print(secondFieldKey)
print(thirdFieldKey)
print(fourthFieldKey)

user_input = """Find websites related to {text:query} using {tool:google}. Browse three results to gather information on {text:query} using {tool:browse_website}. Display the results in the format <Content: Content of the website, URL: URL of the website> using {tool:display}"""

output_format = "I have displayed the results in the given format."


st.subheader("Search")
st.markdown("**Ask a query and Nuggt would provide you answers along with the relevant sources. This app was created with a single AI command,**")
st.markdown("""Find websites related to **:blue[{ text : query }]** using **:green[{ tool : google }]**. Browse three results to gather information on **:blue[{ text : query }]** using **:green[{ tool : browse_website }]**. Display the results in the format **<Content: Content of the website, URL: URL of the website>** using **:green[{ tool : display }]**  \n
""")
        
if user_input and output_format:
    variables = extract_variables(user_input)
    nuggt(user_input, output_format, variables)