# -*- coding: utf-8 -*-
# Copyright 2024-2025 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from dataclasses import dataclass

st.set_page_config(page_title="To-do list", page_icon=":memo:")

# Declare alias for st.session_state, just for convenience.
state = st.session_state


@dataclass
class Todo:
    text: str
    is_done = False


if "todos" not in state:
    state.todos = [
        Todo(text="Buy milk"),
        Todo(text="Wash dishes"),
        Todo(text="Write a novel"),
    ]


def remove_todo(i):
    state.todos.pop(i)


def add_todo():
    state.todos.append(Todo(text=state.new_item_text))
    state.new_item_text = ""


def check_todo(i, new_value):
    state.todos[i].is_done = new_value


def delete_all_checked():
    state.todos = [t for t in state.todos if not t.is_done]


with st.container(horizontal_alignment="center"):
    st.title(
        ":orange[:material/checklist:] To-do list",
        width="content",
        anchor=False,
    )

with st.form(key="new_item_form", border=False):
    with st.container(
        horizontal=True,
        vertical_alignment="bottom",
    ):
        st.text_input(
            "New item",
            label_visibility="collapsed",
            placeholder="Add to-do item",
            key="new_item_text",
        )

        st.form_submit_button(
            "Add",
            icon=":material/add:",
            on_click=add_todo,
        )

if state.todos:
    with st.container(gap=None, border=True):
        for i, todo in enumerate(state.todos):
            with st.container(horizontal=True, vertical_alignment="center"):
                st.checkbox(
                    todo.text,
                    value=todo.is_done,
                    width="stretch",
                    on_change=check_todo,
                    args=[i, not todo.is_done],
                )
                st.button(
                    ":material/delete:",
                    type="tertiary",
                    key=f"delete_{i}",
                    on_click=remove_todo,
                    args=[i],
                )

    with st.container(horizontal=True, horizontal_alignment="center"):
        st.button(
            ":small[Delete all checked]",
            icon=":material/delete_forever:",
            type="tertiary",
            on_click=delete_all_checked,
        )

else:
    st.info("No to-do items. Go fly a kite! :material/family_link:")
