import cmdstanpy.install_cmdstan

from superDev import *

def make_leftside_of_dataview(data):
    data["kw_split"] = data["Original Search Query"].apply(lambda x: x.split())
    data["kw_split"] = data.kw_split.apply(
        lambda x: [
            kw
            for kw in x
            if any(char.isalpha() or char.isdigit() for char in kw)
            and kw not in stop_words  # 불용어와 기호 제거
        ]
    )

    data["kw_split_lemma"] = data.kw_split.apply(
        lambda x: [
            kw if pos_tag([kw])[0][1] == "NN" else lemmatizer.lemmatize(kw) for kw in x
        ]
    )
    data["joined_kw_split_lemma"] = data["kw_split_lemma"].apply(lambda x: " ".join(x))

    def generate_ngrams(text, max_n):
        n_grams = []
        for n in range(1, max_n + 1):
            n_grams.extend([" ".join(grams) for grams in ngrams(text.split(), n)])
        return n_grams

    # n-gram 생성 (예: 최대 3-gram까지)
    max_n = 3
    data["all_ngrams"] = data["joined_kw_split_lemma"].apply(
        lambda x: generate_ngrams(x, max_n)
    )

    # 빈도수 및 Broad Search Term 계산
    ngram_freq = Counter()
    broad_search_terms = {}

    for _, row in data.iterrows():
        for ngram in row["all_ngrams"]:
            ngram_freq[ngram] += 1
            if ngram not in broad_search_terms:
                broad_search_terms[ngram] = row["Search Volume"]
            else:
                broad_search_terms[ngram] += row["Search Volume"]

    # 결과를 DataFrame으로 변환
    ngram_df = pd.DataFrame(
        {
            "Normalized Root": ngram_freq.keys(),
            "Frequency": ngram_freq.values(),
            "Broad Search Term": [
                broad_search_terms[ngram] for ngram in ngram_freq.keys()
            ],
        }
    )

    ngram_df.sort_values(by="Frequency", ascending=False, inplace=True)
    return ngram_df

def generate_uuid():
    return str(uuid.uuid4()), str(uuid.uuid4())


def DataView():
    if st.session_state.make_folder:
        if st.session_state.data_view_update:
            print(f'키 새로 발급~!!!!')
            key1, key2 = generate_uuid()
            st.session_state.data_view1_key = key1
            st.session_state.data_view2_key = key2

        all_df = pd.concat(
            [st.session_state.main_folder_df, st.session_state.uncate_df]
        )
        origianl_df = all_df[
            ["Original Search Query", "Search Volume"]
        ].drop_duplicates()
        leftside_part = make_leftside_of_dataview(origianl_df)
        left_side, right_side = st.columns([0.4, 1])
        with left_side:
            st.subheader("Normalized Root")
            st.text("DataDive의 Normalized Root와 동일 역할")
            leftside_part = leftside_part.reset_index(drop=True)
            st.dataframe(leftside_part)

        with right_side:
            a,b, c, d= st.columns([2,5,1,1])
            a.subheader("Group Folder")
            st.text("각 키워드가 어떠한 형태로 서로 연관되어 있는지 확인 가능")
            st.text("Categorized View는 초기 설정 세팅의 조건을 만족하는 그룹, Uncate는 설정에서 벗어나는 그룹")
            main_tab, uncate_tab = st.tabs(["Categorized View", "UnCategorized View"])

            with main_tab:
                data_view1 = st.session_state.main_folder_df.copy()[
                    [
                        "Main Folder",
                        "Sub Folder",
                        "Unique Normalized Search Query",
                        "Original Search Query",
                        "Search Volume",
                        # "Priority",
                        # "KW Push",
                        # "Phase",
                        # "Difficulty Level",
                    ]
                ]
                down_file = convert_df(data_view1)
                down_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                c.download_button(
                    label = ':floppy_disk: :blue[Download (Main)]',
                    data = down_file,
                    file_name = f'main_group_folder_{down_time}.csv',
                )

                gb1 = GridOptionsBuilder.from_dataframe(data_view1)
                gb1.configure_column("Main Folder", width=200, rowGroup=True, hide=True)
                gb1.configure_column("Sub Folder", rowGroup=True, hide=True)
                gb1.configure_column("Unique Normalized Search Query", rowGroup=True)
                gb1.configure_default_column(
                    groupable=True, aggFunc="sum", value=True, enableRowGroup=True
                )
                #
                gridOptions1 = gb1.build()
                gridOptions1["groupKeys"] = [
                    "Main Folder",
                    "Sub Folder",
                    "Unique Normalized Search Query",
                ]
                #
                AgGrid(
                    data_view1,
                    gridOptions=gridOptions1,
                    enable_enterprise_modules=True,
                    fit_columns_on_grid_load=True,
                    ensure_data_fits=True,
                    enable_quicksearch=True,
                    key= st.session_state.data_view1_key,
                )

            with uncate_tab:
                data_view2 = st.session_state.uncate_df.copy()[
                    [
                        "Main Folder",
                        "Sub Folder",
                        "Unique Normalized Search Query",
                        "Original Search Query",
                        "Search Volume",
                        # "Priority",
                        # "KW Push",
                        # "Phase",
                        # "Difficulty Level",
                    ]
                ]

                down_file = convert_df(data_view2)
                down_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                d.download_button(
                    label = ':floppy_disk: :red[Download (Uncate)]',
                    data = down_file,
                    file_name = f'uncate_group_folder_{down_time}.csv',
                )

                gb2 = GridOptionsBuilder.from_dataframe(data_view2)
                gb2.configure_column("Main Folder", rowGroup=True, hide=True)
                gb2.configure_column("Sub Folder", rowGroup=True, hide=True)
                gb2.configure_column("Unique Normalized Search Query", rowGroup=True)

                gb2.configure_default_column(
                    groupable=True, aggFunc="sum", value=True, enableRowGroup=True
                )
                #
                gridOptions2 = gb2.build()
                gridOptions2["groupKeys"] = [
                    "Main Folder",
                    "Sub Folder",
                    "Unique Normalized Search Query",
                ]
                #
                AgGrid(
                    data_view2,
                    gridOptions=gridOptions2,
                    enable_enterprise_modules=True,
                    fit_columns_on_grid_load=True,
                    ensure_data_fits=True,
                    enable_quicksearch=True,
                    key = st.session_state.data_view2_key,
                )

        del st.session_state[st.session_state.data_view1_key]
        del st.session_state[st.session_state.data_view2_key]
        st.session_state.data_view_update = False
