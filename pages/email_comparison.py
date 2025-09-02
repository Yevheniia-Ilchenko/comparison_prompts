import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import os
from samples.email import *

def extract_knots_from_section(raw_json):
    """Спеціальна функція для витягування knots_from_section навіть з неповного JSON"""
    try:
        # Спочатку спробуємо стандартний підхід через JSON
        cleaned_json = raw_json.replace("```json\n", "").replace("\n```", "").strip()
        data = json.loads(cleaned_json)
        if "entities" in data and "knots_from_section" in data["entities"]:
            return data["entities"]["knots_from_section"]
    except:
        pass
    
    # Якщо JSON не парситься, використовуємо регулярний вираз з додатковою обробкою
    try:
        import re
        # Шукаємо початок секції knots_from_section
        section_pattern = r'"knots_from_section":\s*\['
        match = re.search(section_pattern, raw_json)
        
        if not match:
            return []
        
        # Знаходимо початкову позицію
        start_pos = match.end()
        content = raw_json[start_pos:]
        
        # Розбиваємо на рядки і шукаємо групи
        section_knots = []
        current_group = []
        bracket_level = 0
        
        for line in content.split('\n'):
            line = line.strip()
            
            # Рахуємо рівень вкладеності дужок
            if '[' in line:
                bracket_level += 1
                if bracket_level == 1:  # Початок нової групи
                    current_group = []
            
            # Знаходимо елементи в лапках
            if '"' in line and ',' in line:
                item = line.strip().strip(',').strip('"')
                if item and bracket_level >= 1:
                    current_group.append(item)
            
            # Закінчення групи
            if ']' in line:
                bracket_level -= 1
                if bracket_level == 0 and current_group:  # Закінчення групи верхнього рівня
                    section_knots.append(current_group.copy())
                    current_group = []
            
            # Якщо знайшли закриваючу дужку для всього масиву або кінець файлу
            if bracket_level < 0 or '}' in line or '"topics":' in line:
                break
        
        # Додаємо останню групу, якщо вона не порожня
        if current_group and bracket_level >= 0:
            section_knots.append(current_group)
        
        return section_knots
    except Exception as e:
        print(f"Error extracting knots: {str(e)}")
        return []

def has_excessive_duplicates(entities_list):
    """Check if there are excessive duplicate entities in the list, indicating extraction issues"""
    if not entities_list or len(entities_list) == 0:
        return False
    
    # Flatten the nested lists if needed
    all_entities = []
    for group in entities_list:
        all_entities.extend(group)
    
    # Count occurrences of each entity
    from collections import Counter
    entity_counts = Counter(all_entities)
    
    # Count total duplicates
    total_entities = len(all_entities)
    unique_entities = len(set(all_entities))
    duplicate_count = total_entities - unique_entities
    duplicate_percentage = 1 - (unique_entities / total_entities) if total_entities > 0 else 0
    
    # Return true if there are significant duplicates (more than 10 and more than 20%)
    return duplicate_count > 10 and duplicate_percentage > 0.2

