import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import Dict, Any

st.set_page_config(
    page_title="Single Prompt Analysis",
    page_icon="📄",
    layout="wide"
)

st.title("Original Prompt FileCategory with Denoise Analysis")
st.markdown("""
This dashboard visualizes the results of a original prompt with the addition of denoise applied to different real-world files, 
with a special focus on how noise in files affects extraction quality.

The analysis shows how the same prompt performs on clean files versus files with HTML markup, 
advertisements, and other noise elements.
""")

# Define available category files
category_files = {
    "Government & Law": {
        "clean": "results/real_file/government_and_law_real_result.json",
        "with_noise": "results/real_file/government_and_law_with_noise_result.json",
        "original": "results/real_file/government_and_law_result.json"
    },
    "Business & Corporate": {
        "clean": "results/real_file/business_real_result.json",
        "with_noise": "results/real_file/business_with_noise_result.json"
    },
    "Healthcare & Medical 2": {
        "clean": "results/real_file/medical_real_2_result.json",
        "with_noise": "results/real_file/medical_2_with_noise_result.json"
    },
    "Scientific Research": {
        "clean": "results/real_file/research_real_result.json",
        "with_noise": "results/real_file/research_with_noise_result.json"
    }
}

# Create data structures to store metrics
all_metrics = {}

# Load the category data
@st.cache_data
def load_file_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        st.error(f"Error loading file data: {str(e)}")
        return None

# Load all category data
category_data = {}
for category_name, file_dict in category_files.items():
    category_data[category_name] = {}
    for file_type, file_path in file_dict.items():
        data = load_file_data(file_path)
        if data:
            category_data[category_name][file_type] = data
            # Store metrics for summary
            if category_name not in all_metrics:
                all_metrics[category_name] = {}
            all_metrics[category_name][file_type] = data["metrics"]["total"]

# Special section for Government & Law comparison
st.header("Government & Law Document Analysis")
st.markdown("""
### Impact of Document Noise on Extraction Quality

This section compares how the same prompt performs on three versions of government and law documents:
1. **Clean Text**: Plain text document with minimal formatting
2. **With Noise**: HTML document with advertisements, navigation elements, and other noise
3. **Original**: Base HTML document
""")

# Get the Government & Law data
gov_law_data = category_data.get("Government & Law", {})

