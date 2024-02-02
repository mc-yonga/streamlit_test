import streamlit as st
import pprint


def priority_col_update():
    pprint.pprint(st.session_state.priority_tag_info)
    priority_tag_info = st.session_state.priority_tag_info
    priority_tag_list = priority_tag_info.keys()

    for priority_tag in priority_tag_list:
        main_folders = priority_tag_info[priority_tag]["main_folder"]
        sub_folders = priority_tag_info[priority_tag]["sub_folder"]
        search_querys = priority_tag_info[priority_tag]["search_query"]

        priority_cond = st.session_state.main_folder_df.apply(
            lambda row: (row["Main Folder"] in main_folders)
            | (row["Sub Folder"] in sub_folders)
            | (row["Unique Normalized Search Query"] in search_querys),
            axis=1,
        )

        st.session_state.main_folder_df.loc[priority_cond, "Priority"] = priority_tag
        # st.session_state.main_folder_df.loc[~priority_cond, "Priority"] = ""
        print(f"priority_tag_info {priority_tag} 업데이트 완료")
    st.session_state.data_view_update = True


def kwPush_col_update():
    pprint.pprint(st.session_state.kwpush_tag_info)
    kwpush_tag_info = st.session_state.kwpush_tag_info
    kwpush_tag_list = kwpush_tag_info.keys()

    for kwpush_tag in kwpush_tag_list:
        main_folders = kwpush_tag_info[kwpush_tag]["main_folder"]
        sub_folders = kwpush_tag_info[kwpush_tag]["sub_folder"]
        search_querys = kwpush_tag_info[kwpush_tag]["search_query"]

        kwpush_cond = st.session_state.main_folder_df.apply(
            lambda row: (row["Main Folder"] in main_folders)
            | (row["Sub Folder"] in sub_folders)
            | (row["Unique Normalized Search Query"] in search_querys),
            axis=1,
        )

        st.session_state.main_folder_df.loc[kwpush_cond, "KW Push"] = kwpush_tag
        # st.session_state.main_folder_df.loc[~kwpush_cond, "KW Push"] = ""
        print(f"kwpush_tag_info {kwpush_tag} 업데이트 완료")
    st.session_state.data_view_update = True


def phase_col_update():
    pprint.pprint(st.session_state.phase_tag_info)
    phase_tag_info = st.session_state.phase_tag_info
    phase_tag_list = phase_tag_info.keys()

    for phase_tag in phase_tag_list:
        main_folders = phase_tag_info[phase_tag]["main_folder"]
        sub_folders = phase_tag_info[phase_tag]["sub_folder"]
        search_querys = phase_tag_info[phase_tag]["search_query"]

        phase_cond = st.session_state.main_folder_df.apply(
            lambda row: (row["Main Folder"] in main_folders)
            | (row["Sub Folder"] in sub_folders)
            | (row["Unique Normalized Search Query"] in search_querys),
            axis=1,
        )

        st.session_state.main_folder_df.loc[phase_cond, "Phase"] = phase_tag
        # st.session_state.main_folder_df.loc[~phase_cond, "Phase"] = ""
        print(f"phase_tag_info {phase_tag} 업데이트 완료")
    st.session_state.data_view_update = True


def diffi_col_update():
    pprint.pprint(st.session_state.diffi_tag_info)
    diffi_tag_info = st.session_state.diffi_tag_info
    diffi_tag_list = diffi_tag_info.keys()

    for diffi_tag in diffi_tag_list:
        main_folders = diffi_tag_info[diffi_tag]["main_folder"]
        sub_folders = diffi_tag_info[diffi_tag]["sub_folder"]
        search_querys = diffi_tag_info[diffi_tag]["search_query"]

        diffi_cond = st.session_state.main_folder_df.apply(
            lambda row: (row["Main Folder"] in main_folders)
            | (row["Sub Folder"] in sub_folders)
            | (row["Unique Normalized Search Query"] in search_querys),
            axis=1,
        )

        st.session_state.main_folder_df.loc[diffi_cond, "Difficulty Level"] = diffi_tag
        # st.session_state.main_folder_df.loc[~diffi_cond, "Difficulty Level"] = ""
        print(f"diffi_tag_info {diffi_tag} 업데이트 완료")
    st.session_state.data_view_update = True


