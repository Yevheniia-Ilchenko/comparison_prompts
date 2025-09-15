import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import os
from typing import Dict, Any

st.set_page_config(
    page_title="File Category Comparison",
    page_icon="📊",
    layout="wide"
)

st.title("File Category Comparison")
st.markdown("""
This dashboard visualizes the comparison of different prompting approaches across various document categories.

**Original Approach**: Processes the document using multiple prompts sequentially (legacy approach). First identifies the category, then extracts entities based on that category.

**Combined Approach**: Processes the entire document using a single comprehensive prompt, maintaining full context and extracting entities in one go.

The comparison shows metrics like execution time, cost, and token usage across different document categories.
""")

# Define available category files
category_files = {
    "Business & Corporate": "results/business_and_corporate_.json",
    "Healthcare & Medical": "results/healthcare_medical.json",
    "IT & Software": "results/it_software.json",
    "Legal & Government": "results/legal_government.json",
    "Scientific Research": "results/scientific_research.json"
}

# Create data structures to store aggregated information from all categories
all_original_metrics = {}
all_combined_metrics = {}

# Load the category data
@st.cache_data
def load_category_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        st.error(f"Error loading category data: {str(e)}")
        return None

# Load all category data
category_data = {}
for category_name, file_path in category_files.items():
    data = load_category_data(file_path)
    if data:
        category_data[category_name] = data
        # Store metrics for summary
        all_original_metrics[category_name] = data["original_approach"]["total_metrics"]
        all_combined_metrics[category_name] = data["combined_approach"]["metrics"]

# Create tabs for each category
category_tabs = st.tabs(list(category_files.keys()))