st.set_page_config(
    page_title="Email Analysis Comparison",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    with open("results/real_email_combined_prompts_v9.json", "r", encoding="utf-8") as file:
        return json.load(file)

data = load_data()

st.title("Email Analysis Comparison: New vs. Optimized Prompts")
st.markdown("""This dashboard visualizes the differences between two different prompting approaches for email analysis:

1. **New Prompt**: A more concise approach that extracts entities and topics with basic descriptions

2. **Optimized Prompt**: An enhanced approach that provides more detailed topic descriptions and better structured entity relationships

The comparison highlights differences in accuracy, structure, efficiency, and cost between these approaches.""")

# Metrics comparison section
st.header("Performance Metrics Comparison for different email categories")

available_categories = list(data.keys())
available_categories = [cat for cat in available_categories if cat != "summary"]
tab_names = [cat.replace("_", " ").title() for cat in available_categories]

tabs = st.tabs(tab_names)

# Process each email category
for i, (tab, category) in enumerate(zip(tabs, available_categories)):
    with tab:
        col1, col2 = st.columns(2)
        
        # Metrics comparison
        with st.container():
            st.subheader("Execution Metrics")
            
            # Create metrics comparison dataframe
            metrics_new = data[category]["metrics_comparison"]["new_prompt"]
            metrics_opt = data[category]["metrics_comparison"]["optimized_prompt"]
            differences = data[category]["metrics_comparison"]["differences"]

            try:
                # Use our special function to extract data
                new_section_knots = extract_knots_from_section(data[category]["raw_results"]["new_prompt"])
                
                # Calculate total and unique entities
                all_entities = []
                for group in new_section_knots:
                    all_entities.extend(group)
                
                total_raw_entities = len(all_entities)
                unique_raw_entities = len(set(all_entities))
                duplicate_count = total_raw_entities - unique_raw_entities
                duplicate_percentage = 1 - (unique_raw_entities / total_raw_entities) if total_raw_entities > 0 else 0

                has_duplicate_issue = (
                                    (total_raw_entities > 1000) or 
                                    (duplicate_count > 10 and duplicate_percentage > 0.2))            
            except Exception as e:
                print(f"Error processing section knots: {str(e)}")
                new_section_knots = []
                total_raw_entities = 0
                unique_raw_entities = 0
                has_duplicate_issue = False
            
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
        # Extract topics for both approaches
        try:
            new_prompt_json = data[category]["raw_results"]["new_prompt"].replace("```json\n", "").replace("\n```", "")
            # Additional processing to remove potentially problematic characters
            new_prompt_json = new_prompt_json.strip()
            try:
                new_prompt_data = json.loads(new_prompt_json)
                new_topics = new_prompt_data.get("topics", [])
                
                # Check if topics were found
                if not new_topics:
                    st.warning("⚠️ No topics were found in the new prompt output, which may indicate incorrect data extraction.")
                    with st.expander("Show Raw Results"):
                        st.text_area("Raw JSON Output", data[category]["raw_results"]["new_prompt"], height=400)
                
                parsing_method_new = "JSON parsing"
            except json.JSONDecodeError as e:
                st.warning("⚠️ This output contains incorrect data extraction.")

                topic_count = new_prompt_json.count('"topic_name"')
                # Create a simple structure to display something
                new_topics = [{"topic_name": f"Topic {i+1}", "topic_description": "Description not available due to parsing issues", "relevance_score": "N/A"} for i in range(topic_count)]
                parsing_method_new = "Raw string analysis"
        except Exception as e:
            st.error(f"Error processing '{category}' (new_prompt): {str(e)}")
            new_topics = []
            parsing_method_new = "Failed"

        try:
            optimized_prompt_json = data[category]["raw_results"]["optimized_prompt"].replace("```json\n", "").replace("\n```", "")
            # Additional processing to remove potentially problematic characters
            optimized_prompt_json = optimized_prompt_json.strip()
            try:
                optimized_prompt_data = json.loads(optimized_prompt_json)
                optimized_topics = optimized_prompt_data.get("topics", [])
                
                # Check if topics were found
                if not optimized_topics:
                    st.warning("⚠️ No topics were found in the optimized prompt output, which may indicate incorrect data extraction.")
                    with st.expander("Show Raw Results"):
                        st.text_area("Raw JSON Output", data[category]["raw_results"]["optimized_prompt"], height=400)
                
                parsing_method_opt = "JSON parsing"
            except json.JSONDecodeError as e:
                st.warning(f"Warning: JSON parsing failed for '{category}' (optimized_prompt). Using raw string analysis.")
                # Count topics by counting occurrences of "topic_name"
                topic_count = optimized_prompt_json.count('"topic_name"')
                # Create a simple structure to display something
                optimized_topics = [{"topic_name": f"Topic {i+1}", "topic_description": "Description not available due to parsing issues", "relevance_score": "N/A"} for i in range(topic_count)]
                parsing_method_opt = "Raw string analysis"
        except Exception as e:
            st.error(f"Error processing '{category}' (optimized_prompt): {str(e)}")
            optimized_topics = []
            parsing_method_opt = "Failed"
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"##### New Prompt Topics ({parsing_method_new})")
            if not new_topics:
                st.warning("⚠️ No topics found in the structure")
            else:
                for topic in new_topics:
                    with st.expander(f"{topic.get('topic_name')} (Score: {topic.get('relevance_score', 'N/A')})"):
                        st.write(topic.get('topic_description'))

        with col2:
            st.markdown(f"##### Optimized Prompt Topics ({parsing_method_opt})")
            if not optimized_topics:
                st.warning("⚠️ No topics found in the structure")
            else:
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
            if has_duplicate_issue:
                st.warning("⚠️ Detected large number of duplicates in raw data, indicating incorrect data extraction.")
                st.write(f"Total raw entities: {total_raw_entities}, Unique entities (without duplicates): {unique_raw_entities}. ")
            else:
                st.write(f"Total: {knots_comparison['new_prompt_knots_count']}")
            
            # Show entities in a scrollable container if there are many
            if len(new_entities) >= 150:
                with st.expander("Show unique entities"):
                    st.markdown("""
                    <div style="max-height: 200px; overflow-y: scroll;">
                    """, unsafe_allow_html=True)
                    st.write(", ".join(sorted(list(new_entities))))
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
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
        col1, col2, col3 = st.columns([1, 1, 2])  # Додаємо третю колонку для порожнього простору
        font_size = 10
        with col1:
            st.markdown(f"<span style='font-size: {font_size+2}pt;'>Common entities: {knots_comparison['common_knots_count']}</span>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size: {font_size+2}pt;'>Only in new: {knots_comparison['only_in_new_count']}</span>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size: {font_size+2}pt;'>Only in optimized: {knots_comparison['only_in_optimized_count']}</span>", unsafe_allow_html=True)

        with col2:
            # Check if there are too many entities to visualize
            new_prompt_count = knots_comparison['new_prompt_knots_count']
            optimized_prompt_count = knots_comparison['optimized_prompt_knots_count']
            display_new_count = total_raw_entities if has_duplicate_issue else new_prompt_count
            if new_prompt_count > 150 or optimized_prompt_count > 150 or has_duplicate_issue:
                st.warning(f"⚠️ Too many entities to visualize effectively (New:  {display_new_count}, Optimized: {optimized_prompt_count}).")

            else:
                # Створюємо ще менший графік
                fig, ax = plt.subplots(figsize=(3, 3))  # Ще менший розмір
                
                # Налаштовуємо мінімальний розмір для кожної підмножини
                min_size = 10
                
                # Розраховуємо нормалізовані розміри
                # Розраховуємо нормалізовані розміри на основі фактичних даних
                total_entities = max(knots_comparison["only_in_new_count"] + knots_comparison["only_in_optimized_count"] + knots_comparison["common_knots_count"], 1)
                
                # Забезпечуємо мінімальний розмір для кожної підмножини
                a_size = max(min_size, int(100 * knots_comparison["only_in_new_count"] / total_entities))
                b_size = max(min_size, int(100 * knots_comparison["only_in_optimized_count"] / total_entities))
                ab_size = max(min_size, int(100 * knots_comparison["common_knots_count"] / total_entities))
                
                # Змінюємо рядки 374-412 на цей код
                # Створюємо діаграму Венна з точним контролем над розмірами та підписами
                from matplotlib_venn import venn2_circles

                # Створюємо діаграму з правильними розмірами множин
                # Використовуємо другий формат: (Aonly, Bonly, AB)
                venn = venn2(subsets=(
                    knots_comparison["only_in_new_count"],  # Тільки в A (без перетину)
                    knots_comparison["only_in_optimized_count"],  # Тільки в B (без перетину)
                    knots_comparison["common_knots_count"]  # Перетин A і B
                ), set_labels=('New', 'Opt'))

                # Налаштовуємо кольори та прозорість
                if venn:
                    # Налаштовуємо кольори для кращого вигляду
                    for patch_id in ['10', '01', '11']:
                        patch = venn.get_patch_by_id(patch_id)
                        if patch:
                            if patch_id == '10':
                                patch.set_color('#ff9999')  # Тільки A (світло-червоний)
                            elif patch_id == '01':
                                patch.set_color('#99cc99')  # Тільки B (світло-зелений)
                            elif patch_id == '11':
                                patch.set_color('#cc8866')  # Перетин (коричневий)
                            patch.set_alpha(0.7)
    
                    # Додаємо контури для кращого вигляду
                    venn2_circles(subsets=(
                        knots_comparison["only_in_new_count"],
                        knots_comparison["only_in_optimized_count"],
                        knots_comparison["common_knots_count"]
                    ), linestyle='solid', linewidth=0.5, color='gray')
                    
                    # Додаємо підписи для множин
                    if hasattr(venn, 'set_labels') and venn.set_labels:
                        label_a = venn.get_label_by_id('A')
                        label_b = venn.get_label_by_id('B')
                        
                        if label_a:
                            label_a.set_text(f'New prompt\n({knots_comparison["only_in_new_count"] + knots_comparison["common_knots_count"]})')
                            label_a.set_fontsize(font_size)
                        
                        if label_b:
                            label_b.set_text(f'Optimized prompt\n({knots_comparison["only_in_optimized_count"] + knots_comparison["common_knots_count"]})')
                            label_b.set_fontsize(font_size)
                    
                    # Встановлюємо підписи для кожної області з правильними значеннями
                    if hasattr(venn, 'subset_labels') and venn.subset_labels and len(venn.subset_labels) >= 3:
                        for i, label in enumerate(venn.subset_labels):
                            if label:
                                if i == 0:  # Тільки в New
                                    label.set_text(f'{knots_comparison["only_in_new_count"]}')
                                elif i == 1:  # Тільки в Optimized
                                    label.set_text(f'{knots_comparison["only_in_optimized_count"]}')
                                elif i == 2:  # Перетин
                                    label.set_text(f'{knots_comparison["common_knots_count"]}')
                                label.set_fontsize(font_size)
                    
                    # Налаштовуємо заголовок та вигляд
                    plt.title("Entity Overlap", fontsize=font_size)
                    plt.tight_layout()
                    plt.axis('off')

                # Використовуємо st.pyplot з обмеженою шириною
                st.pyplot(fig, use_container_width=False)
                
        # Extract knots from raw results
        try:
            # Use our special function to extract data
            new_section_knots = extract_knots_from_section(data[category]["raw_results"]["new_prompt"])
            
            # Additional check for problematic data
            # Count total and unique entities across all groups
            all_entities = []
            for group in new_section_knots:
                all_entities.extend(group)

            total_entities = len(all_entities)
            unique_entities = len(set(all_entities))
            duplicate_count = total_entities - unique_entities
            duplicate_percentage = 1 - (unique_entities / total_entities) if total_entities > 0 else 0

            if total_entities > 1000 or (duplicate_count > 10 and duplicate_percentage > 0.2):
                st.warning("⚠️ Detected large number of duplicates, indicating incorrect data extraction.")
        except Exception as e:
            st.error(f"Error processing section knots: {str(e)}")
            new_section_knots = []
            
        try:
            if parsing_method_opt != "Failed" and "entities" in (optimized_prompt_data if parsing_method_opt == "JSON parsing" else {}):
                optimized_section_knots = optimized_prompt_data["entities"].get("knots_from_section", [])
                optimized_paragraph_knots = optimized_prompt_data["entities"].get("knots_from_paragraph", [])
            else:
                # Try to extract using regex if JSON parsing failed
                import re
                section_pattern = r'"knots_from_section":\s*\[(.*?)\]'
                match = re.search(section_pattern, optimized_prompt_json, re.DOTALL)
                if match:
                    section_content = match.group(1)
                    # This is a simplified approach - might not work for all cases
                    optimized_section_knots = []
                    current_group = []
                    for line in section_content.split('\n'):
                        if '[' in line:
                            current_group = []
                        elif ']' in line and current_group:
                            optimized_section_knots.append(current_group)
                        elif '"' in line:
                            item = line.strip().strip(',').strip('"')
                            if item:
                                current_group.append(item)
                else:
                    optimized_section_knots = []
                
                # Similarly for paragraph knots
                paragraph_pattern = r'"knots_from_paragraph":\s*\[(.*?)\]'
                match = re.search(paragraph_pattern, optimized_prompt_json, re.DOTALL)
                if match:
                    paragraph_content = match.group(1)
                    optimized_paragraph_knots = []
                    current_group = []
                    for line in paragraph_content.split('\n'):
                        if '[' in line:
                            current_group = []
                        elif ']' in line and current_group:
                            optimized_paragraph_knots.append(current_group)
                        elif '"' in line:
                            item = line.strip().strip(',').strip('"')
                            if item:
                                current_group.append(item)
                else:
                    optimized_paragraph_knots = []
        except Exception:
            optimized_section_knots = []
            optimized_paragraph_knots = []
        
        # Knots from section comparison
        st.markdown("---")
        st.subheader("Knots from Section Comparison")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("##### New Prompt Section Knots")
            if new_section_knots:
                all_entities = []
                for group in new_section_knots:
                    all_entities.extend(group)

                all_entities = []
                for group in new_section_knots:
                    all_entities.extend(group)

                total_entities = len(all_entities)
                unique_entities = len(set(all_entities))
                duplicate_count = total_entities - unique_entities
                duplicate_percentage = 1 - (unique_entities / total_entities) if total_entities > 0 else 0

                if (total_entities > 1000) or (duplicate_count > 10 and duplicate_percentage > 0.2):
                    st.warning("⚠️ This email contains a large number of duplicate entities, indicating incorrect data extraction.")
                    st.write(f"Total entities: {total_entities}, Unique entities: {unique_entities}")
                    
                    # Show in a compact view with scrolling capability
                    with st.expander("Show entities (contains massive duplicates)"):
                        st.markdown("""
                        <div style="max-height: 300px; overflow-y: scroll;">
                        """, unsafe_allow_html=True)
                        
                        # Show first 100 unique entities
                        st.write(f"First 100 all_entities (out of {len(all_entities)}):")
                        st.write(", ".join(list(all_entities)[:100]) + "...")
                        
                        st.markdown("</div>", unsafe_allow_html=True)
                elif has_excessive_duplicates(new_section_knots):
                    # Standard handling for other cases with duplicates
                    st.warning("⚠️ Detected excessive duplicate entities, which may indicate incorrect data extraction.")
                    
                    # Count total entities and unique entities
                    all_entities = []
                    for group in new_section_knots:
                        all_entities.extend(group)
                    
                    unique_entities = set(all_entities)
                    
                    st.write(f"Total raw entities: {len(all_entities)}, Unique entities (without duplicates): {len(unique_entities)}")
                    
                    # Show in a container with limited height
                    with st.expander("Show entities (may contain duplicates)"):
                        st.markdown("""
                        <div style="max-height: 300px; overflow-y: scroll;">
                        """, unsafe_allow_html=True)
                        
                        for i, knot_group in enumerate(new_section_knots):
                            st.markdown(f"**Section {i+1} ({len(knot_group)} entities)**")
                            st.write(", ".join(knot_group))
                        
                        st.markdown("</div>", unsafe_allow_html=True)
                else:
                    # Normal case without duplicates
                    for i, knot_group in enumerate(new_section_knots):
                        with st.expander(f"Section {i+1} ({len(knot_group)} entities)"):
                            st.write(", ".join(knot_group))
            else:
                # Check if there's raw data that might contain knots but failed to parse
                raw_new_prompt = data[category]["raw_results"]["new_prompt"]
                if "knots_from_section" in raw_new_prompt:
                    st.warning("⚠️ Failed to extract section knots properly from new prompt data")
                    with st.expander("Show Raw Results"):
                        st.text_area("Raw JSON Output", raw_new_prompt, height=300)
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
    categories_display = [cat.replace("_", " ").title() for cat in available_categories]
    time_diffs = [data[cat]["metrics_comparison"]["differences"]["time_difference_percentage"] for cat in available_categories]
    cost_diffs = [data[cat]["metrics_comparison"]["differences"]["cost_difference_percentage"] for cat in available_categories]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(categories_display))
    width = 0.35
    
    ax.bar([i - width/2 for i in x], cost_diffs, width, label='Cost Difference %')
    ax.bar([i + width/2 for i in x], time_diffs, width, label='Time Difference %')
    
    ax.set_ylabel('Percentage (%)')
    ax.set_title('Cost and Time Differences by Email Category')
    ax.set_xticks(x)
    ax.set_xticklabels(categories_display)
    ax.legend()
    
    st.pyplot(fig)

