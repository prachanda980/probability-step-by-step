import streamlit as st
import nbformat
import os
import base64
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Interactive Python Tutorial",
    page_icon="🎓",
    layout="wide",
)

# Custom CSS for a clean, premium look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stMarkdown {
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
    }
    .stCodeBlock {
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    .step-container {
        background-color: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .navigation-buttons {
        display: flex;
        justify-content: space-between;
        margin-top: 2rem;
    }
    .lesson-header {
        color: #1e3d59;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to load notebooks
def get_notebook_files(directory="notebooks"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return [f for f in os.listdir(directory) if f.endswith(".ipynb")]

def load_notebook(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        return nb
    except Exception as e:
        st.error(f"Error loading notebook: {e}")
        return None

def render_output(output):
    """Renders Jupyter notebook cell outputs in Streamlit."""
    if output.output_type == 'stream':
        st.text(output.text)
    elif output.output_type in ['execute_result', 'display_data']:
        data = output.data
        if 'image/png' in data:
            image_data = base64.b64decode(data['image/png'])
            st.image(image_data)
        elif 'image/jpeg' in data:
            image_data = base64.b64decode(data['image/jpeg'])
            st.image(image_data)
        elif 'image/svg+xml' in data:
            st.svg(data['image/svg+xml'])
        elif 'text/html' in data:
            st.components.v1.html(data['text/html'], scrolling=True)
        elif 'text/plain' in data:
            st.text(data['text/plain'])

def run_code(code):
    """Executes code and captures output (simplistic implementation)."""
    # In a real-world app, you might want to use an interactive kernel
    # For now, we'll use a simple execution model
    # Note: exec() is dangerous in public apps, but fits local tutorial needs
    import sys
    from io import StringIO
    
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    
    try:
        # We can pass globals/locals to maintain state across cells if desired
        exec(code, st.session_state.get('code_globals', {}))
        result = redirected_output.getvalue()
    except Exception as e:
        result = str(e)
    finally:
        sys.stdout = old_stdout
    
    return result

# Sidebar - Lesson Selection
st.sidebar.title("📚 Lessons")
notebook_files = get_notebook_files()

if not notebook_files:
    st.sidebar.warning("No notebooks found in 'notebooks/' folder.")
    selected_notebook = None
else:
    # Format filenames for better display
    labels = {f: f.replace("-", " ").replace("_", " ").replace(".ipynb", "").title() for f in notebook_files}
    selected_notebook = st.sidebar.selectbox(
        "Select a Lesson",
        notebook_files,
        format_func=lambda x: labels[x]
    )

# Main Content
if selected_notebook:
    # State management for steps
    if 'current_lesson' not in st.session_state or st.session_state.current_lesson != selected_notebook:
        st.session_state.current_lesson = selected_notebook
        st.session_state.current_step = 0
        st.session_state.code_globals = {} # Reset code execution state for new lesson

    nb_path = os.path.join("notebooks", selected_notebook)
    nb = load_notebook(nb_path)
    
    if nb:
        # Filter empty cells
        cells = [c for c in nb.cells if c.source.strip()]
        total_steps = len(cells)
        
        current_step = st.session_state.current_step
        
        # Display Progress
        st.sidebar.progress((current_step + 1) / total_steps if total_steps > 0 else 0)
        st.sidebar.write(f"Step {current_step + 1} of {total_steps}")
        
        # Current Cell Content
        cell = cells[current_step]
        
        st.title(labels[selected_notebook])
        
        # Check for optional README.md in a subfolder or same folder
        # For simplicity, we'll check if a .md file with same name exists
        readme_path = nb_path.replace(".ipynb", ".md")
        if os.path.exists(readme_path):
            with open(readme_path, 'r') as f:
                st.info(f.read())

        with st.container():
            st.markdown(f"### Step {current_step + 1}")
            if cell.cell_type == 'markdown':
                st.markdown(cell.source)
            elif cell.cell_type == 'code':
                st.markdown("#### 💻 Code")
                st.code(cell.source, language='python')
                
                # Execution Option
                if st.button("▶️ Run Code"):
                    output = run_code(cell.source)
                    st.markdown("#### 📤 Output")
                    st.info(output if output else "Code executed successfully (no output).")
                
                # Show saved outputs from notebook
                if 'outputs' in cell and cell.outputs:
                    with st.expander("Show Saved Output", expanded=True):
                        for out in cell.outputs:
                            render_output(out)

        # Navigation
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("Previous", disabled=(current_step == 0)):
                st.session_state.current_step -= 1
                st.rerun()
        
        with col3:
            if st.button("Next", disabled=(current_step == total_steps - 1)):
                st.session_state.current_step += 1
                st.rerun()
                
        # Optional: Jump to step
        st.sidebar.markdown("---")
        jump_step = st.sidebar.slider("Jump to Step", 1, total_steps, current_step + 1)
        if jump_step != current_step + 1:
            st.session_state.current_step = jump_step - 1
            st.rerun()

        # Download options
        st.sidebar.markdown("---")
        st.sidebar.write(" Export Lesson")
        if st.sidebar.button("Download as Text"):
            full_text = ""
            for c in cells:
                full_text += f"--- STEP ---\n{c.source}\n\n"
            st.sidebar.download_button("Click to Download", full_text, file_name=f"{selected_notebook}.txt")

else:
    st.title("Welcome to Python Interactive Tutorials!")
    st.write("Please select a lesson from the sidebar to get started.")
    st.image("https://img.icons8.com/clouds/200/000000/python.png")
