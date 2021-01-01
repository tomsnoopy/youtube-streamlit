import streamlit as st
import numpy as np
import pandas as pd

st.title('streamlit 超入門2') #タイトルを付けたいときは、.titleをつければよい

st.write('DataFrame') #本文を追加したいときは、.writeをつければよい

#pythonと同じように簡単に表を作ることができる。しかもソートもできる
df = pd.DataFrame( {
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30 ,40]
})

st.write(df)

#writeは表の大きさを指定できないが、dataframeは表の大きさを指定することができる
st.dataframe(df.style.highlight_max(axis = 0), width = 1000, height = 1000)

#tableでも表を作成することができる。これは静的な表を作りたいときに使用する
#表の作成方法は、refrence guide > API reference > display dataに細かく記載されている
st.table(df) 

#マークダウンを使うこともできる→"""とダブルクォーテーションを3つで囲む
#```を3つ並べると、「pythonのコードを書くよ」というメッセージになる
#マジックコマンドの作成方法は、refrence guide > API reference > display textに細かく記載されている

"""
 # 章
 ## 節
 ### 項

 ```python
 import streamlit as st
 import numpy as np
 import pandas as pd

"""

#チャートを書く
df = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c']
)
df

#チャートの作成方法は、refrence guide > API reference > display chartに細かく記載されている
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)


#マップをプロットする
df = pd.DataFrame(
    np.random.rand(100,2)/ [50,50]  +[35.69,139.70],
    columns = ['lat','lon']
)
st.map(df)

#画像を表示させる
#まず、PILをインポートする
from PIL import Image

st.write('Display Image')
#同階層のフォルダにある写真を指定する
img = Image.open('sample.png')

#st.imageで写真を表示させる
#チャートの作成方法は、refrence guide > API reference > display mediaに細かく記載されている
st.image(img, caption = "tom", use_column_width = True)  #use_column_width = Trueは写真の幅に合わせて表示してくれる

#インタラクティブなウィジェットを作成する
#チェックボックスありなしで画像を表示させる

st.write('Display Image')
if st.checkbox('Show Image'):
    img = Image.open('sample.png')
    st.image(img, caption = "tom", use_column_width = True)  #use_column_width = Trueは写真の幅に合わせて表示してくれる

#セレクトボックスによる値の動的な表示
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)
'あなたが好きな数字は、', option ,'です。'


#テキスト入力による動的な表示
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味は', text ,'です。'


#スライダーによる動的な表示
#これらの動的な表示は、API reference > display interactive widgetsに記載されている。
condition = st.slider('あなたの今の調子は？',0,100,50)
'あなたのコンディションは、', condition 

#レイアウトを整える
#サイドバーを追加する

# text1 = st.sidebar.text_input('あなたの趣味を教えてください')
# condition1 = st.sidebar.slider('あなたの今の調子は？',0,100,50)

# #sidebarを入れていないから、メインのところに表示される
# 'あなたの趣味は', text1 ,'です。' 
# 'あなたのコンディションは、', condition1

# コメントアウトする練習
# コメントアウトする練習

#2カラムレイアウトにする
left_column, right_column = st.beta_columns(2) #()内を3，4とすればカラム数を増やすことができる
button = left_column.button('ここは左カラムです')  #buttonでボタンを表示することができる
if button:
    right_column.write('ここは右カラムです')

#エキスパンダーを作成する
expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3')

#プログレスバーを作成する
import time

st.write('プログレスバーの表示')
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteretion{i+1}')
    bar.progress(i+1)
    time.sleep(0.1) #timeで「何秒ごとに表示させる」という指示になる。

"Done!!!!"

#アプリへの公開