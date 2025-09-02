import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import os
from typing import Dict, Any

st.set_page_config(
    page_title="File Comparison",
    page_icon="📄",
    layout="wide"
)

st.title("File Chunks Comparison")
st.markdown("""
This dashboard visualizes the analysis of file chunks, showing entities and topics extracted from different parts of the document.

**Separate Approach**: Processes the document using multiple prompts sequentially (legacy approach). Each chunk is analyzed independently with limited context awareness. This approach did not utilize topics extraction

**Combined Approach**: Processes the entire document using a single comprehensive prompt, maintaining full context and relationships between different parts of the document.

            
The file comparison tabs show results for different context window sizes (16K and 32K tokens), allowing comparison of how increasing context affects analysis quality and performance.

**Test Documents:**
- **File 1**: ~112,607 tokens
- **File 2**: ~3,440 tokens
- **File 3**: ~56,347 tokens
            
            """)

# Define available comparison files
comparison_files = {
    "File Comparison 1 (16k tokens)": "results/file_comparison_1_v16.json",
    "File Comparison 1 (32k tokens)": "results/file_comparison_1_v32.json",
    "File Comparison 2": "results/file_comparison_2_.json",
    "File Comparison 3(16k tokens)": "results/file_comparison_3_v16.json",
    "File Comparison 3(32k tokens)": "results/file_comparison_3_v32.json",
}

# Create data structures to store aggregated information from all files
all_separate_metrics = {}
all_combined_metrics = {}
all_separate_entities_dict = {}  # Словник для підрахунку кількості входжень кожної сутності
all_combined_entities_dict = {} 
all_separate_topics = []
all_combined_topics = []
all_common_entities_dict = {}

# Create a selector for comparison files
comparison_tabs = st.tabs(list(comparison_files.keys()))

# Load the selected comparison data
@st.cache_data
def load_file_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        st.error(f"Error loading comparison data: {str(e)}")
        return None