with col2:
    st.subheader("Analysis Quality Comparison")
    
    # Compare the number of topics and entities identified
    topic_counts = {
        "New": [],
        "Optimized": []
    }

    entity_counts = {
        "New": [],
        "Optimized": []
    }

    # Track parsing methods used
    parsing_methods = {
        "New": [],
        "Optimized": []
    }

    for cat in available_categories:
        # Get topic counts for new prompt
        try:
            raw_new_prompt = data[cat]["raw_results"]["new_prompt"]
            # Try to parse JSON
            cleaned_json = raw_new_prompt.replace("```json\n", "").replace("\n```", "").strip()
            try:
                new_prompt_data = json.loads(cleaned_json)
                topic_counts["New"].append(len(new_prompt_data.get("topics", [])))
                parsing_methods["New"].append("JSON")
            except json.JSONDecodeError:
                # Fallback to counting occurrences of "topic_name"
                topic_count = raw_new_prompt.count('"topic_name"')
                topic_counts["New"].append(topic_count)
                parsing_methods["New"].append("Raw")
        except Exception:
            topic_counts["New"].append(0)
            parsing_methods["New"].append("Failed")
        
        # Get topic counts for optimized prompt
        try:
            raw_optimized_prompt = data[cat]["raw_results"]["optimized_prompt"]
            # Try to parse JSON
            cleaned_json = raw_optimized_prompt.replace("```json\n", "").replace("\n```", "").strip()
            try:
                optimized_prompt_data = json.loads(cleaned_json)
                topic_counts["Optimized"].append(len(optimized_prompt_data.get("topics", [])))
                parsing_methods["Optimized"].append("JSON")
            except json.JSONDecodeError:
                # Fallback to counting occurrences of "topic_name"
                topic_count = raw_optimized_prompt.count('"topic_name"')
                topic_counts["Optimized"].append(topic_count)
                parsing_methods["Optimized"].append("Raw")
        except Exception:
            topic_counts["Optimized"].append(0)
            parsing_methods["Optimized"].append("Failed")
        
        # Get entity counts
        entity_counts["New"].append(data[cat]["knots_comparison"]["new_prompt_knots_count"])
        entity_counts["Optimized"].append(data[cat]["knots_comparison"]["optimized_prompt_knots_count"])

    # Create DataFrames for the counts
    topic_df = pd.DataFrame(topic_counts, index=categories_display)
    entity_df = pd.DataFrame(entity_counts, index=categories_display)
    
    # Plot the counts
    st.write("Number of Topics Identified:")
    st.bar_chart(topic_df)
    
    # Display parsing method information
    if "Raw" in parsing_methods["New"] or "Raw" in parsing_methods["Optimized"] or "Failed" in parsing_methods["New"] or "Failed" in parsing_methods["Optimized"]:
        st.info("Note: Some categories required raw string parsing instead of JSON parsing due to formatting issues.")
        
        for i, cat in enumerate(categories_display):
            method_new = parsing_methods["New"][i]
            method_opt = parsing_methods["Optimized"][i]
            if method_new != "JSON" or method_opt != "JSON":
                st.write(f"**{cat}**: New Prompt - {method_new} parsing, Optimized Prompt - {method_opt} parsing")
    
    st.write("Number of Entities Identified:")
    st.bar_chart(entity_df)
    
    # Add conclusions
    st.markdown("""
    ### Key Findings:
    
    1. **Execution Cost**: The optimized approach shows varying cost results depending on the email type. 

    2. **Execution Time**: Processing time also varies by email type. For some types, the optimized approach is faster, for others - slower.

    3. **Topic Quality**: The optimized approach provides more detailed and contextual topic descriptions, while the new approach uses more concise formulations.
    
    4. **Data Extraction Issues**:
        The *new prompt* approach shows significant issues with entity extraction in specific emails (particularly email 4), producing massive amounts of duplicate entities (even when called again, the situation repeats itself).
        
        Occasionally, on some calls, the optimized approach extracts email addresses as knots, though less often than the *new prompt*.
    
    5. **Topic Generation Failures**: In some cases, the new prompt fails to generate topics for complex emails (like email 4).
                
    6. **Result Stability**: Both prompting approaches show inconsistent results across runs, especially with complex and information-rich emails (the most difficult to process are 3d and 4th emails). However, the *optimized prompt* proved to be more stable.
    """)

