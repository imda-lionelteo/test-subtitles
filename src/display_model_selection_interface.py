import streamlit as st


def display_meralion_model_selection():
    """
    Display the MERaLiON model selection interface.

    Shows information about the MERaLiON-2-10B-ASR model including
    its capabilities and supported formats.
    """
    with st.container(border=False):
        st.markdown(
            """
        <div class="step-section">
            <b>MERaLiON-2-10B-ASR</b>
            <p>Supports audio up to 5 minutes with automatic chunking per 30 seconds. Accepts wav/mp3/ogg formats, 16khz, mono channel.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )


def display_other_models_selection():
    """
    Display the other models selection interface.

    Provides checkboxes for selecting additional ASR models to compare
    against MERaLiON, with future models shown as disabled placeholders.
    """
    with st.container(border=False):
        st.markdown(
            """
        <div class="step-section">
            <b>Other ASR Models</b>
            <p style="margin: 0.5rem 0; font-size: 0.9em;">Select models to compare against MERaLiON:</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Model selection checkboxes
        whisper_selected = st.checkbox("Whisper API", value=True, key="whisper_model")

        # Placeholder for future models (disabled for now)
        st.checkbox("OpenAI Whisper", value=False, disabled=True, key="openai_whisper", help="Coming soon")
        st.checkbox("Google Speech-to-Text", value=False, disabled=True, key="google_stt", help="Coming soon")
        st.checkbox("Azure Speech Services", value=False, disabled=True, key="azure_speech", help="Coming soon")

        # Store selected models in session state for use by compare button
        if "selected_models" not in st.session_state:
            st.session_state.selected_models = []

        # Update selected models based on checkboxes
        selected_models = []
        if whisper_selected:
            selected_models.append("Whisper API")

        st.session_state.selected_models = selected_models


def display_model_selection_interface():
    """
    Display the model selection interface for transcription comparison.

    This function orchestrates the display of model selection components,
    allowing users to choose which AI models to compare for audio transcription.
    Includes both MERaLiON and other available ASR models with a comparison
    initiation button.

    Returns:
        list: Selected models if comparison button is clicked, None otherwise
    """
    # Create bordered container for organized layout
    with st.container(border=True):
        # Display instructional header with styling
        st.markdown(
            """
        <div class="step-section">
            <h2>Step 2: Select Models for Comparison</h2>
            <p>Choose which AI models you want to compare</p>
            <hr style="margin: 0.5rem 0;">
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Create two-column layout for comparison results with vertical divider
        col1, _, col2 = st.columns([1, 0.05, 1])
        with col1:
            display_meralion_model_selection()
        with col2:
            display_other_models_selection()

        # Add spacing and compare button
        st.markdown("<br>", unsafe_allow_html=True)

        # Center the compare button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            # Check if any models are selected
            selected_models = st.session_state.get("selected_models", [])
            button_disabled = len(selected_models) == 0

            if st.button("🔄 Start Comparison", type="primary", use_container_width=True, disabled=button_disabled):
                return selected_models
