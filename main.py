import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit \n')
st.title('超超超・超超超・超超超超超入門')



#----------------------------------------------------------------------
#st.write('Display Image')

# if st.checkbox('Show Image'):
#     img = Image.open('nuko.jpg')
#     st.image(img, caption='N U K O', use_column_width=True)

#----------------------------------------------------------------------
#st.sidebar.write('Interactive Widgets')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問合わせ1')
expander1.write('問い合わせ1の回答を書く')
expander2 = st.expander('問合わせ2')
expander2.write('問い合わせ2の回答を書く')
expander3 = st.expander('問合わせ3')
expander3.write('問い合わせ3の回答を書く')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。 ',
#     list(range(1,11))
# )
#'あなたの好きな数字は、', option, 'です。'


#----------------------------------------------------------------------
#st.write('DataFrame')

#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns = ['a', 'b', 'c']
#)


#st.table(df.style.highlight_max(axis=0))

#st.line_chart(df)

#st.area_chart(df)

#st.bar_chart(df)

#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns = ['lat', 'lon']
#)

#st.map(df)