for tab_name, tab in zip(comparison_files.keys(), comparison_tabs):
    with tab:
        # Load the data for this tab
        data = load_file_data(comparison_files[tab_name])
        
        # Only proceed if data was loaded successfully
        if data:
            st.subheader(f"Execution Metrics - {tab_name}")
            
            # Get metrics
            separate_metrics = data["separate_approach"]["metrics"]
            combined_metrics = data["combined_approach"]["metrics"]
            
            # Calculate differences
            time_difference = separate_metrics["execution_time"] - combined_metrics["execution_time"]
            time_difference_percentage = (time_difference / separate_metrics["execution_time"]) * 100
            
            cost_difference = separate_metrics["cost"] - combined_metrics["cost"]
            cost_difference_percentage = (cost_difference / separate_metrics["cost"]) * 100
            
            tokens_difference = separate_metrics["total_tokens"] - combined_metrics["total_tokens"]
            tokens_difference_percentage = (tokens_difference / separate_metrics["total_tokens"]) * 100

            separate_entities = set(data["separate_approach"]["knots"])
            combined_entities = set(data["combined_approach"]["knots"])
            
            # Зберігаємо метрики та сутності для загального підсумку
            all_separate_metrics[tab_name] = separate_metrics
            all_combined_metrics[tab_name] = combined_metrics
            
            # Додаємо унікальні сутності з поточного файлу до загальних словників
            for entity in separate_entities:
                if entity in all_separate_entities_dict:
                    all_separate_entities_dict[entity] += 1
                else:
                    all_separate_entities_dict[entity] = 1
            
            for entity in combined_entities:
                if entity in all_combined_entities_dict:
                    all_combined_entities_dict[entity] += 1
                else:
                    all_combined_entities_dict[entity] = 1
            


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
                    st.metric("Separate Approach Time (s)", 
                                f"{separate_metrics.get('execution_time'):.2f}")
                    
                    st.metric("Separate Approach Cost ($)", 
                                f"{separate_metrics.get('cost'):.6f}")
                
                with col1b:
                    st.metric("Combined Approach Time (s)", 
                                f"{combined_metrics.get('execution_time'):.2f}",
                                f"{time_difference_percentage:.1f}%")
                    
                    st.metric("Combined Approach Cost ($)", 
                                f"{combined_metrics.get('cost'):.6f}",
                                f"{cost_difference_percentage:.1f}%")

            with col2:
                st.markdown("""
                <small>
                <b>Token Usage Comparison</b><br>
                Shows total tokens processed by each approach.
                </small>
                """, unsafe_allow_html=True)
                
                st.metric("Separate Approach Tokens", 
                        f"{separate_metrics['total_tokens']}")
                
                st.metric("Combined Approach Tokens", 
                        f"{combined_metrics['total_tokens']}",
                        f"{tokens_difference_percentage:.1f}%")

            with col3:
                st.markdown("""
                <small>
                <b>Token Efficiency</b><br>
                Shows tokens difference between approaches.
                </small>
                """, unsafe_allow_html=True)
                
                st.metric("Token Difference", 
                        f"{tokens_difference}")
                
                # Додаткова інформація про вхідні/вихідні токени
                st.write(f"Separate: {separate_metrics['input_tokens']} in / {separate_metrics['output_tokens']} out")
                st.write(f"Combined: {combined_metrics['input_tokens']} in / {combined_metrics['output_tokens']} out")


            st.subheader("Entities Comparison")

            # Отримуємо дані про сутності
            knots_comparison = data["knots_comparison"]

            # Створюємо набори сутностей для порівняння
            separate_entities = set(data["separate_approach"]["knots"])
            combined_entities = set(data["combined_approach"]["knots"])
            
            # Зберігаємо метрики та сутності для загального підсумку
            all_separate_metrics[tab_name] = separate_metrics
            all_combined_metrics[tab_name] = combined_metrics


            # Створюємо колонки для списків сутностей
            col1, col2 = st.columns(2)

            with col1:
                
                st.markdown("##### Separate Approach Entities without duplicates")
                st.write(f"Total: {len(separate_entities)}")
                
                # Показуємо сутності в контейнері з прокруткою, якщо їх багато
                if len(separate_entities) >= 50:
                    with st.expander("Show all entities"):
                        st.markdown("""
                        <div style="max-height: 200px; overflow-y: scroll;">
                        """, unsafe_allow_html=True)
                        st.write(", ".join(sorted(list(separate_entities))))
                        st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.write(", ".join(sorted(list(separate_entities))))

            with col2:
                st.markdown("##### Combined Approach Entities without duplicates")
                st.write(f"Total: {len(combined_entities)}")
                
                # Показуємо сутності в контейнері з прокруткою, якщо їх багато
                if len(combined_entities) >= 50:
                    with st.expander("Show all entities"):
                        st.markdown("""
                        <div style="max-height: 200px; overflow-y: scroll;">
                        """, unsafe_allow_html=True)
                        st.write(", ".join(sorted(list(combined_entities))))
                        st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.write(", ".join(sorted(list(combined_entities))))

            # Створюємо діаграму Венна для перекриття сутностей
            common_entities = separate_entities.intersection(combined_entities)
            only_separate = separate_entities - combined_entities
            only_combined = combined_entities - separate_entities
            
            for entity in common_entities:
                if entity in all_common_entities_dict:
                    all_common_entities_dict[entity] += 1
            else:
                all_common_entities_dict[entity] = 1

            st.markdown("##### Entity Overlap Analysis")
            col1, col2, col3 = st.columns([1, 1, 2])
            font_size = 10

            with col1:
                st.markdown(f"<span style='font-size: {font_size+2}pt;'>Common entities: {len(common_entities)}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='font-size: {font_size+2}pt;'>Only in separate: {len(only_separate)}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='font-size: {font_size+2}pt;'>Only in combined: {len(only_combined)}</span>", unsafe_allow_html=True)

            # Показуємо спільні та унікальні сутності
            st.subheader("Entity Lists")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("##### Common Entities")
                if common_entities:
                    with st.expander(f"Show common entities ({len(common_entities)})"):
                        st.markdown("""
                        <div style="max-height: 300px; overflow-y: scroll;">
                        """, unsafe_allow_html=True)
                        st.write(", ".join(sorted(list(common_entities))))
                        st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.info("No common entities found.")

            with col2:
                st.markdown("##### Only in Separate Approach")
                if only_separate:
                    with st.expander(f"Show unique entities ({len(only_separate)})"):
                        st.markdown("""
                        <div style="max-height: 300px; overflow-y: scroll;">
                        """, unsafe_allow_html=True)
                        st.write(", ".join(sorted(list(only_separate))))
                        st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.info("No unique entities in Separate Approach.")

            with col3:
                st.markdown("##### Only in Combined Approach")
                if only_combined:
                    with st.expander(f"Show unique entities ({len(only_combined)})"):
                        st.markdown("""
                        <div style="max-height: 300px; overflow-y: scroll;">
                        """, unsafe_allow_html=True)
                        st.write(", ".join(sorted(list(only_combined))))
                        st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.info("No unique entities in Combined Approach.")

            st.subheader("Topics Analysis")

            # Функція для витягування тем з raw_json
            def extract_topics(raw_json):
                if not raw_json:
                    return []
                
                # Результуючий список всіх тем
                all_topics = []
                
                # Розділяємо на блоки JSON
                json_blocks = []
                
                # Перевіряємо, чи є markdown розмітка
                if "```json" in raw_json:
                    # Розділяємо за markdown блоками
                    blocks = raw_json.split("```json")
                    for i, block in enumerate(blocks):
                        if i > 0:  # Пропускаємо перший елемент (він перед першим ```json)
                            block_content = block.split("```")[0].strip()
                            json_blocks.append(block_content)
                else:
                    # Якщо немає markdown розмітки, вважаємо весь текст одним JSON
                    json_blocks = [raw_json]
                
                # Обробляємо кожен блок JSON
                for block in json_blocks:
                    try:
                        json_data = json.loads(block)
                        if "topics" in json_data:
                            all_topics.extend(json_data.get("topics", []))
                    except json.JSONDecodeError:
                        # Якщо не вдалося розпарсити блок як JSON, спробуємо використати регулярний вираз
                        try:
                            import re
                            topics_match = re.search(r'"topics"\s*:\s*\[(.*?)\]', block, re.DOTALL)
                            if topics_match:
                                topics_str = f'{{"topics": [{topics_match.group(1)}]}}'
                                try:
                                    json_data = json.loads(topics_str)
                                    all_topics.extend(json_data.get("topics", []))
                                except:
                                    pass
                        except:
                            pass
                
                # Якщо не знайшли жодної теми, повертаємо порожній список
                return all_topics

            # Отримуємо теми з обох підходів
            separate_topics = extract_topics(data["separate_approach"].get("raw_json", ""))
            combined_topics = extract_topics(data["combined_approach"].get("raw_json", ""))
            
            # Зберігаємо теми для загального підсумку
            all_separate_topics.extend(separate_topics)
            all_combined_topics.extend(combined_topics)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("##### Separate Approach Topics.")
                st.markdown(f"<span style='font-size: {font_size+2}pt;'>This approach did not utilize topics extraction</span>", unsafe_allow_html=True)

                if not separate_topics:
                    st.warning("⚠️ No topics found or could not parse JSON")
                else:
                    for topic in separate_topics:
                        with st.expander(f"{topic.get('topic_name')} (Score: {topic.get('relevance_score', '0')})"):
                            st.write(topic.get('topic_description', 'No description available'))

            with col2:
                st.markdown("##### Combined Approach Topics")
                if not combined_topics:
                    st.warning("⚠️ No topics found or could not parse JSON")
                else:
                    st.markdown(f"<span style='font-size: {font_size+2}pt;'>Total topics: {len(combined_topics)}</span>", unsafe_allow_html=True)

                    for topic in combined_topics:
                        with st.expander(f"{topic.get('topic_name')} (Score: {topic.get('relevance_score', 'N/A')})"):
                            st.write(topic.get('topic_description', 'No description available'))

            st.subheader("Knots from Section Analysis")

            # Функція для витягування knots_from_section та keywords_named_entities з raw_json
            def extract_knots_from_section(raw_json, approach="combined"):
                if not raw_json:
                    return []
                
                all_knots = []
                json_blocks = []
                
                if "```json" in raw_json:
                    blocks = raw_json.split("```json")
                    for i, block in enumerate(blocks):
                        if i > 0:  # Пропускаємо перший елемент (він перед першим ```json)
                            block_content = block.split("```")[0].strip()
                            json_blocks.append(block_content)
                else:
                    # Якщо немає markdown розмітки, вважаємо весь текст одним JSON
                    json_blocks = [raw_json]
                
                # Обробляємо кожен блок JSON
                for block in json_blocks:
                    try:
                        # Спробуємо спочатку обробити блок як повний JSON
                        json_data = json.loads(block)
                        
                        if "knots_from_section" in json_data:
                            # Якщо knots_from_section знаходиться в корені JSON
                            all_knots.extend(json_data["knots_from_section"])
                        elif "entities" in json_data and "knots_from_section" in json_data["entities"]:
                            # Якщо knots_from_section знаходиться в entities
                            all_knots.extend(json_data["entities"]["knots_from_section"])
                    except json.JSONDecodeError:
                        # Якщо не вдалося розпарсити як повний JSON, спробуємо знайти відповідні секції
                        try:
                            # Шукаємо knots_from_section
                            start_idx = block.find('"knots_from_section"')
                            if start_idx != -1:
                                # Знаходимо початок масиву після knots_from_section
                                array_start = block.find('[', start_idx)
                                if array_start != -1:
                                    # Використовуємо лічильник дужок
                                    bracket_count = 1
                                    array_end = array_start + 1
                                    
                                    while bracket_count > 0 and array_end < len(block):
                                        if block[array_end] == '[':
                                            bracket_count += 1
                                        elif block[array_end] == ']':
                                            bracket_count -= 1
                                        array_end += 1
                                    
                                    if bracket_count == 0:
                                        array_content = block[array_start:array_end]
                                        try:
                                            knots_str = f'{{"knots_from_section": {array_content}}}'
                                            json_data = json.loads(knots_str)
                                            all_knots.extend(json_data["knots_from_section"])
                                        except:
                                            try:
                                                knots_str = f'{{"entities": {{"knots_from_section": {array_content}}}}}'
                                                json_data = json.loads(knots_str)
                                                all_knots.extend(json_data["entities"]["knots_from_section"])
                                            except:
                                                pass
                        except Exception as e:
                            # Якщо щось пішло не так, спробуємо використати регулярний вираз
                            try:
                                import re
                                # Шукаємо knots_from_section
                                knots_matches = re.finditer(r'"knots_from_section"\s*:\s*(\[\s*\[.*?\]\s*\])', block, re.DOTALL)
                                for match in knots_matches:
                                    try:
                                        knots_str = f'{{"knots_from_section": {match.group(1)}}}'
                                        json_data = json.loads(knots_str)
                                        all_knots.extend(json_data["knots_from_section"])
                                    except:
                                        pass
                            except:
                                pass
                
                return all_knots

            separate_knots = extract_knots_from_section(data["separate_approach"].get("raw_json", ""), approach="separate")
            combined_knots = extract_knots_from_section(data["combined_approach"].get("raw_json", ""), approach="combined")

            # Підраховуємо унікальні сутності для сепарованого підходу
            separate_all_entities = []
            for group in separate_knots:
                separate_all_entities.extend(group)
            separate_entities_count = len(set(separate_all_entities))

            separate_all_entities = []
            for group in separate_knots:
                separate_all_entities.extend(group)
            separate_entities_count = len(set(separate_all_entities))

            # Підраховуємо унікальні сутності для комбінованого підходу
            combined_all_entities = []
            for group in combined_knots:
                combined_all_entities.extend(group)
            combined_entities_count = len(set(combined_all_entities))



            col1, col2 = st.columns(2)

            with col1:
                st.markdown("##### Separate Approach Knots from Section")
                if not separate_knots:
                    st.warning("⚠️ No knots found or could not parse JSON")
                else:
                    # Підраховуємо загальну кількість сутностей та унікальних сутностей
                    all_entities = []
                    for group in separate_knots:
                        all_entities.extend(group)
                    
                    total_entities = len(all_entities)
                    unique_entities = len(set(all_entities))
                    duplicate_count = total_entities - unique_entities
                    duplicate_percentage = 1 - (unique_entities / total_entities) if total_entities > 0 else 0
                    
                    # Порівнюємо з загальною кількістю сутностей
                    knots_match = "✅" if separate_entities_count == len(set(all_entities)) else "❌"
                    st.write(f"Total raw entities: {total_entities}, Unique entities: {unique_entities}, Sections: {len(separate_knots)}")
                    # st.write(f"Knots count: {separate_entities_count}, Unique knots from sections: {len(set(all_entities))} {knots_match}")
                    
                    if len(separate_knots) > 50:
                        with st.expander(f"Show all {len(separate_knots)} sections"):
                            st.markdown("""
                            <div style="max-height: 400px; overflow-y: scroll;">
                            """, unsafe_allow_html=True)
                            
                            for i, knot_group in enumerate(separate_knots):
                                st.markdown(f"**Section {i+1}** ({len(knot_group)} entities)")
                                st.write(", ".join(knot_group))
                                st.markdown("---")
                            
                            st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        # Показуємо групи сутностей як раніше
                        for i, knot_group in enumerate(separate_knots):
                            with st.expander(f"Section {i+1} ({len(knot_group)} entities)"):
                                st.write(", ".join(knot_group))

            with col2:
                st.markdown("##### Combined Approach Knots from Section")
                if not combined_knots:
                    st.warning("⚠️ No knots found or could not parse JSON")
                else:
                    # Підраховуємо загальну кількість сутностей та унікальних сутностей
                    all_entities = []
                    for group in combined_knots:
                        all_entities.extend(group)
                    
                    total_entities = len(all_entities)
                    unique_entities = len(set(all_entities))
                    duplicate_count = total_entities - unique_entities
                    duplicate_percentage = 1 - (unique_entities / total_entities) if total_entities > 0 else 0
                    
                    knots_match = "✅" if combined_entities_count == len(set(all_entities)) else "❌"
                    
                    st.write(f"Total raw entities: {total_entities}, Unique entities: {unique_entities}, Sections: {len(combined_knots)}")
                    # st.write(f"Knots count: {combined_entities_count}, Unique knots from sections: {len(set(all_entities))} {knots_match}")
                    
                    if len(combined_knots) > 50:
                        with st.expander(f"Show all {len(combined_knots)} sections"):
                            st.markdown("""
                            <div style="max-height: 400px; overflow-y: scroll;">
                            """, unsafe_allow_html=True)
                            
                            for i, knot_group in enumerate(combined_knots):
                                st.markdown(f"**Section {i+1}** ({len(knot_group)} entities)")
                                st.write(", ".join(knot_group))
                                st.markdown("---")
                            
                            st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        # Показуємо групи сутностей як раніше
                        for i, knot_group in enumerate(combined_knots):
                            with st.expander(f"Section {i+1} ({len(knot_group)} entities)"):
                                st.write(", ".join(knot_group))

