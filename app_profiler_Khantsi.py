import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Dr. Motlagomang Khantsi"
field = "Microbiologist"
institution = "North-West University"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://scholar.googleusercontent.com/citations?view_op=view_photo&user=vLQzzEYAAAAJ&citpid=2",
    caption="MamzoKhay"
)

st.header("Professional Summary")
st.write("I have always aspired to witness significant progress within our generation and lifetime. I aim to make a meaningful contribution to the community through active participation in transdisciplinary research and innovation. I firmly believe that every individual possesses remarkable potential and excellence, needing only proper guidance and fair opportunities to reach their full potential.")
# Add a section for publications
st.header("Publications")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Publications.csv", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
Microbiology_data = pd.DataFrame({
    "Experiment": ["PGPR", "CLPP", "Metagenomics", "Bioinformatics"],
    "Data volume (GB)": [3.2, 2.9, 9.4, 11.1],
    "Date": pd.date_range(start="2025-01-01", periods=4),
})

Microbial_data = pd.DataFrame({
    "Genus Name": ["Bacillus", "Pseudomonas", "Proteobacteria", "Salmonella", "Actionobacteria"],
    "Abundance (Size)": [2.0, 4.6, 1.8, 0.2, 12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

Sampling_site_data = pd.DataFrame({
    "City": ["Mahikeng", "Stella", "Lichtenburg", "Rustenburg", "Brits"],
    "Temperature (°C)": [25, 10, 13, 25, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2025-01-01", periods=5),
})

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Microbiology Experiments", "Sampling Site Data"]
)

if data_option == "Microbiology Experiments":
    st.write("### Microbiology Experiment Data")
    st.dataframe(Microbiology_data)
    # Add widget to filter by Energy levels
    energy_filter = st.slider("Filter by Data volume (GB)", 0.0, 10.0, (0.0, 10.0))
    filtered_Microbiology = Microbiology_data[
        Microbiology_data["Data volume (GB)"].between(energy_filter[0], energy_filter[1])
    ]
    st.write(f"Filtered Results for Energy Range {energy_filter}:")
    st.dataframe(filtered_Microbiology)


elif data_option == "Sampling Site Data":
    st.write("### Sampling Site Data")
    st.dataframe(Sampling_site_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_weather = Sampling_site_data[
        Sampling_site_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        Sampling_site_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_weather)

# Add a contact section
st.header("Motlagomang Khantsi")
email = "motlagomang.khantsi@nwu.ac.za"
st.write(f"You can reach {name} at {email}.")