st.markdown("---")
st.caption("Email Analysis Comparison Dashboard")

# Helper functions for email processing
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

def extract_email_parts(raw_email):
    """Extract key parts from a raw email"""
    import re
    import email
    from email.header import decode_header
    
    # Try to parse using email module first
    try:
        # Parse the email
        msg = email.message_from_string(raw_email)
        
        # Extract and decode subject
        subject = msg.get("Subject", "No subject")
        decoded_subject = ""
        for part, encoding in decode_header(subject):
            if isinstance(part, bytes):
                try:
                    decoded_part = part.decode(encoding or 'utf-8', errors='replace')
                except:
                    decoded_part = part.decode('utf-8', errors='replace')
            else:
                decoded_part = part
            decoded_subject += decoded_part
        
        # Clean up subject (remove =?utf-8?q?= and similar markers)
        decoded_subject = re.sub(r'=\?utf-8\?q\?|\?=', '', decoded_subject)
        
        # Extract sender
        sender = msg.get("From", "Unknown sender")
        
        # Extract date
        date = msg.get("Date", "Unknown date")
        
        # Extract body
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    try:
                        body = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', errors='replace')
                        break
                    except:
                        pass
                elif content_type == "text/html":
                    try:
                        body = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', errors='replace')
                        # Try to extract text from HTML
                        body = re.sub(r'<[^>]+>', ' ', body)
                        body = re.sub(r'\s+', ' ', body)
                        break
                    except:
                        pass
        else:
            try:
                body = msg.get_payload(decode=True).decode(msg.get_content_charset() or 'utf-8', errors='replace')
            except:
                body = msg.get_payload()
        
        if not body:
            body = "Email body could not be extracted"
    except Exception as e:
        # Fallback to regex if email parsing fails
        # Extract subject
        subject_match = re.search(r'Subject: (.*?)\n', raw_email, re.IGNORECASE)
        decoded_subject = subject_match.group(1) if subject_match else "No subject"
        decoded_subject = re.sub(r'=\?utf-8\?q\?|\?=', '', decoded_subject)
        
        # Extract sender
        from_match = re.search(r'From: (.*?)\n', raw_email, re.IGNORECASE)
        sender = from_match.group(1) if from_match else "Unknown sender"
        
        # Extract date
        date_match = re.search(r'Date: (.*?)\n', raw_email, re.IGNORECASE)
        date = date_match.group(1) if date_match else "Unknown date"
        
        # Extract body (simplified approach)
        # Find a blank line followed by content
        body_match = re.search(r'\n\s*\n(.*)', raw_email, re.DOTALL)
        body = body_match.group(1) if body_match else "Email body could not be extracted"
    
    # Clean up the subject - remove encoding markers
    decoded_subject = re.sub(r'=\?utf-8\?q\?|\?=', '', decoded_subject)
    
    return {
        "subject": decoded_subject,
        "sender": sender,
        "date": date,
        "body": body
    }