# Display data for each category
for tab_name, tab in zip(category_files.keys(), category_tabs):
    with tab:
        # Load the data for this tab
        data = category_data.get(tab_name)
        
        # Only proceed if data was loaded successfully
        if data:
            st.subheader(f"Execution Metrics - {tab_name}")
            
            # Get metrics
            original_metrics = data["original_approach"]["total_metrics"]
            combined_metrics = data["combined_approach"]["metrics"]
            comparison = data["comparison"]
            
            # Display metrics in columns
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <small>
                <b>Time and Cost Comparison</b><br>
                Shows execution metrics for both approaches.
                </small>
                """, unsafe_allow_html=True)
                
                col1a, col1b = st.columns(2)
                
                with col1a:
                    st.metric("Original Approach Time (s)", 
                              f"{original_metrics.get('execution_time'):.2f}")
                    
                    st.metric("Original Approach Cost ($)", 
                              f"{original_metrics.get('cost'):.6f}")
                
                with col1b:
                    st.metric("Combined Approach Time (s)", 
                              f"{combined_metrics.get('execution_time'):.2f}",
                              f"{comparison.get('time_savings_percentage'):.1f}%")
                    
                    st.metric("Combined Approach Cost ($)", 
                              f"{combined_metrics.get('cost'):.6f}",
                              f"{comparison.get('cost_savings_percentage'):.1f}%")
            
            with col2:
                st.markdown("""
                <small>
                <b>Token Usage Comparison</b><br>
                Shows total tokens processed by each approach.
                </small>
                """, unsafe_allow_html=True)
                
                st.metric("Original Approach Tokens", 
                        f"{original_metrics['total_tokens']}")
                
                st.metric("Combined Approach Tokens", 
                        f"{combined_metrics['tokens']['total']}",
                        f"{comparison['token_difference']}")
            
            with col3:
                st.markdown("""
                <small>
                <b>Token Efficiency</b><br>
                Shows tokens difference between approaches.
                </small>
                """, unsafe_allow_html=True)
                
                # Create a simple chart to visualize token usage
                fig, ax = plt.subplots(figsize=(4, 3))
                labels = ['Original', 'Combined']
                values = [original_metrics['total_tokens'], combined_metrics['tokens']['total']]
                colors = ['#ff9999', '#66b3ff']
                
                ax.bar(labels, values, color=colors)
                ax.set_ylabel('Tokens')
                ax.set_title('Token Usage Comparison')
                
                st.pyplot(fig)
            
            # Display extracted data comparison
            st.subheader("Extracted Data Comparison")
            
            # Create columns for original and combined approaches
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("##### Original Approach Extracted Data")
                
                # Format the JSON for better display
                original_result = data["original_approach"]["knots_result"]
                try:
                    # Try to parse as JSON if it's a string
                    if isinstance(original_result, str):
                        original_json = json.loads(original_result)
                    else:
                        original_json = original_result
                    
                    # Display as JSON with syntax highlighting
                    st.json(original_json)
                except:
                    # Fall back to displaying as text if JSON parsing fails
                    st.text_area("Raw Result", original_result, height=400)
            
            with col2:
                st.markdown("##### Combined Approach Extracted Data")
                
                # Format the JSON for better display
                combined_result = data["combined_approach"]["result"]
                try:
                    # Clean up the result if it has markdown code blocks
                    if isinstance(combined_result, str):
                        combined_result = combined_result.replace("```json", "").replace("```", "").strip()
                        combined_json = json.loads(combined_result)
                    else:
                        combined_json = combined_result
                    
                    # Display as JSON with syntax highlighting
                    st.json(combined_json)
                except:
                    # Fall back to displaying as text if JSON parsing fails
                    st.text_area("Raw Result", combined_result, height=400)

# Summary section
st.markdown("---")
st.header("Overall Comparison Summary (All Categories)")

# Create comparison charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Performance Comparison Across All Categories")
    
    # Calculate average metrics across all categories
    avg_original_time = sum(m["execution_time"] for m in all_original_metrics.values()) / len(all_original_metrics)
    avg_combined_time = sum(m["execution_time"] for m in all_combined_metrics.values()) / len(all_combined_metrics)
    avg_original_cost = sum(m["cost"] for m in all_original_metrics.values()) / len(all_original_metrics)
    avg_combined_cost = sum(m["cost"] for m in all_combined_metrics.values()) / len(all_combined_metrics)
    avg_original_tokens = sum(m["total_tokens"] for m in all_original_metrics.values()) / len(all_original_metrics)
    avg_combined_tokens = sum(m["tokens"]["total"] for m in all_combined_metrics.values()) / len(all_combined_metrics)
    
    # Calculate percentage differences
    time_diff_pct = ((avg_original_time - avg_combined_time) / avg_original_time) * 100 if avg_original_time > 0 else 0
    cost_diff_pct = ((avg_original_cost - avg_combined_cost) / avg_original_cost) * 100 if avg_original_cost > 0 else 0
    tokens_diff_pct = ((avg_original_tokens - avg_combined_tokens) / avg_original_tokens) * 100 if avg_original_tokens > 0 else 0
    
    # Create DataFrame for comparison
    metrics_df = pd.DataFrame({
        "Metric": ["Execution Time (s)", "Cost ($)", "Total Tokens"],
        "Avg Original": [avg_original_time, avg_original_cost, avg_original_tokens],
        "Avg Combined": [avg_combined_time, avg_combined_cost, avg_combined_tokens],
        "Avg Difference %": [time_diff_pct, cost_diff_pct, tokens_diff_pct]
    })
    
    st.table(metrics_df.set_index("Metric"))
    
    # Create a bar chart for time and cost differences by category
    categories_display = list(category_data.keys())
    time_diffs = [category_data[cat]["comparison"]["time_savings_percentage"] for cat in categories_display]
    cost_diffs = [category_data[cat]["comparison"]["cost_savings_percentage"] for cat in categories_display]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(categories_display))
    width = 0.35
    
    ax.bar([i - width/2 for i in x], cost_diffs, width, label='Cost Difference %')
    ax.bar([i + width/2 for i in x], time_diffs, width, label='Time Difference %')
    
    ax.set_ylabel('Percentage (%)')
    ax.set_title('Cost and Time Differences by Category')
    ax.set_xticks(x)
    ax.set_xticklabels([cat.replace(" & ", "\n") for cat in categories_display], rotation=0)
    ax.legend()
    
    # Add a horizontal line at 0%
    ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
    
    # Add annotations for negative values
    for i, v in enumerate(cost_diffs):
        if v < 0:
            ax.text(i - width/2, v - 10, f"{v:.1f}%", ha='center', fontsize=8)
    
    for i, v in enumerate(time_diffs):
        if v < 0:
            ax.text(i + width/2, v - 10, f"{v:.1f}%", ha='center', fontsize=8)
    
    st.pyplot(fig)

with col2:
    st.subheader("Token Usage Comparison Across All Categories")
    
    # Create a DataFrame for token usage by category
    token_data = {
        "Category": categories_display,
        "Original": [all_original_metrics[cat]["total_tokens"] for cat in categories_display],
        "Combined": [all_combined_metrics[cat]["tokens"]["total"] for cat in categories_display]
    }
    
    token_df = pd.DataFrame(token_data)
    
    # Create a grouped bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(categories_display))
    width = 0.35
    
    ax.bar([i - width/2 for i in x], token_df["Original"], width, label='Original Approach')
    ax.bar([i + width/2 for i in x], token_df["Combined"], width, label='Combined Approach')
    
    ax.set_ylabel('Token Count')
    ax.set_title('Token Usage by Category')
    ax.set_xticks(x)
    ax.set_xticklabels([cat.replace(" & ", "\n") for cat in categories_display], rotation=0)
    ax.legend()
    
    st.pyplot(fig)
    
    # Calculate token savings
    token_df["Difference"] = token_df["Original"] - token_df["Combined"]
    token_df["Savings %"] = (token_df["Difference"] / token_df["Original"]) * 100
    
    # Display token savings table
    st.subheader("Token Savings by Category")
    display_df = token_df[["Category", "Original", "Combined", "Difference", "Savings %"]]
    display_df["Savings %"] = display_df["Savings %"].apply(lambda x: f"{x:.1f}%")
    st.table(display_df.set_index("Category"))

# Add conclusions
st.markdown("""
### Key Findings:

