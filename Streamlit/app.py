import streamlit as st
import pandas as pd

def home():
    st.title("Home")

    st.header("Different Widgets in Streamlit")
    st.divider()

    st.caption('Text:')
    st.write('Hello, World!')

    st.divider()

    st.caption('Slider:')
    st.slider('Select a number',1,50)

    st.divider()

    st.caption('Code:')
    code="""
    #include<stdio.h>
    #include<conio.h>

    void main()
    {
        clrscr();
        printf("Hello, World!");
        getch();
    }
    """
    st.code(code,language='c')

    st.divider()

    st.caption('& more....')

def plot():
    st.title("Plot")
    st.caption("Here you can upload a csv data file and plot your data.")

    file=st.file_uploader("Choose a csv file",type='csv')

    if file is not None:
        df=pd.read_csv(file)
        st.write("File Uploaded!")

        if st.button("Preview Data"):
            st.write(df.head())
        if st.button("Summarize Data"):
            st.write(df.describe())
        
        st.divider()

        st.header("Filter Data")
        columns=df.columns.tolist()
        selected_col=st.selectbox("Select column to filter",columns)
        unique_values =df[selected_col].unique()
        selected_values=st.selectbox("Select a value",unique_values)
        filtered_df=df[df[selected_col]==selected_values]
        st.dataframe(filtered_df)

        st.divider()
        
        st.subheader("Streamlit Bar Chart")
        st.bar_chart(df.set_index('City')['Rainfall'],x_label='City',y_label='Rainfall')

        st.divider()

        st.subheader("Streamlit Line Chart")
        x_col=st.selectbox("Select x-axis",columns)
        y_col=st.selectbox("Select y-axis",columns)
        st.line_chart(filtered_df.set_index(x_col)[y_col])

        

def main():
    st.sidebar.subheader("Streamlit")
    page=st.sidebar.radio("Pages:",["Home","Plot"])

    if page=="Home":
        home()
    if page=="Plot":
        plot()

if __name__=='__main__':
    main()