import streamlit as st
formbtn = st.button("Form")
if "formbtn_state" not in st.session_state:
    st.session_state.formbtn_state = False
if formbtn or st.session_state.formbtn_state:
    st.session_state.formbtn_state = True
    st.subheader("User Info Form")
    with st.form(key='user_info'):
        st.write('User Information')
        name = st.text_input(label="Name :")
        phone = st.text_input(label="Phone :")
        dno = st.text_input(label="No of Tickets Required :")
        submit_form = st.form_submit_button(label="Register", help="Click to register!")
        if submit_form:
            st.write(submit_form)
            if name and phone and dno:
                st.success(
                    f"ID:  \n Name: {name}  \n Phone: {phone}  \n No Of Ticket: {dno}"
                )
            else:
                st.warning("Please fill all the fields")