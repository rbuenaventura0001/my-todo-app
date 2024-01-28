import streamlit as st
import functions

todos = functions.get_todos()


# st.set_page_config(layout="wide")
# can use this to configure web app

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>."
         " The way to use this app is to enter your task for the day in the input box below and press the enter key."
         " If you would like to complete the task simply click the checkbox next to the task you want to complete."
         " This is a group effort so don't complete the task unless it is agreed upon. A chatbox will be added later so"
         " we can use that to communicate. Thanks for using the app. Let's get going!",
         unsafe_allow_html=True)

# can use html code to customize web app

st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



# changes to file
