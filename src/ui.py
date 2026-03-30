"""
src/ui.py
=========
Small UI helpers shared across Streamlit pages.
"""

from __future__ import annotations

import streamlit as st
from src.downloader import PL_SEASONS, format_season


def season_banner(n_sims: int = 1000) -> None:
    """
    Render a consistent banner showing which season is being predicted and
    what seasons were used for training.
    """
    if "data" not in st.session_state:
        return

    data = st.session_state["data"]
    target = format_season(data["target_season"])

    train_seasons = [format_season(s) for s in PL_SEASONS[:-1]]
    first_train = train_seasons[0]
    last_train = train_seasons[-1]

    st.info(
        f"🔮 **Predicting season: {target}**  ·  "
        f"Model trained on: {first_train} → {last_train}  ·  "
        f"{n_sims:,} Monte Carlo simulations"
    )