# Create tabs for real emails only
st.header("Real Email Examples")

# Import real emails
try:
    from samples.real_email import real_email_1, real_email_2, real_email_3, real_email_4, real_email_5, real_email_6
    has_real_emails = True
except ImportError:
    has_real_emails = False

if has_real_emails:
    # Real emails
    real_email_tabs = st.tabs(["Real Email 1", "Real Email 2", "Real Email 3", "Real Email 4", "Real Email 5", "Real Email 6"])
    
    real_email_samples = {
        "Real Email 1": real_email_1,
        "Real Email 2": real_email_2,
        "Real Email 3": real_email_3,
        "Real Email 4": real_email_4,
        "Real Email 5": real_email_5,
        "Real Email 6": real_email_6
    }
    
    # Display real emails
    for i, (tab_name, email_tab) in enumerate(zip(["Real Email 1", "Real Email 2", "Real Email 3", "Real Email 4", "Real Email 5", "Real Email 6"], real_email_tabs)):
        with email_tab:
            try:
                # Extract email parts
                email_parts = extract_email_parts(real_email_samples[tab_name])
                
                # Display structured email information
                st.subheader(email_parts["subject"])
                
                # Create tabs for different views
                raw_tab, html_tab, text_tab = st.tabs(["Raw Email", "HTML View", "Text View"])
                
                with raw_tab:
                    st.text_area("Raw Email", real_email_samples[tab_name][:5000] + ("..." if len(real_email_samples[tab_name]) > 5000 else ""), height=400)
                
                with html_tab:
                    # Try to extract HTML content
                    html_content = ""
                    try:
                        import email
                        msg = email.message_from_string(real_email_samples[tab_name])
                        
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            if content_type == "text/html":
                                try:
                                    html_content = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', errors='replace')
                                    break
                                except Exception:
                                    pass
                    except Exception:
                        html_content = ""
                    
                    if html_content:
                        st.components.v1.html(html_content, height=500, scrolling=True)
                    else:
                        st.info("No HTML content found in this email")
                
                with text_tab:
                    st.markdown("### Email Body")
                    st.text_area("Content", email_parts["body"], height=400)
            except Exception as e:
                st.error(f"Error processing email: {str(e)}")
                st.text_area("Raw Email Content", real_email_samples[tab_name][:5000] + ("..." if len(real_email_samples[tab_name]) > 5000 else ""), height=400)
else:
    st.warning("Real email samples could not be loaded. Make sure samples/real_email.py exists and contains the required variables.")
        
