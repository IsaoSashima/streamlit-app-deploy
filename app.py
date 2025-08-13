import streamlit as st

st.title("サンプルアプリ②: 少し複雑なWebアプリ")

st.write("##### 動作モード1: 文字数カウント") # 「#」を付けると見出しテキストとして大きく太くなる。最大6つまで付けられ、数が少ないほどより大きく太く表示される
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("##### 動作モード2: BMI値の計算")
st.write("身長と体重を入力することで、肥満度を表す体型指数のBMI値を算出できます。")

selected_item = st.radio(
    "動作モードを選択してください。", # ラジオボタンのラベルとして上部に表示されるテキスト
    ["文字数カウント", "BMI値の計算"] # デフォルト（アプリ起動時）ではリストの左端の要素がselected_itemには格納される
)

st.divider()

if selected_item == "文字数カウント":
    input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")
    text_count = len(input_message)

else:
    height = st.text_input(label="身長（cm）を入力してください。")
    weight = st.text_input(label="体重（kg）を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "文字数カウント":
        if input_message:
            st.write(f"文字数: **{text_count}**")

        else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")

    else:
        if height and weight:
            try:
                bmi = round(int(weight) / ((int(height)/100) ** 2), 1) # round関数によって小数点以下1桁まで表示
                st.write(f"BMI値: {bmi}")

            except ValueError as e:
                st.error("身長と体重は数値で入力してください。")

        else:
            st.error("身長と体重をどちらも入力してください。")