# Загальний підсумок за межами циклу по табах
st.markdown("---")
st.header("Overall Comparison Summary (All Files)")

# Створюємо графік для порівняння підходів
col1, col2 = st.columns(2)

with col1:
    st.subheader("Performance Comparison Across All Files")
    
    # Обчислюємо середні значення для всіх файлів
    if all_separate_metrics and all_combined_metrics:
        # Обчислюємо середні значення метрик
        avg_separate_time = sum(m["execution_time"] for m in all_separate_metrics.values()) / len(all_separate_metrics)
        avg_combined_time = sum(m["execution_time"] for m in all_combined_metrics.values()) / len(all_combined_metrics)
        avg_separate_cost = sum(m["cost"] for m in all_separate_metrics.values()) / len(all_separate_metrics)
        avg_combined_cost = sum(m["cost"] for m in all_combined_metrics.values()) / len(all_combined_metrics)
        avg_separate_tokens = sum(m["total_tokens"] for m in all_separate_metrics.values()) / len(all_separate_metrics)
        avg_combined_tokens = sum(m["total_tokens"] for m in all_combined_metrics.values()) / len(all_combined_metrics)
        
        # Обчислюємо відсоткові різниці
        time_diff_pct = ((avg_separate_time - avg_combined_time) / avg_separate_time) * 100 if avg_separate_time > 0 else 0
        cost_diff_pct = ((avg_separate_cost - avg_combined_cost) / avg_separate_cost) * 100 if avg_separate_cost > 0 else 0
        tokens_diff_pct = ((avg_separate_tokens - avg_combined_tokens) / avg_separate_tokens) * 100 if avg_separate_tokens > 0 else 0
        
        # Створюємо DataFrame для порівняння
        metrics_df = pd.DataFrame({
            "Metric": ["Execution Time (s)", "Cost ($)", "Total Tokens"],
            "Avg Separate": [avg_separate_time, avg_separate_cost, avg_separate_tokens],
            "Avg Combined": [avg_combined_time, avg_combined_cost, avg_combined_tokens],
            "Avg Difference %": [time_diff_pct, cost_diff_pct, tokens_diff_pct]
        })
        
        st.table(metrics_df.set_index("Metric"))
        
        # Показуємо деталі для кожного файлу
        with st.expander("Show details for each file"):
            for file_name in all_separate_metrics.keys():
                st.subheader(file_name)
                file_separate = all_separate_metrics[file_name]
                file_combined = all_combined_metrics[file_name]
                
                file_time_diff = ((file_separate["execution_time"] - file_combined["execution_time"]) / file_separate["execution_time"]) * 100 if file_separate["execution_time"] > 0 else 0
                file_cost_diff = ((file_separate["cost"] - file_combined["cost"]) / file_separate["cost"]) * 100 if file_separate["cost"] > 0 else 0
                file_tokens_diff = ((file_separate["total_tokens"] - file_combined["total_tokens"]) / file_separate["total_tokens"]) * 100 if file_separate["total_tokens"] > 0 else 0
                
                file_df = pd.DataFrame({
                    "Metric": ["Execution Time (s)", "Cost ($)", "Total Tokens"],
                    "Separate": [file_separate["execution_time"], file_separate["cost"], file_separate["total_tokens"]],
                    "Combined": [file_combined["execution_time"], file_combined["cost"], file_combined["total_tokens"]],
                    "Difference %": [file_time_diff, file_cost_diff, file_tokens_diff]
                })
                
                st.table(file_df.set_index("Metric"))
        
        # Створюємо графік порівняння для середніх значень
        fig, ax = plt.subplots(figsize=(10, 6))
        x = range(3)
        width = 0.35
        
        # Нормалізуємо дані для графіка
        normalized_separate = [
            avg_separate_time / max(avg_separate_time, avg_combined_time) if max(avg_separate_time, avg_combined_time) > 0 else 0,
            avg_separate_cost / max(avg_separate_cost, avg_combined_cost) if max(avg_separate_cost, avg_combined_cost) > 0 else 0,
            avg_separate_tokens / max(avg_separate_tokens, avg_combined_tokens) if max(avg_separate_tokens, avg_combined_tokens) > 0 else 0
        ]
        
        normalized_combined = [
            avg_combined_time / max(avg_separate_time, avg_combined_time) if max(avg_separate_time, avg_combined_time) > 0 else 0,
            avg_combined_cost / max(avg_separate_cost, avg_combined_cost) if max(avg_separate_cost, avg_combined_cost) > 0 else 0,
            avg_combined_tokens / max(avg_separate_tokens, avg_combined_tokens) if max(avg_separate_tokens, avg_combined_tokens) > 0 else 0
        ]
        
        ax.bar([i - width/2 for i in x], normalized_separate, width, label='Separate Approach')
        ax.bar([i + width/2 for i in x], normalized_combined, width, label='Combined Approach')
        
        ax.set_ylabel('Normalized Value')
        ax.set_title('Average Performance Metrics Comparison (All Files)')
        ax.set_xticks(x)
        ax.set_xticklabels(["Time", "Cost", "Tokens"])
        ax.legend()
        
        st.pyplot(fig)
    else:
        st.warning("No data available for performance comparison")