1. **Execution Cost**: The combined approach is more expensive.

2. **Execution Time**: Processing time also varies by category, combined approach show increased processing time in most situations.

3. **Token Usage**: The combined approach generally uses more tokens across most categories because the prompt itself is larger and more complex.

""")

st.markdown("---")

st.header("File Examples")

# List of files to load
file_samples = [
    {"name": "business_and_corporate", "path": "samples/business_and_corporate_test_doc.txt"},
    {"name": "healthcare_medical", "path": "samples/healthcare_medical_test_doc.txt"},
    {"name": "it_software", "path": "samples/it_test_doc.txt"},
    {"name": "scientific_research", "path": "samples/academic_test_doc.txt"},
    {"name": "legal_government", "path": "samples/legal_government_test_doc.txt"},

]

# Load files
loaded_files = {}
for file_info in file_samples:
    try:
        # First try to import from samples module
        module_name = file_info["path"].split("/")[-1].replace(".txt", "")
        try:
            module = __import__(f"samples.{module_name}", fromlist=[module_name])
            loaded_files[file_info["name"]] = getattr(module, module_name)
        except (ImportError, AttributeError):
            # If import fails, try to read the file directly
            try:
                with open(file_info["path"], "r", encoding="utf-8") as f:
                    loaded_files[file_info["name"]] = f.read()
            except:
                continue
    except Exception as e:
        st.warning(f"Failed to load file {file_info['name']}: {str(e)}")

if loaded_files:
    # Create tabs for each loaded file
    file_tabs = st.tabs(list(loaded_files.keys()))
    
    # Display content of each file
    for i, (file_name, file_tab) in enumerate(zip(loaded_files.keys(), file_tabs)):
        with file_tab:
            try:
                st.subheader(file_name)
                
                file_content = loaded_files[file_name]
                st.text_area("Raw Document (first 15000 characters)", file_content[:15000] + ("..." if len(file_content) > 5000 else ""), height=400)
                
            except Exception as e:
                st.error(f"Error displaying file {file_name}: {str(e)}")
else:
    st.warning("Could not load any files. Make sure the files exist in the samples/ directory.")

st.caption("File Category Comparison Dashboard")