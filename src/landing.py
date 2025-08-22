import streamlit as st

from src.display_audio_upload_interface import display_audio_upload_interface
from src.display_comparison_interface import display_comparison_interface
from src.display_model_selection_interface import display_model_selection_interface
from src.styles.landing_style import apply_landing_styles


def display_banner():
    """
    Display the professional banner at the top of the main page.

    Renders a styled HTML banner containing the application title and description.
    """
    st.markdown(
        """
    <div class="banner" style="padding: 1rem 1rem;">
        <h3>MERaLiON-2 Audio Transcription Comparison</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )


def display_main_page():
    """
    Display the complete homepage layout.

    This function orchestrates the display of all homepage components including
    the banner, spacing, and upload section with appropriate styling applied.
    The comparison interface is only shown after a file has been uploaded.
    """
    # Apply custom CSS styling for homepage components
    apply_landing_styles()

    # Display the main banner with title and description
    display_banner()

    # Add visual spacing between banner and upload section
    st.markdown("<br>", unsafe_allow_html=True)

    # Display the audio file upload interface
    uploaded_file = display_audio_upload_interface()

    # Only display the comparison interface if a file has been uploaded
    if uploaded_file is not None:
        st.markdown("<br>", unsafe_allow_html=True)
        selected_models = display_model_selection_interface()
        if selected_models:
            st.info(f"Comparing MERaLiON with {selected_models}")
            display_comparison_interface()
