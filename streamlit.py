import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import os


st.set_page_config(
    page_title="Email Analysis Comparison",
    page_icon="📊",
    layout="wide"
)
@st.cache_data
def load_data():
    with open("results/all_emails_analysis_1755618712.json", "r", encoding="utf-8") as file:
        return json.load(file)

data = load_data()

st.title("Email Analysis Comparison: Separate vs. Combined Prompts")
st.markdown("""This dashboard visualizes the differences between two different prompting approaches for email analysis:

1. **Separate Execution**: A three-step process consisting of:
   - **Denoising**: Cleaning and normalizing the email text
   - **Knots Extraction**: Identifying keywords, named entities, and relationships from paragraphs and sections
   - **Topic Formation**: Creating structured topics with detailed descriptions

2. **Combined Execution**: A single-step process that attempts to perform all three tasks simultaneously.

The comparison highlights differences in accuracy, structure, efficiency, and cost between these approaches.""")

# Metrics comparison section
st.header("Performance Metrics Comparison for different email categories")

# Create tabs for different email categories
tabs = st.tabs(["Corporate", "Organizational", "Marketing", "Conversation"])

# Function to extract topics from JSON
def extract_topics(data_section, execution_type):
    if execution_type == "separate":
        # Parse the topics JSON string
        topics_str = data_section["separate_execution"]["topics"]
        # Remove the ```json and ``` markers
        topics_str = topics_str.replace("```json\n", "").replace("\n```", "")
        topics = json.loads(topics_str)
        return topics
    else:  # combined
        result_str = data_section["combined_execution"]["result"]
        result_str = result_str.replace("```json\n", "").replace("\n```", "")
        result = json.loads(result_str)
        return result["topics"]

# Function to extract knots from JSON
def extract_knots(data_section, execution_type):
    if execution_type == "separate":
        # Parse the knots JSON string
        knots_str = data_section["separate_execution"]["knots"]
        # Remove the ```json and ``` markers
        knots_str = knots_str.replace("```json\n", "").replace("\n```", "")
        knots = json.loads(knots_str)
        return knots
    else:  # combined
        result_str = data_section["combined_execution"]["result"]
        result_str = result_str.replace("```json\n", "").replace("\n```", "")
        result = json.loads(result_str)
        return result["entities"]

