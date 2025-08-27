import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import os
from samples.email import *

st.set_page_config(
    page_title="Email Analysis Comparison",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    with open("results/combined_prompts_comparison.json", "r", encoding="utf-8") as file:
        return json.load(file)

data = load_data()

st.title("Email Analysis Comparison: New vs. Optimized Prompts")
st.markdown("""This dashboard visualizes the differences between two different prompting approaches for email analysis:

1. **New Prompt**: A more concise approach that extracts entities and topics with basic descriptions
   
2. **Optimized Prompt**: An enhanced approach that provides more detailed topic descriptions and better structured entity relationships

The comparison highlights differences in accuracy, structure, efficiency, and cost between these approaches.""")

# Metrics comparison section
st.header("Performance Metrics Comparison for different email categories")

# Create tabs for different email categories
tabs = st.tabs(["Corporate", "Organizational", "Marketing", "Conversation"])

# Process each email category
for i, (tab, category) in enumerate(zip(tabs, ["corporate", "organizational", "marketing", "conversation"])):
    with tab:
        col1, col2 = st.columns(2)
        
        # Metrics comparison
        with st.container():
            st.subheader("Execution Metrics")
            
            # Create metrics comparison dataframe
            metrics_new = data[category]["metrics_comparison"]["new_prompt"]
            metrics_opt = data[category]["metrics_comparison"]["optimized_prompt"]
            differences = data[category]["metrics_comparison"]["differences"]
            
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
                    st.metric("New Prompt Time (s)", 
                            f"{metrics_new.get('execution_time'):.2f}")
                    
                    st.metric("New Prompt Cost ($)", 
                            f"{metrics_new.get('cost'):.6f}")
                
                with col1b:
                    st.metric("Optimized Time (s)", 
                            f"{metrics_opt.get('execution_time'):.2f}",
                            f"{differences['time_difference_percentage']:.1f}%")
                    
                    st.metric("Optimized Cost ($)", 
                            f"{metrics_opt.get('cost'):.6f}",
                            f"{differences['cost_difference_percentage']:.1f}%")
            
            with col2:
                st.markdown("""
                <small>
                <b>Token Usage Comparison</b><br>
                Shows total tokens processed by each approach.
                </small>
                """, unsafe_allow_html=True)
                
                st.metric("New Prompt Tokens", 
                        f"{metrics_new['tokens']['total']}")
                
                st.metric("Optimized Prompt Tokens", 
                        f"{metrics_opt['tokens']['total']}")

            with col3:
                st.markdown("""
                <small>
                <b>Token Efficiency</b><br>
                Shows tokens difference between approaches.
                </small>
                """, unsafe_allow_html=True)
                
                st.metric("Token Difference", 
                        f"{differences['total_tokens_difference']}")
        
        # Horizontal line
        st.markdown("---")
        
        # Topics comparison
        st.subheader("Topic Analysis Comparison")
        
        # Extract topics for both approaches
        new_prompt_results = json.loads(data[category]["raw_results"]["new_prompt"].replace("```json\n", "").replace("\n```", ""))
        optimized_prompt_results = json.loads(data[category]["raw_results"]["optimized_prompt"].replace("```json\n", "").replace("\n```", ""))
        
        new_topics = new_prompt_results.get("topics", [])
        optimized_topics = optimized_prompt_results.get("topics", [])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### New Prompt Topics")
            for topic in new_topics:
                with st.expander(f"{topic.get('topic_name')} (Score: {topic.get('relevance_score', 'N/A')})"):
                    st.write(topic.get('topic_description'))
        
        with col2:
            st.markdown("##### Optimized Prompt Topics")
            for topic in optimized_topics:
                with st.expander(f"{topic.get('topic_name')} (Score: {topic.get('relevance_score', 'N/A')})"):
                    st.write(topic.get('topic_description'))
        
        # Horizontal line
        st.markdown("---")
        
        # Keywords and Named Entities
        st.subheader("Keywords and Named Entities")
        
        # Extract knots comparison data
        knots_comparison = data[category]["knots_comparison"]
        
        # Create sets of entities for comparison
        new_entities = set(knots_comparison.get("common_knots", []) + knots_comparison.get("only_in_new", []))
        optimized_entities = set(knots_comparison.get("common_knots", []) + knots_comparison.get("only_in_optimized", []))
        
        # Create columns for entity lists
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### New Prompt Entities")
            st.write(f"Total: {knots_comparison['new_prompt_knots_count']}")
            st.write(", ".join(sorted(list(new_entities))))
        
        with col2:
            st.markdown("##### Optimized Prompt Entities")
            st.write(f"Total: {knots_comparison['optimized_prompt_knots_count']}")
            st.write(", ".join(sorted(list(optimized_entities))))
        
        # Create Venn diagram for entity overlap
        common_entities = set(knots_comparison.get("common_knots", []))
        only_new = set(knots_comparison.get("only_in_new", []))
        only_optimized = set(knots_comparison.get("only_in_optimized", []))
        
        st.markdown("##### Entity Overlap Analysis")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.write(f"Common entities: {knots_comparison['common_knots_count']}")
            st.write(f"Only in new: {knots_comparison['only_in_new_count']}")
            st.write(f"Only in optimized: {knots_comparison['only_in_optimized_count']}")
        
        with col2:
            # Create and display Venn diagram
            fig, ax = plt.subplots(figsize=(6, 4))
            venn = venn2(subsets=(len(only_new), len(only_optimized), len(common_entities)), 
                         set_labels=('New Prompt', 'Optimized Prompt'))
            plt.title("Entity Overlap Between Approaches")
            st.pyplot(fig)
        
        # Extract knots from raw results
        if "entities" in new_prompt_results:
            new_section_knots = new_prompt_results["entities"].get("knots_from_section", [])
        else:
            new_section_knots = []
            
        if "entities" in optimized_prompt_results:
            optimized_section_knots = optimized_prompt_results["entities"].get("knots_from_section", [])
            optimized_paragraph_knots = optimized_prompt_results["entities"].get("knots_from_paragraph", [])
        else:
            optimized_section_knots = []
            optimized_paragraph_knots = []
        
        # Knots from section comparison
        st.markdown("---")
        st.subheader("Knots from Section Comparison")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("##### New Prompt Section Knots")
            if new_section_knots:
                for i, knot_group in enumerate(new_section_knots):
                    with st.expander(f"Section {i+1} ({len(knot_group)} entities)"):
                        st.write(", ".join(knot_group))
            else:
                st.info("No section knots available in new prompt")

        with col2:
            st.markdown("##### Optimized Prompt Section Knots")
            if optimized_section_knots:
                for i, knot_group in enumerate(optimized_section_knots):
                    with st.expander(f"Section {i+1} ({len(knot_group)} entities)"):
                        st.write(", ".join(knot_group))
            else:
                st.info("No section knots available in optimized prompt")
                
        # Knots from paragraph comparison if available
        if optimized_paragraph_knots:
            st.markdown("---")
            st.subheader("Knots from Paragraph Comparison")
            
            col1, col2 = st.columns(2)
            
            with col2:
                st.markdown("##### Optimized Prompt Paragraph Knots")
                for i, knot_group in enumerate(optimized_paragraph_knots):
                    with st.expander(f"Paragraph {i+1} ({len(knot_group)} entities)"):
                        st.write(", ".join(knot_group))

# Add summary section at the bottom
st.markdown("---")
st.header("Overall Comparison Summary")

# Calculate average metrics across all categories
avg_cost_diff_percentage = data["summary"]["avg_cost_diff_percentage"]
avg_time_diff_percentage = data["summary"]["avg_time_diff_percentage"]
avg_new_knots = data["summary"]["avg_new_knots_count"]
avg_optimized_knots = data["summary"]["avg_optimized_knots_count"]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Performance Comparison")
    st.metric("Average Cost Difference", f"{avg_cost_diff_percentage:.1f}%")
    st.metric("Average Time Difference", f"{avg_time_diff_percentage:.1f}%")
    
    # Create a bar chart for time and cost differences
    categories = ["Corporate", "Organizational", "Marketing", "Conversation"]
    time_diffs = [data[cat.lower()]["metrics_comparison"]["differences"]["time_difference_percentage"] for cat in categories]
    cost_diffs = [data[cat.lower()]["metrics_comparison"]["differences"]["cost_difference_percentage"] for cat in categories]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(categories))
    width = 0.35
    
    ax.bar([i - width/2 for i in x], cost_diffs, width, label='Cost Difference %')
    ax.bar([i + width/2 for i in x], time_diffs, width, label='Time Difference %')
    
    ax.set_ylabel('Percentage (%)')
    ax.set_title('Cost and Time Differences by Email Category')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    
    st.pyplot(fig)

