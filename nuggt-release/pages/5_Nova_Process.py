from nuggt import *
from helper.sidebar_functions import sidebar_logo

sidebar_logo("assets/nova-process-logo.png")

user_input = """Unpack the problem: {text:problem_description} using {tool:nova_process}. Assemble expertise needed for {text:skills_needed} using {tool:nova_process}. Collaboratively ideate to generate a solution using {tool:nova_process}."""

output_format = "The Nova Process has generated a solution."

st.subheader("Nova Process")
st.markdown("**Define a problem and Nova Process will guide through unpacking the problem, assembling expertise and collaboratively ideating for a solution.**")
st.markdown("""Unpack the problem: **:blue[{ text:problem_description }]** using **:green[{ tool:nova_process }]**. Assemble expertise needed for **:blue[{ text:skills_needed }]** using **:green[{ tool:nova_process }]**. Collaboratively ideate to generate a solution using **:green[{ tool:nova_process }]**.  \n""")

if user_input:
    variables = extract_variables(user_input)
    
    # Problem Unpacking
    problem_key_phrases = problem_unpacking(variables)
    
    # Expertise Assembly
    assigned_roles_identifiers = expertise_assembly(variables.get('skills_needed'))
    
    # Collaborative Ideation
    solution = collaborative_ideation(problem_key_phrases, assigned_roles_identifiers)
    
    st.markdown("**Solution:** {}".format(solution))
