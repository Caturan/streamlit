"""
# Advanced Concept of Streamlit 

Now that we know how a Streamşlit app runs and handles data, let's talk about being efficient. 
Caching allows we to save the outpu of a function so we can skip over it on rerun. 
Session State lets we save information for each user that is preserved between reruns. 
This not only allows we to avoid unecessary recalculation, but also allows we to create dynamic pages and handle progressive processes. 
"""

"""
## Caching 

Caching allows us to app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations. 

The basic idea behinf caching is to store the results of expensive function calls and return the cached result when the same inputs occur again. 
This avoid repeated execution of a function with the same input values. 

To cache a function in Streamlit, we need to apply a caching decorator to it. We have two choices:
* st.cache_data is the recommended way to cache computations that return data. Use st.cache_data when we use a function that returns a serializable data object. 
It creates a new copy of the data at each function call, making it safe against mutaions and race conditions.

* st.cache_resource is the recommended way to cache global resources like ML models or database connections. Use st.cache_resource when our function returns unserializable objects that we don't want to load multiple times. 
It retuns the cached object itself, which is shared across all reruns and sessions without copying or duplication. 
If we mutate an object that is cached using st.cache_resource, that mutation will exist across all reruns and sessions.
"""
import streamlit as st 

@st.cache_data 
def long_running_function(param1, param2):
    return ...

"""
Before running the code, Streamlit checks its cache for a previously saved result. If yes, it will return that not rerun the function. 
During the development, the cache updates automatically as the function code changes, ensuring that the latest changes are reflected in the cache. 

st.cache_data -> anything you CAN store in a database  -- python primitives; dataframes; API calls
st.cache_resource -> anything you CAN'T store in a database  -- Ml models; database connections
"""


