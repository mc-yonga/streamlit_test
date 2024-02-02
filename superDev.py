import pandas as pd
import psycopg2
import streamlit as st
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter
import numpy as np
from st_aggrid import AgGrid, GridOptionsBuilder
import uuid
import datetime

lemmatizer = WordNetLemmatizer()
nltk.download("wordnet")
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
try:
    stop_words = set(stopwords.words("english"))
except AttributeError:
    pass

conn = psycopg2.connect(
    host="db.yjolqcetitlpjbwwxnly.supabase.co",
    port="5432",
    dbname="postgres",
    user="postgres",
    password="superDev1!@#$%^&",
)
cursor = conn.cursor()


def drop_table(name):
    query = f"""
    DROP TABLE "{name}"
    """
    cursor.execute(query)
    conn.commit()
    print(f"{name} table 제거 완료")


def create_table(name):
    query = f"""
    CREATE TABLE "{name}" (
        category text,
        main_folder text,
        sub_folder text,
        search_query text,
        search_volume integer,
        original_search_query text,
        priority text,
        kw_push text,
        phase text,
        difficulty_level text
           );
        """
    "Search Query Tag"
    # text ARRAY
    cursor.execute(query)
    conn.commit()
    print(f"{name} 테이블 추가 완료")


def insert_data(name, data):  # 모든 문자열 열에 대해 replace 수행
    str_columns = data.select_dtypes(include=["object"])
    data[str_columns.columns] = str_columns.applymap(lambda x: x.replace("'", "''"))

    # 데이터 일괄 처리를 위한 쿼리 생성
    values = []
    for row in data.itertuples():
        values.append(
            f"('{row.category}', '{row.main_folder}', '{row.sub_folder}', '{row.search_query}', {row.search_volume}, '{row.original_search_query}', '{row.priority}', '{row.kw_push}', '{row.phase}', '{row.difficulty_level}')"
        )

    query = f"""INSERT INTO "{name}" (category, main_folder, sub_folder, search_query, search_volume, original_search_query, priority, kw_push, phase, difficulty_level) VALUES {', '.join(values)}"""

    try:
        cursor.execute(query)
        conn.commit()
        print(f"{name} 태그 데이터 저장 완료")
    except Exception as e:
        print(f"데이터 삽입 중 오류 발생: {e}")
        conn.rollback()


def update_data(name, data):
    for row in data.itertuples():
        category = row.category
        main_folder = row.main_folder
        main_folder = main_folder.replace("'", "''")
        sub_folder = row.sub_folder
        sub_folder = sub_folder.replace("'", "''")
        search_query = row.search_query
        search_query = search_query.replace("'", "''")
        search_volume = row.search_volume
        # kw_split = row.kw_split
        # kw_split = ' '.join(kw_split)
        original_search_query = row.original_search_query
        original_search_query = original_search_query.replace("'", "''")
        priority = row.priority
        kw_push = row.kw_push
        phase = row.phase
        difficulty = row.difficulty_level

        priority_query = f"""
        UPDATE "{name}"
        set priority = '{priority}'
        WHERE category = '{category}' AND main_folder = '{main_folder}' AND sub_folder = '{sub_folder}' AND search_query = '{search_query}' AND original_search_query ='{original_search_query}'
        """
        cursor.execute(priority_query)

        kw_query = f"""
        UPDATE {name}
        set kw_push = '{kw_push}'
        WHERE category = '{category}' AND main_folder = '{main_folder}' AND sub_folder = '{sub_folder}' AND search_query = '{search_query}' AND original_search_query ='{original_search_query}'
        """
        cursor.execute(kw_query)

        phase_query = f"""
        UPDATE {name}
        set phase = '{phase}'
        WHERE category = '{category}' AND main_folder = '{main_folder}' AND sub_folder = '{sub_folder}' AND search_query = '{search_query}' AND original_search_query ='{original_search_query}'
        """
        cursor.execute(phase_query)

        difficulty_query = f"""
        UPDATE {name}
        set difficulty_level = '{difficulty}'
        WHERE category = '{category}' AND main_folder = '{main_folder}' AND sub_folder = '{sub_folder}' AND search_query = '{search_query}' AND original_search_query ='{original_search_query}'
        """
        cursor.execute(difficulty_query)

    conn.commit()
    print("태그 업데이트 완료")


def fetch_data(table_name):
    total_result = []
    query = f"""SELECT category, main_folder, sub_folder, search_query, search_volume, original_search_query, priority, kw_push, phase, difficulty_level FROM "{table_name}";"""
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        total_result.append(row)

    columns = [
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
    df = pd.DataFrame(total_result, columns=columns)
    df["kw_split"] = df.search_query.apply(lambda x: x.split())
    df = df[
        [
            "category",
            "main_folder",
            "sub_folder",
            "search_query",
            "search_volume",
            "original_search_query",
            "kw_split",
            "priority",
            "kw_push",
            "phase",
            "difficulty_level",
        ]
    ]

    return df


def fetch_table_list():
    total_table = []
    cursor.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
    )
    tables = cursor.fetchall()
    for table in tables:
        total_table.append(table[0])

    return total_table