def priority_col_update2():
    pprint.pprint(st.session_state.priority_tag_info2)
    priority_tag_info = st.session_state.priority_tag_info2
    priority_tag_list = priority_tag_info.keys()

    for priority_tag in priority_tag_list:
        main_folders = priority_tag_info[priority_tag]["main_folder"]
        sub_folders = priority_tag_info[priority_tag]["sub_folder"]
        search_querys = priority_tag_info[priority_tag]["search_query"]

        priority_cond = st.session_state.uncate_df.apply(
            lambda row: (row["Main Folder"] in main_folders)
            | (row["Sub Folder"] in sub_folders)
            | (row["Unique Normalized Search Query"] in search_querys),
            axis=1,
        )

        st.session_state.uncate_df.loc[priority_cond, "Priority"] = priority_tag
        # st.session_state.uncate_df.loc[~priority_cond, "Priority"] = ""
        print(f"priority_tag_info {priority_tag} 업데이트 완료")
    st.session_state.data_view_update = True


def kwPush_col_update2():
    pprint.pprint(st.session_state.kwpush_tag_info2)
    kwpush_tag_info = st.session_state.kwpush_tag_info2
    kwpush_tag_list = kwpush_tag_info.keys()

    for kwpush_tag in kwpush_tag_list:
        main_folders = kwpush_tag_info[kwpush_tag]["main_folder"]
        sub_folders = kwpush_tag_info[kwpush_tag]["sub_folder"]
        search_querys = kwpush_tag_info[kwpush_tag]["search_query"]

        kwpush_cond = st.session_state.uncate_df.apply(
            lambda row: (row["Main Folder"] in main_folders)
            | (row["Sub Folder"] in sub_folders)
            | (row["Unique Normalized Search Query"] in search_querys),
            axis=1,
        )

        st.session_state.uncate_df.loc[kwpush_cond, "KW Push"] = kwpush_tag
        # st.session_state.uncate_df.loc[~kwpush_cond, "KW Push"] = ""
        print(f"kwpush_tag_info {kwpush_tag} 업데이트 완료")
    st.session_state.data_view_update = True

def phase_col_update2():
    pprint.pprint(st.session_state.phase_tag_info2)
    phase_tag_info = st.session_state.phase_tag_info2
    phase_tag_list = phase_tag_info.keys()

    for phase_tag in phase_tag_list:
        main_folders = phase_tag_info[phase_tag]["main_folder"]
        sub_folders = phase_tag_info[phase_tag]["sub_folder"]
        search_querys = phase_tag_info[phase_tag]["search_query"]

        phase_cond = st.session_state.uncate_df.apply(
            lambda row: (row["Main Folder"] in main_folders)
            | (row["Sub Folder"] in sub_folders)
            | (row["Unique Normalized Search Query"] in search_querys),
            axis=1,
        )

        st.session_state.uncate_df.loc[phase_cond, "Phase"] = phase_tag
        # st.session_state.uncate_df.loc[~phase_cond, "Phase"] = ""
        print(f"phase_tag_info {phase_tag} 업데이트 완료")
    st.session_state.data_view_update = True

def diffi_col_update2():
    pprint.pprint(st.session_state.diffi_tag_info2)
    diffi_tag_info = st.session_state.diffi_tag_info2
    diffi_tag_list = diffi_tag_info.keys()

    for diffi_tag in diffi_tag_list:
        main_folders = diffi_tag_info[diffi_tag]["main_folder"]
        sub_folders = diffi_tag_info[diffi_tag]["sub_folder"]
        search_querys = diffi_tag_info[diffi_tag]["search_query"]

        diffi_cond = st.session_state.uncate_df.apply(
            lambda row: (row["Main Folder"] in main_folders)
            | (row["Sub Folder"] in sub_folders)
            | (row["Unique Normalized Search Query"] in search_querys),
            axis=1,
        )

        st.session_state.uncate_df.loc[diffi_cond, "Difficulty Level"] = diffi_tag
        # st.session_state.uncate_df.loc[~diffi_cond, "Difficulty Level"] = ""
        print(f"diffi_tag_info {diffi_tag} 업데이트 완료")
    st.session_state.data_view_update = True

