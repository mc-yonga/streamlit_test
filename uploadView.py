from superDev import *

def UploadView():
    col1, col2 = st.columns([1, 0.3])
    with col1:
        # load_tabs = ['Upload File', 'Import data from DataDive']
        # upload_tap, db_load_tab = st.tabs(load_tabs)
        # with upload_tap:
        st.write(":no_entry: :red[파일 업로드 or 저장된 테이블 중 하나만 선택해주세요.]")
        st.text("파일 업로드는 새로운 분석을 하고 싶을때 사용, 저장된 테이블 불러오기는 과거 상황을 이어 진행하고 싶을때 사용됩니다.")
        uploaded_file = st.file_uploader("파일을 선택하세요", type=["xlsx"])
        db_tables = fetch_table_list()
        db_file_name = st.selectbox(
            "저장된 테이블을 선택하세요", [None] + db_tables, key="select_db_table"
        )

    load_button = st.button(label="Save")

    with col2:
        word_count = st.number_input(label="Word Count", step=1, min_value=3)
        main_keywords_huddle = st.number_input(
            label="Main Keyword Huddle", step=1, min_value=10
        )
        sub_keywords_huddle = st.number_input(
            label="Sub Keyword Huddle", step=1, min_value=5
        )

    if load_button:
        st.session_state.load_state = (
            False  # save 버튼을 누르는 순간 load_state를 False 해서 새로운 데이터에 make_folder 함수를 돌림
        )
        if db_file_name or uploaded_file:
            if db_file_name != None and db_file_name:
                print("db 파일 로드")
                db_load_file = fetch_data(db_file_name)
                load_way = "db"
                table_name = db_file_name
            else:
                print("업로드 파일 로드")
                load_way = "upload"
                db_load_file = None
                table_name = None

            # 버튼이 눌렸을 때만 세션 상태 업데이트
            st.session_state["uploaded_file"] = uploaded_file
            st.session_state["db_load_file"] = db_load_file
            st.session_state["load_way"] = load_way
            st.session_state["word_count"] = word_count
            st.session_state["main_keywords_huddle"] = main_keywords_huddle
            st.session_state["sub_keywords_huddle"] = sub_keywords_huddle
            st.session_state["button_clicked"] = load_button
            st.session_state["load_state"] = True
            st.session_state["table_name"] = table_name

            with st.spinner("잠시만 기다려주세요..."):
                if st.session_state.load_state == True:
                    if st.session_state.load_way == "upload":
                        make_folder(uploaded_file, word_count, main_keywords_huddle, sub_keywords_huddle)
                    else:
                        data_from_db()

            st.info("Data View 생성이 완료되었습니다. Data view 탭으로 이동하여 결과를 확인하세요~!")
        else:
            st.error("업로드 파일을 확인하세요")

    image_url = "data_upload_ex.png"
    st.image(image_url, caption="데이터 예시", width=800)