def update_total_kws_df():
    if len(st.session_state.tagged_roots) > 0:
        for roots in st.session_state.tagged_roots:
            root1_kw = roots[0]
            root2_kw = roots[1]
            tag_kw = roots[2]

            append_cond = (st.session_state.total_kws_df["tier1"].isin([root1_kw])) & (
                st.session_state.total_kws_df["tier2"].isin([root2_kw])
            )

            st.session_state.total_kws_df.loc[
                append_cond, "tag"
            ] = st.session_state.total_kws_df.loc[append_cond, "tag"].apply(
                lambda tags: tags + [tag_kw]
                if tag_kw not in tags and isinstance(tags, list)
                else tags  # 리스트에 값을 추가
            )
            # print(f'태그 테스트 중 >> {tag_kw}, tier1 >> {root1_kw}, tier2 >> {root2_kw}')

    elif len(st.session_state.tagged_roots) == 0:
        st.session_state.total_kws_df["tag"] = [[]] * len(st.session_state.total_kws_df)

    st.session_state.total_kws_df["tag"] = st.session_state.total_kws_df["tag"].apply(
        lambda x: list(set(x))
    )
    st.session_state.tag_inputs = list(
        set([item[2] for item in st.session_state.tagged_roots])
    )

def convert_df(df):
    return df.to_csv()

def kw_normalization(data):
    data["kw_split"] = data.search_query.apply(lambda x: x.split())
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
    data.rename(columns={"search_query": "original_search_query"}, inplace=True)
    data["search_query"] = data.kw_split_lemma.apply(lambda x: " ".join(x))

    return data