# Process each email category
for i, (tab, category) in enumerate(zip(tabs, ["corporate", "organizational", "marketing", "conversation"])):
    with tab:
        col1, col2 = st.columns(2)
        
        # Metrics comparison
        with st.container():
            st.subheader("Execution Metrics")
            
            # Create metrics comparison dataframe
            metrics_sep = data[category]["separate_execution"]["metrics"]
            metrics_comb = data[category]["combined_execution"]["metrics"]
            comparison = data[category]["comparison"]["separate_vs_combined"]
            
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
                    st.metric("Separate Time (s)", 
                            f"{metrics_sep.get('total_execution_time', metrics_sep['total_execution_time']):.2f}")
                    
                    st.metric("Separate Cost ($)", 
                            f"{metrics_sep.get('total_cost', metrics_sep['total_cost']):.6f}")
                
                with col1b:
                    st.metric("Combined Time (s)", 
                            f"{metrics_comb.get('execution_time', metrics_comb['execution_time']):.2f}",
                            f"-{comparison['time_savings_percentage']:.1f}%")
                    
                    st.metric("Combined Cost ($)", 
                            f"{metrics_comb.get('cost', metrics_comb['cost']):.6f}",
                            f"-{comparison['cost_savings_percentage']:.1f}%")
            
            with col2:
                st.markdown("""
                <small>
                <b>Token Usage Comparison</b><br>
                Shows total tokens processed by each approach.
                </small>
                """, unsafe_allow_html=True)
                
                st.metric("Separate Execution Tokens", 
                        f"{metrics_sep.get('total_input_tokens', metrics_sep['total_input_tokens']) + metrics_sep.get('total_output_tokens', metrics_sep['total_output_tokens'])}")
                
                st.metric("Combined Execution Tokens", 
                        f"{metrics_comb['tokens']['total']}")

            with col3:
                st.markdown("""
                <small>
                <b>Token Efficiency</b><br>
                Shows tokens saved with combined approach.
                </small>
                """, unsafe_allow_html=True)
                
                st.metric("Token Reduction", 
                        f"{comparison['input_tokens_difference'] + comparison['output_tokens_difference']}")
        
        # Horizontal line
        st.markdown("---")
        
        # Topics comparison
        st.subheader("Topic Analysis Comparison")
        
        # Extract topics for both approaches
        separate_topics = extract_topics(data[category], "separate")
        combined_topics = extract_topics(data[category], "combined")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Separate Execution Topics")
            for topic in separate_topics:
                with st.expander(f"{topic.get('topic_name')}"):
                    st.write(topic.get('topic_description'))
        
        with col2:
            st.markdown("##### Combined Execution Topics")
            for topic in combined_topics:
                with st.expander(f"{topic.get('topic_name')} (Score: {topic.get('relevance_score', 'N/A')})"):
                    st.write(topic.get('topic_description'))
        
        # Horizontal line
        st.markdown("---")
        
        # Keywords and Named Entities
        st.subheader("Keywords and Named Entities")
        
        # Extract knots for both approaches
        separate_knots = extract_knots(data[category], "separate")
        combined_knots = extract_knots(data[category], "combined")
        
        # Create sets of entities for comparison
        if separate_knots.get("keywords_named_entities"):
            separate_entities = set(separate_knots.get("keywords_named_entities", []))
        else:
            separate_entities = set()
            
        if combined_knots.get("knots_from_paragraph"):
            # Flatten the nested lists and create a set
            combined_entities = set()
            for entity_list in combined_knots.get("knots_from_paragraph", []):
                combined_entities.update(entity_list)
        else:
            combined_entities = set()
        
        # Create columns for entity lists
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Separate Execution Entities")
            st.write(f"Total: {len(separate_entities)}")
            st.write(", ".join(sorted(list(separate_entities))))
        
        with col2:
            st.markdown("##### Combined Execution Entities")
            st.write(f"Total: {len(combined_entities)}")
            st.write(", ".join(sorted(list(combined_entities))))
        
        # Create Venn diagram for entity overlap
        common_entities = separate_entities.intersection(combined_entities)
        only_separate = separate_entities - combined_entities
        only_combined = combined_entities - separate_entities
        
        st.markdown("##### Entity Overlap Analysis")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.write(f"Common entities: {len(common_entities)}")
            st.write(f"Only in separate: {len(only_separate)}")
            st.write(f"Only in combined: {len(only_combined)}")
        
        with col2:
            # Create and display Venn diagram
            fig, ax = plt.subplots(figsize=(6, 4))
            venn = venn2(subsets=(len(only_separate), len(only_combined), len(common_entities)), 
                         set_labels=('Separate Execution', 'Combined Execution'))
            plt.title("Entity Overlap Between Approaches")
            st.pyplot(fig)
        
        # Knots from paragraph comparison
        st.markdown("---")
        st.subheader("Knots from Paragraph Comparison")
        
        # Extract knots from paragraph for both approaches
        separate_paragraph_knots = separate_knots.get("knots_from_paragraph", [])
        combined_paragraph_knots = combined_knots.get("knots_from_paragraph", [])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Separate Execution Paragraph Knots")
            for i, knot_group in enumerate(separate_paragraph_knots):
                with st.expander(f"Paragraph {i+1} ({len(knot_group)} entities)"):
                    st.write(", ".join(knot_group))
        
        with col2:
            st.markdown("##### Combined Execution Paragraph Knots")
            for i, knot_group in enumerate(combined_paragraph_knots):
                with st.expander(f"Paragraph {i+1} ({len(knot_group)} entities)"):
                    st.write(", ".join(knot_group))
        
        # Knots from section comparison
        st.markdown("---")
        st.subheader("Knots from Section Comparison")

        # Extract knots from section for both approaches
        separate_section_knots = separate_knots.get("knots_from_section", [])

        # Check if combined execution has section knots (unlikely, but we should check)
        combined_section_knots = []
        if "knots_from_section" in combined_knots:
            combined_section_knots = combined_knots.get("knots_from_section", [])

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("##### Separate Execution Section Knots")
            if separate_section_knots:
                for i, knot_group in enumerate(separate_section_knots):
                    with st.expander(f"Section {i+1} ({len(knot_group)} entities)"):
                        st.write(", ".join(knot_group))
            else:
                st.info("No section knots available in separate execution")

        with col2:
            st.markdown("##### Combined Execution Section Knots")
            if combined_section_knots:
                for i, knot_group in enumerate(combined_section_knots):
                    with st.expander(f"Section {i+1} ({len(knot_group)} entities)"):
                        st.write(", ".join(knot_group))
            else:
                st.error("⚠️ Missing Feature: 'knots_from_section' structure is not available in combined execution")
                st.markdown("""
                The combined execution approach does not extract section-level knots, 
                which is a significant structural limitation compared to the separate execution approach.
                """)

