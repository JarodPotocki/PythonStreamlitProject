"""
Class:\tCS230 — Section HB1S
Name:\tJarod Potocki
\tI pledge that I have completed the programming assignment independently.
\tI have not copied the code from a student or any other source.
\tI have not given my code to any student.
"""
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk
import streamlit as st

print(__doc__)

print("Exercise #1: Final Project ")

DATA_URL = "C:/Users/Jarod Potocki/PycharmProjects/CS230/skyscrapers (1).csv"


def read_data(fileName):
    df = pd.read_csv(fileName)
    lst = []

    columns = ['Name', ' Metres', 'Year', 'City', 'Lat', 'Lon']

    for index, row in df.iterrows():
        sub = []
        for col in columns:
            index_no = df.columns.get_loc(col)
            sub.append(row[index_no])
        lst.append(sub)

    return lst


print(read_data(DATA_URL))

st.echo()
def metres(data):
    metres = []

    for i in range(len(data)):
        if data[i][1] not in metres:
            metres.append(int(data[i][1]))

    return metres


def names(data):
    names = []

    for i in range(len(data)):
        if data[i][0] not in names:
            names.append(data[i][0])

    return names


def combine(data, lst1, lst2):
    name_feet_dict = {}
    for key in lst1:
        for value in lst2:
            name_feet_dict[key] = value
            lst2.remove(value)

    return name_feet_dict


def bar_chart(name_metres_dict):
    x = (name_metres_dict.keys())
    y = (name_metres_dict.values())

    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.ylabel('metres')
    plt.xlabel('skyscraper')
    plt.show()


def map(data, name, year):
    data2 = pd.read_csv(DATA_URL, encoding = 'utf-8')
    map_df = data2[['Name', 'Lat', 'Lon']]
    map_df.rename(columns={'Lat': 'lat', 'Lon': 'lon'}, inplace=True)
    view_state = pdk.ViewState(latitude=map_df['lat'].mean(), longitude=map_df['lon'].mean, zoom=10, pitch=0)
    layer = pdk.Layer('ScatterplotLayer', data=map_df, get_position=['lon', 'lat'], get_radius=50,
                      get_color=[0, 255, 255], pickable=True)


    st.map(map_df)


def main():
    data = read_data(DATA_URL)
    data2 = pd.read_csv(DATA_URL)

    st.title('Skyscrapers Across the World!')
    st.write('Here are some of the tallest skyscrapers across the world')

    names_select = st.sidebar.multiselect('Select name of buildings you want to see', names(read_data(DATA_URL)))
    yearlimit = st.sidebar.slider('Set Year Limit', 1900, 2021, 2000)

    st.write('Map of Buildings')
    map(data, names_select, yearlimit)
    st.write('\nHeight of Buildings')

    st.pyplot(bar_chart(combine(data, names_select, metres(read_data(DATA_URL)))))
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.write("Here is a little quiz")
    form = st.form(key='my-form')
    name = form.text_input('Name a tower in New York City')
    submit = form.form_submit_button('Submit')
    if submit:
        if name == "Empire State Building".lower() or name == 'One World Trade Center'.lower() or name == 'Central Park Tower'.lower() or name == '111 West 57th St'.lower() or name == 'One Vanderbuilt'.lower() or name == '432 Park Avenue'.lower() or name == 'Two World Trade Center'.lower() or name == '30 Hudson Yards'.lower() or name == 'Bank of America Tower'.lower():
            st.write(f'YES, {name} is in New York City')
        else:
            st.write(f'NO, {name} is not in New York City')
    else:
        pass


main()
