# 🎓 Interactive Python Tutorial System

Transform your Jupyter Notebooks into interactive, step-by-step learning experiences. Build premium-quality coding tutorials with zero effort.

🚀 **Live Demo:** [data-science-statistics.streamlit.app](https://data-science-statistics.streamlit.app/)

---

## ✨ Features

- **📂 Automatic Lesson Detection**: Simply drop your `.ipynb` files into the `notebooks/` folder, and they appear in the app instantly.
- **⏭️ Step-by-Step Navigation**: Breaks down complex notebooks into manageable "steps" with intuitive Next/Previous buttons.
- **⚡ Interactive Code Execution**: Edit and run Python code directly in the browser. Maintains state across steps!
- **📊 Rich Media Support**: Renders Markdown, LaTeX equations, syntax-highlighted code, and rich outputs like Matplotlib plots, images, and tables.
- **📈 Progress Tracking**: Visual progress bars and step counters to keep learners engaged.
- **📝 Lesson Overviews**: Support for optional `.md` files to provide context or learning objectives for each lesson.

---

## 🛠️ Local Setup

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:prachanda980/probability-step-by-step.git
   cd probability-step-by-step
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```text
.
├── app.py                # Main Streamlit application engine
├── notebooks/           # Store your .ipynb tutorial files here
│   ├── Introduction.ipynb
│   └── Introduction.md   # Optional lesson overview metadata
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 💡 How it Works

The system parses the JSON structure of a Jupyter Notebook. 
- **Markdown cells** are rendered as formatted text.
- **Code cells** are rendered in a syntax-highlighted block with an execution button.
- **Outputs** are captured from the notebook metadata or generated live.

To create a new lesson, simply upload your `.ipynb` file to the `notebooks/` directory.

---

## 👨‍💻 Author

**Prachanda Oli**  
[GitHub](https://github.com/prachanda980)

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.