# Display metrics comparison for Government & Law
if gov_law_data:
    st.subheader("Metrics Comparison")
    
    # Calculate data extraction completeness for each version
    completeness_data = {}
    
    for version in ["clean", "with_noise", "original"]:
        data = gov_law_data.get(version)
        if data:
            non_empty_count = 0
            total_fields = 0
            
            extracted_data = data.get("extracted_data", {}).get("extracted_data", {})
            for section, section_data in extracted_data.items():
                if isinstance(section_data, dict):
                    for field, value in section_data.items():
                        total_fields += 1
                        if value and value != [] and value != {}:
                            non_empty_count += 1
                elif isinstance(section_data, list):
                    total_fields += 1
                    if section_data:
                        non_empty_count += 1
            
            completeness_data[version] = {
                "non_empty": non_empty_count,
                "total": total_fields,
                "percentage": (non_empty_count/total_fields)*100 if total_fields > 0 else 0
            }
    
    # Create a DataFrame for comparison
    metrics_df = pd.DataFrame({
        "Metric": ["Execution Time (s)", "Cost ($)", "Total Tokens", "Data Completeness"],
        "Clean Text": [
            gov_law_data.get("clean", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            gov_law_data.get("clean", {}).get("metrics", {}).get("total", {}).get("cost", 0),
            gov_law_data.get("clean", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            f"{completeness_data.get('clean', {}).get('non_empty', 0)}/{completeness_data.get('clean', {}).get('total', 0)} ({completeness_data.get('clean', {}).get('percentage', 0):.1f}%)"
        ],
        "With Noise": [
            gov_law_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            gov_law_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("cost", 0),
            gov_law_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            f"{completeness_data.get('with_noise', {}).get('non_empty', 0)}/{completeness_data.get('with_noise', {}).get('total', 0)} ({completeness_data.get('with_noise', {}).get('percentage', 0):.1f}%)"
        ],
        "Original": [
            gov_law_data.get("original", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            gov_law_data.get("original", {}).get("metrics", {}).get("total", {}).get("cost", 0),
            gov_law_data.get("original", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            f"{completeness_data.get('original', {}).get('non_empty', 0)}/{completeness_data.get('original', {}).get('total', 0)} ({completeness_data.get('original', {}).get('percentage', 0):.1f}%)"
        ]
    })
    
    st.table(metrics_df.set_index("Metric"))
    
    # Create smaller charts and place them side by side
    col1, col2 = st.columns(2)

    with col1:
        # Create a bar chart for token usage comparison
        fig, ax = plt.subplots(figsize=(5, 3))
        token_data = [
            gov_law_data.get("clean", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            gov_law_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            gov_law_data.get("original", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0)
        ]
        
        ax.bar(["Clean", "With Noise", "Original"], token_data, color=['#66b3ff', '#ff9999', '#99ff99'])
        ax.set_ylabel('Total Tokens')
        ax.set_title('Token Usage Comparison')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        st.pyplot(fig)

    with col2:
        # Create a bar chart for execution time comparison
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        time_data = [
            gov_law_data.get("clean", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            gov_law_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            gov_law_data.get("original", {}).get("metrics", {}).get("total", {}).get("execution_time", 0)
        ]
        
        ax2.bar(["Clean", "With Noise", "Original"], time_data, color=['#66b3ff', '#ff9999', '#99ff99'])
        ax2.set_ylabel('Time (s)')
        ax2.set_title('Execution Time Comparison')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        st.pyplot(fig2)

    # Create a bar chart for data completeness comparison
    fig3, ax3 = plt.subplots(figsize=(3, 2))
    completeness_percentages = [
        completeness_data.get('clean', {}).get('percentage', 0),
        completeness_data.get('with_noise', {}).get('percentage', 0),
        completeness_data.get('original', {}).get('percentage', 0)
    ]

    bars = ax3.bar(["Clean", "With Noise", "Original"], completeness_percentages, color=['#66b3ff', '#ff9999', '#99ff99'])
    ax3.set_ylabel('Completeness (%)', fontsize=8)
    ax3.set_title('Data Extraction Completeness', fontsize=9)
    ax3.set_ylim(0, 100)
    ax3.tick_params(axis='x', labelsize=7, rotation=45)
    ax3.tick_params(axis='y', labelsize=7)

    # Add percentage labels on top of the bars
    for i, v in enumerate(completeness_percentages):
        ax3.text(i, v + 2, f"{v:.1f}%", ha='center', fontsize=7)

    plt.tight_layout()

    # Use columns to make the chart smaller in the UI
    col1, col2 = st.columns([1, 1])
    with col1:
        st.pyplot(fig3)
    # Display extracted data comparison
    st.subheader("Extracted Data Comparison")
    
    # Create tabs for each version
    gov_tabs = st.tabs(["Clean Text", "With Noise", "Original"])
    
    # Display extracted data for each version
    for tab_name, tab in zip(["clean", "with_noise", "original"], gov_tabs):
        with tab:
            data = gov_law_data.get(tab_name)
            if data:
                # Count non-empty fields
                non_empty_count = 0
                total_fields = 0
                
                extracted_data = data.get("extracted_data", {})
                for section, section_data in extracted_data.get("extracted_data", {}).items():
                    if isinstance(section_data, dict):
                        for field, value in section_data.items():
                            total_fields += 1
                            if value and value != [] and value != {}:
                                non_empty_count += 1
                    elif isinstance(section_data, list):
                        total_fields += 1
                        if section_data:
                            non_empty_count += 1
                
                # Display completeness metric first
                st.metric("Data Extraction Completeness", f"{non_empty_count}/{total_fields} fields", 
                        f"{(non_empty_count/total_fields)*100:.1f}% complete")
                
                # Format the JSON for better display in an expander
                with st.expander("Show Extracted Data JSON"):
                    st.json(extracted_data)



# After the Government & Law section, add a new section for Business & Corporate
st.markdown("---")
st.header("Business & Corporate Document Analysis")
st.markdown("""
### Impact of Document Noise on Extraction Quality

This section compares how the same prompt performs on two versions of business documents:
1. **Clean Text**: Plain text document with minimal formatting
2. **With Noise**: HTML document with advertisements, navigation elements, and other noise
""")

# Get the Business & Corporate data
business_data = category_data.get("Business & Corporate", {})

# Display metrics comparison for Business & Corporate
if business_data and len(business_data) > 1:  # Make sure we have both clean and noisy versions
    st.subheader("Metrics Comparison")
    
    # Calculate data extraction completeness for each version
    completeness_data = {}
    
    for version in ["clean", "with_noise"]:
        data = business_data.get(version)
        if data:
            non_empty_count = 0
            total_fields = 0
            
            extracted_data = data.get("extracted_data", {}).get("extracted_data", {})
            for section, section_data in extracted_data.items():
                if isinstance(section_data, dict):
                    for field, value in section_data.items():
                        total_fields += 1
                        if value and value != [] and value != {}:
                            non_empty_count += 1
                elif isinstance(section_data, list):
                    total_fields += 1
                    if section_data:
                        non_empty_count += 1
            
            completeness_data[version] = {
                "non_empty": non_empty_count,
                "total": total_fields,
                "percentage": (non_empty_count/total_fields)*100 if total_fields > 0 else 0
            }
    
    # Create a DataFrame for comparison
    metrics_df = pd.DataFrame({
        "Metric": ["Execution Time (s)", "Cost ($)", "Total Tokens", "Data Completeness"],
        "Clean Text": [
            business_data.get("clean", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            business_data.get("clean", {}).get("metrics", {}).get("total", {}).get("cost", 0),
            business_data.get("clean", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            f"{completeness_data.get('clean', {}).get('non_empty', 0)}/{completeness_data.get('clean', {}).get('total', 0)} ({completeness_data.get('clean', {}).get('percentage', 0):.1f}%)"
        ],
        "With Noise": [
            business_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            business_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("cost", 0),
            business_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            f"{completeness_data.get('with_noise', {}).get('non_empty', 0)}/{completeness_data.get('with_noise', {}).get('total', 0)} ({completeness_data.get('with_noise', {}).get('percentage', 0):.1f}%)"
        ]
    })
    
    st.table(metrics_df.set_index("Metric"))
    
    # Create smaller charts and place them side by side
    col1, col2 = st.columns(2)

    with col1:
        # Create a bar chart for token usage comparison
        fig, ax = plt.subplots(figsize=(5, 3))
        token_data = [
            business_data.get("clean", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            business_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0)
        ]
        
        ax.bar(["Clean", "With Noise"], token_data, color=['#66b3ff', '#ff9999'])
        ax.set_ylabel('Total Tokens')
        ax.set_title('Token Usage Comparison')
        plt.tight_layout()
        
        st.pyplot(fig)

    with col2:
        # Create a bar chart for execution time comparison
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        time_data = [
            business_data.get("clean", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            business_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("execution_time", 0)
        ]
        
        ax2.bar(["Clean", "With Noise"], time_data, color=['#66b3ff', '#ff9999'])
        ax2.set_ylabel('Time (s)')
        ax2.set_title('Execution Time Comparison')
        plt.tight_layout()
        
        st.pyplot(fig2)

    # Create a bar chart for data completeness comparison
    fig3, ax3 = plt.subplots(figsize=(3, 2))
    completeness_percentages = [
        completeness_data.get('clean', {}).get('percentage', 0),
        completeness_data.get('with_noise', {}).get('percentage', 0)
    ]

    bars = ax3.bar(["Clean", "With Noise"], completeness_percentages, color=['#66b3ff', '#ff9999'])
    ax3.set_ylabel('Completeness (%)', fontsize=8)
    ax3.set_title('Data Extraction Completeness', fontsize=9)
    ax3.set_ylim(0, 100)
    ax3.tick_params(axis='x', labelsize=7)
    ax3.tick_params(axis='y', labelsize=7)

    # Add percentage labels on top of the bars
    for i, v in enumerate(completeness_percentages):
        ax3.text(i, v + 2, f"{v:.1f}%", ha='center', fontsize=7)

    plt.tight_layout()

    # Use columns to make the chart smaller in the UI
    col1, col2 = st.columns([1, 1])
    with col1:
        st.pyplot(fig3)
    # Display extracted data comparison
    st.subheader("Extracted Data Comparison")
    
    # Create tabs for each version
    business_tabs = st.tabs(["Clean Text", "With Noise"])
    
    # Display extracted data for each version
    for tab_name, tab in zip(["clean", "with_noise"], business_tabs):
        with tab:
            data = business_data.get(tab_name)
            if data:
                # Count non-empty fields
                non_empty_count = 0
                total_fields = 0
                
                extracted_data = data.get("extracted_data", {})
                for section, section_data in extracted_data.get("extracted_data", {}).items():
                    if isinstance(section_data, dict):
                        for field, value in section_data.items():
                            total_fields += 1
                            if value and value != [] and value != {}:
                                non_empty_count += 1
                    elif isinstance(section_data, list):
                        total_fields += 1
                        if section_data:
                            non_empty_count += 1
                
                # Display completeness metric first
                st.metric("Data Extraction Completeness", f"{non_empty_count}/{total_fields} fields", 
                        f"{(non_empty_count/total_fields)*100:.1f}% complete")
                
                # Format the JSON for better display in an expander
                with st.expander("Show Extracted Data JSON"):
                    st.json(extracted_data)

# After the Business & Corporate section, add a new section for Healthcare & Medical 2
st.markdown("---")
st.header("Healthcare & Medical 2 Document Analysis")
st.markdown("""
### Impact of Document Noise on Extraction Quality

This section compares how the same prompt performs on two versions of healthcare documents:
1. **Clean Text**: Plain text document with minimal formatting
2. **With Noise**: Document with advertisements, formatting, and other noise elements
""")

# Get the Healthcare & Medical 2 data
medical2_data = category_data.get("Healthcare & Medical 2", {})

# Display metrics comparison for Healthcare & Medical 2
if medical2_data and len(medical2_data) > 1:  # Make sure we have both clean and noisy versions
    st.subheader("Metrics Comparison")
    
    # Calculate data extraction completeness for each version
    completeness_data = {}
    
    for version in ["clean", "with_noise"]:
        data = medical2_data.get(version)
        if data:
            non_empty_count = 0
            total_fields = 0
            
            extracted_data = data.get("extracted_data", {}).get("extracted_data", {})
            for section, section_data in extracted_data.items():
                if isinstance(section_data, dict):
                    for field, value in section_data.items():
                        total_fields += 1
                        if value and value != [] and value != {}:
                            non_empty_count += 1
                elif isinstance(section_data, list):
                    total_fields += 1
                    if section_data:
                        non_empty_count += 1
            
            completeness_data[version] = {
                "non_empty": non_empty_count,
                "total": total_fields,
                "percentage": (non_empty_count/total_fields)*100 if total_fields > 0 else 0
            }
    
    # Create a DataFrame for comparison
    metrics_df = pd.DataFrame({
        "Metric": ["Execution Time (s)", "Cost ($)", "Total Tokens", "Data Completeness"],
        "Clean Text": [
            medical2_data.get("clean", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            medical2_data.get("clean", {}).get("metrics", {}).get("total", {}).get("cost", 0),
            medical2_data.get("clean", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            f"{completeness_data.get('clean', {}).get('non_empty', 0)}/{completeness_data.get('clean', {}).get('total', 0)} ({completeness_data.get('clean', {}).get('percentage', 0):.1f}%)"
        ],
        "With Noise": [
            medical2_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            medical2_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("cost", 0),
            medical2_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            f"{completeness_data.get('with_noise', {}).get('non_empty', 0)}/{completeness_data.get('with_noise', {}).get('total', 0)} ({completeness_data.get('with_noise', {}).get('percentage', 0):.1f}%)"
        ]
    })
    
    st.table(metrics_df.set_index("Metric"))
    
    # Create smaller charts and place them side by side
    col1, col2 = st.columns(2)

    with col1:
        # Create a bar chart for token usage comparison
        fig, ax = plt.subplots(figsize=(5, 3))
        token_data = [
            business_data.get("clean", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            business_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0)
        ]
        
        ax.bar(["Clean", "With Noise"], token_data, color=['#66b3ff', '#ff9999'])
        ax.set_ylabel('Total Tokens')
        ax.set_title('Token Usage Comparison')
        plt.tight_layout()
        
        st.pyplot(fig)

    with col2:
        # Create a bar chart for execution time comparison
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        time_data = [
            business_data.get("clean", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            business_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("execution_time", 0)
        ]
        
        ax2.bar(["Clean", "With Noise"], time_data, color=['#66b3ff', '#ff9999'])
        ax2.set_ylabel('Time (s)')
        ax2.set_title('Execution Time Comparison')
        plt.tight_layout()
        
        st.pyplot(fig2)

    # Create a bar chart for data completeness comparison
    fig3, ax3 = plt.subplots(figsize=(3, 2))
    completeness_percentages = [
        completeness_data.get('clean', {}).get('percentage', 0),
        completeness_data.get('with_noise', {}).get('percentage', 0)
    ]

    bars = ax3.bar(["Clean", "With Noise"], completeness_percentages, color=['#66b3ff', '#ff9999'])
    ax3.set_ylabel('Completeness (%)', fontsize=8)
    ax3.set_title('Data Extraction Completeness', fontsize=9)
    ax3.set_ylim(0, 100)
    ax3.tick_params(axis='x', labelsize=7)
    ax3.tick_params(axis='y', labelsize=7)

    # Add percentage labels on top of the bars
    for i, v in enumerate(completeness_percentages):
        ax3.text(i, v + 2, f"{v:.1f}%", ha='center', fontsize=7)

    plt.tight_layout()

    # Use columns to make the chart smaller in the UI
    col1, col2 = st.columns([1, 1])
    with col1:
        st.pyplot(fig3)
    
    # Display extracted data comparison
    st.subheader("Extracted Data Comparison")
    
    # Create tabs for each version
    medical2_tabs = st.tabs(["Clean Text", "With Noise"])
    
    # Display extracted data for each version
    for tab_name, tab in zip(["clean", "with_noise"], medical2_tabs):
        with tab:
            data = medical2_data.get(tab_name)
            if data:
                # Count non-empty fields
                non_empty_count = 0
                total_fields = 0
                
                extracted_data = data.get("extracted_data", {})
                for section, section_data in extracted_data.get("extracted_data", {}).items():
                    if isinstance(section_data, dict):
                        for field, value in section_data.items():
                            total_fields += 1
                            if value and value != [] and value != {}:
                                non_empty_count += 1
                    elif isinstance(section_data, list):
                        total_fields += 1
                        if section_data:
                            non_empty_count += 1
                
                # Display completeness metric first
                st.metric("Data Extraction Completeness", f"{non_empty_count}/{total_fields} fields", 
                        f"{(non_empty_count/total_fields)*100:.1f}% complete")
                
                # Format the JSON for better display in an expander
                with st.expander("Show Extracted Data JSON"):
                    st.json(extracted_data)


# After the Healthcare & Medical 2 section, add a new section for Scientific Research
st.markdown("---")
st.header("Scientific Research Document Analysis")
st.markdown("""
### Impact of Document Noise on Extraction Quality

This section compares how the same prompt performs on two versions of scientific research documents:
1. **Clean Text**: Plain text document with minimal formatting
2. **With Noise**: HTML document with advertisements, navigation elements, and other noise
""")

# Get the Scientific Research data
research_data = category_data.get("Scientific Research", {})

# Display metrics comparison for Scientific Research
if research_data and len(research_data) > 1:  # Make sure we have both clean and noisy versions
    st.subheader("Metrics Comparison")
    
    # Calculate data extraction completeness for each version
    completeness_data = {}
    
    for version in ["clean", "with_noise"]:
        data = research_data.get(version)
        if data:
            non_empty_count = 0
            total_fields = 0
            
            extracted_data = data.get("extracted_data", {}).get("extracted_data", {})
            for section, section_data in extracted_data.items():
                if isinstance(section_data, dict):
                    for field, value in section_data.items():
                        total_fields += 1
                        if value and value != [] and value != {}:
                            non_empty_count += 1
                elif isinstance(section_data, list):
                    total_fields += 1
                    if section_data:
                        non_empty_count += 1
            
            completeness_data[version] = {
                "non_empty": non_empty_count,
                "total": total_fields,
                "percentage": (non_empty_count/total_fields)*100 if total_fields > 0 else 0
            }
    
    # Create a DataFrame for comparison
    metrics_df = pd.DataFrame({
        "Metric": ["Execution Time (s)", "Cost ($)", "Total Tokens", "Data Completeness"],
        "Clean Text": [
            research_data.get("clean", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            research_data.get("clean", {}).get("metrics", {}).get("total", {}).get("cost", 0),
            research_data.get("clean", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            f"{completeness_data.get('clean', {}).get('non_empty', 0)}/{completeness_data.get('clean', {}).get('total', 0)} ({completeness_data.get('clean', {}).get('percentage', 0):.1f}%)"
        ],
        "With Noise": [
            research_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            research_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("cost", 0),
            research_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            f"{completeness_data.get('with_noise', {}).get('non_empty', 0)}/{completeness_data.get('with_noise', {}).get('total', 0)} ({completeness_data.get('with_noise', {}).get('percentage', 0):.1f}%)"
        ]
    })
    
    st.table(metrics_df.set_index("Metric"))
    
    # Create smaller charts and place them side by side
    col1, col2 = st.columns(2)
    
    with col1:
        # Create a bar chart for token usage comparison
        fig, ax = plt.subplots(figsize=(5, 3))
        token_data = [
            research_data.get("clean", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0),
            research_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("total_tokens", 0)
        ]
        
        ax.bar(["Clean", "With Noise"], token_data, color=['#66b3ff', '#ff9999'])
        ax.set_ylabel('Total Tokens')
        ax.set_title('Token Usage Comparison')
        plt.tight_layout()
        
        st.pyplot(fig)
    
    with col2:
        # Create a bar chart for execution time comparison
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        time_data = [
            research_data.get("clean", {}).get("metrics", {}).get("total", {}).get("execution_time", 0),
            research_data.get("with_noise", {}).get("metrics", {}).get("total", {}).get("execution_time", 0)
        ]
        
        ax2.bar(["Clean", "With Noise"], time_data, color=['#66b3ff', '#ff9999'])
        ax2.set_ylabel('Time (s)')
        ax2.set_title('Execution Time Comparison')
        plt.tight_layout()
        
        st.pyplot(fig2)
    
    # Create a bar chart for data completeness comparison
    fig3, ax3 = plt.subplots(figsize=(3, 2))
    completeness_percentages = [
        completeness_data.get('clean', {}).get('percentage', 0),
        completeness_data.get('with_noise', {}).get('percentage', 0)
    ]

    bars = ax3.bar(["Clean", "With Noise"], completeness_percentages, color=['#66b3ff', '#ff9999'])
    ax3.set_ylabel('Completeness (%)', fontsize=8)
    ax3.set_title('Data Extraction Completeness', fontsize=9)
    ax3.set_ylim(0, 100)
    ax3.tick_params(axis='x', labelsize=7)
    ax3.tick_params(axis='y', labelsize=7)

    # Add percentage labels on top of the bars
    for i, v in enumerate(completeness_percentages):
        ax3.text(i, v + 2, f"{v:.1f}%", ha='center', fontsize=7)

    plt.tight_layout()

    # Use columns to make the chart smaller in the UI
    col1, col2 = st.columns([1, 1])
    with col1:
        st.pyplot(fig3)
    
    # Display extracted data comparison
    st.subheader("Extracted Data Comparison")
    
    # Create tabs for each version
    research_tabs = st.tabs(["Clean Text", "With Noise"])
    
    # Display extracted data for each version
    for tab_name, tab in zip(["clean", "with_noise"], research_tabs):
        with tab:
            data = research_data.get(tab_name)
            if data:
                # Count non-empty fields
                non_empty_count = 0
                total_fields = 0
                
                extracted_data = data.get("extracted_data", {})
                for section, section_data in extracted_data.get("extracted_data", {}).items():
                    if isinstance(section_data, dict):
                        for field, value in section_data.items():
                            total_fields += 1
                            if value and value != [] and value != {}:
                                non_empty_count += 1
                    elif isinstance(section_data, list):
                        total_fields += 1
                        if section_data:
                            non_empty_count += 1
                
                # Display completeness metric first
                st.metric("Data Extraction Completeness", f"{non_empty_count}/{total_fields} fields", 
                         f"{(non_empty_count/total_fields)*100:.1f}% complete")
                
                # Format the JSON for better display in an expander
                with st.expander("Show Extracted Data JSON"):
                    st.json(extracted_data)


# Summary section
st.markdown("---")
st.header("Overall Analysis Summary")

# Create comparison chart for all categories
if all_metrics:
    # Prepare data for token usage comparison
    categories = []
    token_values = []
    
    # Create short category names for better display
    category_mapping = {
        "Government & Law": "Gov & Law",
        "Business & Corporate": "Business",
        "Healthcare & Medical": "Healthcare",
        "Healthcare & Medical 2": "Healthcare 2",
        "Scientific Research": "Research"
    }
    
    for category, metrics_dict in all_metrics.items():
        if "clean" in metrics_dict:
            # Use short names for categories
            short_name = category_mapping.get(category, category)
            categories.append(short_name)
            token_values.append(metrics_dict["clean"]["total_tokens"])
    
    # Create a smaller bar chart
    fig, ax = plt.subplots(figsize=(4, 2.5))
    bars = ax.bar(categories, token_values, width=0.6)
    
    # Customize appearance for small size
    ax.set_ylabel('Tokens', fontsize=8)
    ax.set_title('Token Usage by Category', fontsize=9)
    ax.tick_params(axis='x', labelsize=7, rotation=45)
    ax.tick_params(axis='y', labelsize=7)
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=6)
    
    # Adjust layout to make it compact
    plt.tight_layout()
    
    # Use a column to make the chart smaller in the UI
    col1, col2 = st.columns([1, 1])
    with col1:
        st.pyplot(fig)

# Add conclusions
st.markdown("""
### Key Findings:

1. **Noise Impact**: Documents with HTML markup, advertising, and other noise elements require more tokens to process, but can result in less complete data extraction. The more noise, the worse the quality of the knots. For example, in the Healthcare & Medical 2 Document file, there is less noise than in others and prompt copes well with denoising.

2. **Extraction Quality**: The prompt performs best on clean, well-structured text documents across all categories.

3. **Category Differences**: Different document categories have varying levels of extraction completeness based on the prompt's design,  but it also depends very much on the context of the document itself .
""")

st.markdown("---")

# File examples section
st.header("File Examples")

# Function to load file content
@st.cache_data
def load_file_content(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error loading file: {str(e)}"

# List of files to display
file_samples = [
    {"name": "Government & Law (Clean)", "path": "samples/real_file/government_and_law_real.txt"},
    {"name": "Government & Law (With Noise)", "path": "samples/real_file/government_and_law_with_noise.txt"},
    {"name": "Government & Law (Original HTML)", "path": "samples/real_file/government_and_law.html"},
    {"name": "Business & Corporate (Clean)", "path": "samples/real_file/business_real.txt"},
    {"name": "Business & Corporate (With Noise)", "path": "samples/real_file/business_with_noise.txt"},
    {"name": "Healthcare & Medical 2 (Clean)", "path": "samples/real_file/medical_real_2.txt"},
    {"name": "Healthcare & Medical 2 (With Noise)", "path": "samples/real_file/medical_2_with_noise.txt"},
    {"name": "Scientific Research (Clean)", "path": "samples/real_file/research_real.txt"},
    {"name": "Scientific Research (With Noise)", "path": "samples/real_file/research_with_noise.txt"}
]

# Create tabs for each file
file_tabs = st.tabs([file_info["name"] for file_info in file_samples])

# Display content of each file
for i, (file_info, file_tab) in enumerate(zip(file_samples, file_tabs)):
    with file_tab:
        st.subheader(file_info["name"])
        file_content = load_file_content(file_info["path"])
        st.text_area("Raw Document", file_content[:15000] + ("..." if len(file_content) > 15000 else ""), height=400)

st.caption("Single Prompt Analysis Dashboard")