with col2:
    st.subheader("Analysis Quality Comparison")
    
    # Compare the number of topics and entities identified
    topic_counts = {
        "New": [len(json.loads(data[cat]["raw_results"]["new_prompt"].replace("```json\n", "").replace("\n```", "")).get("topics", [])) for cat in ["corporate", "organizational", "marketing", "conversation"]],
        "Optimized": [len(json.loads(data[cat]["raw_results"]["optimized_prompt"].replace("```json\n", "").replace("\n```", "")).get("topics", [])) for cat in ["corporate", "organizational", "marketing", "conversation"]]
    }
    
    entity_counts = {
        "New": [data[cat]["knots_comparison"]["new_prompt_knots_count"] for cat in ["corporate", "organizational", "marketing", "conversation"]],
        "Optimized": [data[cat]["knots_comparison"]["optimized_prompt_knots_count"] for cat in ["corporate", "organizational", "marketing", "conversation"]]
    }
    
    # Create DataFrames for the counts
    topic_df = pd.DataFrame(topic_counts, index=["Corporate", "Organizational", "Marketing", "Conversation"])
    entity_df = pd.DataFrame(entity_counts, index=["Corporate", "Organizational", "Marketing", "Conversation"])
    
    # Plot the counts
    st.write("Number of Topics Identified:")
    st.bar_chart(topic_df)
    
    st.write("Number of Entities Identified:")
    st.bar_chart(entity_df)
    
    # Add conclusions
    st.markdown("""
    ### Key Findings:
    
    1. **Execution Cost**: The optimized approach shows mixed cost results - it's cheaper for corporate and conversation emails, but more expensive for organizational and marketing emails. On average, there's a cost savings of about 1.4%.

    2. **Execution Time**: Processing time also varies by category. On average, the optimized approach is 9% slower.

    3. **Topic Quality**: The optimized approach provides more detailed and contextual topic descriptions, while the new approach uses more concise formulations.
""")