def make_folder(data, word_count, main_keywords_huddle, sub_keywords_huddle):
    print("Maker folder Start !!")
    origin_data = pd.read_excel(data, index_col=0)

    data = origin_data[["Keyword", "SV"]].copy()
    data.rename(
        columns={"Keyword": "search_query", "SV": "search_volume"}, inplace=True
    )
    data = data.sort_values("search_volume", ascending=False)

    data["kw_split"] = data.search_query.apply(lambda x: x.split())
    data.index = np.arange(len(data))

    data = kw_normalization(data)  # 써치쿼리를 nomarlization
    sq_volumes = list(zip(data.search_query, data.search_volume))

    total_folder = {}
    while True:
        top_folder_name = sq_volumes[0][0]
        top_folder_name_split = top_folder_name.split()
        total_sub_folder_df = data[
            data.kw_split_lemma.apply(
                lambda x: all(elem in x for elem in top_folder_name_split)
            )
        ]
        sub_folder_keywords = total_sub_folder_df.search_query.tolist()

        total_sub_folder = {}
        while True:
            sub_folder_name = sub_folder_keywords[0]
            sub_folder_name_split = sub_folder_name.split()
            sub_total_df = total_sub_folder_df[
                total_sub_folder_df.kw_split_lemma.apply(
                    lambda x: all(elem in x for elem in sub_folder_name_split)
                )
            ]

            total_sub_keywords = sub_total_df.search_query.tolist()

            total_sub_folder[sub_folder_name] = sub_total_df
            if len(sub_folder_name_split) > 1:
                sub_folder_keywords = list(
                    filter(lambda x: x not in total_sub_keywords, sub_folder_keywords)
                )
            else:
                sub_folder_keywords.remove(sub_folder_name)

            # print(
            #     f'top folder name >> {top_folder_name}, sub_folder_name >> {sub_folder_name}, sub keyword 갯수 >> {len(sub_total_df)}, sub_folder갯수 >> {len(sub_folder_keywords)}')
            if len(sub_folder_keywords) == 0:
                break

        total_folder[top_folder_name] = total_sub_folder
        sq_volumes = list(filter(lambda x: top_folder_name not in x[0], sq_volumes))

        if len(sq_volumes) == 0:
            break

    ### line 123 ~ 143 / top folder uncate 만들기 ###
    uncate_main_folders = []

    for main_folder in total_folder.keys():
        sub_folders = total_folder[main_folder].keys()
        sub_folder_dfs = []
        for sub_folder in sub_folders:
            sub_folder_df = total_folder[main_folder][sub_folder]
            sub_folder_dfs.append(sub_folder_df)

        sub_folder_dfs = pd.concat(sub_folder_dfs)
        sub_folder_dfs = sub_folder_dfs.drop_duplicates(subset="search_query")
        # print(f'써브폴더 dfs 갯수 >> {len(sub_folder_dfs)}, 메인키워드 허들 갯수 >> {main_keywords_huddle}, 타입1 >> {type(len(sub_folder_dfs))}, 타입2 >> {type(main_keywords_huddle)}')
        if (
            len(sub_folder_dfs) < main_keywords_huddle
            or len(main_folder.split()) > word_count
        ):
            uncate_main_folders.append(main_folder)

    uncate_dfs = {}
    for uncate_folder in uncate_main_folders:
        uncate_dfs[uncate_folder] = total_folder[uncate_folder]
        del total_folder[uncate_folder]

    total_folder["uncategorized"] = uncate_dfs

    ### line 145 ~ 161  / sub_folder keyword 의 수가 적으면 언카테고리로 이동시킴 ###
    for folder_name in total_folder.keys():
        if folder_name == "uncategorized":
            continue
        sub_folder_list = total_folder[folder_name].keys()
        sub_uncate_dfs = []
        remove_sub_folders = []
        for sub_folder in sub_folder_list:
            sub_folder_df = total_folder[folder_name][sub_folder]
            if len(sub_folder_df) < sub_keywords_huddle:
                remove_sub_folders.append(sub_folder)
                sub_uncate_dfs.append(sub_folder_df)
                # print(f'sub_folder >> {sub_folder}, {len(sub_folder_df)} 언카테고리로 이동')
        if len(sub_uncate_dfs) > 0:
            total_folder[folder_name]["uncategorized"] = pd.concat(sub_uncate_dfs)
            for remove_folder_name in remove_sub_folders:
                del total_folder[folder_name][remove_folder_name]

    ### line 96 ~ 121 / 폴더명이 긴 폴더를 >> 폴더명이 짧은 폴더로 합치기 위한 코드 ###
    sorted_total_folder_names = sorted(
        list(total_folder.keys()), key=len
    )  # 폴더이름이 짧은게 위로 올라오도록 정렬

    for folder_name in sorted_total_folder_names:
        if folder_name not in total_folder.keys():
            # print(folder_name, '폴더는 이미 제거됨')
            continue
        folder_name_split = folder_name.split()
        merge_folder_names = [
            keyword
            for keyword in sorted_total_folder_names
            if all(folder_part in keyword for folder_part in folder_name_split)
            and " ".join(folder_name_split) != keyword
        ]

        if len(merge_folder_names) >= 1:
            for merge_folder_name in merge_folder_names:
                if (
                    merge_folder_name in total_folder.keys()
                ):  ### 토탈폴더에 지워야 될 폴더가 있으면 폴더합병을 진행
                    sub_merge_folder_names = total_folder[merge_folder_name].keys()
                else:
                    continue
                for sub_merge_folder_name in sub_merge_folder_names:
                    if (
                        sub_merge_folder_name not in total_folder[folder_name].keys()
                    ):  ### 폴더안에 서브폴더 키워드가 없어야 합병을 진행함
                        merge_df = total_folder[merge_folder_name][
                            sub_merge_folder_name
                        ]
                        total_folder[folder_name][sub_merge_folder_name] = merge_df

                    # print(f'{merge_folder_name}의 {sub_merge_folder_name}을 {folder_name}에 병합 완료함')

                del total_folder[merge_folder_name]

    main_dict = {"main": {x: y for x, y in total_folder.items()}}
    total_folder.update(main_dict)
    total_folder = {
        key: value
        for key, value in total_folder.items()
        if key in ["main", "uncategorized"]
    }
    del total_folder["main"]["uncategorized"]
    st.session_state.total_folder = total_folder.copy()

    ### unique data 만드는곳 ###
    main_folder_data = []
    for folder_name in total_folder["main"].keys():
        sub_folders = total_folder["main"][folder_name].keys()
        for sub_folder in sub_folders:
            df = total_folder["main"][folder_name][sub_folder]
            a = df.copy()
            a["main_folder"] = folder_name
            a["sub_folder"] = sub_folder
            main_folder_data.append(a)

    main_folder_df = pd.concat(main_folder_data)
    main_folder_df["Category"] = "Main"
    main_folder_df["priority"] = ""
    main_folder_df["kw_push"] = ""
    main_folder_df["phase"] = ""
    main_folder_df["difficulty_level"] = ""
    st.session_state.main_folder_df = main_folder_df.copy()[
        [
            "Category",
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
    ]
    st.session_state.main_folder_df.rename(
        columns={
            "main_folder": "Main Folder",
            "sub_folder": "Sub Folder",
            "search_query": "Unique Normalized Search Query",
            "search_volume": "Search Volume",
            "priority": "Priority",
            "original_search_query": "Original Search Query",
            "kw_push": "KW Push",
            "phase": "Phase",
            "difficulty_level": "Difficulty Level",
        },
        inplace=True,
    )

    ### normalized data 만드는곳 ###
    nomarlized_main = (
        main_folder_df.groupby("search_query")["search_volume"].sum().reset_index()
    )
    for row in nomarlized_main.itertuples():
        search_query = row.search_query
        frequency = len(
            nomarlized_main[
                nomarlized_main.search_query.apply(lambda x: search_query in x)
            ]
        )
        index = row.Index
        nomarlized_main.at[index, "Frequency"] = frequency
    nomarlized_main = nomarlized_main.sort_values("Frequency", ascending=False)[
        ["search_query", "Frequency", "search_volume"]
    ]
    st.session_state.nomarlized_main = nomarlized_main.copy()
    st.session_state.nomarlized_main.rename(
        columns={"search_query": "Search Query", "search_volume": "Search Volume"},
        inplace=True,
    )

    #### 언카테 폴더로 만드는 데이터 ####

    uncate_data = []
    for folder_name in total_folder["uncategorized"].keys():
        sub_folders = total_folder["uncategorized"][folder_name].keys()
        for sub_folder in sub_folders:
            df = total_folder["uncategorized"][folder_name][sub_folder]
            a = df.copy()
            a["main_folder"] = folder_name
            a["sub_folder"] = sub_folder
            uncate_data.append(a)

    uncate_df = pd.concat(uncate_data)
    uncate_df["Category"] = "Uncate"
    uncate_df["priority"] = ""
    uncate_df["kw_push"] = ""
    uncate_df["phase"] = ""
    uncate_df["difficulty_level"] = ""

    st.session_state.uncate_df = uncate_df.copy()[
        [
            "Category",
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
    ]
    st.session_state.uncate_df.rename(
        columns={
            "main_folder": "Main Folder",
            "sub_folder": "Sub Folder",
            "search_query": "Unique Normalized Search Query",
            "search_volume": "Search Volume",
            "original_search_query": "Original Search Query",
            "priority": "Priority",
            "kw_push": "KW Push",
            "phase": "Phase",
            "difficulty_level": "Difficulty Level",
        },
        inplace=True,
    )

    nomarlized_uncate = (
        uncate_df.groupby("search_query")["search_volume"].sum().reset_index()
    )
    for row in nomarlized_uncate.itertuples():
        search_query = row.search_query
        frequency = len(
            nomarlized_uncate[
                nomarlized_uncate.search_query.apply(lambda x: search_query in x)
            ]
        )
        index = row.Index
        nomarlized_uncate.at[index, "Frequency"] = frequency
    nomarlized_uncate = nomarlized_uncate.sort_values("Frequency", ascending=False)[
        ["search_query", "Frequency", "search_volume"]
    ]
    st.session_state.normalized_uncate = nomarlized_uncate.copy()
    st.session_state.normalized_uncate.rename(
        columns={"search_query": "Search Query", "search_volume": "Search Volume"},
        inplace=True,
    )

    st.session_state.load_state = False  # unique normalized data가 만들어졌으면 load state를 True로 전환, 이렇게 해야 make folder가 실행이 안됨
    st.session_state.make_folder = True


def data_from_db():
    table_name = st.session_state.table_name
    db_data = fetch_data(table_name)

    main_data = db_data[db_data.category == "Main"].copy()
    uncate_data = db_data[db_data.category != "Main"].copy()

    main_data.rename(
        columns={
            "category": "Category",
            "main_folder": "Main Folder",
            "sub_folder": "Sub Folder",
            "search_query": "Unique Normalized Search Query",
            "search_volume": "Search Volume",
            "priority": "Priority",
            "original_search_query": "Original Search Query",
            "kw_push": "KW Push",
            "phase": "Phase",
            "difficulty_level": "Difficulty Level",
        },
        inplace=True,
    )

    uncate_data.rename(
        columns={
            "category": "Category",
            "main_folder": "Main Folder",
            "sub_folder": "Sub Folder",
            "search_query": "Unique Normalized Search Query",
            "search_volume": "Search Volume",
            "priority": "Priority",
            "original_search_query": "Original Search Query",
            "kw_push": "KW Push",
            "phase": "Phase",
            "difficulty_level": "Difficulty Level",
        },
        inplace=True,
    )

    st.session_state.main_folder_df = main_data.copy()
    st.session_state.uncate_df = uncate_data.copy()

    st.session_state.load_state = False  # unique normalized data가 만들어졌으면 load state를 True로 전환, 이렇게 해야 make folder가 실행이 안됨
    st.session_state.make_folder = True

if __name__ == "__main__":
    table_list = fetch_table_list()
    for table in table_list:
        drop_table(table)

    # a = drop_table("aaa aaa")
    # print(a)
