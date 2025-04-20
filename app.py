# https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart
# https://github.com/streamlit/streamlit/issues/455#issuecomment-1811044197

import os
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_pickle(os.path.join('data', 'embedded.pkl'))
    return df


def main():
    df = load_data()

    st.title("UMAP Plot Interactive")

    color_map = {
    'sdss': 'pink',
    'AGNrt': 'red',
    'NOAGNrt': 'green',
    'TNG100': 'cyan',
    'TNG50': 'purple',
    'UHDrt': 'black',
    'n80rt': 'orange'
}

    fig = px.scatter(df, x='f0', y='f1', color='label', color_discrete_map=color_map, hover_name='filename')

    col1, col2 = st.columns([4, 1])  

    with col1:
        current_dict = st.plotly_chart(fig, on_select='rerun', selection_mode='points')

    click_check = current_dict['selection']['point_indices']
    if click_check:
        image_path = current_dict['selection']['points'][0]['hovertext']
        with Image.open(image_path) as img:
            with col2:
                st.image(img, caption=f'{image_path}')

        st.write(current_dict)



if __name__ == "__main__":
    main()