st.markdown("---")
st.caption("Email Analysis Comparison Dashboard")


email_tabs = st.tabs(["Corporate Email", "Organizational Email", "Marketing Email", "Conversation Email"])

email_samples = {
    "Corporate Email": test_email_1_html,
    "Organizational Email": test_email_2_html if 'test_email_2_html' in locals() else "Sample not available",
    "Marketing Email": test_email_3_html if 'test_email_3_html' in locals() else "Sample not available",
    "Conversation Email": test_email_4_html if 'test_email_4_html' in locals() else "Sample not available"
}

def get_plain_text(html_content):
    import re
    
    html_content = re.sub(r'<style>.*?</style>', '', html_content, flags=re.DOTALL)
    
    html_content = re.sub(r'<head>.*?</head>', '', html_content, flags=re.DOTALL)
    
    html_content = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'\n\n\1\n', html_content)
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content)
    html_content = re.sub(r'<br[^>]*>', '\n', html_content)
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'\n• \1', html_content)
    html_content = re.sub(r'<ul[^>]*>|</ul>|<ol[^>]*>|</ol>', '\n', html_content)
    
    html_content = re.sub(r'<[^>]+>', '', html_content)
    
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&#39;', "'")
    
    html_content = re.sub(r'\n\s*\n', '\n\n', html_content)
    html_content = re.sub(r' +', ' ', html_content)
    
    lines = html_content.split('\n')
    lines = [line.strip() for line in lines]
    html_content = '\n'.join(lines)
    
    return html_content.strip()

for i, (tab_name, email_tab) in enumerate(zip(["Corporate Email", "Organizational Email", "Marketing Email", "Conversation Email"], email_tabs)):
    with email_tab:
        html_tab, text_tab = st.tabs(["HTML View", "Text View"])
        
        with html_tab:
            st.markdown("### HTML Version")
            st.components.v1.html(email_samples[tab_name], height=500, scrolling=True)
        
        with text_tab:
            st.markdown("### Text Version")
            if email_samples[tab_name] != "Sample not available":
                st.text_area("Email Content", get_plain_text(email_samples[tab_name]), height=400)
            else:
                st.info("Sample not available")