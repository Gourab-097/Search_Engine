import streamlit as st

# --- Company Name at top-left ---
# st.write("cts")
# st.markdown(
#     """
#     <div style="text-align: left; font-size:24px; font-weight:bold; color:#2C3E50;">
#         Cognizant
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# Control which screen is shown
if "page" not in st.session_state:
    st.session_state.page = "home"

# --------------- SCREEN 1 ----------------
if st.session_state.page == "home":

    st.subheader("⚖️ Legal AI Assistant")
    st.title("What legal task can AI help today?")

    if st.button("Ask a legal question"):
        st.session_state.page = "button1"

    if st.button("Generate a draft"):
        st.write("to be implemented")

    if st.button("Summarize a case"):
        st.write("to be implemented")

# --------------- SCREEN 2 ----------------
# ask a legal question
elif st.session_state.page == "button1":

    # Sidebar (only on this screen)
    st.sidebar.title("Advanced Options")
    territory = st.sidebar.selectbox("Choose Territory", ["United States", "Canada"])
    
    if territory == "United States":
        us_jurisdictions = ["Alabama","Alaska","Arizona","Arkansas","California",
                            "Colorado","Connecticut","Delaware","Florida","Georgia",
                            "Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas",
                            "Kentucky","Louisiana","Maine","Maryland",
                            "Massachusetts","Michigan","Minnesota","Mississippi",
                            "Missouri","Montana","Nebraska","Nevada","New Hampshire",
                            "New Jersey","New Mexico","New York","North Carolina",
                            "North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
                            "Rhode Island","South Carolina","South Dakota",
                            "Tennessee","Texas","Utah","Vermont","Virginia",
                            "Washington","West Virginia","Wisconsin","Wyoming"]
        jurisdiction = st.sidebar.selectbox("Select a Jurisdiction: ", us_jurisdictions)
    elif territory == "Canada":
        ca_jurisdictions = ["Alberta","British Columbia","Manitoba","New Brunswick",
                            "Nova Scotia","Ontario","Prince Edward Island","Quebec",
                            "Saskatchewan","Nunavut","Yukon"]
        jurisdiction = st.sidebar.selectbox("Select a Jurisdiction: ", ca_jurisdictions)

    search_type = st.sidebar.radio("Search Alogoritm: ", ["Lexical", "Semantic", "Hybrid"])
    if search_type == "Lexical":
        st.sidebar.number_input("BM25 Threshold: ", min_value=36.0, max_value=200.0, 
                                value=51.4, step=0.1, format="%.f")
    elif search_type == "Semantic":
        st.sidebar.number_input("KNN Threshold: ", min_value=0.0, max_value=1.0, 
                                value=0.75, step=0.1, format="%.f")
    else:
        st.sidebar.number_input("BM25 Threshold: ", min_value=36.0, max_value=200.0, 
                                value=51.4, step=0.1, format="%.f")
        st.sidebar.number_input("KNN Threshold: ", min_value=0.0, max_value=1.0, 
                                value=0.75, step=0.1, format="%.f")
        st.sidebar.number_input("Hybrid Weight: ", min_value=0.0, max_value=10.0, 
                                value=6.5, step=0.1, format="%.f")

    st.subheader("⚖️ Legal AI Assistant")
    st.title("Ask your legal question")

    user_query = st.text_input(
        "Your question",
        placeholder="Type your legal question here..."
    )

    if user_query.strip():
        if st.button("Submit"):
            st.success("Query submitted")
            # st.write("You asked:")
            # st.write(user_query)

    if st.button("⬅ Back"):
        st.session_state.page = "home"

