import streamlit as st


def apply_landing_styles():
    """
    Apply CSS styling for the homepage components.

    This function contains all the CSS styling for the banner and upload sections
    of the homepage, providing a consistent and professional appearance.
    """
    st.markdown(
        """
    <style>
    .banner {
        border-radius: 15px;
        text-align: center;
        padding: 2rem 1rem;
        margin: 0;
    }

    .banner h1 {
        color: black;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }

    .banner p {
        color: black;
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        font-weight: 300;
    }

    .upload-section h2 {
        color: black;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0 0 1rem 0;
    }

    .upload-section p {
        color: black;
        font-size: 1rem;
        margin: 0 0 1rem 0;
        font-weight: 300;
    }

    .step-section h2 {
        color: black;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0 0 1rem 0;
    }

    .step-section p {
        color: black;
        font-size: 1rem;
        margin: 0 0 1rem 0;
        font-weight: 300;
    }

    .metadata-section {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #e9ecef;
    }

    .metadata-section h3 {
        color: #495057;
        font-size: 1.25rem;
        font-weight: 600;
        margin: 0 0 1rem 0;
        border-bottom: 2px solid #dee2e6;
        padding-bottom: 0.5rem;
    }

    .metadata-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }

    .metadata-item {
        background-color: white;
        padding: 0.75rem;
        border-radius: 6px;
        border: 1px solid #dee2e6;
    }

    .metadata-label {
        font-weight: 600;
        color: #6c757d;
        font-size: 0.875rem;
        margin-bottom: 0.25rem;
    }

    .metadata-value {
        color: #212529;
        font-size: 1rem;
        font-weight: 500;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
