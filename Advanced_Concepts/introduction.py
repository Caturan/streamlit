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


"""
## Session State

Session State provides a dictionary-like interface where we can save information that is preserved between script reruns. 
Use st.session_state with key or attribute notation to store and recall values. For example, st.session_state["m_key] or st.session_state.my_key. 
Remember that widgets handle their statefulness all by themselves, so you won't always need to use Session State!

### What is a session? 
A session is a single instance of viewing an app. If you view an app from two different tabs in your browser, each tab will have its own session. So each viewer of an app will have a Session State tied to their specific view. 
Streamlit maintains this session as the user interacts with the app. If the user refreshes their browser page or reloads the URL to the app,
their Session State resets and they begin again with a new session.
"""
if "counter" not in st.session_state:
    st.session_state.counter = 0 
st.session_state.counter += 1 

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

"""
There are a few common scenarios where Session State is helpful. As demonstrated above, Session State is used when you have a progressive process that you want to build upon from one rerun to the next. Session State can also be used to prevent recalculation, similar to caching. 
However, the differences are important:
- Caching associates stored values to specific functions and inputs. Cached values are accessible to all users across all sessions.
- Session State associates stored values to keys (strings). Values in session state are only available in the single session where it was saved.


If you have random number generation in your app, you'd likely use Session State. Here's an example where data is generated randomly at the beginning of each session. By saving this random information in Session State,
 each user gets different random data when they open the app but it won't keep changing on them as they interact with it. 
If you select different colors with the picker you'll see that the data does not get re-randomized with each rerun. (If you open the app in a new tab to start a new session, you'll see different data!)
"""
import pandas as pd 
import numpy as np 

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20,2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)


"""
If you are pulling the same data for all users, you would likely cache a function that retrieves that data.
On the other hand, if we pull data specific to a user, such as querying their personal information, we may want to save that in Session State.
That way, the queried data is only available in that one session.
"""