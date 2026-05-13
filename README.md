🧠 Persistent Homology Analyzer – Topological Data Analysis (TDA)
A Python-based project that applies Topological Data Analysis (TDA) to uncover hidden geometric structures in data using persistent homology.
This project demonstrates how to detect connected components and loops in noisy datasets using modern computational topology tools.

🚀 Features

📊 Generate synthetic datasets (circle, clusters)
🔄 Compute persistent homology using Vietoris–Rips filtration
📈 Visualize:

Persistence diagrams
Barcode plots


🧠 Detect:

Connected components (H₀)
Loops (H₁)


⚡ Robust to noisy data
🎯 Simple, educational implementation


🧰 Technologies Used
🔹 Programming

Python 3

🔹 Libraries

NumPy – numerical computation
Matplotlib – visualization
Ripser – persistent homology computation
Persim – diagram plotting
Scikit-learn – dataset generation


📁 Project Structure
tda-persistent-homology/
│
├── data/
│   └── sample_outputs/
│
├── images/
│   ├── point_cloud.png
│   ├── persistence_diagram.png
│   ├── barcode.png
│   └── flowchart.png
│
├── tda_project.py
├── requirements.txt
├── README.md
└── LICENSE


⚙️ Installation
1. Clone the Repository
Shellgit clone https://github.com/tfgregixx/tda-persistent-homology.gitcd tda-persistent-homology
2. Install Dependencies
Shellpip install -r requirements.txt

▶️ Usage
Run the project:
Shellpython tda_project.py

🔄 How It Works

Generate a point cloud dataset (e.g., noisy circle)
Build Vietoris–Rips complex
Compute persistent homology
Extract topological features (H₀, H₁)
Visualize results with diagrams


📊 Flowchart
✅ ASCII Version
        Start
          |
          v
 Generate Point Cloud
          |
          v
 Build VR Complex
          |
          v
 Compute Persistence
          |
          v
   Extract Features
  (H0, H1)
          |
          v
  Plot Diagrams
          |
          v
        End


🖼️Flowchart Image
## 📊 Flowchart

![Flowchart](images/flowchart.png)
``

📉 Example Output
Figure_1.png

🧪 Example Use Cases

Shape detection in noisy datasets
Image topology analysis
Biological data patterns
Machine learning feature extraction
Manifold learning verification


📈 Key Insights
✅ Detects hidden structure in data
✅ Robust to noise
✅ Identifies loops and clusters
✅ Works without labels

🔮 Future Enhancements

Interactive GUI (Tkinter / Streamlit)
Support for real-world datasets
Higher-dimensional homology (H₂)
GPU acceleration
Integration with ML pipelines


🤝 Contributing
Contributions are welcome!
Steps:

Fork repository
Create branch
Commit changes
Open Pull Request


📜 License 




Simple
Acceptable for academic work
Allows reuse with credit


🙏 Acknowledgments

Topological Data Analysis research community
Ripser & Persim libraries
Open-source contributors


📌 Author
Preethi Regina S D
Student – Topological Data Analysis Project