def LabelView():
    normal_col, uncate_col = st.tabs([":blue[Categorized View]", ":green[UnCategorized View]"])
    if st.session_state.make_folder == False:
        st.error("데이터 업로드 안됨")
    else:
        with normal_col:
            a, b, c, d = st.tabs(
                ["Priority Tag", "KW Push Tag", "Phase Tag", "Difficulty Level"]
            )
            with a:
                st.subheader("Append Priority Tag")
                total_main_folders = st.session_state.main_folder_df[
                    "Main Folder"
                ].unique()
                total_sub_folders = st.session_state.main_folder_df[
                    "Sub Folder"
                ].unique()
                total_search_query = st.session_state.main_folder_df[
                    "Unique Normalized Search Query"
                ].unique()

                priority1, priority2, priority3, priority4, priority5 = st.columns(5)
                priority_main_folder = priority1.multiselect(
                    "Select Main Folder", total_main_folders, key="priority1"
                )
                priority_sub_folder = priority2.multiselect(
                    "Select Sub Folder", total_sub_folders, key="priority2"
                )
                priority_search_query = priority3.multiselect(
                    "Select Search Query", total_search_query, key="priority3"
                )
                options = [
                    "Very high",
                    "High",
                    "Moderate",
                    "Low",
                    "Very low",
                    "Unsetted",
                ]
                priority_tag = priority4.selectbox(
                    "Choose Tag", options, key="priority4"
                )
                priority_tag_button = priority5.button("Append", key="priority5")

                if priority_tag_button:
                    if (
                        len(
                            priority_main_folder
                            + priority_sub_folder
                            + priority_search_query
                        )
                        == 0
                    ):
                        st.error("태그 대상을 선택하세요")
                    else:
                        priority_tag_data = dict(
                            main_folder=priority_main_folder,
                            sub_folder=priority_sub_folder,
                            search_query=priority_search_query,
                        )
                        if (
                            priority_tag
                            not in st.session_state.priority_tag_info.keys()
                        ):
                            st.session_state.priority_tag_info[
                                priority_tag
                            ] = priority_tag_data
                            st.info("신규 태그 생성 완료")
                        elif priority_tag in st.session_state.priority_tag_info.keys():
                            main_folders = st.session_state.priority_tag_info[
                                priority_tag
                            ]["main_folder"]
                            sub_folders = st.session_state.priority_tag_info[
                                priority_tag
                            ]["sub_folder"]
                            search_querys = st.session_state.priority_tag_info[
                                priority_tag
                            ]["search_query"]

                            main_folder = list(main_folders) + list(
                                priority_main_folder
                            )
                            main_folder = list(set(main_folder))

                            sub_folder = list(sub_folders) + list(priority_sub_folder)
                            sub_folder = list(set(sub_folder))

                            search_querys = list(search_querys) + list(
                                priority_search_query
                            )
                            search_querys = list(set(search_querys))

                            st.session_state.priority_tag_info[priority_tag] = dict(
                                main_folder=main_folder,
                                sub_folder=sub_folder,
                                search_query=search_querys,
                            )
                            st.info("태그 업데이트 완료")

                        priority_col_update()
                        # st.dataframe(st.session_state.main_folder_df)  #이부분 보여줘서 더헷갈려서 지움

            with b:
                st.subheader("Append KW Push")
                kw_push1, kw_push2, kw_push3, kw_push4, kw_push5 = st.columns(5)
                kw_main_folder = kw_push1.multiselect(
                    "Select Main Folder", total_main_folders, key="kw1"
                )
                kw_sub_folder = kw_push2.multiselect(
                    "Select Sub Folder", total_sub_folders, key="kw2"
                )
                kw_search_query = kw_push3.multiselect(
                    "Select Search Query", total_search_query, key="kw3"
                )
                options = [
                    "Need to Rank",
                    "Want to Rank",
                    "Keep Rank Position",
                    "Lost Rank Position",
                    "Rank Higher",
                    "Rank Lower",
                    "Unsetted",
                ]
                kw_tag = kw_push4.selectbox("Choose Tag", options, key="kw4")

                kw_tag_button = kw_push5.button("Append", key="kw5")

                if kw_tag_button:
                    if len(kw_main_folder + kw_sub_folder + kw_search_query) == 0:
                        st.error("태그 대상을 선택하세요")
                    else:
                        kwpush_tag_data = dict(
                            main_folder=kw_main_folder,
                            sub_folder=kw_sub_folder,
                            search_query=kw_search_query,
                        )
                        if kw_tag not in st.session_state.kwpush_tag_info.keys():
                            st.session_state.kwpush_tag_info[kw_tag] = kwpush_tag_data
                            st.info("신규 태그 생성 완료")
                        elif kw_tag in st.session_state.kwpush_tag_info.keys():
                            main_folders = st.session_state.kwpush_tag_info[kw_tag][
                                "main_folder"
                            ]
                            sub_folders = st.session_state.kwpush_tag_info[kw_tag][
                                "sub_folder"
                            ]
                            search_querys = st.session_state.kwpush_tag_info[kw_tag][
                                "search_query"
                            ]

                            main_folder = list(main_folders) + list(kw_main_folder)
                            main_folder = list(set(main_folder))

                            sub_folder = list(sub_folders) + list(kw_sub_folder)
                            sub_folder = list(set(sub_folder))

                            search_querys = list(search_querys) + list(kw_search_query)
                            search_querys = list(set(search_querys))

                            st.session_state.kwpush_tag_info[kw_tag] = dict(
                                main_folder=main_folder,
                                sub_folder=sub_folder,
                                search_query=search_querys,
                            )
                            st.info("태그 업데이트 완료")

                        kwPush_col_update()
                        # st.dataframe(st.session_state.main_folder_df)

            with c:
                st.subheader("Append Phase Push")
                (
                    phase_push1,
                    phase_push2,
                    phase_push3,
                    phase_push4,
                    phase_push5,
                ) = st.columns(5)
                phase_main_folder = phase_push1.multiselect(
                    "Select Main Folder", total_main_folders, key="phase1"
                )
                phase_sub_folder = phase_push2.multiselect(
                    "Select Sub Folder", total_sub_folders, key="phase2"
                )
                phase_search_query = phase_push3.multiselect(
                    "Select Search Query", total_search_query, key="phase3"
                )
                options = [
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                ]
                phase_tag = phase_push4.selectbox("Choose Tag", options, key="phase4")
                phase_tag_button = phase_push5.button("Append", key="phase5")

                if phase_tag_button:
                    if (
                        len(phase_main_folder + phase_sub_folder + phase_search_query)
                        == 0
                    ):
                        st.error("태그 대상을 선택하세요")
                    else:
                        phase_tag_data = dict(
                            main_folder=phase_main_folder,
                            sub_folder=phase_sub_folder,
                            search_query=phase_search_query,
                        )
                        if phase_tag not in st.session_state.phase_tag_info.keys():
                            st.session_state.phase_tag_info[phase_tag] = phase_tag_data
                            st.info("신규 태그 생성 완료")
                        elif phase_tag in st.session_state.phase_tag_info.keys():
                            main_folders = st.session_state.phase_tag_info[phase_tag][
                                "main_folder"
                            ]
                            sub_folders = st.session_state.phase_tag_info[phase_tag][
                                "sub_folder"
                            ]
                            search_querys = st.session_state.phase_tag_info[phase_tag][
                                "search_query"
                            ]

                            main_folder = list(main_folders) + list(phase_main_folder)
                            main_folder = list(set(main_folder))

                            sub_folder = list(sub_folders) + list(phase_sub_folder)
                            sub_folder = list(set(sub_folder))

                            search_querys = list(search_querys) + list(
                                phase_search_query
                            )
                            search_querys = list(set(search_querys))

                            st.session_state.phase_tag_info[phase_tag] = dict(
                                main_folder=main_folder,
                                sub_folder=sub_folder,
                                search_query=search_querys,
                            )
                            st.info("태그 업데이트 완료")

                        phase_col_update()
                        # st.dataframe(st.session_state.main_folder_df)
            with d:
                st.subheader("Append Difficulty Level Tag")
                (
                    difficult_push1,
                    difficult_push2,
                    difficult_push3,
                    difficult_push4,
                    difficult_push5,
                ) = st.columns(5)
                diffi_main_folder = difficult_push1.multiselect(
                    "Select Main Folder", total_main_folders, key="diffi1"
                )
                diffi_sub_folder = difficult_push2.multiselect(
                    "Select Sub Folder", total_sub_folders, key="diffi2"
                )
                diffi_search_query = difficult_push3.multiselect(
                    "Select Search Query", total_search_query, key="diffi3"
                )
                options = [
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                ]
                diffi_tag = difficult_push4.selectbox(
                    "Choose Tag", options, key="diffi4"
                )
                diffi_tag_button = difficult_push5.button("Append", key="diffi5")

                if diffi_tag_button:
                    if (
                        len(diffi_main_folder + diffi_sub_folder + diffi_search_query)
                        == 0
                    ):
                        st.error("태그 대상을 선택하세요")
                    else:
                        diffi_tag_data = dict(
                            main_folder=diffi_main_folder,
                            sub_folder=diffi_sub_folder,
                            search_query=diffi_search_query,
                        )
                        if diffi_tag not in st.session_state.diffi_tag_info.keys():
                            st.session_state.diffi_tag_info[diffi_tag] = diffi_tag_data
                            st.info("신규 태그 생성 완료")
                        elif diffi_tag in st.session_state.diffi_tag_info.keys():
                            main_folders = st.session_state.diffi_tag_info[
                                diffi_tag
                            ]["main_folder"]
                            sub_folders = st.session_state.diffi_tag_info[
                                diffi_tag
                            ]["sub_folder"]
                            search_querys = st.session_state.diffi_tag_info[
                                diffi_tag
                            ]["search_query"]

                            main_folder = list(main_folders) + list(diffi_main_folder)
                            main_folder = list(set(main_folder))

                            sub_folder = list(sub_folders) + list(diffi_sub_folder)
                            sub_folder = list(set(sub_folder))

                            search_querys = list(search_querys) + list(
                                diffi_search_query
                            )
                            search_querys = list(set(search_querys))

                            st.session_state.diffi_tag_info[diffi_tag] = dict(
                                main_folder=main_folder,
                                sub_folder=sub_folder,
                                search_query=search_querys,
                            )
                            st.info("태그 업데이트 완료")

                        diffi_col_update()
                        # st.dataframe(st.session_state.main_folder_df)

            st.markdown("---")
            st.subheader("Merge Main Folder")
            (merge_push1, merge_push2, merge_push3) = st.columns(3)

            folder_list = list(
                st.session_state.main_folder_df["Main Folder"].unique().tolist()
            )
            child = merge_push1.selectbox("Choose Child", folder_list, key="merge1")
            parents = merge_push2.selectbox("Choose Parents", folder_list, key="merge2")

            merge_btn = merge_push3.button("Merge")

            if merge_btn:
                if parents == child:
                    st.error("Parents 와 Child 폴더명을 다르게 선택하세요")
                else:
                    if merge_btn:
                        merge_cond = (
                            st.session_state.main_folder_df["Main Folder"] == child
                        )
                        st.session_state.main_folder_df.loc[
                            merge_cond, "Main Folder"
                        ] = parents
                        st.info(f"{child}폴더가 {parents}폴더로 이동하였습니다")
                        st.dataframe(st.session_state.main_folder_df)
                        st.session_state.data_view_update = True

            st.markdown("---")
            st.subheader("Merge Sub Folder")
            sub_merge_push1, sub_merge_push2, sub_merge_push3, sub_merge_push4 = st.columns(4)
            main_folder = sub_merge_push1.selectbox("Choose Main Folder", folder_list, key="sub_merge1")

            sub_folder_list = st.session_state.main_folder_df[st.session_state.main_folder_df['Main Folder'] == main_folder]['Sub Folder'].unique().tolist()
            child_sub_folder = sub_merge_push2.selectbox('Choose Sub Folder', sub_folder_list, key = "sub_merge2")
            parent_sub_folder = sub_merge_push3.selectbox('Choose Sub Folder', sub_folder_list, key = "sub_merge3")
            sub_folder_merge_btn = sub_merge_push4.button('Merge', key = "sub_merge4")

            if sub_folder_merge_btn:
                if parent_sub_folder == child_sub_folder:
                    st.error("Parents 와 Child 폴더명을 다르게 선택하세요")
                else:
                    print(f'메인폴더 >> {main_folder}, 써브폴더 >> {child_sub_folder}')
                    child_cond = (
                        (st.session_state.main_folder_df["Main Folder"] == main_folder) &
                        (st.session_state.main_folder_df["Sub Folder"] == child_sub_folder)
                    )

                    st.session_state.main_folder_df.loc[child_cond, 'Sub Folder'] = parent_sub_folder
                    st.info(f"{child_sub_folder}폴더가 {parent_sub_folder}폴더로 이동하였습니다")
                    st.dataframe(st.session_state.main_folder_df.loc[child_cond])
                    st.session_state.data_view_update = True

        with uncate_col:
            a, b, c, d = st.tabs(
                ["Priority Tag", "KW Push Tag", "Phase Tag", "Difficulty Level"]
            )
            with a:
                st.subheader("Append Priority Tag")

                total_main_folders = st.session_state.uncate_df["Main Folder"].unique()
                total_sub_folders = st.session_state.uncate_df["Sub Folder"].unique()
                total_search_query = st.session_state.uncate_df[
                    "Unique Normalized Search Query"
                ].unique()

                priority1, priority2, priority3, priority4, priority5 = st.columns(5)
                priority_main_folder = priority1.multiselect(
                    "Select Main Folder", total_main_folders, key="uncate_priority1"
                )
                priority_sub_folder = priority2.multiselect(
                    "Select Sub Folder", total_sub_folders, key="uncate_priority2"
                )
                priority_search_query = priority3.multiselect(
                    "Select Search Query", total_search_query, key="uncate_priority3"
                )
                options = [
                    "Very high",
                    "High",
                    "Moderate",
                    "Low",
                    "Very low",
                    "Unsetted",
                ]
                priority_tag = priority4.selectbox(
                    "Choose Tag", options, key="uncate_priority4"
                )
                priority_tag_button = priority5.button("Append", key="uncate_priority5")

                if priority_tag_button:
                    if (
                        len(
                            priority_main_folder
                            + priority_sub_folder
                            + priority_search_query
                        )
                        == 0
                    ):
                        st.error("태그 대상을 선택하세요")
                    else:
                        priority_tag_data = dict(
                            main_folder=priority_main_folder,
                            sub_folder=priority_sub_folder,
                            search_query=priority_search_query,
                        )
                        if (
                            priority_tag
                            not in st.session_state.priority_tag_info2.keys()
                        ):
                            st.session_state.priority_tag_info2[
                                priority_tag
                            ] = priority_tag_data
                            st.info("신규 태그 생성 완료")
                        elif priority_tag in st.session_state.priority_tag_info2.keys():
                            main_folders = st.session_state.priority_tag_info2[
                                priority_tag
                            ]["main_folder"]
                            sub_folders = st.session_state.priority_tag_info2[
                                priority_tag
                            ]["sub_folder"]
                            search_querys = st.session_state.priority_tag_info2[
                                priority_tag
                            ]["search_query"]

                            main_folder = list(main_folders) + list(
                                priority_main_folder
                            )
                            main_folder = list(set(main_folder))

                            sub_folder = list(sub_folders) + list(priority_sub_folder)
                            sub_folder = list(set(sub_folder))

                            search_querys = list(search_querys) + list(
                                priority_search_query
                            )
                            search_querys = list(set(search_querys))

                            st.session_state.priority_tag_info2[priority_tag] = dict(
                                main_folder=main_folder,
                                sub_folder=sub_folder,
                                search_query=search_querys,
                            )
                            st.info("태그 업데이트 완료")

                        priority_col_update2()
                        # st.dataframe(st.session_state.uncate_df)

            with b:
                st.subheader("Append KW Push")
                kw_push1, kw_push2, kw_push3, kw_push4, kw_push5 = st.columns(5)
                kw_main_folder = kw_push1.multiselect(
                    "Select Main Folder", total_main_folders, key="uncate_kw1"
                )
                kw_sub_folder = kw_push2.multiselect(
                    "Select Sub Folder", total_sub_folders, key="uncate_kw2"
                )
                kw_search_query = kw_push3.multiselect(
                    "Select Search Query", total_search_query, key="uncate_kw3"
                )
                options = [
                    "Need to Rank",
                    "Want to Rank",
                    "Keep Rank Position",
                    "Lost Rank Position",
                    "Rank Higher",
                    "Rank Lower",
                    "Unsetted",
                ]
                kw_tag = kw_push4.selectbox("Choose Tag", options, key="uncate_kw4")

                kw_tag_button = kw_push5.button("Append", key="uncate_kw5")

                if kw_tag_button:
                    if len(kw_main_folder + kw_sub_folder + kw_search_query) == 0:
                        st.error("태그 대상을 선택하세요")
                    else:
                        kwpush_tag_data = dict(
                            main_folder=kw_main_folder,
                            sub_folder=kw_sub_folder,
                            search_query=kw_search_query,
                        )
                        if kw_tag not in st.session_state.kwpush_tag_info2.keys():
                            st.session_state.kwpush_tag_info2[kw_tag] = kwpush_tag_data
                            st.info("신규 태그 생성 완료")
                        elif kw_tag in st.session_state.kwpush_tag_info.keys():
                            main_folders = st.session_state.kwpush_tag_info2[kw_tag][
                                "main_folder"
                            ]
                            sub_folders = st.session_state.kwpush_tag_info2[kw_tag][
                                "sub_folder"
                            ]
                            search_querys = st.session_state.kwpush_tag_info2[kw_tag][
                                "search_query"
                            ]

                            main_folder = list(main_folders) + list(kw_main_folder)
                            main_folder = list(set(main_folder))

                            sub_folder = list(sub_folders) + list(kw_sub_folder)
                            sub_folder = list(set(sub_folder))

                            search_querys = list(search_querys) + list(kw_search_query)
                            search_querys = list(set(search_querys))

                            st.session_state.kwpush_tag_info2[kw_tag] = dict(
                                main_folder=main_folder,
                                sub_folder=sub_folder,
                                search_query=search_querys,
                            )
                            st.info("태그 업데이트 완료")

                        kwPush_col_update2()
                        # st.dataframe(st.session_state.uncate_df)

            with c:
                st.subheader("Append Phase Push")
                (
                    phase_push1,
                    phase_push2,
                    phase_push3,
                    phase_push4,
                    phase_push5,
                ) = st.columns(5)
                phase_main_folder = phase_push1.multiselect(
                    "Select Main Folder", total_main_folders, key="uncate_phase1"
                )
                phase_sub_folder = phase_push2.multiselect(
                    "Select Sub Folder", total_sub_folders, key="uncate_phase2"
                )
                phase_search_query = phase_push3.multiselect(
                    "Select Search Query", total_search_query, key="uncate_phase3"
                )
                options = [
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                ]
                phase_tag = phase_push4.selectbox(
                    "Choose Tag", options, key="uncate_phase4"
                )
                phase_tag_button = phase_push5.button("Append", key="uncate_phase5")

                if phase_tag_button:
                    if (
                        len(phase_main_folder + phase_sub_folder + phase_search_query)
                        == 0
                    ):
                        st.error("태그 대상을 선택하세요")
                    else:
                        phase_tag_data = dict(
                            main_folder=phase_main_folder,
                            sub_folder=phase_sub_folder,
                            search_query=phase_search_query,
                        )
                        if phase_tag not in st.session_state.phase_tag_info2.keys():
                            st.session_state.phase_tag_info2[phase_tag] = phase_tag_data
                            st.info("신규 태그 생성 완료")
                        elif phase_tag in st.session_state.phase_tag_info2.keys():
                            main_folders = st.session_state.phase_tag_info2[phase_tag][
                                "main_folder"
                            ]
                            sub_folders = st.session_state.phase_tag_info2[phase_tag][
                                "sub_folder"
                            ]
                            search_querys = st.session_state.phase_tag_info2[phase_tag][
                                "search_query"
                            ]

                            main_folder = list(main_folders) + list(phase_main_folder)
                            main_folder = list(set(main_folder))

                            sub_folder = list(sub_folders) + list(phase_sub_folder)
                            sub_folder = list(set(sub_folder))

                            search_querys = list(search_querys) + list(
                                phase_search_query
                            )
                            search_querys = list(set(search_querys))

                            st.session_state.phase_tag_info[phase_tag] = dict(
                                main_folder=main_folder,
                                sub_folder=sub_folder,
                                search_query=search_querys,
                            )
                            st.info("태그 업데이트 완료")

                        phase_col_update2()
                        # st.dataframe(st.session_state.uncate_df)`

            with d:
                st.subheader("Append Difficulty Level Tag")
                (
                    difficult_push1,
                    difficult_push2,
                    difficult_push3,
                    difficult_push4,
                    difficult_push5,
                ) = st.columns(5)
                diffi_main_folder = difficult_push1.multiselect(
                    "Select Main Folder", total_main_folders, key="uncate_diffi1"
                )
                diffi_sub_folder = difficult_push2.multiselect(
                    "Select Sub Folder", total_sub_folders, key="uncate_diffi2"
                )
                diffi_search_query = difficult_push3.multiselect(
                    "Select Search Query", total_search_query, key="uncate_diffi3"
                )
                options = [
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                ]
                diffi_tag = difficult_push4.selectbox(
                    "Choose Tag", options, key="uncate_diffi4"
                )
                diffi_tag_button = difficult_push5.button("Append", key="uncate_diffi5")

                if diffi_tag_button:
                    if (
                        len(diffi_main_folder + diffi_sub_folder + diffi_search_query)
                        == 0
                    ):
                        st.error("태그 대상을 선택하세요")
                    else:
                        diffi_tag_data = dict(
                            main_folder=diffi_main_folder,
                            sub_folder=diffi_sub_folder,
                            search_query=diffi_search_query,
                        )
                        if diffi_tag not in st.session_state.diffi_tag_info2.keys():
                            st.session_state.diffi_tag_info[diffi_tag] = diffi_tag_data
                            st.info("신규 태그 생성 완료")
                        elif diffi_tag in st.session_state.diffi_tag_info2.keys():
                            main_folders = st.session_state.diffi_tag_info2[
                                diffi_tag
                            ]["main_folder"]
                            sub_folders = st.session_state.diffi_tag_info2[
                                diffi_tag
                            ]["sub_folder"]
                            search_querys = st.session_state.diffi_tag_info2[
                                diffi_tag
                            ]["search_query"]

                            main_folder = list(main_folders) + list(diffi_main_folder)
                            main_folder = list(set(main_folder))

                            sub_folder = list(sub_folders) + list(diffi_sub_folder)
                            sub_folder = list(set(sub_folder))

                            search_querys = list(search_querys) + list(
                                diffi_search_query
                            )
                            search_querys = list(set(search_querys))

                            st.session_state.diffi_tag_info2[diffi_tag] = dict(
                                main_folder=main_folder,
                                sub_folder=sub_folder,
                                search_query=search_querys,
                            )
                            st.info("태그 업데이트 완료")

                        diffi_col_update2()
                        # st.dataframe(st.session_state.uncate_df)

            st.markdown("---")
            st.subheader("Merge Folder")
            (merge_push1, merge_push2, merge_push3) = st.columns(3)

            folder_list = list(
                st.session_state.uncate_df["Main Folder"].unique().tolist()
            )
            child = merge_push1.selectbox(
                "Choose Child", folder_list, key="uncate_merge1"
            )
            parents = merge_push2.selectbox(
                "Choose Parents", folder_list, key="uncate_merge2"
            )

            merge_btn = merge_push3.button("Merge", key="uncate_merge3")

            if merge_btn:
                if parents == child:
                    st.error("Parents 와 Child 폴더명을 다르게 선택하세요")
                else:
                    if merge_btn:
                        merge_cond = st.session_state.uncate_df["Main Folder"] == child
                        st.session_state.uncate_df.loc[
                            merge_cond, "Main Folder"
                        ] = parents
                        st.info(f"{child}폴더가 {parents}폴더로 이동하였습니다")
                        st.dataframe(st.session_state.uncate_df)
                        st.session_state.data_view_update = True

            sub_merge_push1, sub_merge_push2, sub_merge_push3, sub_merge_push4 = st.columns(4)
            main_folder = sub_merge_push1.selectbox("Choose Main Folder", folder_list, key="uncate_sub_merge1")

            sub_folder_list = st.session_state.uncate_df[st.session_state.uncate_df['Main Folder'] == main_folder]['Sub Folder'].unique().tolist()
            child_sub_folder = sub_merge_push2.selectbox('Choose Sub Folder', sub_folder_list, key = "uncate_sub_merge2")
            parent_sub_folder = sub_merge_push3.selectbox('Choose Sub Folder', sub_folder_list, key = "uncate_sub_merge3")
            sub_folder_merge_btn = sub_merge_push4.button('Merge', key = "uncate_sub_merge4")

            if sub_folder_merge_btn:
                if parent_sub_folder == child_sub_folder:
                    st.error("Parents 와 Child 폴더명을 다르게 선택하세요")
                else:
                    print(f'메인폴더 >> {main_folder}, 써브폴더 >> {child_sub_folder}')
                    child_cond = (
                        (st.session_state.uncate_df["Main Folder"] == main_folder) &
                        (st.session_state.uncate_df["Sub Folder"] == child_sub_folder)
                    )

                    st.session_state.uncate_df.loc[child_cond, 'Sub Folder'] = parent_sub_folder
                    st.info(f"{child_sub_folder}폴더가 {parent_sub_folder}폴더로 이동하였습니다")
                    st.dataframe(st.session_state.uncate_df.loc[child_cond])
                    st.session_state.data_view_update = True