num_files = 5  # Number of files to generate

for i in range(num_files):
    with open(f'medical_info_{i+1}.tex', 'w') as f:
        f.write(r"""
\documentclass{article}
\usepackage{graphicx}
\usepackage{array}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage[normalem]{ulem}

\begin{document}

\begin{Form}
\section*{Medical Information Form}

\subsection*{Personal Information}
\begin{tabular}{|p{3.5cm}|p{6cm}|}
    \hline
    Name: & \TextField[name=name, width=6cm]{} \\
    \hline
    Date of Birth: & \TextField[name=dob, width=6cm]{} \\
    \hline
    Gender: & \ChoiceMenu[combo,name=gender, width=6cm]{}{Male, Female} \\
    \hline
\end{tabular}

\subsection*{Medical History}
\begin{enumerate}[label=\arabic*.]
    \item Allergies: \\
""")
        for j in range(3):  # Generate three checkboxes
            if j == i % 3:  # Make one checkbox black, others white
                f.write(r"    \fbox{\CheckBox[name=allergy%d]{} Allergy%d} \quad " % (j+1, j+1))
            else:
                f.write(r"    \CheckBox[name=allergy%d]{} Allergy%d \quad " % (j+1, j+1))
        f.write(r"""
    
    \item Chronic Conditions: \\
""")
        for j in range(3):  # Generate three checkboxes
            if j == (i + 1) % 3:  # Make one checkbox black, others white
                f.write(r"    \fbox{\CheckBox[name=chronic%d]{} Chronic%d} \quad " % (j+1, j+1))
            else:
                f.write(r"    \CheckBox[name=chronic%d]{} Chronic%d \quad " % (j+1, j+1))
        f.write(r"""
    
    \item Medications Currently Taking: \\
    \TextField[name=medications, multiline=true, width=10cm,height=1.5cm]{}
    
    \item Previous Surgeries: \\
    \TextField[name=surgeries, multiline=true, width=10cm,height=1.5cm]{}
\end{enumerate}

\subsection*{Consent}
I hereby authorize the release of any medical information necessary to process my claim.\\[0.2cm]
\fbox{\CheckBox[name=consent]{} I consent to the release of my medical information.}

\subsection*{Signature}
\TextField[name=signature, width=6cm]{}

\subsection*{Date}
\TextField[name=date, width=6cm]{}

\end{Form}

\end{document}
""")
