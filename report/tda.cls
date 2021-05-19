\ProvidesClass{tda}[Time Domain Astrophysics template]

% load in the main exam class with appropriate options
\LoadClass[11pt,a4paper]{exam} 

%space out the lines by 25% more than the default (basically 1.5 line spacing)
%\linespread{1.25}

%load in some commonly needed packages 
\RequirePackage{ifthen,amsmath,amssymb,amsthm,bm,graphicx,color,natbib}

%increase the printed page area width
\extrawidth{2.5cm}

%increase header space on title page only
\extraheadheight[1cm]{0cm}

%setup page headers/footers for first and subsequent pages
\pagestyle{headandfoot}
\lhead{}
\chead[\bfseries \Large \thecourse]{}
\lfoot{\footnotesize Astrophysics Research Institute, Liverpool John Moores University\\ \thecourse}
\cfoot{}
\rfoot{Page \thepage{} of \numpages}
\footrule

% define newcommands for user set page header details
\newcommand*{\course}[1]{\def\thecourse{#1}}
