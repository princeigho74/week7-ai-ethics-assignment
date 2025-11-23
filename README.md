# AI Ethics Assignment: Designing Responsible and Fair AI Systems

## Overview
This repository contains my complete AI Ethics assignment, including theoretical analysis, case studies, and a practical fairness audit of the COMPAS recidivism prediction system.

## Contents

- **compas_audit.py** - Python script for fairness analysis using AI Fairness 360
- **written_answers.pdf** - Complete written assignment with case studies
- **healthcare_ai_policy.pdf** - Bonus: Ethical guidelines for healthcare AI

## Installation
```bash
pip install aif360 pandas numpy matplotlib seaborn scikit-learn jupyter
```

## Running the Audit
```bash
python compas_audit.py
```

This will:
- Download the COMPAS dataset
- Perform fairness analysis
- Generate visualizations
- Create an audit report

## Key Findings

The COMPAS audit reveals:
- **44.9%** false positive rate for African-American defendants
- **23.5%** false positive rate for Caucasian defendants
- **Disparate Impact Ratio: 0.55** (below 0.8 threshold)

## Technologies Used

- Python 3.8+
- AI Fairness 360
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn

## Assignment Components

### Part 1: Theoretical Understanding
- Algorithmic bias definitions and examples
- Transparency vs explainability analysis
- GDPR impact on AI development

### Part 2: Case Study Analysis
- Amazon's biased hiring tool
- Facial recognition in policing

### Part 3: Practical Audit
- COMPAS recidivism dataset fairness analysis
- Bias metrics and visualizations
- Remediation recommendations

### Part 4: Ethical Reflection
- Personal project ethical considerations
- Implementation of fairness principles

## License

MIT License - Educational purposes

## Author

Happy Igho Umukoro  
princeigho74@gmail.com 
Date: November 2025
```

### Sample requirements.txt

Create this file listing all dependencies:
```
aif360>=0.5.0
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=0.24.0
jupyter>=1.0.0
```

### After Uploading

1. **Get your repository URL**: `https://github.com/YOUR-USERNAME/ai-ethics-assignment`

2. **Add this to your assignment submission**:
   - Include the GitHub link in your PDF
   - Add it to your submission email

3. **Make it look professional**:
   - Add a `.gitignore` file to exclude unnecessary files
   - Add screenshots to your README
   - Include a license file

### Quick .gitignore Template

Create `.gitignore` to exclude temporary files:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/

# Jupyter Notebook
.ipynb_checkpoints

# Data files (if large)
*.csv

# OS
.DS_Store
Thumbs.db
