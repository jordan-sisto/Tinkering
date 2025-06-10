# Trench Crusade Warband Builder

This project provides three interactive tools for building legal warbands for Trench Crusade.

## 📦 Features

- Select faction, units, gear, weapons, and Goetic powers
- Ducat budget enforcement
- Summary and validation of warband legality

## 🛠 Setup

```bash
pip install -r requirements.txt
```

## 🔧 CLI Tool

```bash
python cli_builder.py
```

This launches an interactive terminal warband builder.

## 📒 Jupyter Notebook

Open `notebook_interface.ipynb` in JupyterLab or VSCode to run warband-building logic step-by-step.

## 🌐 Streamlit Web App

```bash
streamlit run streamlit_app.py
```

Use your browser to build a warband via GUI.

## 📁 Files

- `core_builder_module.py`: Core logic
- `trench_data.py`: Sample faction data
- `cli_builder.py`: CLI interface
- `notebook_interface.ipynb`: Jupyter test notebook
- `streamlit_app.py`: Streamlit web app
- `requirements.txt`: Required libraries

---

Built for hobbyists playing Trench Crusade ⚔️