# Add summary section at the bottom
st.markdown("---")
st.header("Overall Comparison Summary")

# Calculate average metrics across all categories
avg_time_savings = sum(data[cat]["comparison"]["separate_vs_combined"]["time_savings_percentage"] for cat in ["corporate", "organizational", "marketing", "conversation"]) / 4
avg_cost_savings = sum(data[cat]["comparison"]["separate_vs_combined"]["cost_savings_percentage"] for cat in ["corporate", "organizational", "marketing", "conversation"]) / 4

col1, col2 = st.columns(2)

with col1:
    st.subheader("Performance Comparison")
    st.metric("Average Time Savings", f"{avg_time_savings:.1f}%")
    st.metric("Average Cost Savings", f"{avg_cost_savings:.1f}%")
    
    # Create a bar chart for time and cost savings
    categories = ["Corporate", "Organizational", "Marketing", "Conversation"]
    time_savings = [data[cat.lower()]["comparison"]["separate_vs_combined"]["time_savings_percentage"] for cat in categories]
    cost_savings = [data[cat.lower()]["comparison"]["separate_vs_combined"]["cost_savings_percentage"] for cat in categories]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(categories))
    width = 0.35
    
    ax.bar([i - width/2 for i in x], time_savings, width, label='Time Savings %')
    ax.bar([i + width/2 for i in x], cost_savings, width, label='Cost Savings %')
    
    ax.set_ylabel('Percentage (%)')
    ax.set_title('Time and Cost Savings by Email Category')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    
    st.pyplot(fig)

with col2:
    st.subheader("Analysis Quality Comparison")
    
    # Compare the number of topics and entities identified
    topic_counts = {
        "Separate": [len(extract_topics(data[cat], "separate")) for cat in ["corporate", "organizational", "marketing", "conversation"]],
        "Combined": [len(extract_topics(data[cat], "combined")) for cat in ["corporate", "organizational", "marketing", "conversation"]]
    }
    
    # Create a DataFrame for the topic counts
    topic_df = pd.DataFrame(topic_counts, index=["Corporate", "Organizational", "Marketing", "Conversation"])
    
    # Plot the topic counts
    st.write("Number of Topics Identified:")
    st.bar_chart(topic_df)
    
    # Add conclusions
    st.markdown("""
    ### Key Findings:
    
    1. **Efficiency**: The combined execution approach shows significant time and cost savings across all email categories.
    
    2. **Topic Quality**: The separate execution provides more structured topics with detailed descriptions, while combined execution uses hashtag-style naming (#topic‑name) with relevance scores but often misses expected topic names.
    
    3. **Entity Recognition**: The separate execution provides better structured entity recognition, while the combined approach:
       - Incorrectly includes URLs and dates as entities
       - Is missing key structures like `keywords_named_entities` and `knots_from_section`
       - Doesn't form the expected structure for knowledge extraction""")

st.markdown("---")
st.caption("Email Analysis Comparison Dashboard")