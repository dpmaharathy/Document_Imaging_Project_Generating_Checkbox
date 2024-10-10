import os

def generate_document(filename, checkbox_color):
    with open(filename, 'w') as f:
        f.write(r'''\documentclass{article}
\usepackage{graphicx}
\usepackage{array}
\usepackage{enumitem} % Load enumitem before hyperref
\usepackage{hyperref}
\usepackage[normalem]{ulem}
\usepackage{xcolor}

% Redefine \CheckBox to use square checkboxes
\renewcommand{\CheckBox}[2][]{%
    \mbox{\textcolor{''' + checkbox_color + r'''}{\CheckBoxFalseSymbol}\makebox[0pt][l]{\textcolor{''' + checkbox_color + r'''}{\CheckBoxTrueSymbol}}\rule[-0.4ex]{0.55em}{1.5ex}}%
    \raisebox{0.3ex}{\makebox[0pt][l]{#2}}%
}

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
\begin{itemize}
    \item Disease
    \item[$\square$] Penicillin 
    \item[$\square$] Peanuts \quad 
    \item[$\square$] Latex
    
    \item Chronic Conditions: \\
    \item[$\square$] Asthma \quad \item[$\square$] Diabetes \quad \item[$\square$] Hypertension
    
    \item Medications Currently Taking: \\
    \TextField[name=medications, multiline=true, width=10cm,height=1.5cm]{}
    
    \item Previous Surgeries: \\
    \TextField[name=surgeries, multiline=true, width=10cm,height=1.5cm]{}
\end{itemize}

\subsection*{Consent}
I hereby authorize the release of any medical information necessary to process my claim.\\[0.2cm]
\CheckBox[name=consent]{} I consent to the release of my medical information.

\subsection*{Signature}
\TextField[name=signature, width=6cm]{}

\subsection*{Date}
\TextField[name=date, width=6cm]{}

\end{Form}

\end{document}''')

# Generate documents with different checkbox configurations
checkbox_colors = ['white', 'black']
for i, checkbox_color in enumerate(checkbox_colors):
    filename = f'document_{i + 1}.tex'
    generate_document(filename, checkbox_color)
    print(f'{filename} generated.')

    # Compile LaTeX file to PDF
    os.system(f'pdflatex {filename}')
    print(f'{filename} compiled to PDF.')
