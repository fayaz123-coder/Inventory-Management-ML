from unittest import result
import streamlit as st 
import pickle


pickle_in = open("C:\Works\Feynn_Intern\classifier2.pkl","rb")
classifier = pickle.load(pickle_in)

def pred(New_Release_Flag,StrengthFactor,PriceReg,ItemCount, LowUserPrice, LowNetPrice):
    prediction = classifier.predict([[New_Release_Flag,StrengthFactor,PriceReg,ItemCount, LowUserPrice, LowNetPrice]])
    print(prediction)
    return prediction


def main():



    st.title("INVENTORY MANAGMENT")
    New_Release_Flag = st.text_input("New_Release_Flag")
    StrengthFactor = st.text_input("StrengthFactor")
    PriceReg= st.text_input("PriceReg")
    ItemCount =st.text_input("ItemCount")
    LowUserPrice = st.text_input("LowUserPrice")
    LowNetPrice = st.text_input("LowNetPrice")
    
    
    if st.button("Submit"):
        result = pred(New_Release_Flag,StrengthFactor,PriceReg,ItemCount,LowUserPrice,LowNetPrice)
        st.success("The Output is{}".format(result))
        st.text("0->Demand rate is less 1 -> Demand rate is High")


if __name__== '__main__':
    main()