with col2:
    st.subheader("Analysis Quality Comparison Across All Files")
    
    all_separate_entities = set(all_separate_entities_dict.keys())
    all_combined_entities = set(all_combined_entities_dict.keys())
    only_separate = all_separate_entities - all_combined_entities
    only_combined = all_combined_entities - all_separate_entities
    common_all_files = all_separate_entities.intersection(all_combined_entities)
    
    # Підраховуємо загальну кількість унікальних сутностей з урахуванням дублікатів між файлами
    total_separate_entities = sum(all_separate_entities_dict.values())
    total_combined_entities = sum(all_combined_entities_dict.values())
    
    # Створюємо DataFrame для порівняння кількості сутностей і тем
    quality_df = pd.DataFrame({
        "Metric": [ "Total Entities", "Topics"],
        "All Separate": [ total_separate_entities, len(all_separate_topics)],
        "All Combined": [ total_combined_entities, len(all_combined_topics)]
    })
    
    
    st.table(quality_df.set_index("Metric"))
    
    # Показуємо діаграму Венна для всіх файлів
    st.markdown("##### Entity Overlap Analysis (All Files)")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"Common entities: {len(common_all_files)}")
        st.markdown(f"Only in separate: {len(only_separate)}")
        st.markdown(f"Only in combined: {len(only_combined)}")
    
    with col2:
        try:
            venn = venn2(subsets=(
                len(only_separate),
                len(only_combined),
                len(common_all_files)
            ), set_labels=('Separate', 'Combined'))
        except Exception as e:
            st.error(f"Error creating Venn diagram: {str(e)}")
    
    # Створюємо графік порівняння
    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(2)
    width = 0.35
    
    ax.bar([i - width/2 for i in x], [len(all_separate_entities), len(all_separate_topics)], width, label='Separate Approach')
    ax.bar([i + width/2 for i in x], [len(all_combined_entities), len(all_combined_topics)], width, label='Combined Approach')
    
    ax.set_ylabel('Count')
    ax.set_title('Entities and Topics Comparison (All Files)')
    ax.set_xticks(x)
    ax.set_xticklabels(["Entities", "Topics"])
    ax.legend()
    
    st.pyplot(fig)
    
    # Додаємо висновки
    st.markdown("""
    ### Key Findings (Across All Files):
    
    1. **Execution Cost**: The combined approach shows significant cost savings compared to the separate approach.
    
    2. **Execution Time**: Processing time is reduced with the combined approach.
    
    3. **Entity Coverage**: The analysis shows differences in entity extraction between approaches. In most cases, the combined approach extracts more entities and identifies more sections
    """)

st.markdown("---")
st.caption("File Analysis Comparison Dashboard")


st.header("File Examples")

# List of files to load
file_samples = [
    {"name": "File 1", "path": "samples/technical_test_doc_1.txt"},
    {"name": "File 2", "path": "samples/technical_test_doc_2.txt"},
    {"name": "File 3", "path": "samples/technical_test_doc_3.txt"},

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