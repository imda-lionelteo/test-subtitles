from datetime import timedelta

import librosa
import pandas as pd
import streamlit as st


def extract_audio_metadata(uploaded_file):
    """
    Extract comprehensive metadata from an uploaded audio file.

    This function uses librosa to analyze the audio file and extract various
    properties including duration, file size, sample rate, channel configuration,
    and format information.

    Args:
        uploaded_file: Streamlit uploaded file object containing the audio data

    Returns:
        dict: Dictionary containing audio metadata with keys:
            - filename: Original filename of the uploaded file
            - file_size: File size formatted as MB string
            - duration: Duration formatted as HH:MM:SS string
            - sample_rate: Sample rate formatted with commas and Hz unit
            - channels: Channel configuration (Mono or Stereo with count)
            - format: File format extension in uppercase
        None: If metadata extraction fails
    """
    try:
        # Load audio file using librosa with original sample rate preserved
        audio_data, sample_rate = librosa.load(uploaded_file, sr=None)

        # Calculate total duration in seconds and format as HH:MM:SS
        duration_seconds = len(audio_data) / sample_rate
        duration_formatted = str(timedelta(seconds=int(duration_seconds)))

        # Convert file size from bytes to megabytes for readability
        file_size_bytes = uploaded_file.size
        file_size_mb = file_size_bytes / (1024 * 1024)

        # Determine channel configuration (mono vs stereo/multichannel)
        channels = 1 if len(audio_data.shape) == 1 else audio_data.shape[0]

        # Compile all metadata into a structured dictionary
        metadata = {
            "filename": uploaded_file.name,
            "file_size": f"{file_size_mb:.2f} MB",
            "duration": duration_formatted,
            "sample_rate": f"{sample_rate:,} Hz",
            "channels": "Mono" if channels == 1 else f"Stereo ({channels} channels)",
            "format": uploaded_file.name.split(".")[-1].upper(),
        }

        return metadata

    except Exception as e:
        # Display error message to user if metadata extraction fails
        st.error(f"Error extracting metadata: {str(e)}")
        return None


def display_audio_metadata_table(metadata):
    """
    Display audio file metadata in a professionally formatted table.

    This function creates a pandas DataFrame from the metadata dictionary
    and displays it using Streamlit's dataframe component with custom
    column configurations for optimal presentation.

    Args:
        metadata (dict): Dictionary containing audio metadata with property-value pairs
    """
    if metadata:
        # Prepare structured data for tabular display
        metadata_data = {
            "Property": ["Filename", "Duration", "File Size", "Sample Rate", "Format", "Channels"],
            "Value": [
                metadata["filename"],
                metadata["duration"],
                metadata["file_size"],
                metadata["sample_rate"],
                metadata["format"],
                metadata["channels"],
            ],
        }

        # Create DataFrame for structured data presentation
        df = pd.DataFrame(metadata_data)

        # Display as a professionally styled table with custom column configurations
        st.dataframe(
            df,
            use_container_width=True,  # Make table responsive to container width
            hide_index=True,  # Hide row indices for cleaner appearance
            column_config={
                "Property": st.column_config.TextColumn("Property", help="Audio file properties", width="medium"),
                "Value": st.column_config.TextColumn("Value", help="Property values", width="large"),
            },
        )


def display_audio_upload_interface():
    """
    Display the complete audio file upload interface with metadata extraction.

    This function renders a bordered container with:
    1. Instructional header and description
    2. File uploader widget for audio files
    3. Audio player for uploaded files
    4. Metadata extraction and display functionality

    The interface supports multiple audio formats and provides real-time
    feedback during metadata processing.

    Returns:
        uploaded_file: The uploaded file object, or None if no file uploaded
    """
    # Create bordered container for organized layout
    with st.container(border=True):
        # Display instructional header with styling
        st.markdown(
            """
        <div class="upload-section">
            <h2>Step 1: Select Your Audio File</h2>
            <p>Upload an audio file to compare transcription accuracy across multiple AI models</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # File uploader widget with supported format specifications
        uploaded_file = st.file_uploader(
            "Choose an audio file",
            type=["wav", "mp3"],  # Supported audio formats
            help="Supported formats: WAV, MP3",
        )

        # Process and display uploaded file information
        if uploaded_file is not None:
            # Add visual separator between upload and metadata sections
            st.markdown("<hr style='margin: 0.5rem 0;'>", unsafe_allow_html=True)

            # Display section header for audio information
            st.markdown(
                """
            <div class="upload-section">
                <h2>Audio File Information</h2>
            </div>
            """,
                unsafe_allow_html=True,
            )

            # Embed audio player for file preview
            st.audio(uploaded_file, format="audio/wav")

            # Create a unique key for the uploaded file to cache metadata
            file_key = f"{uploaded_file.name}_{uploaded_file.size}"

            # Check if metadata is already cached for this file
            if f"metadata_{file_key}" not in st.session_state:
                # Extract and display metadata with loading indicator (only if not cached)
                with st.spinner("Extracting audio metadata..."):
                    metadata = extract_audio_metadata(uploaded_file)
                    # Cache the metadata in session state
                    st.session_state[f"metadata_{file_key}"] = metadata
            else:
                # Use cached metadata
                metadata = st.session_state[f"metadata_{file_key}"]

            # Display the metadata table
            if metadata:
                display_audio_metadata_table(metadata)

        return uploaded_file
