import streamlit as st
from streamlit.logger import get_logger

from src.landing import display_main_page

logger = get_logger(__name__)


def apply_custom_css():
    """
    Apply custom CSS styles to the Streamlit application.

    Hides the default Streamlit header and footer, and applies custom styles
    for the sections bar to enhance the user interface.

    Returns:
        None
    """
    hide_decoration_bar_style = """<style>header {visibility: hidden;}</style>"""
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                            footer {visibility: hidden;}</style>"""
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)


def set_custom_width_layout():
    """
    Configure the page layout with a custom width between "centered" and "wide".

    Sets the page title and applies custom CSS to adjust the container width
    for better content display.

    Returns:
        None
    """
    # Create a layout width between "centered" and "wide"
    st.set_page_config(
        page_title="Audio Transcription Comparison Tool",
        layout="centered",  # Start with centered as base
        page_icon="🎵",  # Set the favicon
    )

    # Apply custom CSS to make it wider than default centered, but not as wide as "wide"
    st.markdown(
        """
    <style>
    .block-container {
        max-width: 1000px;  # Adjust this value as needed (centered is ~730px, wide is ~1168px)
        padding-top: 0.5rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
        margin: 0 auto;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


def main():
    """
    Initialize the application and display the UI components.

    Sets up the session state for new sessions, configures the page layout,
    applies custom CSS, and renders the UI components including the sections bar,
    current section content, and navigation buttons.

    Returns:
        None
    """
    # Set the page layout and width
    set_custom_width_layout()

    # Apply custom CSS styles
    apply_custom_css()

    # Display the main page
    display_main_page()


# Main execution
if __name__ == "__main__":
    main()
