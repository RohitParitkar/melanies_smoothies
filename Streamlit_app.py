# Import python packages
import streamlit as st
# from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie!:cup_with_straw:")
st.write(
    """Choose the Fruits you want in your custom Smoothie!
    """
)

# import streamlit as st

# option = st.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone"))

# st.write("You selected:", option)

# option = st.selectbox(
#     "What is your favorite fruit?",
#     ("Banana", "Stawberries", "Peaches"))

# st.write("Your Favorite fruit is:", option)

from snowflake.snowpark.functions import col
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)

Ingredients_list =  st.multiselect(
    'Choose up to 5 ingredients: '
    , my_dataframe
)

if Ingredients_list:
    # st.write(Ingredients_list)
    # st.text(Ingredients_list)

    Ingredients_string = ''

    for fruit_chosen in Ingredients_list:
        Ingredients_string += fruit_chosen + ' '

    # st.write(Ingredients_string)


    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + Ingredients_string + """')"""

    # st.write(my_insert_stmt)
    
    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        
        st.success('Your Smoothie is ordered!', icon="✅")

    
