import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from streamlit.source_util import (
    page_icon_and_name, 
    calc_md5, 
    get_pages,
    _on_pages_changed
)

def delete_page(main_script_path_str, page_name):

    current_pages = get_pages(main_script_path_str)

    #debug
    # st.write(current_pages)

    for key, value in current_pages.items():
        if value['page_name'] == page_name:
            del current_pages[key]
            break
        else:
            pass
    _on_pages_changed.send()

def add_page(main_script_path_str, page_name):
    pages = get_pages(main_script_path_str)
    main_script_path = Path(main_script_path_str)
    pages_dir = main_script_path.parent / "pages"
    # st.write(list(pages_dir.glob("*.py"))+list(main_script_path.parent.glob("*.py")))
    script_path = [f for f in list(pages_dir.glob("*.py"))+list(main_script_path.parent.glob("*.py")) if f.name.find(page_name) != -1][0]
    script_path_str = str(script_path.resolve())
    pi, pn = page_icon_and_name(script_path)
    psh = calc_md5(script_path_str)
    pages[psh] = {
        "page_script_hash": psh,
        "page_name": pn,
        "icon": pi,
        "script_path": script_path_str,
    }
    _on_pages_changed.send()

# hides the logout and login pages based on the authentication status
def hide_logout_login_pages(current_page):
    if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
        add_page(current_page, "Login")
        delete_page(current_page, "Logout")
    else:
        delete_page(current_page, "Login")
        add_page(current_page, "Logout")
        