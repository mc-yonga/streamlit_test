from uploadView import *
from dataView import *
from labelView import *
from tagView import *

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    if "uploaded_file" not in st.session_state:
        st.session_state["uploaded_file"] = None
    if "db_load_file" not in st.session_state:
        st.session_state["db_load_file"] = None
    if "word_count" not in st.session_state:
        st.session_state["word_count"] = None
    if "main_keywords_huddle" not in st.session_state:
        st.session_state["main_keywords_huddle"] = None
    if "sub_keywords_huddle" not in st.session_state:
        st.session_state["sub_keywords_huddle"] = None
    if "load_way" not in st.session_state:
        st.session_state.load_way = None
    if "load_state" not in st.session_state:
        st.session_state.load_state = False
    if "main_folder_df" not in st.session_state:
        st.session_state.main_folder_df = None
    if "uncate_df" not in st.session_state:
        st.session_state.uncate_df = None
    if "nomarlized_main" not in st.session_state:
        st.session_state.nomarlized_main = None
    if "normalized_uncate" not in st.session_state:
        st.session_state.normalized_uncate = None
    if "priority_tag_info" not in st.session_state:
        st.session_state.priority_tag_info = {}
    if "kwpush_tag_info" not in st.session_state:
        st.session_state.kwpush_tag_info = {}
    if "phase_tag_info" not in st.session_state:
        st.session_state.phase_tag_info = {}
    if "diffi_tag_info" not in st.session_state:
        st.session_state.diffi_tag_info = {}
    if "priority_tag_info2" not in st.session_state:
        st.session_state.priority_tag_info2 = {}
    if "kwpush_tag_info2" not in st.session_state:
        st.session_state.kwpush_tag_info2 = {}
    if "phase_tag_info2" not in st.session_state:
        st.session_state.phase_tag_info2 = {}
    if "diffi_tag_info2" not in st.session_state:
        st.session_state.diffi_tag_info2 = {}
    if "tag_view" not in st.session_state:
        st.session_state.tag_view = None
    if "total_folder" not in st.session_state:  # 딕셔너리 형태로 main, uncategorized 데이터를 관리
        st.session_state.total_folder = {}
    if "make_folder" not in st.session_state:   # normalized와 unique data 가 만들어졌으면 True
        st.session_state.make_folder = False
    if 'table_name' not in st.session_state:
        st.session_state.table_name = None
    if 'data_view1_key' not in st.session_state:
        st.session_state.data_view1_key = None
    if 'data_view2_key' not in st.session_state:
        st.session_state.data_view2_key = None



    st.title(":dart: Keyword Classify Solution")
    tab_titles = [":one: Upload View", ":two: Data View", ":three: Label View", ":four: Tag View"]
    upload_tab, dataview_tab, labelview_tab, tagview_tab = st.tabs(
        tab_titles
    )

    with upload_tab:
        UploadView()

    with labelview_tab:
        LabelView()

    with dataview_tab:
        DataView()

    with tagview_tab:
        TagView()
