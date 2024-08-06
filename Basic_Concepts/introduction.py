"""

streamlit run your_script.py

"""

# Display and style data
"""

There are a few ways to display data (tables, arrays, data frames) in Streamlit apps. 
Below, we will be introduces to magic and st.write(), which can be used to write anything from text to tables. 


"""

# Use magic 
"""

We can also write to our app without calling any Streamlit methods. Streamlit supports "magic commands", 
which means we dont have to use st.write() at all!!

"""

"""
# My first app 
Here's our first attempt at using data to create a table:
"""
import streamlit as st 
import pandas as pd 

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

df

"""

Any time that Streamlit sees a variable or a literal value on its own line, 
it automatically wirtes that to our app using st.write(). 

"""

"""

# Write a data frame
Along with magic commands, st.write() is Streamlit's "Swiiss Army knife". 
We can pass almost anything to st.write(): text data, Matplotlib figures, Altair charts, and more. 

"""
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


"""

There are other data specific functions like st.dataframe() and st.table() that we can also use for displaying data.
Let's understand when to use these features and how to add colors and styling to our data frames. 

We might be asking ourself, "why wouldn't i always use st.write()?" There are a few reasons:
1. Magic and st.write() inspect the type of data we have passed in, and then decide how to best render it in the app. 
    Sometimes we want to draw it another way. For example, instead of drawing a dataframe as an interactive table, 
    we may want to draw it as a static table using st.table(df).

2. The second reason is that other methods return an object that can be used and modified, either by adding data to it or replacing it. 

3. Finally, if we use a more specific Streamlit method we can pass additional arguments to customize its behaviour. 

For example, let's create a data frame and change its formatting with a Pandas Styler object. 
In this example, we will use Numpy to generate a random sample, and the st.dataframe() method to draw an interactive table. 
    
"""
import numpy as np 
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

"""
Let's expand on the first example using the Pandas Styler object to highlight some elements in the interactive table. 
"""
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))

"""

Streamlit also has a method for static table generation: st.table().

"""
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.table(dataframe)


"""

# Draw charts and maps 
Streamlit supports several popular data charting libraires like Matplotlib, Altair, deck.gl, and more. 
In this section, we will add a bar chart, line chart, and a map to our app. 

## Draw a line chart 
We can easliy add a line chart to our app with st.line_chart(). We will generate a random sample using Numpy and then chart it. 

"""
chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns=['c', 'a', 't']
)
st.line_chart(chart_data)


"""

## Plot a map 
With st.map() we can display data poits on a map. Let's use Numpy to generate some sample data and plot it on a map of San Francisco. 

"""
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [38.5, 27.7],   
    columns=['lat', 'lon']
)
st.map(map_data)


"""

# Widgets
When we have got the data or model into the state that we want to  explore, 
we can add in widgets like st.slider(), st.button() or st.selectbox(). 
It, really straightforward-treat widgets as variables:

"""
x = st.slider('x')
st.write(x, 'squared is', x * x)

"""

Widgets can also be accessed by key, if we choose to specify a string to use as the unique key for the widget:

"""
st.text_input("Your name", key="name")

# We can access the value at any point with:
st.session_state.name

"""
Every widget with a key is automatically added to Session State.
"""

"""
# Use checkboxes to show/hide data 

One use case for checkboxes is to hide or show a specific chart or section in an app. 
st.checkbox() takes a single argument, which is the widget label. 
In this sample, the checkbox is used to toggle a conditional statement. 

"""
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
        )

    chart_data


"""
# Use a selectbox for options 

Use st.selectbox to choose from a series. We can write in the options we want, 
or pass through an array or data frame column. 

Let's use the df data frame we created earlier. 
"""
df = pd.DataFrame({
    'first column': [7, 19, 22, 10],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best',
    df['first column']
)
'You selected: ', option

"""
Another sample for the selectbox()
"""
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
    index=None,
    placeholder="Select contact method..."
)
st.write("You selected: ", option)


"""
# Layout 

Streamlit makes it easy to organize our widgets in a left panel sidebar with st.sidebar. 
Each elemet that's passed to st.sidebar is pinned to the left, allowing users to focus on the content in our app while still having access to UI controls. 

For example, if we want to add a selectbox and a slider to a sidebar, use st.sidebar.slider and st.sidebar.selectbox instead of st.slider and st.selectbox:

"""
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


"""
Beyond the sidebar, Streamlit offers several other ways to control the layout of our app. 
st.columns lets we place widgets side-by-side, and st.expander lets we conserve space by hiding away large content. 
"""
left_column, right_column = st.columns(2)
# We can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call streamlit functions inside a "with" blocks:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


"""
st.expander sample:
"""
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *quaranteed* to be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")



"""
# Show progress

When adding long running computations to an app, we can use st.progres() to display status in real time. 

Firsti let's important time. We'are going to use the time.sleep() method to simulate a long running computation:
"""
import time 

'Starting a long computation...'

# Add a placeholder 
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration. 
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'... and now we\'re done! '