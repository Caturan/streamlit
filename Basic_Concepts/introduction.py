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