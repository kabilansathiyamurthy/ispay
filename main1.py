import time
import streamlit as st
import pyqrcode
from PIL import Image
a = "upi://pay?pa=kabilansathiya12345@oksbi&am="
b = ".00&cu=INR"
op =  ["Please Select the Service type","Free Darshan","Special Darshan (50)" ,"VIP Darshan (100)" ,"Vehicle pooja (2 - Wheeler) (100)", " Vehicle Pooja (4 - Wheeler & Above) (200) "]
col1, col2, col3 = st.columns(3)
with col1:
    st.write('       ')
with col2:
    st.image("003.png")
with col3:
    st.write('       ')
def run1():
    st.empty()
    rate = 0
    rate2 = 0
    choice = st.selectbox("Enter the Service Type :",op)
    ch1=len(choice)
    st.write(f"You have entered the option: {choice} ")
    if ch1 == 12:
        pass
    elif ch1 == 20:
        rate += 50
    elif ch1 == 17:
        rate += 100
    elif ch1 == 33:
        rate += 100
    elif ch1 == 43:
        rate += 200
    else:
        exit()
    st.subheader("User Info Form")
    with st.form(key='user_info'):
        st.write('User Information')
        name = st.text_input(label="Name :")
        phone = st.text_input(label="Phone :")
        dno = st.number_input(label="No of Tickets Required :",value=0)
        submit_form = st.form_submit_button(label="Submit", help="Click to register!")
        rate = rate * dno
        if submit_form:
            bar = st.progress(20)
            time.sleep(0.2)
            bar.progress(40)
            time.sleep(0.2)
            bar.progress(60)
            time.sleep(0.2)
            bar.progress(80)
            time.sleep(0.2)
            bar.progress(100)
            if name and phone and dno:
                st.success(
                    f"Details:  \n Name : {name}  \n Phone: {phone}  \n No Of Ticket: {dno}  \n Total Amount: {rate}"
                )
                if ch1 == 12:
                    rate3 = str(rate)
                else:
                    rate2 = str(rate)
                    final = a + rate2 + b
                    qr1 = pyqrcode.create(final)
                    qr1.png("001.png", scale=100)
                    c = Image.open("001.png")
                    st.image('001.png')
                    with st.spinner(text='In Progress'):
                        time.sleep(1)
                        st.form_submit_button(label="Payment Completed", help="Click to Complete")
            else:
                st.warning("Please fill all the fields")
    if st.button("Continue"):
        run1()
        pass
    if st.button("Exit"):
        exit()
def run2():
        run1()
if __name__ == "__main__":
    run1()