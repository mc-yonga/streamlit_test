from st_aggrid import AgGrid, GridOptionsBuilder
from superDev import *


def TagView():
    col1, col2, col3 = st.columns([0.2, 0.2, 1])
    table_name = col1.text_input("저장명을 입력하세요")
    insert_btn = col2.button(":computer: :blue[Save in to DB]")

    if st.session_state.make_folder == False:
        st.error("데이터가 없습니다. 업로드 뷰에서 Save 버튼을 클릭하세요")
    else:
        total_data = pd.concat(
            [st.session_state.main_folder_df, st.session_state.uncate_df]
        )
        st.session_state.tag_view = total_data.copy()[
            [
                "Unique Normalized Search Query",
                "Search Volume",
                "Original Search Query",
                "Priority",
                "KW Push",
                "Phase",
                "Difficulty Level",
            ]
        ]

        down_file = convert_df(total_data)
        down_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        col2.download_button(
            label=':floppy_disk: :green[Download]',
            data = down_file,
            file_name = f'tagview_file_{down_time}.csv'
        )

        ## 다시 불러올시 kw_split이 붙는 이슈가 있어서 존재할시 날리는 코드 작성
        if "kw_split" in total_data.columns:
            total_data = total_data.drop(columns=["kw_split"])
        with st.spinner("DB에 저장중입니다... 완료되기 전까지 창을 나가거나, 한번더 누르지 마세요."):
            if insert_btn:
                if table_name:
                    total_data.columns = [
                        "category",
                        "main_folder",
                        "sub_folder",
                        "search_query",
                        "search_volume",
                        "original_search_query",
                        "priority",
                        "kw_push",
                        "phase",
                        "difficulty_level",
                    ]

                    table_list = fetch_table_list()
                    if table_name not in table_list:
                        create_table(table_name)
                        insert_data(table_name, total_data)
                        st.info(f"{table_name} 저장이 완료되었습니다.")
                    else:
                        drop_table(table_name)
                        create_table(table_name)
                        insert_data(table_name, total_data)
                        st.info(f"{table_name} 업데이트가 완료되었습니다.")
                else:
                    st.error('저장명을 입력하세요요')
            # 네 개의 탭 생성

        if st.session_state.table_name != None:
            st.write(f":red['{st.session_state.table_name}' 테이블 작업중 ...]")

        tab_titles = ["Priority", "KW Push", "Phase", "Difficulty Level"]
        tabs = st.tabs(tab_titles)
        for tab, column in zip(tabs, tab_titles):
            with tab:
                # 공통 컬럼과 추가 컬럼 선택
                columns_to_show = [
                    "Unique Normalized Search Query",
                    "Original Search Query",
                    "Search Volume",
                ] + tab_titles

                # DataFrame 필터링
                filtered_df = st.session_state.tag_view[columns_to_show].copy()
                filtered_df = filtered_df.drop_duplicates()

                # GridOptionsBuilder를 사용하여 AgGrid 구성
                gb = GridOptionsBuilder.from_dataframe(filtered_df)
                gb.configure_default_column(
                    groupable=True, value=True, enableRowGroup=True, editable=True
                )

                gb.configure_column(column, rowGroup=True)
                # gb.configure_selection(
                #     "multiple", use_checkbox=True
                # )  # 다중 선택 및 체크박스 사용 설정

                gridOptions = gb.build()
                gridOptions["groupKeys"] = [column, "Unique Normalized Search Query"]

                # 그룹화된 AgGrid 표시
                AgGrid(
                    filtered_df, gridOptions=gridOptions, enable_enterprise_modules=True
                )

        # st.dataframe(st.session_state.main_folder_df)
        # st.dataframe(st.session_state.uncate_df)
