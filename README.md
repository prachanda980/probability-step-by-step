# Interactive Python Tutorial System

This is a Streamlit-based application designed to read Jupyter Notebooks and display them as step-by-step interactive lessons.

## Features
- **Automatic Detection**: Automatically finds all `.ipynb` files in the `notebooks/` folder.
- **Step-by-Step Navigation**: Move through markdown and code cells using "Next" and "Previous" buttons.
- **Interactive Execution**: Run code cells directly in the browser and see the results.
- **Rich Rendering**: Supports formatted text (Markdown), syntax-highlighted code, and rich outputs (tables, images, text).
- **Progress Tracking**: Sidebar shows progress through each lesson.

## Setup

1. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Folder Structure
- `app.py`: The main application logic.
- `notebooks/`: Place your Jupyter Notebook files here.
- `requirements.txt`: List of required Python packages.

## Customizing Lessons
- Each notebook in the `notebooks/` folder becomes a lesson.
- If you add a `.md` file with the same name as the notebook (e.g., `Introduction.md` for `Introduction.ipynb`), it will be displayed as an introductory info box for that lesson.
