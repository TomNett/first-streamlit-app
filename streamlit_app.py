import streamlit as st
#set the app to be the full page width
st.set_page_config(layout="wide")
background_image = '''
<style>
body {
background-image: url("https://www.lefthudson.com/wp-content/uploads/2019/11/soccer-field-wallpapers-lovely-backgrounds-real-madrid-2017-wallpaper-cave-this-week-of-soccer-field-wallpapers.jpg");
background-size: cover;
}
</style>
'''
st.markdown(background_image, unsafe_allow_html=True)
st.markdown("<style> body {color: white;}</style>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; margin-top: 15px;'>Streamlit Example Soccer Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<style> .css-18c15ts {padding-top: 1rem; margin-top:-75px;} </style>", unsafe_allow_html=True)
left_column, right_column = st.beta_columns(2)
left_column.text(' ')
left_column.text(' ')
left_column.text(' ')
left_column.text('Choose A Player for Analysis:')

# Space out the maps so the second one is 3x the size of the other three
player_image_container, horizontal_bar_container = st.columns((1, 3))
player_image_container.text(' ')
player_image_container.text(' ')
player_image_container.text(' ')
with player_image_container:
    st.image(get_and_display_player_image(epl_strikers_df, player), width=300)
with horizontal_bar_container:
    st.plotly_chart(plot_horizontal_bar(epl_strikers_df, player), 
                    use_container_width=True
    )
line_plot_container, scatter_plot_container = st.columns(2)
with line_plot_container:
    st.plotly_chart(plot_line_plot(epl_strikers_df, player),
                    use_container_width=True
   )
with scatter_plot_container:
    st.plotly_chart(plot_scatter_plot(epl_strikers_df,player),
                  use_container_width=True
    )
